"""Угадай число"""
"""Теперь угадывает ПК"""


import numpy as np
def random_predict(number:int=1)->int:
    """Рандомно угадываем число

    Args:
        number (int): загадываем число по умолчанию число равно 1

    Returns:
        int: число попыток за которое угадали число
    """
    count=0
    while True:
        count+=1
        predict_number=np.random.randint(1,101) #предлогаемое число
        if predict_number==number:
            # print(f"Число равно {predict_number} попыток {count}")
            break# выход из цикла если угадали
    
    return(count) #возвращаем количество попыток

def skope_game(random_predict)->int:
    """[summary]

    Args:
        random_predict ([type]): функцию которую запустим 1000 раз

    Returns:
        int: среднее количество попыток угадать
    """
    np.random.seed(1)
    Trys_ls=[]
    random_arry=np.random.randint(1,101,size=1000)

    for i in random_arry:
        predict_number=np.random.randint(1,101)
        Trys_ls.append(random_predict(predict_number))
    
    score=sum(Trys_ls)/len(Trys_ls)
    print(f"среднее количество попыток {score}")
    return score

if __name__=="__main__":
    skope_game(random_predict)

