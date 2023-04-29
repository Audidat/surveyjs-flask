from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/cuestionario_covid')
def survey():
    return render_template('cuestionario_covid.html',nombre="Pablo")


if __name__ == '__main__':
    app.run()
