from flask_restful import Resource
from v1.logs import get_log
class GetLog(Resource):
    def get(self):
        return get_log('helloworld')