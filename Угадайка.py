import random
import logging

logging.basicConfig(filename='guessing_game.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def guessing_game():
    while True:
        try:
            N = int(input("Введите максимальное число: "))  # Ввод максимального числа
            k = int(input("Введите количество попыток: "))  # Ввод количества попыток
            if N <= 0 or k <= 0:
                raise ValueError("Число и количество попыток должны быть положительными")
            break
        except ValueError as error:
            print(f"Ошибка: {error}. Попробуйте снова.")

    logging.info(f"Новая игра: N={N}, k={k}")

    number = random.randint(1, N)
    logging.info(f"Загаданное число: {number}")

    for _ in range(k):
        while True:
            try:
                guess = int(input(f"Угадайте число от 1 до {N}: "))
                if guess < 1 or guess > N:
                    raise ValueError("Число должно быть в диапазоне от 1 до N")
                break
            except ValueError as error:
                print(f"Ошибка: {error}. Попробуйте снова.")
            logging.info(f"Попытка пользователя: {guess}")

        if guess == number:
            logging.info("Игра завершена: Пользователь угадал")
            print("Вы угадали!")
            return
        elif guess < number:
            logging.info("Подсказка: Загаданное число больше")
            print("Загаданное число больше")
        else:
            logging.info("Подсказка: Загаданное число меньше")
            print("Загаданное число меньше")

    logging.info("Игра завершена: Попытки закончились")
    print(f"Попытки закончились. Было загадано число {number}")


guessing_game()