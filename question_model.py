class Question:

    # attributes
    def __init__(self, q_text, question_number):
        self.question = q_text
        self.question_number = question_number

    def display_question(self):
        print(f"Q.{self.question_number}: {self.question} (True or False):")
