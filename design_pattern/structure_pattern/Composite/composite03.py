from abc import ABC, abstractmethod

# Component インターフェース
class OrganizationComponent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self):
        pass


# Leaf クラス (従業員)
class Employee(OrganizationComponent):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position

    def display(self):
        print(f'従業員: {self.name}({self.position})')


# Composite クラス (部門)
class Department(OrganizationComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children: list[OrganizationComponent] = []

    def add(self, component: OrganizationComponent):
        self.children.append(component)

    def remove(self, component: OrganizationComponent):
        self.children.remove(component)

    def display(self):
        print(self.name)
        for child in self.children:
            if type(child) == Employee:
                print(f'  {child.name}({child.position})')
            else:
                child.display()
                


# 使用例
# 以下は使用例です
# IT 部門
it_department = Department("IT Department")

# IT 部門に従業員を追加
developer = Employee("John", "Developer")
developer2 = Employee("Mike", "Developer")
developer3 = Employee("Mark", "Developer")
manager = Employee("Sakata", "Manager")
it_department.add(developer)
it_department.add(developer2)
it_department.add(developer3)
it_department.add(manager)

# サブ部門: QA 部門
qa_department = Department("QA Department")

# QA 部門に従業員を追加
tester1 = Employee("Alice", "Tester")
tester2 = Employee("Bob", "Tester")
qa_department.add(tester1)
qa_department.add(tester2)

# IT 部門に QA 部門を追加
it_department.add(qa_department)

it_department.display()