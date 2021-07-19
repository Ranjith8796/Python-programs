class Vehicle:
    def __init__(self,color,maximum_speed,price):
        self.color=color
        self.maximum_speed=maximum_speed
        self.price=price

class Car(Vehicle):
    def __init__(self,number_of_tires):
        super().__init__('red',200,500000)
        self.number_of_tires=number_of_tires
    
    def car_details():
        print('A {}-colored car with a maximum speed of {} km/h is priced at {} with {} tires'.format(c.color,c.maximum_speed,c.price,c.number_of_tires))

c = Car(4)
Car.car_details()
