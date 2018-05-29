from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello from Flask</h1>'

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    return '<h1>Post: {}</h1>'.format(post_id)

if __name__ == '__main__':
    app.run()