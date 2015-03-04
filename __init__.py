from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app

app = create_app()


@app.route('/')
def apj():
    return render_template('apj.html')

if __name__ == '__main__':
    app.run()
