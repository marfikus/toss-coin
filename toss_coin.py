
import random

def toss_coin(throws=1):
    """
    Имитация подбрасывания монетки.
    """
    # состояния монетки (аверс\реверс):
    coin_states = [False, True]
    # результаты бросков:
    results = []
    
    for throw in range(throws):
        print("Throw {} of {}".format(throw + 1, throws))
        
        # получаем начальное состояние монетки:
        coin_state = random.choice(coin_states)
        
        # получаем количество переворотов в полёте для способа 1:
        # (или время броска для способа 2)
        flip_num = random.randint(10000, 1000000)
        # print(flip_num)
        
        # подбрасываем:
        for i in range(flip_num):
            # имитация вращения.
            # способ 1: постоянное вращение:
            # if coin_state:
                # coin_state = False
            # else:
                # coin_state = True
                
            # способ 2: иногда может и не перевернуться:
            # (больше вариативности, но и работает это медленнее)
            coin_state = random.choice(coin_states)
            
        results.append(coin_state)
        
    return results
    
print(toss_coin(3))
