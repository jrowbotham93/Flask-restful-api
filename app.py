from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from resources.item import Item, Items
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) 

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)