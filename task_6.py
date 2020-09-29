result_a = float(input('Введите результат первого дня в км: '))
result_b = float(input('Какого результата хотите достичь? '))
day = 1
print(f'1-й день: {result_a}')
while result_a < result_b:
    proc = result_a / 100 *10
    result_a = result_a + proc
    day += 1
    print(f'{day}-й день: {result_a:.2f}')