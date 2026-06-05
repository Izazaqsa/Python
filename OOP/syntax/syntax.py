class CarModel :
    def __init__(self,car_name, car_type):
        self.name = car_name 
        self.model = car_type
        self.color = 'black'
    
car1 = CarModel ('ferrari', 1974)
print (car1.name)
print (car1.model)
print (car1.color)

car2 = CarModel ('buggati',2000)
print (car2.name )
print (car2.model)
print (car2.color)