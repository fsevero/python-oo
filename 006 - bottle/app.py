from bottle import route, run, request

@route('/')
def index():
    return '<h1>Hello from bottle</h1>'

@route('/hello')
@route('/hello/<name>')
def hello(name='Anonymous'):
    return '<h1>Hello, {}</h1>'.format(name)


@route('/login', method='GET')
def login():
    return '''
    <form action="/login" method="post">
        username: <input name="username" type="text" />
        password: <input name="password" type="password" />
        <input value="Login" type="submit" />
    </form>
    '''

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if check_login(username, password):
        return '<h1>Logged as user {}</h1>'.format(username)
    else:
        return '<h1>Not allowed</h1>'


def check_login(username, password):
    return False

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)