
def main():
    print("Простой калькулятор суммы")
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print("Сумма:", a + b)
    except ValueError:
        print("Ошибка: необходимо ввести числа.")


if __name__ == "__main__":
    main()
