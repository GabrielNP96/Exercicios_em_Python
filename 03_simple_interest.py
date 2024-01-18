# calcular juros simples

try:
    def simple_interest(value_of_debt, interest_rate, time_of_debt,):

        interest_in_decimals = interest_rate / 100
        total_interest = value_of_debt * interest_in_decimals * time_of_debt
        amount = value_of_debt + total_interest

        return print(f'o resultado total do seus juros é R${round(total_interest, 2)} e o montante é R${round(amount, 2)}')

    initial_value_of_debt= float(input("Digite o valor da divida: "))
    interest_rate = float(input("Digite a taxa de juros sem o %: "))
    debt_time = float(input("Quando tempo dura a divida? digite apenas o número em mêses. "))

    simple_interest(initial_value_of_debt, interest_rate, debt_time)

except:
    print('Digite números válidos')