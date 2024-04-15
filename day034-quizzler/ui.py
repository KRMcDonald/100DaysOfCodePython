from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.q_text = "placeholder"
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20)
        self.score_label = Label(self.window, text=f"Score: {self.quiz.score}", font=("Arial", 14), bg=THEME_COLOR, fg="white", pady=20)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(self.window, width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.statement_label = Label(self.window, text=self.q_text, wraplength=280, justify=LEFT, fg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.statement_label.grid(column=0, row=1, columnspan=2)
        self.check_img = PhotoImage(file='images/true.png')
        self.x_img = PhotoImage(file='images/false.png')
        self.true_button = Button(image=self.check_img, command=self.clicked_true, width=100, height=97, borderwidth=0, highlightthickness=0)
        self.true_button.grid(column=0, row=2, pady=20)
        self.false_button = Button(image=self.x_img, width=100, command=self.clicked_false, height=97, borderwidth=0, highlightthickness=0)
        self.false_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.statement_label.configure(text=q_text)
        self.true_button.configure(state=NORMAL)
        self.false_button.configure(state=NORMAL)


    def clicked_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def clicked_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        self.true_button.configure(state=DISABLED)
        self.false_button.configure(state=DISABLED)
        if is_right:
            col = "green"
        else:
            col = "red"
        self.score_label.configure(text=f"Score: {self.quiz.score}")
        self.canvas.configure(bg=col)
        self.statement_label.configure(bg=col, fg="white")

        self.window.after(1000, self.reset_colors_next)

    def reset_colors_next(self):
        self.canvas.configure(bg="white")
        self.statement_label.configure(bg="white", fg=THEME_COLOR)
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            # print("You've completed the quiz")
            # print(f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.statement_label.configure(text=f"Your final score was {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.configure(state=DISABLED)
            self.false_button.configure(state=DISABLED)
