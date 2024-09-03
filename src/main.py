class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

# Create an instance of MyClass
obj = MyClass("Maciek")

# Call the greet method
obj.greet()