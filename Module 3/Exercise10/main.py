from choice import ChoiceQuestion

def main():
    first = ChoiceQuestion()
    first.setText("1x1")
    first.addChoice("-1", False)
    first.addChoice("11", False)
    first.addChoice("0", False)
    first.addChoice("1", True)

    second = ChoiceQuestion()
    second.setText("2x2")
    second.addChoice("8", False)
    second.addChoice("4", True)
    second.addChoice("12", False)
    second.addChoice("2", False)

    third = ChoiceQuestion()
    third.setText("3x3")
    third.addChoice("9", True)
    third.addChoice("3", False)
    third.addChoice("6", False)
    third.addChoice("18", False)

    fourth = ChoiceQuestion()
    fourth.setText("4x4")
    fourth.addChoice("-12", False)
    fourth.addChoice("4", False)
    fourth.addChoice("16", True)
    fourth.addChoice("8", False)

    fifth = ChoiceQuestion()
    fifth.setText("5x5")
    fifth.addChoice("-50", False)
    fifth.addChoice("25", True)
    fifth.addChoice("50", False)
    fifth.addChoice("10", False)

    presentQuestion(first)
    presentQuestion(second)
    presentQuestion(third)
    presentQuestion(fourth)
    presentQuestion(fifth)

def presentQuestion(q):
    q.display()
    response=input("Your Answer: ")
    if q.checkAnswer(response) == False:
        print(q.checkAnswer(response))
        presentQuestion(q)
    elif q.checkAnswer(response) == True:
        print(q.checkAnswer(response))

main()
