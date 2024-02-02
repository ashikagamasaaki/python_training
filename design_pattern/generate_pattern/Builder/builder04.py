from abc import ABC, abstractmethod

# Product
class House:
    def __init__(self):
        self.__floor_type = None
        self.__wall_color = None
        self.__roof_shape = None
        
    def __str__(self):
        return f"Floor Type: {self.__floor_type}\nWall Color: {self.__wall_color}\nRoof Shape: {self.__roof_shape}"

    @property
    def floorType(self):
        return self.__floor_type
    
    @floorType.setter
    def floorType(self, floor_type):
        self.__floor_type = floor_type
        

    @property
    def WallColor(self):
        return self.__wall_color
    
    @WallColor.setter
    def WallColor(self, wall_color):
        self.__wall_color = wall_color
        

    @property
    def RoofShape(self):
        return self.__roof_shape
    
    @RoofShape.setter
    def RoofShape(self, roof_shape):
        self.__roof_shape = roof_shape
        

# Builder
class IHouseBuilder(ABC):
    def __init__(self):
        self._house = House()
    
    @abstractmethod
    def build_floor(self, floor_type):
        pass
    
    @abstractmethod
    def build_wall(self, wall_color):
        pass
    
    @abstractmethod
    def build_roof(self, roof_shape):
        pass
    
    def get_result(self):
        return self._house
    
# ConcretBuilder
class HouseBuilder(IHouseBuilder):
    def __init__(self):
        super().__init__()
        
    def build_floor(self, floor_type):
        self._house.floorType = floor_type
    
    def build_wall(self, wall_color):
        self._house.WallColor = wall_color
    
    def build_roof(self, roof_shape):
        self._house.RoofShape = roof_shape

# Director
class HouseDirector:
    def __init__(self, builder: IHouseBuilder):
        self.__builder = builder
    
    def build_house(self, floor_type, wall_color, roof_shape):
        self.__builder.build_floor(floor_type)
        self.__builder.build_wall(wall_color)
        self.__builder.build_roof(roof_shape)
        return self.__builder.get_result()


house_builder = HouseBuilder()
house_director = HouseDirector(house_builder)
print(house_director.build_house('大理石', '黒', '瓦屋根'))
