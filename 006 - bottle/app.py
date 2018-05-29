from bottle import route, run

@route('/hello')
def index():
    return '<h1>Hello from bottle</h1>'


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)