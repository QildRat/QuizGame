class Quizbrain:

    def __init__(self, answer):
        self.answer = answer
        self.score = 0
        self.guesses = 0

    def check_answer(self, guess):
        # print(f"answer is: {self.answer}")
        if self.answer == guess:
            print("You got it right!")
            return True
        else:
            print("That's wrong.")
            return False
