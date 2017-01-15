import pymongo

client = pymongo.MongoClient("mongodb://moulick:1011sailboat@localhost")
reddit_db = client.reddit
collection = reddit_db.toblerone
print('Database Ok')

FIELDS = {'score': True,
          'ups': True,
          'ratio': True,
          'downs': True,
          'time': True,
          '_id': False}

projects = collection.find(projection=FIELDS)
for project in projects:
    print(project)
