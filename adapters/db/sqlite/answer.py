from domain.entities.answer import Answer

class AnswerRepo:
    def __init__(self, con):
        self.con = con

    def create(self, question_id, user, text):
        cur = self.con.cursor()

        cur.execute("""
            INSERT INTO answers (question_id, username, text) VALUES ({0}, '{1}', '{2}')
        """.format(question_id, user, text))

        self.con.commit()
        return True

    def get_by_question(self, question_id):
        cur = self.con.cursor()

        answers = []

        cur.execute("SELECT * FROM answers WHERE question_id = {0}".format(question_id))

        for row in cur.fetchall():
            answer = Answer(
                a_id=row[0],
                user=row[1],
                question=row[2],
                text=row[3]
            )
            answers.append(answer)

        return answers