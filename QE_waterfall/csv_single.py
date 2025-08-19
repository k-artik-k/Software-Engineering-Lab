import matplotlib.pyplot as plt
import pandas as pd

def quad(day, a, b, c):
    return a * day ** 2 + b * day + c

def main():
    
    df = pd.read_csv('coeff.csv')
    a, b, c = df.loc[0, ['a', 'b', 'c']]

    num_days = int(input("Enter no. of days to model: "))

  
    days = list(range(1, num_days + 1))
    temp = [quad(day, a, b, c) for day in days]

    
    future_days = list(range(num_days + 1, num_days + 8))
    predicted_temp = [quad(day, a, b, c) for day in future_days]

    
    plt.plot(days, temp, label=f'Model: {a}x² + {b}x + {c}', color='blue')

    plt.plot(future_days, predicted_temp, label='Predicted (7 days)', color='red', linestyle='--')

    plt.title('CSV Single Input with Prediction')
    plt.xlabel('Days')
    plt.ylabel('Temp (°C)')
    plt.legend()
    plt.show()

main()
