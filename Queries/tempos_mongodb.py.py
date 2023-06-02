from pymongo import MongoClient
import time

# Conectando ao servidor MongoDB
client = MongoClient('localhost', 27017)
db = client['store']
collection = db['store_users']

# Definindo a sua query de agregação
pipeline = [
    { 
        '$unwind': "$Orders" 
        },{
            '$group': 
            {
                '_id': "$Username",
                'Gasto': 
                {
                    '$sum': "$Orders.Total"
                    }
            }
        }, {
            '$sort': 
            { 
                'Gasto': -1 
                }
            },{ 
                '$limit': 1 
    }
]

# Executando a query e calculando o tempo de execução
start_time = time.time()
result = list(collection.aggregate(pipeline))
end_time = time.time()
execution_time = end_time - start_time

# Imprimindo o resultado e o tempo de execução
print('Resultado:', result)
print('Tempo de execução:', execution_time, 'segundos')