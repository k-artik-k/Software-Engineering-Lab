import matplotlib.pyplot as plt


def quad(day, a, b, c):
    return a * (day ** 2) + b * day + c

def main():
    
    a, b, c = 1, -2, 3  
    
 
    num_days = 10
    
    
    days = []
    temps = []
    
    for day in range(1, num_days + 1):
        temp = quad(day, a, b, c)
        days.append(day)
        temps.append(temp)
    

    plt.plot(days, temps, marker='o', label=f'Temperature: {a}x² + {b}x + {c}')
    plt.title('Temperature Model (Iterative, Hardcoded)')
    plt.xlabel('Days')
    plt.ylabel('Temp (°C)')
    plt.legend()
    plt.grid(True)
    plt.show()

main()
