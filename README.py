class SafeOperations:
    def __init__(self, data):
        self.data = data

    def divide(self, a, b):
        try:
            result = a / b
            return f"Результат ділення: {result}"
        except ZeroDivisionError:
            return "Помилка: Ділення на нуль!"

    def get_element(self, index):
        try:
            return f"Елемент на позиції {index}: {self.data[index]}"
        except IndexError:
            return "Помилка: Індекс поза межами списку!"

    def to_integer(self, value):
        try:
            result = int(value)
            return f"Ціле число: {result}"
        except ValueError:
            return "Помилка: Неможливо перетворити на ціле число!"


safe = SafeOperations([10, 20, 30])


print(safe.divide(10, 2))         
print(safe.divide(5, 0))         

print(safe.get_element(1))       
print(safe.get_element(10))     

print(safe.to_integer("123"))     
print(safe.to_integer("abc"))     
