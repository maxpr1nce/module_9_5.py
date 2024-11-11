class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start  # Сброс pointer на start
        return self

    def __next__(self):
        current = self.pointer
        if (self.step > 0 and current >= self.stop) or (self.step < 0 and current <= self.stop):
            raise StopIteration  # Завершаем итерацию при достижении границы
        self.pointer += self.step  # Увеличиваем pointer на step
        return current  # Возвращаем текущее значение

# Примеры использования:
# Итерация с положительным шагом
print("Итерация с положительным шагом:")
try:
    it1 = Iterator(1, 10, 2)
    for number in it1:
        print(number)
except StepValueError as e:
    print(e)

# Итерация с отрицательным шагом
print("\nИтерация с отрицательным шагом:")
try:
    it2 = Iterator(10, 0, -2)
    for number in it2:
        print(number)
except StepValueError as e:
    print(e)

# Попробуем с шагом равным нулю
print("\nПопытка использовать шаг равный нулю:")
try:
    it3 = Iterator(0, 5, 0)
except StepValueError as e:
    print(e)