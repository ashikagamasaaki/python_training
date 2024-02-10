from abc import ABC, abstractmethod

class Applicant:
    def __init__(self, name, age, gendar):
        self.__name = name
        self.__age = age
        self.__gendar = gendar
        
    @property
    def name(self):
        return self.__name
        
    @property
    def age(self):
        return self.__age
        
    @property
    def gendar(self):
        return self.__gendar
    
    def __str__(self):
        return f'氏名: {self.name}, 年齢: {self.age}歳, 性別: {self.gendar}'
    
# Aggregate
class IInterviewPlace(ABC):
    def __init__(self):
        self._applicants: list[Applicant] = []
    
    @abstractmethod
    def recept(self, applicant: Applicant):
        pass
    
    @abstractmethod
    def get_applicants(self):
        pass
    
    @abstractmethod
    def get_count(self):
        pass
    
    @abstractmethod
    def get_iterator(self):
        pass

# ConcreteAggregate
class InterviewPlace(IInterviewPlace):
    def recept(self, applicant: Applicant):
        self._applicants.append(applicant)
    
    def get_applicants(self):
        return self._applicants

    def get_count(self):
        return len(self._applicants)
    
    def get_iterator(self):
        return InterviewIterator(self)

# Iterator
class IInterviewIterator(ABC):
    def __init__(self, interview_place: IInterviewPlace):
        self._position = 0
        self._interview_place = interview_place
    
    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

class InterviewIterator(IInterviewIterator):
    def has_next(self):
        return self._position < self._interview_place.get_count()
    
    def next(self):
        if self.has_next():
            applicant = self._interview_place.get_applicants()[self._position]
            print(applicant)
            self._position += 1
            return applicant
        print('応募者はもういません')
        return


tanaka = Applicant('Tanaka', 17, '男')
yamada = Applicant('Yamada', 19, '女')
sato = Applicant('Sato', 20, '男')
saito = Applicant('Saito', 23, '男')
kondo = Applicant('Kondo', 30, '女')
okita = Applicant('Okita', 34, '男')

interview_place = InterviewPlace()
interview_place.recept(tanaka)
interview_place.recept(yamada)
interview_place.recept(sato)
interview_place.recept(saito)
interview_place.recept(kondo)
interview_place.recept(okita)

iterator = interview_place.get_iterator()
iterator.next()
iterator.next()
iterator.next()
iterator.next()
iterator.next()
iterator.next()
iterator.next()
iterator.next()