import parse_data as parser
import psycopg2 as pg
import sys

print("Parsing data...")
data = parser.parsefile(sys.argv[1])
print("Done parsing data.")

connection = None

config = {
    'dbname': 'alecrim',
    'user': 'alecrim',
    'password': 'alecrim'
}

try:
    connection = pg.connect(**config)
    print('Connected!')
except:
    print('Failed to connect.')

cursor = connection.cursor()

catMappingCounter = 0

try:
    for current in data:
        # try to insert the main product information
        print(f'attempting to insert ({current.id}, {current.asin}, {current.title}, {current.group}, {current.salesrank})')

        if current.title is None:
            insertProduct = f'insert into product (id, asin) values (%s, %s) on conflict do nothing'
            cursor.execute(insertProduct, (current.id, current.asin))
            connection.commit()
        else:
            insertProduct = f"""insert into product (id, asin, title, productgroup, salesrank) values (%s, %s, %s, %s, %s) on conflict do nothing"""
            cursor.execute(insertProduct, (current.id, current.asin, current.title, current.group, current.salesrank))
            connection.commit()


        #try to insert categories & mappings
        for categoryLine in current.categories:
            if categoryLine is not None and categoryLine is not []:

                insertParentCategory = f"""insert into category (id, title) values ({categoryLine[0].id}, '{categoryLine[0].name}') on conflict do nothing"""
                cursor.execute(insertParentCategory)

                for i in range(1, categoryLine.__len__()):
                    insertCategory = f"""insert into category (id, title, parentcatid) values ({categoryLine[i].id}, '{categoryLine[i].name}', {categoryLine[i - 1].id}) on conflict do nothing"""
                    cursor.execute(insertCategory)

            connection.commit()

            insertCatMapping = f"""insert into productcatmapping (id, productid, categoryid) values ({catMappingCounter}, {current.id}, {categoryLine[-1].id}) on conflict do nothing"""
            catMappingCounter += 1
            cursor.execute(insertCatMapping)
            connection.commit()


        #try to insert reviews & mappings

        for review in current.reviews:

            insertCustomer = f"""insert into customer (id) values ('{review.customerID}') on conflict do nothing"""
            cursor.execute(insertCustomer)
            connection.commit()

            insertReview = f"""insert into review (date, helpful, rating, votes, productid) values ('{review.date}', {review.helpful}, {review.rating}, {review.votes}, {current.id}) RETURNING id"""
            cursor.execute(insertReview)
            connection.commit()

            reviewID = cursor.fetchone()[0]

            insertCustomerReviewMapping = f"""insert into customerreviewmapping (customerid, reviewid) values ('{review.customerID}', '{reviewID}')"""
            cursor.execute(insertCustomerReviewMapping)
            connection.commit()


    for current in data:

        print("adding similarities to product with id ", (current.id))
        print()

        for similar in current.similar:
            getObjectStatement = f"""select * from product where asin = '{similar}'"""
            cursor.execute(getObjectStatement)

            if cursor.fetchone() is not None:
                insertSimilarity = f"""insert into productsimilarity (producta, productb) values ('{current.asin}', '{similar}') on conflict do nothing"""
                cursor.execute(insertSimilarity)

        connection.commit()



    cursor.close()
    connection.commit()

except (Exception, pg.DatabaseError) as error:
    print(error)
finally:
    if connection is not None:
        connection.close()