a = {
    'name': 'ttest',
    'age': 12
}

# print(a.values())

class Car():
    doors = 4
    wheels = 2
    def __init__(self, **kwargs):
        self.doors = 4
        self.wheels = 2
        self.color = kwargs.get('color', 'black')
        self.price = kwargs.get('price', 20)

    def start(self):
        print(self.wheels)

    def __str__(self):
        return '__str__ called'

class Open_Car(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.open_time = 50
    def car_open(self):
        print('car is opening now')



sonata = Car(color='Red', price=24)
print(sonata.color, sonata.price)

test = Open_Car()

# mini = Open_Car(color='Red', price=23, open_time = 70)
# print(mini.color, mini.price)