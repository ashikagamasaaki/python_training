from abc import ABC, abstractmethod

class Car:
    def __init__(self):
        self.__model = None
        self.__engine_type = None
        self.__transmission_type = None
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model
    
    @property
    def engineType(self):
        return self.__engine_type
    
    @engineType.setter
    def engineType(self, engine_type):
        self.__engine_type = engine_type
    
    @property
    def transmissionType(self):
        return self.__transmission_type
    
    @transmissionType.setter
    def transmissionType(self, transmission_type):
        self.__transmission_type = transmission_type
        
    def __str__(self):
        return f"Model: {self.__model}\nEngine: {self.engineType}\nTransmission: {self.__transmission_type}"


class CarBuilder(ABC):
    def __init__(self):
        self._car = Car()
    
    @abstractmethod
    def build_model(self, model):
        pass
    
    @abstractmethod
    def build_engine_type(self, engine_type):
        pass
    
    @abstractmethod
    def build_transmission_type(self, transmission_type):
        pass
    
    def get_result(self):
        return self._car


class ConcreteCarBuilder(CarBuilder):
    def __init__(self):
        super().__init__()
    
    def build_model(self, model):
        self._car.model = model
    
    def build_engine_type(self, engine_type):
        self._car.engineType = engine_type
    
    def build_transmission_type(self, transmission_type):
        self._car.transmissionType = transmission_type


class CarDirector:
    def __init__(self, builder: CarBuilder):
        self.__builder = builder
        
    def construct_car(self, model, engine_type, transmission_type):
        self.__builder.build_model(model)
        self.__builder.build_engine_type(engine_type)
        self.__builder.build_transmission_type(transmission_type)
        return self.__builder.get_result()


builder = ConcreteCarBuilder()
director = CarDirector(builder)

print(director.construct_car('Sedan', 'Gasoline', 'Automatic'))

