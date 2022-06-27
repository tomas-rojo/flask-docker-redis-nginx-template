from flask import Flask, request
from views import hello, redis_test

server = Flask(__name__)

@server.route('/')
def hello_world():
    return hello()

@server.route('/cache')
def try_redis():
    number = request.args.get('number')
    return redis_test(number)