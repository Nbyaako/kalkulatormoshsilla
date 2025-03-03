from random import choice
def main():
    while True:
        print('\nВыберите операцию')
        print('1. Сложение (+)')
        print('2. Вычисление (-)')
        print('3. Умножение (*)')
        print('4. Деление (/)')
        print('5. Выход')

        choice = input('Введите номер операции (1/2/3/4/5):')

        if choice == '5':
            print('До свидания!')
            break

        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))

        if choice == '1':
            print(f'Результат сложение {num1 + num2}')
        elif choice == '2':
            print(f'Результат сложение {num1 - num2}')
        elif choice == '3':
            print(f'Результат сложение {num1 * num2}')
        elif choice == '4':
            if num2 != 0:
                print(f'Результат сложение {num1 / num2}')
            else:
                print('Ошибка! Деление на ноль невозможно')
        else:
            print('Неверный выбор')

if __name__ == '__main__':
    main()