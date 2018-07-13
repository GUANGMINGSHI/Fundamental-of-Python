
Two kinds of object's in Python's OOP model: class object and instance object.

オブジェクトの設計をクラスという. Class consist of variable and method.
For exampel: student class (name, birthday, course), teacher class(name, birthday, lecture)
             Triangle class (bottom, height, area, edge; calc_area, calc_edge) 

クラスに基づいて実際に作成した個々のものをオブジェクトやインスタンスという. For example: two Triangle class (h = 1, b = 1) or (h = 2, b = 2).

every object is an instance of a class. For Example: Kevin is human.

# define a class
class Dog:
  # class attribute
  species = 'mammal'
  
  # Constractor: which function's name same as class name. class 内の"__init__"を自動的に呼び出す. "__init__"can initialization instance.
  def __init__(self, x1, x2):
    self.num1 = x1
    self.num2 = x2
    
  # Method: create same as function, but should add "self" before argument.
  def description(self):
    return "{} is {} years old".format(self.name, self.age)
  def speak(slef, sound):
    return "{} says {}".format(self.name, sound)
    
# Create instance: class.(argument)
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# call method: instance.class()
print(philo.description())
print(mikey.speak("Gruff Gruff"))






