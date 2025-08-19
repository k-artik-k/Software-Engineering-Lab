import matplotlib.pyplot as plt
import pandas as pd

def quad(day, a, b, c):
    return a * day ** 2 + b * day + c

def main():
  
    df = pd.read_csv('coeff_multi.csv')

    num_days = int(input("Enter no. of days to model: "))

    for idx, row in df.iterrows():
        a, b, c = row['a'], row['b'], row['c']

        
        days = list(range(1, num_days + 1))
        temp = [quad(day, a, b, c) for day in days]

        future_days = list(range(num_days + 1, num_days + 8))
        predicted_temp = [quad(day, a, b, c) for day in future_days]

        plt.plot(days, temp, label=f'Model {idx+1}: {a}x² + {b}x + {c}')

       
        plt.plot(future_days, predicted_temp, linestyle='--')

    plt.title('CSV Multiple Input with Prediction')
    plt.xlabel('Days')
    plt.ylabel('Temp (C)')
    plt.legend()
    plt.show()

main()
