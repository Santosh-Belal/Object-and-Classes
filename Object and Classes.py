class person:

  def __init__(self,name,age):

    self.name=name

    self.age=age

  def my_func(self):

        print("Hello how are you ?"+ self.name)

  def __str__(self):

        return f"({self.name})({self.age})"

data=person("Ram",20)

data.my_func()

print(data)
