from flask import Flask
from flaskext.couchdb import CouchDBManager
from flaskext.couchdb import Document
from flaskext.couchdb import TextField, DateTimeField, ListField, BooleanField, DictField, Mapping
import datetime
from flaskext.couchdb import ViewDefinition
from couchdb import Server
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



app = Flask(__name__)


# app.config.update(
#         DEBUG = True,
#         COUCHDB_SERVER = 'http://localhost:5984/',
#         COUCHDB_DATABASE = 'docsdemo'
#     )
# feed = ViewDefinition('docs', 'bycontent', 'function(doc) { emit(doc.content, doc); }', 
#         language='javascript')
manager = CouchDBManager()
manager.setup(app)
# manager.add_viewdef(feed)


# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=manager))
# connect_db(app)


class User(Document):
    doc_type = 'User'
    username = TextField()
    password = TextField()
    email = TextField()
    excel = TextField()



class Post(Document):
    doc_type = 'post'

    content = TextField()
    image = TextField()
    author = TextField()
    comments = DictField(Mapping.build(
    author=TextField(),
    email=TextField(),
    content=TextField()

    ))
    created = DateTimeField(default=datetime.datetime.now)
    tags = ListField(TextField())
    comments_allowed = BooleanField(default=True)


