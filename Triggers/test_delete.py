from pymongo import MongoClient

def remove_document(collection_name, filter_query):
    uri = 'mongodb+srv://store:12345@clustertp.8odepe7.mongodb.net/'
    client = MongoClient(uri)

    try:
        db = client['mydb']
        collection = db[collection_name]
        result = collection.delete_one(filter_query)
        if result.deleted_count > 0:
            print("Document removed successfully.")
        else:
            print("Document not found.")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        client.close()

collection_name = 'departments'  
filter_query = {"Name": "Coisas"} 
remove_document(collection_name, filter_query)
