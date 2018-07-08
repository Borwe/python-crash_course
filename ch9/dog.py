class Dog():
    """A simple attempt to model a dog."""

    def __init__(self,name,age):
        """initialize name and age attributes"""
        self.name=name
        self.age=age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over!")


my_dog=Dog('willie',6)
my_dog.sit()
my_dog.roll_over()