
import random

def toss_coin(times=1):
    coin_states = [False, True]
    results = []
    
    for t in range(times):
        coin_state = random.choice(coin_states)
        
        flip_num = random.randint(10000, 1000000)
        print(flip_num)
        
        for i in range(flip_num):
            # coin = random.choice(coin_states)
            if coin_state:
                coin_state = False
            else:
                coin_state = True
            
        results.append(coin_state)
        
    return results
    
print(toss_coin(3))
