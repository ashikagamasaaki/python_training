import pytest
import unittest01

class TestCal(object):
    @classmethod
    def setup_class(cls):
        cls.cal = unittest01.Cal()
        
    @classmethod
    def teardown_class(cls):
        del cls.cal
    
    def setup_method(self, method):
        print('method={}'.format(method.__name__))
    
    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
    
    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        print(os_name)
        
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            cal = unittest01.Cal()
            cal.add_num_and_double('1', '1')