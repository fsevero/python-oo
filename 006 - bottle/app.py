from bottle import route, run

@route('/')
def index():
    return '<h1>Hello from bottle</h1>'

@route('/hello')
@route('/hello/<name>')
def hello(name='Anonymous'):
    return '<h1>Hello, {}</h1>'.format(name)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)