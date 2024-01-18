# o programa deve dizer se o número é par ou ímpar

try:

    def even_or_odd(num):
        if user_number % 2 == 0 :
            return print(f'O número {num} é par.')
        
        return print(f'O número {num} é impar.')
    
    user_number = int(input('Digite um número: '))

    even_or_odd(user_number)
    
except:
    print('Digite um número válido')