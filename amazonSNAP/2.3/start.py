from PyInquirer import prompt, print_json
import psycopg2 as pg
from terminalplot import plot
import sys

connection = None

try:
    connection = pg.connect(host=sys.argv[1], dbname=sys.argv[2], user=sys.argv[3], password=sys.argv[4])
    print('Connected to DB!')
except:
    print('Failed to connect.')

cursor = connection.cursor()

questionMap = {
    'Listar comentarios mais uteis para um produto': 1,
    'Listar similares com mais vendas para um produto': 2,
    'Mostrar evolucao diaria das medias de avaliacao para um produto': 3,
    'Listar produtos lideres de venda por grupo': 4,
    'Listar produtos com maior media de avaliacoes uteis positivas': 5,
    'Listar 5 categorias de produto com a maior media de avaliacoes uteis positivas': 6,
    'Listar clientes com mais comentarios por grupo de produto': 7
}

mainQuestion = [
    {
        'type': 'list',
        'name': 'main',
        'message': 'O que deseja fazer?',
        'choices': [
            'Listar comentarios mais uteis para um produto',
            'Listar similares com mais vendas para um produto',
            'Mostrar evolucao diaria das medias de avaliacao para um produto',
            'Listar produtos lideres de venda por grupo',
            'Listar produtos com maior media de avaliacoes uteis positivas',
            'Listar 5 categorias de produto com a maior media de avaliacoes uteis positivas',
            'Listar clientes com mais comentarios por grupo de produto'
        ]
    }
]

idQuestion = [
    {
        'type': 'input',
        'name': 'prodID',
        'message': 'Qual e o ID do produto desejado?'
    }
]


def init():
    answers = prompt(mainQuestion)
    option = questionMap.get(answers['main'])

    if option is 1:
        prodID = prompt(idQuestion)['prodID']
        listMostUseful(prodID)
    elif option is 3:
        listDailyAverages(2)
    elif option is 4:
        listGroupSaleLeads()
    elif option is 5:
        listHighestHelpulPositives()
    elif option is 6:
        listMostUsefulPositive()
    elif option is 7:
        listClientsWithMostComments()


def listMostUseful(productid):

    print('Esperando resultado da query...')

    highestRatedUseful = f"""SELECT * FROM review WHERE productid = '{productid}' 
        GROUP BY id ORDER BY rating DESC, helpful DESC LIMIT 5 """

    lowestRatedUseful = f"""
            SELECT * FROM review WHERE productid = '{productid}' 
            GROUP BY id ORDER BY rating ASC, helpful DESC LIMIT 5
        """
    cursor.execute(highestRatedUseful)
    list = cursor.fetchmany(5)

    print()
    print("Melhor avaliadas com maior utilidade:")

    for element in list:
        print("data: ", element[1].strftime('%d/%m/%Y'), "| ID: ", element[0], " | nota: ", element[2], " | votos: ", element[3], " | útil: ", element[4])

    cursor.execute(lowestRatedUseful)
    list = cursor.fetchmany(5)


    print()
    print("Pior avaliadas com maior utilidade:")

    for element in list:
        print("data: ", element[1].strftime('%d/%m/%Y'), "| ID: ", element[0], " | nota: ", element[2], " | votos: ", element[3], " | útil: ", element[4])

    return

def listDailyAverages(productid):

    print('Esperando resultado da query...')

    averages = f"""
        SELECT date, AVG(rating) FROM review 
        WHERE productid = '{productid}' GROUP BY id, date ORDER BY date ASC
    """

    cursor.execute(averages)
    list = cursor.fetchall()

    print('Imprimindo gráfico...')
    print()


    listDate = range(list.__len__())
    listAvg = []

    for element in list:
        listAvg.append(float(element[1]))

    plot(listDate, listAvg)

    return

def listGroupSaleLeads():

    print('Esperando resultado da query...')

    bestSellingBooks = f"""
        SELECT * FROM product WHERE salesrank > 0 
        AND productgroup = 'Book' ORDER BY salesrank ASC LIMIT 10
    """

    bestSellingMovies = f"""
        SELECT * FROM product WHERE salesrank > 0 
        AND productgroup = 'Video' ORDER BY salesrank ASC LIMIT 10        
        """

    bestSellingDVD = f"""
        SELECT * FROM product WHERE salesrank > 0 
        AND productgroup = 'DVD' ORDER BY salesrank ASC LIMIT 10
    """

    bestSellingMusic = f"""
        SELECT * FROM product WHERE salesrank > 0 
        AND productgroup = 'Music' ORDER BY salesrank ASC LIMIT 10        
    """


    cursor.execute(bestSellingBooks)
    list = cursor.fetchall()

    print()
    print("Lideres em Livros:")

    for element in list:
        print("ID: ", element[0], " | ASIN: ", element[1], " | Nome: ", element[2], "| Ranking de vendas: ", element[4])

    cursor.execute(bestSellingMovies)
    list = cursor.fetchall()


    print()
    print("Lideres em Fitas:")

    for element in list:
        print("ID: ", element[0], " | ASIN: ", element[1], " | Nome: ", element[2], "| Ranking de vendas: ", element[4])

    cursor.execute(bestSellingDVD)
    list = cursor.fetchall()


    print()
    print("Lideres em DVDs:")

    for element in list:
        print("ID: ", element[0], " | ASIN: ", element[1], " | Nome: ", element[2], "| Ranking de vendas: ", element[4])

    cursor.execute(bestSellingMusic)
    list = cursor.fetchall()

    print()
    print("Lideres Musica:")

    for element in list:
        print("ID: ", element[0], " | ASIN: ", element[1], " | Nome: ", element[2], "| Ranking de vendas: ", element[4])

    return

def listHighestHelpulPositives():

    print()
    print('Esperando resultado da query...')

    highestHelpful = f"""
        SELECT product.title, productid AS id FROM review NATURAL JOIN product 
        GROUP BY product.title, productid ORDER BY AVG(helpful) DESC, AVG(rating) DESC LIMIT 10    
    """


    cursor.execute(highestHelpful)
    list = cursor.fetchall()

    print()
    print("Produtos com maior media de avaliacoes uteis positivas:")

    for element in list:
        print("ID: ", element[1], " | Nome: ", element[0])

    return

def listMostUsefulPositive():
    print()
    print('Esperando resultado da query...')

    mostUsefulPositive = f"""
        SELECT category.title FROM category, productcatmapping, product, review 
        GROUP BY category.title ORDER BY AVG(rating) DESC, AVG(helpful) DESC LIMIT 5        """

    cursor.execute(mostUsefulPositive)
    list = cursor.fetchall()

    print()
    print("Categoria com avaliações úteis mais positivas:")

    for element in list:
        print("Nome da categoria: ", element[0])

    return

def listClientsWithMostComments():
    print('Esperando resultado da query...')

    bestSellingBooks = f"""
        SELECT customer.id
        FROM product, review, customerreviewmapping, customer
        WHERE product.productgroup = 'Book'
        GROUP by customer.id
        ORDER by count(customerreviewmapping.customerid) DESC
     """

    bestSellingMovies = f"""
        SELECT customer.id
        FROM product, review, customerreviewmapping, customer
        WHERE product.productgroup = 'Movie'
        GROUP by customer.id
        ORDER by count(customerreviewmapping.customerid) DESC
         """

    bestSellingDVD = f"""
        SELECT customer.id
        FROM product, review, customerreviewmapping, customer
        WHERE product.productgroup = 'DVD'
        GROUP by customer.id
        ORDER by count(customerreviewmapping.customerid) DESC
     """

    bestSellingMusic = f"""
        SELECT customer.id
        FROM product, review, customerreviewmapping, customer
        WHERE product.productgroup = 'Music'
        GROUP by customer.id
        ORDER by count(customerreviewmapping.customerid) DESC
     """

    cursor.execute(bestSellingBooks)
    list = cursor.fetchall()

    print()
    print("Clientes com mais comentarios em Livros:")

    for element in list:
        print("ID: ", element[0])

    cursor.execute(bestSellingMovies)
    list = cursor.fetchall()

    print()
    print("Clientes com mais comentarios em Fitas:")

    for element in list:
        print("ID: ", element[0])

    cursor.execute(bestSellingDVD)
    list = cursor.fetchall()

    print()
    print("Clientes com mais comentarios em DVDs:")

    for element in list:
        print("ID: ", element[0])

    cursor.execute(bestSellingMusic)
    list = cursor.fetchall()

    print()
    print("Clientes com mais comentarios Musica:")

    for element in list:
        print("ID: ", element[0])

    return

init()
