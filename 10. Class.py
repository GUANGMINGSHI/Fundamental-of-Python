
Two kinds of object's in Python's OOP model: class object and instance object.

'''
オブジェクトの設計をクラスという. Class = variable + method.
For exampel: student class (name, birthday, course), teacher class(name, birthday, lecture)
             Triangle class (bottom, height, area, edge; calc_area, calc_edge) 
'''
# define a class
class Dog:
  # class attribute
  species = 'mammal'
  
  # Constractor: which function's name same as class name. class 内の"__init__"を自動的に呼び出す. 
  # "__init__"can initialization instance.
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  # Instance method: used to get the contents of an instance.
  # create same as function; add "self" before argument.
  def description(self):
    return "{} is {} years old".format(self.name, self.age)
  def speak(self, sound):
    return "{} says {}".format(self.name, sound)
    
# Create instance: class.(argument)
# クラスに基づいて実際に作成した個々のものをオブジェクトやインスタンスという.
# Every object is an instance of a class. For Example: Kevin is human.
# For example: two Triangle class (h = 1, b = 1) or (h = 2, b = 2).
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# call instance method: instance.class()
print(philo.description())
print(mikey.speak("Gruff Gruff"))






