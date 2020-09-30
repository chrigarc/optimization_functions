import numpy as np

def sphere(vector):
    dimension = len(vector)
    sum = 0;
    for i in range(0, dimension):
        value = vector[i]
        sum+=value**2
    return sum

def ackley(vector):
    dimension = len(vector)
    c = 2 * np.pi;
    b = 0.2;
    a = 20;

    sum1 = 0;
    sum2 = 0;
    for i in range(0, dimension):
        xi = vector[i]
        sum1 = sum1 + xi**2;
        sum2 = sum2 + np.cos(c * xi);

    term1 = -a * np.exp(-b * np.sqrt(sum1 / dimension));
    term2 = -np.exp(sum2 / dimension);

    return term1 + term2 + a + np.exp(1);

def griewank(vector):
    dimension = len(vector)
    sum = 0
    prod = 1;

    for i in range(0, dimension):
        xi = vector[i];
        sum = sum + xi**2 / 4000;
        prod = prod * np.cos(xi / np.sqrt(i+1));

    y = sum - prod + 1;
    return sum

def rastrigin(vector):
    dimension = len(vector)
    sum = 0

    for i in range(0, dimension):
        xi = vector[i];
        sum = sum + (xi**2 - 10 * np.cos(2 * np.pi * xi));

    y = 10 * (dimension+1) + sum;

    return sum

def rosenbrock(vector):
    dimension = len(vector)
    sum = 0

    for i in range(0, dimension-1):
        xi = vector[i];
        xnext = vector[i + 1];
        new = 100 * (xnext - xi**2)**2 + (xi - 1)**2;
        sum = sum + new;

    return sum

def main():
    print("Hello World!")
    #x = np.linspace(-5.2, 5.2, num=2)
    # Crear dos nuevas listas, height and weight
    data = [-4.6, 3.4, 5.2]
    x = np.array(data)
    print(x)
    # y = x + 1
    y = sphere(x)
    print(y)
    y = ackley(x)
    print(y)
    y = griewank(x)
    print(y)
    y = rastrigin(x)
    print(y)
    y = rosenbrock(x)
    print(y)

if __name__ == "__main__":
   main()


