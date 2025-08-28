from brain_games.scripts.brain_games import welcome_user
import random


def calculator(name):
    print('What is the result of the expression?')

    operations = ['+', '-', '*']
    num = 0

    while num < 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(2, 52)
        op = random.choice(operations)
        expression = f"{num1} {op} {num2}"

        print(f'Question: {expression}')

    # Calculamos la respuesta correcta
        if op == '+':
            correct = num1 + num2
        elif op == '-':
            correct = num1 - num2
        else:
            correct = num1 * num2
    
        userGame = input('Your answer: ')


        # Verificar si la respuesta es correcta
        if userGame.strip().isdigit() or (userGame.strip()[0] == '-' and userGame.strip()[1:].isdigit()):
            if int(userGame) == correct:
                print("Correct!")
                num += 1
            else:
                print(f"'{userGame}' is wrong answer ;(. Correct answer was '{correct}'.")
                print(f'Let´s try again, {name}!')
                return  # Termina el juego al primer error
        else:
            print(f"'{userGame}' is not a valid number. Game Over!")
            return

    print(f'Congratulations, {name}!')


def main():

    name = welcome_user()
    calculator(name)

if __name__ == "__main__":
    
    main()
