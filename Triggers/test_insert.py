from pymongo import MongoClient

def add_document(collection_name, document):
    uri = 'mongodb+srv://store:12345@clustertp.8odepe7.mongodb.net/'
    client = MongoClient(uri)

    try:
        db = client['store']
        collection = db[collection_name]
        result = collection.insert_one(document)
        print("New document added with ID:", result.inserted_id)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        client.close()

collection_name = 'departments'
document = {
  "_id": 5,
  "Name": "Coisas",
  "Manager": [],
  "Employees": []
}

add_document(collection_name, document)
