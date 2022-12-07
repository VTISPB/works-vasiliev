class A:
    def __init__(self):
        pass

class C:
    def __init__(self):
        pass

class B(A, C):
    def __init__(self):
        pass

b = B()

print(isinstance(b, B))