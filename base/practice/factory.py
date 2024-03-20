from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self.name = None
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class CarProduct(Vehicle):
    def start(self):
        return '発車します'
    
    def stop(self):
        return '停車します'

class PlaneProduct(Vehicle):
    def start(self):
        return '離陸します'
    
    def stop(self):
        return '着陸します'
        
class VehicleFactory(ABC):
    @abstractmethod
    def create(self):
        pass

class CarCreater(VehicleFactory):
    def create(self):
        return CarProduct()
    
class PlaneCreater(VehicleFactory):
    def create(self):
        return PlaneProduct()