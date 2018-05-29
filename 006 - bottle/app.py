from bottle import route, run, request, template

@route('/')
def index():
    return '<h1>Hello from bottle</h1>'

@route('/hello')
@route('/hello/<name>')
def hello(name='Anonymous'):
    return '<h1>Hello, {}</h1>'.format(name)


@route('/login', method='GET')
def login():
    return template('login')

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    return template('logged', logged=check_login(username, password), username=username)


def check_login(username, password):
    users = {
        'abc': '1234',
        'xyz': '5678',
        '123': 'abcd'
    }
    return (username in users.keys() and users[username] == password)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)