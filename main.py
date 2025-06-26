# ------- Задание 1. BankAccount ---------------------------------------------------------------
print('\n------- Задание 1. BankAccount ---------')
class BankAccount:

    def __init__(
            self,
            owner: str,
            balance: (int, float) = 0
    ):

        if not isinstance(owner, str):
            raise TypeError ('Имя клиента не строка')

        self.__owner = owner
        self.__balance = balance


    def __validate(self, owner: str = '', amount: (int, float) = 1) -> None:

        if not isinstance(owner, str):
            raise TypeError ('Имя клиента не строка')

        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError ('<Баланс отрицателен или не int, float')

    def get_owner(self) -> str:

        return self.__owner

    def set_owner(self, owner: (int, float)) -> None:

        self.__validate(owner, 1)
        self.__owner = owner

    def get_balance(self) -> str:

        return self.__balance

    def set_balance(self, amount: (int, float)) -> None:

        self.__validate('', amount)
        self.__balance = amount

    def __repr__(self) -> str:

        return f'Клиент банка {self.__owner} имеет баланс {self.__balance} рублей\n'


client_bank = BankAccount('Илья')
client_bank.set_balance(75)
print(client_bank)
client_bank.set_owner('Максим')
client_bank.set_balance(798.98)
print(client_bank)

# ------- Задание 2. Rectangle ---------------------------------------------------------------
print('\n------- Задание 2. Rectangle ---------')
class Rectangle:

    def __init__(
            self,
            width: (int, float) = 1,
            height: (int, float) = 1
    ):

        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):

            raise ValueError('Сторона фигуры не int, float')

        if width <= 0 or height <= 0:

            raise ValueError('Сторона фигуры отрицательна или 0')

        self.__width = width
        self.__height = height



    def __validate(self, parameter: (int, float)) -> None:

        if not isinstance(parameter, (int, float)):

            raise ValueError('Сторона фигуры не int, float')

        if parameter <= 0:

            raise ValueError('Сторона фигуры отрицательна или 0')


    def get_width(self) -> (int, float):

        return self.__width

    def get_height(self) -> (int, float):

        return self.__height

    def set_width(self, w: (int, float)) -> None:

        self.__validate(w)
        self.__width = w

    def set_height(self, h: (int, float)) -> None:

        self.__validate(h)
        self.__height = h

    def area(self, h, w) -> (int, float):

        return h * w

    def __repr__(self) -> str:

        return (f'Четырехугольник со сторонами:\n'
                f'ширина = {self.__width},'
                f'высота = {self.__height}\n'
                f'имеет площадь = {self.area(self.__width, self.__height)}\n')

rectangle = Rectangle(1,3)
print(rectangle)
rectangle.set_height(8)
rectangle.set_width(9)
print(rectangle)

# ------- Задание 3. Student ---------------------------------------------------------------
print('\n------- Задание 3. Student ---------')
class Student:

    def __init__(
            self,
            name: str,
            grades: list = []
    ):
        if not isinstance(name, str):
            raise TypeError ('Имя студента не строка')

        if not isinstance(grades, list):
            raise ValueError ('Не является списком оценок')

        self.__name = name
        self.__grades = grades

    def __validate(self, name: str, grades: list) -> None:

        if not isinstance(name, str):
            raise TypeError ('Имя студента не строка')

        if not isinstance(grades, list):
            raise ValueError ('Не является списком оценок')

        if len(grades) != 0:

            for elm in grades:
                if not isinstance(elm, (int, float)) or elm <= 0:
                    raise ValueError('Оценка отрицательна, = 0 или не int, float')



    def get_name(self) -> str:

        return self.__name

    def set_name(self, name: str) -> None:

        self.__validate(name, [])
        self.__name = name

    def get_grades(self) -> list:

        return  self.__grades

    def set_grades(self, grades: list) -> None:

        self.__validate('', grades)
        self.__grades = grades

    def average(self) -> (str, float):

        if len(self.__grades) == 0:
            return 'Список оценок пуст'

        else:
            average_grades = sum(self.__grades)/len(self.__grades)
            return f'{average_grades}'

    def __repr__(self) -> None:

        self.average()

        if len(self.__grades) == 0:
            return f'Студент {self.__name}, не имеет оценок\n'

        return f'Студент {self.__name} имеет средний балл {self.average()}\n'


student = Student('Илья')
print(student)
student.get_name()
student.set_name('Максим')
student.set_grades([1,2,3,4,5,6,7,8,9])
print(student)


# ------- Задание 4. TemperatureLog ---------------------------------------------------------
print('\n------- Задание 4. TemperatureLog ---------')
class TemperatureLog:

    def __init__(
            self,
            city: str = 'Волгоград',
            temperatures: list = [21.5, 22.0, 19.8, 20.1, 23.3, 18.9, 21.0]

    ):

        if not isinstance(city, str):
            raise TypeError('Название города не строка')

        if not isinstance(temperatures, list):
            raise ValueError('Не является списком температур!')

        elif len(temperatures) == 0:
            raise ValueError('Список температур пуст!')

        elif len(temperatures) != 7:
            raise ValueError('Список температур меньше семи показателей!')

        else:
            for elm in temperatures:
                if not isinstance(elm, (int, float)):
                    raise ValueError('Значение температуры в списке не число')

        self.__city = city
        self.__temperatures = temperatures


    def __validate(self, city: str, temperatures: (int, float)) -> None:

        if not isinstance(city, str):
            raise TypeError('Название города не строка')

        if not isinstance(temperatures, list):
            raise ValueError('Не является списком температур!')

        elif len(temperatures) == 0:
            raise ValueError('Список температур пуст!')

        elif len(temperatures) != 7:
            raise ValueError('Список температур меньше семи показателей!')

        else:
            for elm in temperatures:
                if not isinstance(elm, (int, float)):
                    raise ValueError('Значение температуры в списке не число')


    def get_city(self) -> str:

        return self.__city

    def set_city(self, city: str) -> None:

        self.__validate(city, [1,1,1,1,1,1,1])
        self.__city = city

    def get_temperatures(self) -> (int, float):

        return self.__temperatures

    def set_temperatures(self, temps: list) -> None:

        self.__validate('', temps)
        self.__temperatures = temps

    def average_temp(self) -> float:

        return round(sum(self.__temperatures) / len(self.__temperatures), 2)

    def max_temp(self) -> str:

        return max(self.__temperatures)

    def min_temp(self) -> str:

        return min(self.__temperatures)

    def __repr__(self) -> str:

        return (f'Город: {self.__city}\nтемпература в городе:\n'
                f'средняя = {self.average_temp()}\n'
                f'Максимальная = {self.max_temp()}\n'
                f'Минимальная = {self.min_temp()}\n')

city = TemperatureLog()
print(city)
city.set_city('Ставрополь')
city.set_temperatures([1,2,3,4,5,6,28.3])
print(city)


# ------- Задание 5. EmployeePayroll -------------------------------------------------------
print('\n------- Задание 5. EmployeePayroll ---------')
class EmployeePayroll:

    def __init__(
            self,
            name :str,
            salary: (int, float),
            tax_rate: float = 0.1
    ):

        if not isinstance(name, str):
            raise TypeError('Имя сотрудника не строка')

        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError('Значение не является числом или оно меньше 0!')

        if tax_rate <= 0 or tax_rate >= 1:
            raise ValueError('Значение не в диапазоне (0 ≤ rate ≤ 1)')


        self.__name = name
        self.__salary = salary
        self.__tax_rate = tax_rate

    def __validate(self, name: str, salary: (int, float), tax_rate: (int, float)) -> None:

        if not isinstance(name, str):
            raise TypeError('Имя сотрудника не строка')

        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError('Значение не является числом или оно меньше 0!')

        if tax_rate <= 0 or tax_rate >= 1:
            raise ValueError('Значение не в диапазоне (0 ≤ rate ≤ 1)')

    def get_name(self) -> str:

        return self.__name

    def set_name(self, name: str) -> None:

        self.__validate(name, 0, 0.1)
        self.__name = name

    def get_salary(self) -> (int, float):

        return self.__salary

    def set_salary(self, sal: (int, float)) -> None:

        self.__validate('', sal, 0.1)
        self.__salary = sal

    def get_tax_rate(self) -> (int, float):

        return self.__tax_rate

    def set_tax_rate(self, rate: (int, float)) -> None:

        self.__validate('', 0, rate)
        self.__tax_rate = rate

    def net_salary(self) -> float:

        return self.__salary * (1 - self.__tax_rate)

    def annual_net(self) -> float:

        return round(12 * self.net_salary(), 2)

    def __repr__(self) -> str:

        return (f'Сотрудник: {self.__name}\n'
                f'имеет зарплату = {self.__salary}руб\n'
                f'ставка налога = {self.__tax_rate}\n'
                f'зарплата за 12 месяцев = {self.annual_net()}руб\n')

employee = EmployeePayroll('Илья', 59000)
print(employee)
employee.set_name('Дмитрий')
employee.set_salary(107000)
employee.set_tax_rate(0.31)
print(employee)
employee.get_tax_rate()
