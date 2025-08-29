from brain_games.scripts.brain_games import welcome_user
import random
import math


def MCD(name):


    print('Find the greatest common divisor of given numbers.')

    num = 0

    while num < 3:

        num1 = random.randint(1, 200)
        num2 = random.randint(1, 200)

        correct = math.gcd(num1, num2)

        print(f'Question: {num1} {num2}')
        userGame = input('Your answer: ')

        if userGame.strip().isdigit():
            if int(userGame) == correct:
                print('Correct!')
                num += 1
            else:
                print((
                    f"'{userGame}' is wrong answer ;(." 
                    f"Correct answer was '{correct}'."))
                print(f"Let's try again, {name}!")
                return
        else:
            print(f"'{userGame}' is not a valid number. Game Over!")
            return

    print(f'Congratulations, {name}!')


def main():


    name = welcome_user()
    MCD(name)

if __name__ == "__main__":


    main()