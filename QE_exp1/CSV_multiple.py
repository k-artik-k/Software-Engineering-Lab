import matplotlib.pyplot as plt
import pandas as pd

def quad(day, a, b, c):
    return a * day ** 2 + b * day + c

def main():
    df = pd.read_csv('Multiple_inputs.csv')
    
    num_days = int(input("Enter no. of days to model: "))
    days = list(range(1, num_days + 1))

    for idx, row in df.iterrows():
        a = row['a']
        b = row['b']
        c = row['c']
        temp = [quad(day, a, b, c) for day in days]
        plt.plot(days, temp, label=f'Temperature: {a}x² + {b}x + {c}')

    plt.title('CSV Multiple Inputs')
    plt.xlabel('Days')
    plt.ylabel('Temperature (in Cel)')
    plt.legend()
    plt.tight_layout()
    plt.show()

main()
