answers = {
    "What are you dong?": "Programming",
    "How are you?": "I am fine",
    "Where do you go?": "I go home"
}
def get_answer(question, answers):
    return answers.get(question)

def ask_user(answers):
    while True:
        ask_user = input("How are you?")
        answer = get_answer(ask_user, answers)
        print(answer)

        if ask_user == "Bye":
            break

ask_user(answers)