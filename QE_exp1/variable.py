import matplotlib.pyplot as plt
def quad(day,a,b,c):
    temp = a * day ** 2 + b * day + c
    return temp
def main():
    a,b,c = 1, -2, 3
    num_days = int(input("Enter no. of days to model: "))
    days = list(range(1, num_days + 1))
    temp = [quad(day, a, b, c) for day in days]
    plt.plot(days,temp,label = f'Temperature: {a}x^2 + {b}x + {c}')
    plt.title('Weather modelling')
    plt.xlabel('Days')
    plt.ylabel('Temp (in cel)')
    plt.legend()
    plt.show()
main()
