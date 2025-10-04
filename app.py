from controllers.http.question import questions_blueprint
from flask import Flask

app = Flask(__name__)
app.register_blueprint(questions_blueprint)