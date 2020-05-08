class PlayerCharacter:

  memebership = True # Static Attribute
  def __init__(self, name, age): #dynamic attributes ## This is a Constructor Function
    if (PlayerCharacter.memebership):
      self.name = name
      self.age = age

  def shout(self):
    print(f'my name is {self.name} and age is {self.age}')
    return 'done'

  def run(self, hello):
    print(f'my name is {self.name}')

player1 = PlayerCharacter('Cindy', 49)
player2 = PlayerCharacter('Andrew', 30)
player2.attack = 50

print(player1.shout())
print(player2.shout())