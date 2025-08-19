import matplotlib.pyplot as plt

def quad(day, a, b, c):
    return a * day ** 2 + b * day + c

def main():
    equations = [(1, 2, 3), (2, -1, 5), (-1, 3, 10)]
    num_days = 10
    days = list(range(1, num_days + 1))

    for idx, (a, b, c) in enumerate(equations, start=1):
        temp = [quad(day, a, b, c) for day in days]
        plt.plot(days, temp, label=f'Eqn {idx}: {a}x² + {b}x + {c}')

    plt.title('Iterative Quadratic Modeling')
    plt.xlabel('Days')
    plt.ylabel('Temp (in °C)')
    plt.legend()
    plt.show()

main()