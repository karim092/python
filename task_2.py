user_sec = int(input('Введите количество секунд: '))

hour = user_sec // 3600
min_all = user_sec - hour * 3600
min = min_all // 60
sec = min_all - min * 60
if hour < 10:
    hour = f'0{hour}'
if min < 10:
    min = f'0{min}'
if sec < 10:
    sec = f'0{sec}'

print(f'{hour}:{min}:{sec}')