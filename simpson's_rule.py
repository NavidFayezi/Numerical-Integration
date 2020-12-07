import math


def simpsons_rule(f, h, a, b):  # integrate f(x) from x = a to x = b using simpson's rule with a given h
    try:
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
    except Exception as e:
        if e.__class__ == ZeroDivisionError:
            print("Integral does not converge")
        else:
            print(str(e))


def test_func(x):
    return math.exp(-2*x)


def test_func2(x):
    return 27-(2*x)-(9*(math.sqrt(x)))-(16/(x**2))


def adaptive_simpson(f, a, b, e):  # Adaptive Simpson's Quadrature Scheme
    try:
        c = (a+b)/2
        s1 = simpsons_rule(f, (b-a)/2, a, b)
        s2 = simpsons_rule(f, (b-c)/2, c, b) + simpsons_rule(f, (c-a)/2, a, c)
        if abs(s2-s1) < (15 * e):
            return s2 + (s2-s1)/15
        else:
            lans = adaptive_simpson(f, a, c, e/2)
            rans = adaptive_simpson(f, c, b, e/2)
            return lans + rans
    except Exception as e:
        print(str(e))


print()
print("SIMPSON's RULE ", " "*34, "|", "Adaptive Simpson's Quadrature Scheme")
print(50*'*', '|', 50*'*')
print("function1: h = 0.1  |", simpsons_rule(test_func, 0.1, 1, 6), 8*" ", "|", adaptive_simpson(test_func, 1, 6, 0.0001))
print(50*'-', '|', 50*'-',)
print("function1: h = 0.25 |", simpsons_rule(test_func, 0.25, 1, 6), 8*" ", "|", adaptive_simpson(test_func, 1, 6, 0.001))
print(50*'-', '|', 50*'-',)
print("function2: h = 0.1  |", simpsons_rule(test_func2, 0.1, 0, 4), 8*" ", "|", adaptive_simpson(test_func2, 0, 4, 0.001))
