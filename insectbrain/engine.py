class Value:

    def __init__(self, data):
        self.data = data
        
    def __add__(self, other):
        val = Value(self.data + other.data)

    def __mul__(self, other):
        val = Value(self.data + other.data)


a = Value(5)
b = Value(8)

print(a+b)
print(a*b)
