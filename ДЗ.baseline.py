import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    # The first number we choose the median of the range(1, 101), it is 50 and count starts with 1
    # Then as a correction we would add or deduct median numbers between ranges (0, 51) or (50, 101)

    count = 1
    predict_number=50

    if number>predict_number:
        count += 1
        predict_number+=25
        if number>predict_number:
            count += 1
            predict_number+=12
            if number>predict_number:
                # as soon as number equals to predict_number we would stop the game and take count
                while number!=predict_number:
                    count += 1
                    predict_number+=1
            else:
                # as soon as number equals to predict_number we would stop the game and take count
                while number!=predict_number:
                    count += 1
                    predict_number-=1
        elif number==predict_number:
            # if the number equals to 75 it would break and take count
            while number==predict_number:
                break

        else:
            count += 1
            predict_number-=12
            if number>predict_number:
                while number!=predict_number:
                    # as soon as number equals to predict_number we would stop the game and take count
                    count += 1
                    predict_number +=1
            else:
                while number!=predict_number:
                    # as soon as number equals to predict_number we would stop the game and take count
                    count += 1
                    predict_number -=1

    elif number<predict_number:
        predict_number-=25
        count += 1
        if number>predict_number:
            count += 1
            predict_number+=12
            if number>predict_number:
                while number!=predict_number:
                    # as soon as number equals to predict_number we would stop the game and take count
                    count += 1
                    predict_number +=1
            else:
                while number!=predict_number:
                    # as soon as number equals to predict_number we would stop the game and take count
                    count += 1
                    predict_number-=1
        elif number==predict_number:
            # if the number equals to 25 it would break and take count
            while number==predict_number:
                break
        else:
            predict_number-=12
            count += 1
            if number>predict_number:
                while number!=predict_number:
                    # as soon as number equals to predict_number we would stop the game and take count
                    count += 1
                    predict_number +=1
            else:
                while number!=predict_number:
                    # as soon as number equals to predict_number we would stop the game and take count
                    count += 1
                    predict_number -=1
    else:
        while number==predict_number:
            # if the number equals to 50 it would break and take count=1
            break


    # Ваш код заканчивается здесь
    return count

print(f'Количество попыток: {game_core_v3()}')

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)