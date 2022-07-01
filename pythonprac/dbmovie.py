from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@Cluster0.j0ygw.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

# movie = db.movies.find_one({'title':'가버나움'})
# star = movie['star']
#
# all_movies = list(db.movies.find({'star' : star},{'_id':False}))
#
#
# for m in all_movies:
#     print(m['title'])

db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})