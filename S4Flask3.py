from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):

    def get(self):
        response = {
            'code': 201,
            'message': "Hello, Welcome to My App"
        }
        # Business Logic goes here
        return jsonify(response)

    def post(self):
        data = request.get_json()
        response = {
            'code': 201,
            'message': data
        }
        # Business Logic goes here
        return jsonify(response)

class Quotes(Resource):

    quotes = ["Be Exceptional", "Search the candle rather than cursing the darkness", "Work Hard, Work Smart, You Choose"]

    def get(self, index):

        if index > 2:
            response = {
                'code': 201,
                'message': 'success',
                'quote': "No Quote Found :("
            }
            return jsonify(response)
        else:
            response = {
                'code': 201,
                'message': 'success',
                'quote': Quotes.quotes[index]
            }
            return jsonify(response)

api.add_resource(Hello, '/')
api.add_resource(Quotes, '/quotes/<int:index>')

def main():
    app.run()

if __name__ == '__main__':
    main()
