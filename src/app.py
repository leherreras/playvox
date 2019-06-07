from flask import Flask
from common.storage import storage
from apps.crud.api import UsersView
from apps.notes.api import NotesView
app = Flask(__name__)

# Create Mongo connection
storage.connect()

@app.route('/')
def hello_world():
    return 'Hello World!'

UsersView.register(app)
NotesView.register(app)

if __name__ == '__main__':
    app.run()
