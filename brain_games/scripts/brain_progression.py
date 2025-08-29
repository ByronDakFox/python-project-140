from brain_games.scripts.brain_games import welcome_user
import random


def progression(name):

    print('What number is missing in the progression?')

    num = 0

    while num < 3:
        progression, correct = generate()
        question = ' '.join(str(x) for x in progression)
        print(f'Question: {question}')

        userGame = input('Your answer: ')
        
        if userGame.strip().isdigit():
            if int(userGame) == correct:
                print('Correct!')
                num += 1
            else:
                print(f"'{userGame}' is wrong answer ;(. Correct answer was '{correct}'.")
                print(f"Let's try again, {name}!")
                return  # termina los intentos
        else:
            print(f"'{userGame}' is not a valid number. Game Over!")
            return

    print(f'Congratulations, {name}!')



def generate():
    #Genera una progresión aritmética.
    inicio = random.randint(1, 20)          # Primer número
    diferencia = random.randint(2, 10)           # Diferencia común
    longitud = random.randint(5, 10)         # Longitud de la progresión

    progression = [inicio + diferencia * i for i in range(longitud)]
    index = random.randint(0, longitud - 1)
    listaNum = progression[index]
    progression[index] = ".."      # Reemplaza el número con puntos

    return progression, listaNum

def main():

    name = welcome_user()
    progression(name)

if __name__ == "__main__":
    
    main()
