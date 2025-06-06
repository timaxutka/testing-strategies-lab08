from task1.solution import factorial
import doctest


def demonstrate_factorial():
    print("\nДемонстрация работы функции factorial:")
    test_values = [0, 1, 5, 10]

    for n in test_values:
        print(f"factorial({n}) = {factorial(n)}")

    try:
        factorial(-1)
    except ValueError as e:
        print(f"factorial(-1) вызывает ошибку: {e}")


def run_doctests():
    print("\nЗапуск doctests:")
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    demonstrate_factorial()
    run_doctests()