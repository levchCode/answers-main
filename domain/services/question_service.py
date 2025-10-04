class QuestionService:
    def __init__(self, question_repo, answer_repo):
        self.question_repo = question_repo
        self.answer_repo = answer_repo

    def get_one(self, id):
        question = self.question_repo.get_one(id)
        if question is not None:
           question.answers = self.answer_repo.get_by_question(id)
        return question

    def get_all(self):
        return self.question_repo.get_all()
    
    def create(self, user, text):
        return self.question_repo.create(user, text)

    def answer(self, user, question_id, text):
        return self.answer_repo.create(question_id, user, text)
