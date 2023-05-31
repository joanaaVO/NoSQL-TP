import cx_Oracle
from py2neo import Graph, Node, Relationship

# Conexão com a base de dados Oracle
oracle_connection = cx_Oracle.connect('store/12345@localhost:1521/xe')

# Conexão com o base de dados do Neo4j
neo4j_graph = Graph("bolt://localhost:7687") #, auth=("neo4j", "password"))

# Consultas SQL para recuperar os dados das tabelas
sql_store_users = "SELECT * FROM store_users"
sql_product_categories = "SELECT * FROM product_categories"
sql_product = "SELECT * FROM product"
sql_discount = "SELECT * FROM discount"
sql_cart_item = "SELECT * FROM cart_item"
sql_shopping_session = "SELECT * FROM shopping_session"
sql_order_details = "SELECT * FROM order_details"
sql_order_items = "SELECT * FROM order_items"
sql_payment_details = "SELECT * FROM payment_details"
sql_employees = "SELECT * FROM employees"
sql_departments = "SELECT * FROM departments"
sql_addresses = "SELECT * FROM addresses"
sql_employees_archive = "SELECT * FROM employees_archive"
sql_stock = "SELECT * FROM stock"

with oracle_connection.cursor() as cursor:
    # Recupera os dados da tabela store_users
    cursor.execute(sql_store_users)
    for row in cursor:
        user_node = Node("User",
                         user_id=row[0],
                         first_name=row[1],
                         middle_name=row[2],
                         last_name=row[3],
                         phone_number=row[4],
                         email=row[5],
                         username=row[6],
                         user_password=row[7],
                         registered_at=row[8])
        neo4j_graph.create(user_node)

    # Recupera os dados da tabela product_categories
    cursor.execute(sql_product_categories)
    for row in cursor:
        category_node = Node("Category",
                             category_id=row[0],
                             category_name=row[1])
        neo4j_graph.create(category_node)

    # Recupera os dados da tabela product
    cursor.execute(sql_product)
    for row in cursor:
        product_node = Node("Product",
                            product_id=row[0],
                            product_name=row[1],
                            category_id=row[2],
                            sku=row[3],
                            price=row[4],
                            discount_id=row[5],
                            created_at=row[6],
                            last_modified=row[7])
        neo4j_graph.create(product_node)

    # Recupera os dados da tabela discount
    cursor.execute(sql_discount)
    for row in cursor:
        discount_node = Node("Discount",
                             discount_id=row[0],
                             discount_name=row[1],
                             discount_desc=row[2],
                             discount_percent=row[3],
                             is_active_status=row[4],
                             created_at=row[5],
                             modified_at=row[6])
        neo4j_graph.create(discount_node)
    
    # Recupera os dados da tabela cart_item
    cursor.execute(sql_cart_item)
    for row in cursor:
        cart_item_node = Node("CartItem",
                              cart_item_id=row[0],
                              session_id=row[1],
                              product_id=row[2],
                              quantity=row[3],
                              created_at=row[4],
                              modified_at=row[5])
        neo4j_graph.create(cart_item_node)

    # Recupera os dados da tabela shopping_session
    cursor.execute(sql_shopping_session)
    for row in cursor:
        session_node = Node("ShoppingSession",
                            session_id=row[0],
                            user_id=row[1],
                            created_at=row[2],
                            modified_at=row[3])
        neo4j_graph.create(session_node)

    # Recupera os dados da tabela order_details
    cursor.execute(sql_order_details)
    for row in cursor:
        order_details_node = Node("OrderDetails",
                                  order_details_id=row[0],
                                  user_id=row[1],
                                  total=row[2],
                                  payment_id=row[3],
                                  shipping_method=row[4],
                                  delivery_adress_id=row[5],
                                  created_at=row[6],
                                  modified_at=row[7])
        neo4j_graph.create(order_details_node)

    # Recupera os dados da tabela order_items
    cursor.execute(sql_order_items)
    for row in cursor:
        order_items_node = Node("OrderItems",
                                order_items_id=row[0],
                                order_details_id=row[1],
                                product_id=row[2],
                                created_at=row[3],
                                modified_at=row[4])
        neo4j_graph.create(order_items_node)

    # Recupera os dados da tabela payment_details
    cursor.execute(sql_payment_details)
    for row in cursor:
        payment_details_node = Node("PaymentDetails",
                                    payment_details_id=row[0],
                                    order_id=row[1],
                                    amount=row[2],
                                    provider=row[3],
                                    payment_status=row[4],
                                    created_at=row[5],
                                    modified_at=row[6])
        neo4j_graph.create(payment_details_node)

    # Recupera os dados da tabela employees
    cursor.execute(sql_employees)
    employees = []
    for row in cursor:
        employee_node = Node("Employee",
                            employee_id=row[0],
                            first_name=row[1],
                            middle_name=row[2],
                            last_name=row[3],
                            date_of_birth=row[4],
                            department_id=row[5],
                            hire_date=row[6],
                            salary=row[7],
                            phone_number=row[8],
                            email=row[9],
                            ssn_number=row[10])
        employees.append(employee_node)
        neo4j_graph.create(employee_node)

    # Recupera os dados da tabela departments
    cursor.execute(sql_departments)
    for row in cursor:
        department_node = Node("Department",
                            department_id=row[0],
                            department_name=row[1],
                            manager_id=row[2])
        neo4j_graph.create(department_node)

    # Recupera os dados da tabela addresses
    cursor.execute(sql_addresses)
    for row in cursor:
        address_node = Node("Address",
                            address_id=row[0],
                            line1=row[1],
                            line2=row[2],
                            city=row[3],
                            zipcode=row[4],
                            province=row[5],
                            country=row[6])
        neo4j_graph.create(address_node)

    # Recupera os dados da tabela employees_archive
    cursor.execute(sql_employees_archive)
    for row in cursor:
        employee_archive_node = Node("EmployeeArchive",
                                     employee_id=row[0],
                                     first_name=row[1],
                                     middle_name=row[2],
                                     last_name=row[3],
                                     date_of_birth=row[4],
                                     department_id=row[5],
                                     hire_date=row[6],
                                     termination_date=row[7],
                                     salary=row[8],
                                     phone_number=row[9],
                                     email=row[10],
                                     ssn_number=row[11])
        neo4j_graph.create(employee_archive_node)

    # Recupera os dados da tabela stock
    cursor.execute(sql_stock)
    for row in cursor:
        stock_node = Node("Stock",
                          product_id=row[0],
                          quantity=row[1],
                          last_updated=row[2])
        neo4j_graph.create(stock_node)

    # ShoppingSession - StoreUser: Relação "BELONGS_TO_USER"
    shopping_sessions = neo4j_graph.nodes.match("ShoppingSession")
    for session_node in shopping_sessions:
        user_id = session_node["user_id"]
        user_node = neo4j_graph.nodes.match("User", user_id=user_id).first()
        if user_node:
            relationship = Relationship(session_node, "BELONGS_TO_USER", user_node)
            neo4j_graph.create(relationship)

            # Remover o user_id do nodo ShoppingSession
            del session_node["user_id"]
            neo4j_graph.push(session_node)

    # OrderDetails - StoreUser: Relação "BELONGS_TO_USER"
    order_details = neo4j_graph.nodes.match("OrderDetails")
    for order_node in order_details:
        user_id = order_node["user_id"]
        user_node = neo4j_graph.nodes.match("User", user_id=user_id).first()
        if user_node:
            relationship = Relationship(order_node, "BELONGS_TO_USER", user_node)
            neo4j_graph.create(relationship)

            # Remover o user_id do nodo OrderDetails
            del order_node["user_id"]
            neo4j_graph.push(order_node)

    # PaymentDetails - OrderDetails: Relação "BELONGS_TO_ORDER_DETAILS"
    payment_details = neo4j_graph.nodes.match("PaymentDetails")
    for payment_node in payment_details:
        order_id = payment_node["order_id"]
        order_node = neo4j_graph.nodes.match("OrderDetails", order_details_id=order_id).first()
        if order_node:
            relationship = Relationship(payment_node, "BELONGS_TO_ORDER_DETAILS", order_node)
            neo4j_graph.create(relationship)

            # Remover o order_id do nodo PaymentDetails
            del payment_node["order_id"]
            neo4j_graph.push(payment_node)

    # Product - ProductCategory: Relação "BELONGS_TO_CATEGORY"
    products = neo4j_graph.nodes.match("Product")
    for product_node in products:
        category_id = product_node["category_id"]
        category_node = neo4j_graph.nodes.match("Category", category_id=category_id).first()
        if category_node:
            relationship = Relationship(product_node, "BELONGS_TO_CATEGORY", category_node)
            neo4j_graph.create(relationship)

            # Remover o category_id do nodo Product
            del product_node["category_id"]
            neo4j_graph.push(product_node)

    # CartItem - ShoppingSession: Relação "BELONGS_TO_SESSION"
    cart_items = neo4j_graph.nodes.match("CartItem")
    for cart_item_node in cart_items:
        session_id = cart_item_node["session_id"]
        session_node = neo4j_graph.nodes.match("ShoppingSession", session_id=session_id).first()
        if session_node:
            relationship = Relationship(cart_item_node, "BELONGS_TO_SESSION", session_node)
            neo4j_graph.create(relationship)

            # Remover o session_id do nodo CartItem
            del cart_item_node["session_id"]
            neo4j_graph.push(cart_item_node)

    # CartItem - Product: Relação "CONTAINS_PRODUCT"
    cart_items = neo4j_graph.nodes.match("CartItem")
    for cart_item_node in cart_items:
        product_id = cart_item_node["product_id"]
        product_node = neo4j_graph.nodes.match("Product", product_id=product_id).first()
        if product_node:
            relationship = Relationship(cart_item_node, "CONTAINS_PRODUCT", product_node)
            neo4j_graph.create(relationship)

            # Remover o product_id do nodo CartItem
            del cart_item_node["product_id"]
            neo4j_graph.push(cart_item_node)

    # OrderItems - OrderDetails: Relação "BELONGS_TO_ORDER_DETAILS"
    order_items = neo4j_graph.nodes.match("OrderItems")
    for order_item_node in order_items:
        order_id = order_item_node["order_details_id"]
        order_node = neo4j_graph.nodes.match("OrderDetails", order_details_id=order_id).first()
        if order_node:
            relationship = Relationship(order_item_node, "BELONGS_TO_ORDER_DETAILS", order_node)
            neo4j_graph.create(relationship)

            # Remover o oder_details_id do nodo OrderItems
            del order_item_node["order_details_id"]
            neo4j_graph.push(order_item_node)

    # OrderItems - Product: Relação "CONTAINS_PRODUCT"
    order_items = neo4j_graph.nodes.match("OrderItems")
    for order_item_node in order_items:
        product_id = order_item_node["product_id"]
        product_node = neo4j_graph.nodes.match("Product", product_id=product_id).first()
        if product_node:
            relationship = Relationship(order_item_node, "CONTAINS_PRODUCT", product_node)
            neo4j_graph.create(relationship)

            # Remover o product_id do nodo OrderItems
            del order_item_node["product_id"]
            neo4j_graph.push(order_item_node)

    # Product - Discount: Relação "HAS_DISCOUNT"
    products = neo4j_graph.nodes.match("Product")
    for product_node in products:
        discount_id = product_node["discount_id"]
        discount_node = neo4j_graph.nodes.match("Discount", discount_id=discount_id).first()
        if discount_node:
            relationship = Relationship(product_node, "HAS_DISCOUNT", discount_node)
            neo4j_graph.create(relationship)

            # Remover o discount_id do nodo Product
            del product_node["discount_id"]
            neo4j_graph.push(product_node)

    # Product - Stock: Relação "HAS_STOCK"
    products = neo4j_graph.nodes.match("Product")
    for product_node in products:
        product_id = product_node["product_id"]
        stock_node = neo4j_graph.nodes.match("Stock", product_id=product_id).first()
        if stock_node:
            relationship = Relationship(product_node, "HAS_STOCK", stock_node)
            neo4j_graph.create(relationship)

            # Remover o product_id do nodo Stock
            del stock_node["product_id"]
            neo4j_graph.push(stock_node)

    # OrderDetails - PaymentDetails: Relação "HAS_PAYMENT_DETAILS"
    order_details = neo4j_graph.nodes.match("OrderDetails")
    for order_node in order_details:
        payment_id = order_node["payment_id"]
        payment_node = neo4j_graph.nodes.match("PaymentDetails", payment_details_id=payment_id).first()
        if payment_node:
            relationship = Relationship(order_node, "HAS_PAYMENT_DETAILS", payment_node)
            neo4j_graph.create(relationship)

            # Remover o payment_id do nodo OrderDetails
            del order_node["payment_id"]
            neo4j_graph.push(order_node)

    # OrderDetails - Address: Relação "HAS_DELIVERY_ADDRESS"
    order_details = neo4j_graph.nodes.match("OrderDetails")
    for order_node in order_details:
        address_id = order_node["delivery_adress_id"]
        address_node = neo4j_graph.nodes.match("Address", address_id=address_id).first()
        if address_node:
            relationship = Relationship(order_node, "HAS_DELIVERY_ADDRESS", address_node)
            neo4j_graph.create(relationship)

            # Remover o delivery_adress_id do nodo OrderDetails
            del order_node["delivery_adress_id"]
            neo4j_graph.push(order_node)

    # Employee - Department: Relação "BELONGS_TO_DEPARTMENT"
    employees = neo4j_graph.nodes.match("Employee")
    for employee_node in employees:
        department_id = employee_node["department_id"]
        department_node = neo4j_graph.nodes.match("Department", department_id=department_id).first()
        if department_node:
            relationship = Relationship(employee_node, "BELONGS_TO_DEPARTMENT", department_node)
            neo4j_graph.create(relationship)

            # Remover o department_id do nodo Employee
            del employee_node["department_id"]
            neo4j_graph.push(employee_node)

    # Employee - Employee (manager): Relação "REPORTS_TO_MANAGER"
    employees = neo4j_graph.nodes.match("Employee")
    for employee_node in employees:
        manager_id = employee_node["manager_id"]
        manager_node = neo4j_graph.nodes.match("Employee", employee_id=manager_id).first()
        if manager_node:
            relationship = Relationship(employee_node, "REPORTS_TO_MANAGER", manager_node)
            neo4j_graph.create(relationship)

            # Remover o manager_id do nodo Employee
            del employee_node["manager_id"]
            neo4j_graph.push(employee_node)


# Fechar a conexão com a base de dados Oracle
oracle_connection.close()
