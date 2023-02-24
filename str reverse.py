class stack:
  def __init__(self):
    self.data='WATERMELON'
  def reverse(self):
    return self.data[::-1]
object=stack()
print(object.data)
print(object.reverse())

