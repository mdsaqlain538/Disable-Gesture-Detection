from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://admin:admin@cluster0-shard-00-00-kbyvm.mongodb.net:27017,cluster0-shard-00-01-kbyvm.mongodb.net:27017,cluster0-shard-00-02-kbyvm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client['saqlain']
courses = db.courses
data = {
	"text": "Hello Sample Text"
}
result = courses.insert_one(data)
print(result)