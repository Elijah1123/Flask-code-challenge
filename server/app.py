from server import create_app
from flask_restful import Api,Resource


app = create_app()

api = Api(app)

class Home(Resource):
    def get(self):
        return {'message': 'Welcome to the Pizza Restaurant API'}
    
api.add_resource(Home, '/')    

if __name__ == '__main__':
    app.run(debug=True)