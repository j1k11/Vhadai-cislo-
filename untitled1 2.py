import random

secret_number = random.randint(1, 99)

while True:
    try:
        guess = int(input("Вгадайте число від 1 до 99: "))

        if 1 <= guess <= 99:
            if guess < secret_number:
                print("Загадане число більше.")
            elif guess > secret_number:
                print("Загадане число менше.")
            else:
                print("Добре вгадано!")
                break
        else:
            print("Будь ласка, введіть число в межах від 1 до 99.")
    except ValueError:
        print("Будь ласка, введіть коректне число.")

