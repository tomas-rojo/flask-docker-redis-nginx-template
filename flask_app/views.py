import socket
from redis_connection import r
from flask import redirect, render_template

def hello():
    return render_template('index.html', socket_id = socket.gethostname())


def redis_test(number):
    
    try:

        data = r.get('number')

        if data is None or data != number:

            r.set('number', number, ex=10)
            return f'<h1>Number did not existed in Redis...Seting number to {number}...</h1>'

        if data == number:

            return f'<h1>Number {data} already exists in Redis</h1>'

    except:

        return redirect('/')

