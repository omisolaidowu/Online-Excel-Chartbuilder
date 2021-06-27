from db import Post
from couchdb import Server

server = Server()
db = server.create('flaskdb')
post = Post()
# post.store(db)