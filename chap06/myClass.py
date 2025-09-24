from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "멍멍"
# a = Animal() # 에러: 추상 클래스는 인스턴스화 불가 
d = Dog()
print(d.sound()) # "멍멍"

a = Animal(Dog())
print(a.sound())

