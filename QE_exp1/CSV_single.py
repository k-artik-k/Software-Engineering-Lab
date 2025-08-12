import matplotlib.pyplot as plt
import pandas as pd
def quad(day,a,b,c):
    temp = a * day ** 2 + b * day + c
    return temp
def main():
    df = pd.read_csv('Single_input.csv')
    a, b, c = df.loc[0, ['a', 'b', 'c']]
    num_days = int(input("Enter no. of days to model: "))
    days = list(range(1, num_days + 1))
    temp = [quad(day, a, b, c) for day in days]
    plt.plot(days,temp,label = f'Temperature: {a}x^2 + {b}x + {c}')
    plt.title('CSV Single Input')
    plt.xlabel('Days')
    plt.ylabel('Temp (in cel)')
    plt.legend()
    plt.show()
main()
