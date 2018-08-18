
Two kinds of object's in Python's OOP model: class object and instance object.

'''
オブジェクトの設計をクラスという. Class = variable + method.
For exampel: student class (name, birthday, course), teacher class(name, birthday, lecture)
             Triangle class (bottom, height, area, edge; calc_area, calc_edge) 
'''


'''define a simple class'''
class Dog:
# メソッドの文法は関数と同じ     
  pass
# create instance of class
Dog()
Dog()

# メソッドの使用：インスタンス名＋メソッド名
a = Dog()
b = Dog()


"""define a more complex class"""
class Dog:
  # class attribute
  species = 'mammal'
  
  # Constractor: which function's name same as class name. class 内の"__init__"を自動的に呼び出す. 
  # a method of initialization instance 
  def __init__(self, name, age):# self: reference to the class itself.
    # selfでアクセス
    self.name = name
    self.age = age
    
  # Instance method: used to get the contents of an instance.
  # create same as function; add "self" before argument.
  def description(self):
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
