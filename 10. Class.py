
Two kinds of object's in Python's OOP model: class object and instance object.

'''
オブジェクトの設計をクラスという. Class = variable + method.
For exampel: student class (name, birthday, course), teacher class(name, birthday, lecture)
             Triangle class (bottom, height, area, edge; calc_area, calc_edge) 
'''

"""define a class"""
class Dog:
  # class attribute
  species = 'mammal'
  
  # Constractor: which function's name same as class name. class 内の"__init__"を自動的に呼び出す. 
  # method of initialization instance 
  def __init__(self, name, age):# why use (self, name age)?
    self.name = name
    self.age = age
    
  # Instance method: used to get the contents of an instance.
  # create same as function; add "self" before argument.
  def description(self):# why only self?
    # use return or print()
    return "{} is {} years old".format(self.name, self.age)
  def speak(self, sound):
    return "{} says {}".format(self.name, sound)
    
# オブジェクトやインスタンス: クラスに基づいて実際に作成した個々のもの, so class.(argument)
# Every object is an instance of a class. For Example: Kevin is human.
# Create instance "philo" and "mikey"
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# call instance method: instance.method()
print(philo.description())
print(mikey.speak("Gruff Gruff"))


""" conbine two class in one class"""
class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
        
    def introduce_self(self):
        print("My name is " + self.name)
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i
        
    def sit_down(self):
        self.is_sitting = True
    
    def stand_up(self):
        self.is_sitting = False
p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

p1.robot_owned = r1
p2.robot_owned = r2

p1.robot_owned.introduce_self()




