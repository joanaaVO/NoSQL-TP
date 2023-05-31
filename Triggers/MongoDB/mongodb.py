from pymongo import MongoClient
from pymongo.errors import OperationFailure

def handle_insert(collection_name, change):
    print(f"New document inserted in collection {collection_name}:", change['fullDocument'])

def handle_update(collection_name, change):
    print(f"Document updated in collection {collection_name}:", change['fullDocument'])

def handle_delete(collection_name, change):
    print(f"Document deleted in collection {collection_name}:", change['documentKey'])

def setup_change_streams():
    uri = 'mongodb+srv://store:12345@clustertp.8odepe7.mongodb.net/'
    client = MongoClient(uri)

    try:
        db = client['store']
        collections = ['departments', 'employees_archive', 'stock', 'store_users']  # Replace with your collection names

        change_streams = {}

        for collection_name in collections:
            collection = db[collection_name]
            change_streams[collection_name] = collection.watch()

        while True:
            for collection_name, change_stream in change_streams.items():
                for change in change_stream:
                    if change['operationType'] == 'insert':
                        handle_insert(collection_name, change)
                    elif change['operationType'] == 'update':
                        handle_update(collection_name, change)
                    elif change['operationType'] == 'delete':
                        handle_delete(collection_name, change)

    except OperationFailure as e:
        print("An error occurred:", e)

    finally:
        client.close()

setup_change_streams()
