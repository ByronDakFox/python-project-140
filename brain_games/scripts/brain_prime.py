from brain_games.scripts.brain_games import welcome_user
import random


def Numprime(name):

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    num = 0

    while num < 3:
        prime = random.randint(1, 100)

        print(f'Question: {prime}')

        userGame = input('Your answer: ').strip().lower()

        correct = 'yes' if is_prime(prime) else 'no'

        if userGame in ['yes', 'no']:
            if userGame == correct:
                print('Correct!')
                num += 1
            else:
                print(f"'{userGame}' is wrong answer ;(. Correct answer was '{correct}'.")
                print(f"Let's try again, {name}!")
                return
    else:
        print(f'Congratulations, {name}!')        


def is_prime(primo):
    if primo <= 1:
        return False
    for i in range(2, int(primo ** 0.5) + 1):
        if primo % i == 0:
            return False
    return True


def main():

    name = welcome_user()
    Numprime(name)

if __name__ == "__main__":

    main()