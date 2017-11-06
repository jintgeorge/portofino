from flask_restful import Resource

class HelloWorld(Resource):
    def __init__(self):
        self._response = {'message': 'hello world !!'}

    def get(self):
        return self._response