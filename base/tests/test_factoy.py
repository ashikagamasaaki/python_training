from practice.factory import CarCreater
from practice.factory import PlaneCreater
from practice.factory import Vehicle
from practice.factory import VehicleFactory

def test_abstract_method1():
    mock_instance = CarCreater().create()
    assert mock_instance.start() == "発車します"
    
def test_abstract_method2():
    mock_instance = CarCreater().create()
    assert mock_instance.stop() == "停車します"
    
def test_abstract_method3():
    mock_instance = PlaneCreater().create()
    assert mock_instance.start() == "離陸します"
    
def test_abstract_method4():
    mock_instance = PlaneCreater().create()
    assert mock_instance.stop() == "着陸します"

def test_abstract_method5():
    Vehicle.__abstractmethods__ = set()
    vehicle = Vehicle()
    assert None == vehicle.start()
    assert None == vehicle.stop()

def test_abstract_method6():
    VehicleFactory.__abstractmethods__ = set()
    factory = VehicleFactory()
    assert None == factory.create()