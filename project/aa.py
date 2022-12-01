class A:
    def __init__(self):
        pass

class B(A):
    def __init__(self):
        pass

b = A()

print(isinstance(b, B))