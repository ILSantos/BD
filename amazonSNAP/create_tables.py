import psycopg2 as pg
import sys

connection = None

try:
    connection = pg.connect(host=sys.argv[1], dbname=sys.argv[2], user=sys.argv[3], password=sys.argv[4])
    print('Connected!')
except:
    print('Failed to connect.')

cursor = connection.cursor()

createCategory = """
CREATE TABLE category
(
 id          int primary key ,
 title       varchar(100) not null ,
 parentcatid int references Category(id) on delete cascade on update cascade
);
"""

createProduct = """
CREATE TABLE product
(
 id               int primary key,
 asin             char(10) not null unique,
 title            varchar(512),
 productgroup     varchar(20),
 salesrank        int
);
"""

createProductSimilarity = """
CREATE TABLE productsimilarity
(
 id       serial primary key ,
 producta char(10) references product(asin) on delete cascade on update cascade,
 productb char(10) references product(asin) on delete cascade on update cascade DEFERRABLE
);
"""

createReview = """
CREATE TABLE review
(
 id        serial primary key,
 date      date not null,
 rating    int not null,
 votes     int not null,
 helpful   int not null,
 productid int references product(id) on delete cascade on update cascade
);
"""

createCustomer = """
CREATE TABLE customer
(
 id char(14) primary key
);
"""

createProductCatMapping = """
CREATE TABLE productcatmapping
(
 id         serial primary key ,
 productid  int references product(id) on delete cascade on update cascade,
 categoryid int references category(id) on delete cascade on update cascade
);
"""

createCustomerReviewMapping = """
CREATE TABLE customerreviewmapping
(
 id         serial primary key,
 customerid char(14) references customer(id) on delete cascade on update cascade,
 reviewid   int references review(id) on delete cascade on update cascade
);
"""
statements = [createCategory, createProduct, createProductSimilarity, createProductCatMapping,
              createCustomer, createReview, createCustomerReviewMapping]

try:
    for statement in statements:
        cursor.execute(statement)
    cursor.close()
    connection.commit()
except (Exception, pg.DatabaseError) as error:
    print(error)
finally:
    if connection is not None:
        connection.close()