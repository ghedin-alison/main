from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://teste:teste@db/main'

@app.route('/')
def index():
    return 'Flask funcionando!!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
