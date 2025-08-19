import matplotlib.pyplot as plt

def quad(day, a, b, c):
    return a * day ** 2 + b * day + c

def main():
    a, b, c = 1, -2, 3  
    num_days = int(input("Enter no. of days to model: "))

    
    days = list(range(1, num_days + 1))
    temp = [quad(day, a, b, c) for day in days]

 
    future_days = list(range(num_days + 1, num_days + 8))
    predicted_temp = [quad(day, a, b, c) for day in future_days]

   
    plt.plot(days, temp, label=f'Temperature Model: {a}x² + {b}x + {c}', color='blue')

    plt.plot(future_days, predicted_temp, label='Predicted (next 7 days)', color='red', linestyle='--')

  
    plt.title('Weather Modelling & Prediction')
    plt.xlabel('Days')
    plt.ylabel('Temp (°C)')
    plt.legend()
    plt.show()

main()
