# task_1
class MyOpen:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with MyOpen('file.txt', 'w') as f:
    f.write(
        'Духовные ценности направляют человека на свой жизненный путь, формирует отношение к смерти, а также к творческой сфере, саморазвитию.'
        '\nБезусловно, духовные ценности также таят в себе культурные устои [2, с. 159].'
        '\nДуховные ценности в качестве особенной характеристики человека можно изучать со стороны ее природы, содержания, свойственных особенностей.'
        '\nДуховные ценности по природе представляют собой вновь сформированные важные феномены как материального, так и духовного'
        '\nсуществования человека и общества в целом.'
        '\nДуховные ценности состоят из сложных элементов, они отражают мотивы поведения, а также показывают мировоззрения определенного человека.'
        '\nДуховные ценности содержат следующие формы сознания: нравственные, политические, эстетические, религиозные.'
        '\nПервые ростки духовности философы, историки, этнографы и археологи наблюдают уже в доисторических культурах.')


# task_2
class Iterator:
    def __init__(self, l_: list) -> None:
        self.l_ = l_
        self.index = -1

    def __next__(self):
        if self.index + 1 >= len(self.l_):
            raise StopIteration
        self.index += 1
        return self.l_[self.index]

    # def __iter__(self):
    #     return self


class A:
    def __init__(self, some_list: list) -> None:
        self.some_list = some_list

    def __iter__(self):
        return Iterator(self.some_list)


a = A([1, 2, 3, 4])
for i in a:
    print(i)


# task_3
def readliner():
    print('Function started')
    with open('file.txt', 'r') as file:
        for i in open('file.txt'):
            i = yield print(file.readline().replace('\n', ''))
        print('File already closed')
    print('Function stopped')


func = readliner()
try:
    next(func)
    next(func)
    next(func)
    next(func)
    next(func)
    next(func)
    next(func)
    next(func)
    next(func)
except StopIteration as e:
    print(
        f'Iteration already stopped {e}')  # Почему здесь не выводит exception StopIteration, то есть в {e} ничего не попадает


# task_4
class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def increase_speed(self):
        try:
            if self.speed <= 295:
                self.speed += 5
            else:
                raise KeyError
        except KeyError as h:
            print(f'Car cannot move so fast')

    def reduce_speed(self):
        try:
            if self.speed >= 5:
                self.speed -= 5
            else:
                raise ValueError
        except ValueError as something:
            print(f'Car speed cannot be negative')

    def stop(self):
        self.speed = 0


car1 = Car("Porsche", "980", 2021)
car1.reduce_speed()
print(car1.speed)
car1.increase_speed()
car1.increase_speed()
print(car1.speed)
car1.stop()
print(car1.speed)
