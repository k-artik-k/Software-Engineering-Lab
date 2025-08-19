import matplotlib.pyplot as plt

def quad(day, a, b, c):
    return a * day ** 2 + b * day + c

def main():
    
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    num_days = int(input("Enter number of days to model: "))

    days = list(range(1, num_days + 1))
    temp = [quad(day, a, b, c) for day in days]

   
    future_days = list(range(num_days + 1, num_days + 8))
    predicted_temp = [quad(day, a, b, c) for day in future_days]

    plt.plot(days, temp, label='Actual Model', color='blue')
    plt.plot(future_days, predicted_temp, label='Predicted (7 days)', color='green', linestyle='--')

    plt.title('Temperature Prediction (User Input)')
    plt.xlabel('Days')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.show()

main()
