from flask import Flask, render_template
from routes.handle import handle

app = Flask(__name__)

app.register_blueprint(handle)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
