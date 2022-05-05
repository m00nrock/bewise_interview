import datetime as dt
import logging
import sys

import requests
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


MAIN_ENDPOINT = 'https://jservice.io/api/random'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres:postgres@db:5432'
    )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_question = db.Column(db.String())
    text_answer = db.Column(db.String())
    date = db.Column(db.String(100))
    added_at = db.Column(db.DateTime())

    def serialize(self):
        return {
            'id': self.id,
            'text_question': self.text_question,
            'text_answer': self.text_answer,
            'date': self.date,
            'added_at': self.added_at
        }

    def __repr__(self):
        return f'question id: {self.id}'


db.create_all()


@app.route('/questions/', methods=['POST'])
def questions():
    def get_question_from_api(count: int) -> dict:
        return requests.get(MAIN_ENDPOINT, params=dict(count=count)).json()

    def is_record_exists(question: dict) -> dict:
        if question['id'] in list_of_ids:
            logging.error(
                f'Id {question["id"]} уже есть в БД.Запрашиваем новый'
            )
            question = get_question_from_api(1)
            return is_record_exists(question[0])
        logging.info('Дублей нет')
        return question

    if 'questions_num' in request.json:
        count = request.json['questions_num']
        list_of_ids = [question.id for question in Question.query.all()]
        response = get_question_from_api(count)

        for i in response:
            not_exist_records = is_record_exists(i)
            db.session.add(
                Question(
                    id=not_exist_records['id'],
                    text_question=not_exist_records['question'],
                    text_answer=not_exist_records['answer'],
                    date=not_exist_records['created_at'],
                    added_at=dt.datetime.utcnow()
                )
            )
        db.session.commit()
        last_record = Question.query.order_by(desc('added_at')).first()
        if last_record is None:
            return {}
        return last_record.serialize()
    return 'questions_num обязательный параметр'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
