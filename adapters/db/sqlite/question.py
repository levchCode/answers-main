from domain.entities.question import Question
import logging

logger = logging.getLogger('spam_application')
logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


class QuestionRepo:
    def __init__(self, con):
        self.con = con

    def create(self, user, text):
        cur = self.con.cursor()

        cur.execute("""
            INSERT INTO questions (username, text) VALUES ('{0}', '{1}')
        """.format(user, text))

        self.con.commit()
        return True

    def get_one(self, id):
        cur = self.con.cursor()

        cur.execute("SELECT * FROM questions AS q WHERE q.id = {0}".format(id))
        
        res = cur.fetchone()
        question = Question(
            q_id=res[0],
            user=res[1],
            text=res[2]
        )

        return question
        

    def get_all(self):
        cur = self.con.cursor()

        questions = []

        cur.execute("SELECT * FROM questions")

        for row in cur.fetchall():
            question = Question(
                q_id=row[0],
                user=row[1],
                text=row[2]
            )
            questions.append(question)

        return questions