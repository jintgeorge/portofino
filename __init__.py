from flask import Flask, request
from flask_restful import Api
#from flask_redis import FlaskRedis
from v1.helloworld.hello import HelloWorld
from v1.logs.logsummary import LogSum
from v1.helloworld.logs import GetLog

import time
from log import get_circular_logger
logger = get_circular_logger('request_log.log')

app = Flask(__name__)
api = Api(app)
#redis_store = FlaskRedis(app=app, strict=False)
#redis_store.init_app(app)

@app.before_request
def LogRequest():
    # Log every request as it comes through
    try:
        t = request.remote_addr + ' | ' + request.endpoint + ' | ' + str(int(time.time()))
        logger.log(t)
    except:
        return('Api not supported !')

#This could be improved depending on how many Apis we are expecting
api.add_resource(LogSum, '/v1/logs', '/v1/logs/')
api.add_resource(HelloWorld, '/v1/helloworld','/v1/helloworld/')
api.add_resource(GetLog, '/v1/helloworld/logs', '/v1/helloworld/logs/')
