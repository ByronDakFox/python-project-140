from brain_games.scripts.brain_games import welcome_user
import random


def par_impar(name):


    print('Answer "yes" if the number is even, otherwise answer "no".')
    num = 0

    while num < 3:

        tempNum = random.randint(1, 30)
        print(f"Question: {tempNum}")

        userGame = input('Your answer: ').strip().lower()

        if tempNum % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        if result == userGame:
            print('Correct!')
            num +=1

        else:
            print((
                f"'{userGame}' is wrong answer ;(." 
                f"Correct answer was '{result}'."))
            print(f"Let's try again, {name}!")
            break
    else: 
        print(f'Congratulations, {name}!')


def main():


    name = welcome_user()
    par_impar(name)

if __name__ == "__main__":
    main()