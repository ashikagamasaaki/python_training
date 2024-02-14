import os

class Cal(object):
    def add_num_and_double(self, x, y):
        """Add and double

        >>> c = Cal()
        >>> c.add_num_and_double(1,1)
        4
        
        >>> c.add_num_and_double('1','1')
        Traceback (most recent call last):
        ...
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result
    
    def save(self, dir_path, file_name):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w') as f:
            f.write('test')
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()