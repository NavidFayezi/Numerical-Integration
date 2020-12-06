def simpsons_rule(f, h, a, b):  # integrate f(x) from x = a to x = b using simpson's rule with a given h
    n = int((b-a) / (2*h))
    sigma = f(a) + f(b)
    multiply_by_four = 0
    multiply_by_two = 0
    for i in range(1,n+1):
        multiply_by_four += f(a+(2*i-1)*h)
    for i in range(1,n):
        multiply_by_two += f(a+(2*i)*h)
    multiply_by_four *= 4
    multiply_by_two *= 2
    sigma += multiply_by_two + multiply_by_four
    sigma *= h/3
    return sigma


def test_func(x):
    return ((x**2)+1) ** 0.5


print(simpsons_rule(test_func, 0.2, -1, 1))
