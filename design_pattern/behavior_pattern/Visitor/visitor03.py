from __future__ import annotations
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit(self, entory: Entry):
        pass

class ListVisitor(Visitor):
    def visit(self, entory: Entry):
        if type(entory) == Group:
            print(f'{entory.code}: {entory.name}')
        else:
            print(f'  {entory.code}: {entory.name}')

        for child in entory.get_children():
            child.accept(self)

class CountVisitor(Visitor):
    def __init__(self):
        self.__group_count = 0
        self.__employee_count = 0
    
    def visit(self, entory: Entry):
        pass

    def get_group_count(self):
        return self.__group_count
    
    def get_employee_count(self):
        return self.__employee_count
    
class Entry(ABC):
    def __init__(self, code, name):
        self.__code = code
        self.__name = name

    @property
    def code(self):
        return self.__code
    
    @property
    def name(self):
        return self.__name
    
    @abstractmethod
    def get_children(self):
        pass

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

class Group(Entry):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.__entries: list[Entry] = []

    def add(self, entry: Entry):
        self.__entries.append(entry)

    def get_children(self):
        return self.__entries
    
    def accept(self, visitor: Visitor):
        visitor.visit(self)

class Employee(Entry):
    def __init__(self, code, name):
        super().__init__(code, name)
    
    def get_children(self):
        return []
    
    def accept(self, visitor: Visitor):
        visitor.visit(self)