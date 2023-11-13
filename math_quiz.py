import random


def random_interger(min, max):
    """
    This functions return random integer between max and min value.
    """
    try:
        min=int(min)
        max=int(max)
    except:
        print("Error casting to interger")
    return random.randint(min, max)


def select_operator():
    """This function return an operator between +,-,/"""

    return random.choice(['+', '-', '*'])


def calculate_result(n1, n2, o):
    """
    Calculates the result using operator o and operands n1,n2.
    """

    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(t_q):
        n1 = random_interger(1, 10); n2 = random_interger(1, 5.5); o = select_operator()

        PROBLEM, ANSWER = calculate_result(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
