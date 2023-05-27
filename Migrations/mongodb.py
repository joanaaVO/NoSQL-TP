import cx_Oracle
import pymongo

#export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_10:$LD_LIBRARY_PATH
#source ~/.bashrc

def get_manager(id):
    oracle_cursor.execute("SELECT * FROM employees WHERE employee_id = :employee_id", employee_id = id)

    oracle_managers = oracle_cursor.fetchall()

    managers = []
    for row in oracle_managers:
        manager = {
            'First Name': row[1],
            'Middle Name': row[2],
            'Last Name': row[3],
            'Date Of Birth': row[4],
            'Hire Date': row[6],
            'Salary': row[7],
            'Phone Number': row[8],
            'Email': row[9],
            'Ssn Number': row[10]
        }
        managers.append(manager)

    return managers

def get_employees(id):
    oracle_cursor.execute("SELECT * FROM employees WHERE department_id = :department_id", department_id = id)

    oracle_employees = oracle_cursor.fetchall()

    employees = []
    for row in oracle_employees:
        employee = {
            #'_id': row[0],
            'First Name': row[1],
            'Middle Name': row[2],
            'Last Name': row[3],
            'Date Of Birth': row[4],
            'Hire Date': row[6],
            'Salary': row[7],
            'Phone Number': row[8],
            'Email': row[9],
            'Ssn Number': row[10]
        }
        employees.append(employee)

    return employees

def get_cart(id):
    oracle_cursor.execute("SELECT * FROM cart_item WHERE session_id = :session_id", session_id = id)

    oracle_carts = oracle_cursor.fetchall()

    carts = []
    for row in oracle_carts:
        cart = {
            'Product': get_product(row[2]),
            'Quantity': row[3],
            'Created At': row[4],
            'Last Modified': row[5],
        }
        carts.append(cart)

    return carts

def get_sessions(id):
    oracle_cursor.execute("SELECT * FROM shopping_session WHERE user_id = :user_id", user_id = id)

    oracle_sessions = oracle_cursor.fetchall()

    sessions = []
    for row in oracle_sessions:
        session = {
            'Created At': row[2],
            'Last Modified': row[3],
            'Cart': get_cart(row[0])
        }
        sessions.append(session)

    return sessions

def get_discount(id):
    oracle_cursor.execute("SELECT * FROM discount WHERE discount_id = :discount_id", discount_id = id)

    oracle_discounts = oracle_cursor.fetchall()

    discounts = []
    for row in oracle_discounts:
        discount = {
            'Name': row[1],
            'Desc': row[2],
            'Percent': row[3],
            'Is Active Status': row[4],
            'Created At': row[5],
            'Last Modified': row[6]
        }
        discounts.append(discount)

    return discounts


def get_category(id):
    oracle_cursor.execute("SELECT * FROM product_categories WHERE category_id = :category_id", category_id = id)

    oracle_categories = oracle_cursor.fetchall()

    categories = []
    for row in oracle_categories:
        category = {
            'Name': row[1]
        }
        categories.append(category)

    return categories

def get_product(id):
    oracle_cursor.execute("SELECT * FROM product WHERE product_id = :product_id", product_id = id)

    oracle_products = oracle_cursor.fetchall()

    products = []
    for row in oracle_products:
        product = {
            'Name': row[1],
            'Category': get_category(row[2]),
            'Sku': row[3],
            'Price': row[4],
            'Discount': get_discount(row[5]),
            'Created At': row[6],
            'Last Modified': row[7],
        }
        products.append(product)

    return products

def get_items(id):
    oracle_cursor.execute("SELECT * FROM order_items WHERE order_details_id = :order_details_id", order_details_id = id)

    oracle_items = oracle_cursor.fetchall()

    items = []
    for row in oracle_items:
        item = {
            'Product': get_product(row[2]),
            'Created At': row[3],
            'Last Modified': row[4]
        }
        items.append(item)

    return items

def get_address(id):
    oracle_cursor.execute("SELECT * FROM addresses WHERE adress_id = :adress_id", adress_id = id)

    oracle_adress = oracle_cursor.fetchall()

    addresses = []
    for row in oracle_adress:
        address = {
            'Line 1': row[1],
            'Line 2': row[2],
            'City': row[3],
            'Zip Code': row[4],
            'Province': row[5],
            'Country': row[6]
        }
        addresses.append(address)

    return addresses

def get_payment(id):
    oracle_cursor.execute("SELECT * FROM payment_details WHERE order_id = :order_id", order_id = id)

    oracle_payment = oracle_cursor.fetchall()

    payments = []
    for row in oracle_payment:
        payment = {
            'Amount': row[2],
            'Provider': row[3],
            'Payment Status': row[4],
            'Created At': row[5],
            'Last Modified': row[6]
        }
        payments.append(payment)

    return payments

def get_orders(id):
    oracle_cursor.execute("SELECT * FROM order_details WHERE user_id = :user_id", user_id = id)

    oracle_orders = oracle_cursor.fetchall()

    orders = []
    for row in oracle_orders:
        order = {
            'Total': row[2],
            'Payment': get_payment(row[0]),
            'Shipping Method': row[4],
            'Address:': get_address(row[5]),
            'Created_At': row[6],
            'Last Modified': row[7],
            'Items:': get_items(row[0])
        }
        orders.append(order)

    return orders


# Configurações de conexão ao Oracle
oracle_connection = cx_Oracle.connect('store/12345@localhost:1521/xe')

# Configurações de conexão ao MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017')
mongo_db = mongo_client['store']

# Criar coleções no MongoDB
users = mongo_db['store_users']
departments = mongo_db['departments']
archive = mongo_db['employees_archive']
stock = mongo_db['stock']

# Consulta ao Oracle para obter os dados
oracle_cursor = oracle_connection.cursor()
oracle_cursor.execute('SELECT * FROM store_users')
oracle_data = oracle_cursor.fetchall()

for row in oracle_data:
    document = {
        '_id': row[0],
        'First Name':  row[1],
        'Middle Name': row[2],
        'Last Name': row[3],
        'Phone Number': row[4],
        'Email': row[5],
        'Username': row[6],
        'Password': row[7],
        'Registered At': row[8],
        'Orders': get_orders(row[0]),
        'Sessions': get_sessions(row[0])
    }
    users.insert_one(document)

oracle_cursor.execute('SELECT * FROM employees_archive')
oracle_data = oracle_cursor.fetchall()


for row in oracle_data:
    document = {
        'Event Date': row[0],
        'Event Type': row[1],
        'Username': row[2],
        'Old Employee ID': row[3],
        'Old First Name': row[4],
        'Old Middle Name': row[5],
        'Old Last Name': row[6],
        'Old Date Of Birth': row[7],
        'Old Department ID': row[8],
        'Old Hire Date': row[9],
        'Old Salary': row[10],
        'Old Phone Number': row[11],
        'Old Email': row[12],
        'Old Ssn Number': row[13],
        'Old Manager ID': row[14],

        'New Employee ID': row[15],
        'New First Name': row[16],
        'New Middle Name': row[17],
        'New Last Name': row[18],
        'New Date Of Birth': row[19],
        'New Department ID': row[20],
        'New Hire Date': row[21],
        'New Salary': row[22],
        'New Phone Number': row[23],
        'New Email': row[24],
        'New Ssn Number': row[25],
        'New Manager ID': row[26]
    }
    archive.insert_one(document)

oracle_cursor.execute('SELECT * FROM departments')
oracle_data = oracle_cursor.fetchall()


for row in oracle_data:
    document = {
        '_id': row[0],
        'Name': row[1],
        'Manager': get_manager(row[2]),
        'Desc': row[3],
        'Employees': get_employees(row[0])
    }
    departments.insert_one(document)

oracle_cursor.execute('SELECT * FROM stock')
oracle_data = oracle_cursor.fetchall()

for row in oracle_data:
    document = {
            #document['product_id'] = row[0]
            'Quantity': row[1],
            'Max Stock Quantity': row[2],
            'Unit': row[3],
            'Product': get_product(row[0])
    }
    stock.insert_one(document)

# Fechar as conexões
oracle_cursor.close()
oracle_connection.close()
mongo_client.close()
