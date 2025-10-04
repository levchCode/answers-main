from flask import Blueprint, jsonify, request, abort
import psycopg2
from domain.usecases.question import QuestionUsecase
from domain.services.question_service import QuestionService
from adapters.db.sqlite.question import QuestionRepo
from adapters.db.sqlite.answer import AnswerRepo
from adapters.db.sqlite.migrate import migrate_db


questions_blueprint = Blueprint('questions', __name__, url_prefix='/questions')

con = psycopg2.connect(dbname='questions', user='postgres', password='secret', host='postgres', port=5432)

migrate_db(con)

question_repo = QuestionRepo(con=con)
answer_repo = AnswerRepo(con=con)
question_service = QuestionService(question_repo=question_repo, answer_repo=answer_repo)
question_usecase = QuestionUsecase(question_service=question_service)


@questions_blueprint.route("/create", methods=["POST"])
def create():
    body = request.json
    res = question_usecase.create_one(body)
    return jsonify(res)

@questions_blueprint.route("/<question_id>", methods=["GET"])
def view(question_id):
    res = question_usecase.get_one(question_id)
    res.answers = [vars(i) for i in res.answers]
    if res is None:
        abort(404)
    return jsonify(vars(res))

@questions_blueprint.route("/", methods=["GET"])
def all():
    res = question_usecase.get_all()
    return jsonify([vars(i) for i in res])

@questions_blueprint.route("/<question_id>/answer", methods=["POST"])
def answer(question_id):
    body = request.json
    body['question_id'] = question_id
    return jsonify(question_usecase.answer_question(body))