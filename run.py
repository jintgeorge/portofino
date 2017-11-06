from flask import Flask, request
from flask_restful import Api
from flask_redis import FlaskRedis
from v1.helloworld.hello import HelloWorld
from v1.logs.logsummary import LogSummary
from v1.helloworld.logs import GetLog

import time
from log import get_circular_logger
logger = get_circular_logger('request_log.log')

app = Flask(__name__)
api = Api(app)
redis_store = FlaskRedis(app=app, strict=False)
redis_store.init_app(app)
print('Request hit')


#Log every request as it comes through
@app.before_request
def LogRequest():
    print(request.endpoint)
    t = request.remote_addr + ' | ' + request.endpoint + ' | ' + str(int(time.time()))
    #t = '223.3.4.25' + ' | ' + request.endpoint + ' | ' + str(int(time.time()))
    logger.log(t)
    redis_store.set('potato', 'abc')

api.add_resource(HelloWorld, '/v1/helloworld','/v1/helloworld/')
api.add_resource(LogSummary, '/v1/logs')
api.add_resource(GetLog, '/v1/helloworld/logs')

if __name__ == '__main__':
    #init()
    app.run(host='0.0.0.0', port=9090, debug=True, threaded=True)