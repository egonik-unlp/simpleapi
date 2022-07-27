from flask_restful import Api, Resource
from flask import Flask, request

app = Flask(__name__)
api = Api(app)


class BaseClass(Resource):
    def post(self):
        data = request.get_json(force=True)
        return data, 200
    def get(self):
        data = request.get_json(force=True)
        return data, 200


api.add_resource(BaseClass, "/")

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
        port = '80',
        debug = True
    )




        
