#o programa deve exibir a soma e a média

try:

    first_user_number = int(input('Digite um número: '))
    second_user_number = int(input('Digite outro número: '))
    third_user_number = int(input('Digite o ultimo número: '))

    def sum_and_average(num_1, num_2, num_3):
        sum = num_1 + num_2 + num_3
        average = sum / 3
        average = round(average, 2)

        print(f'A soma dos números {num_1}, {num_2}, {num_3} é {sum}')
        print(f'E sua média é {average}')

    sum_and_average(first_user_number, second_user_number, third_user_number)

except:
    print('Digite números válidos')