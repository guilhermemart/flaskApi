import mysql.connector
from models import Product
from decouple import config

mydb = mysql.connector.connect(
    host='localhost',
    user=config('MYSQL_USER',default='MyUser'),
    password=config('MYSQL_PASSWORD', default='MainPassword'),
    database='FlaskApiDb'
)


def get_all():
    cursor = mydb.cursor()
    query = "SELECT id, name, description, price FROM products"
    cursor.execute(query)

    return cursor.fetchall()


def insert(product: Product):
    cursor = mydb.cursor()

    query = f'''
            INSERT INTO 
                products (
                    name, 
                    description, 
                    price
                    ) 
            VALUES (
                '{product.name}', 
                '{product.description}', 
                {product.price}
                )
            '''

    query += ";SELECT LAST_INSERT_ID()"
    id_created = 0
    rows_created = 0
    for result in cursor.execute(query, multi=True):
        if result.with_rows:
            id_created = result.fetchone()[0]
        else:
            rows_created = result.rowcount
    mydb.commit()
    if rows_created > 0:
        return id_created
    return 0


def update_product(product: Product):
    cursor = mydb.cursor()
    query = f'''
        UPDATE products 
            SET 
                name='{product.name}', 
                description='{product.description}', 
                price={product.price}
        WHERE 
            id={product.id}
        '''
    cursor.execute(query)
    mydb.commit()
    return product.id


def delete_product(product_id):
    cursor = mydb.cursor()
    query = f'''
        DELETE FROM products 
        WHERE 
            id={product_id}
        '''
    cursor.execute(query)
    mydb.commit()
    return product_id
