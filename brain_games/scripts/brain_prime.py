from brain_games.scripts.brain_games import welcome_user
import random


def par_impar(name):

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    prime = random.randint(2, 200)
    resul = is_prime(prime)
    print(f'Question: {prime}')
    num = 0


def is_prime(primo):
    #Verifica si el número es primo o no
    if primo <= 1:
        return False
    for i in range(2, int(primo ** 0.5) + 1):
        if primo % i == 0:
            return False
    return True



def main():

    name = welcome_user()
    par_impar(name)

if __name__ == "__main__":
    
    main()