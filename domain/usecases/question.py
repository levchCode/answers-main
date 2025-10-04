class QuestionUsecase:
    def __init__(self, question_service):
        self.question_service = question_service

    def get_one(self, id):
        return self.question_service.get_one(id)

    def get_all(self):
        return self.question_service.get_all()
    
    def create_one(self, data):
        return self.question_service.create(data['user'], data['text'])
    
    def answer_question(self, data):
        return self.question_service.answer(data['user'], data['question_id'], data['text'])