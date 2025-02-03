class ClassDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print('decorator called')
        print(f'Excuting {self.func.__name__}')
        return self.func(*args, **kwargs)

@ClassDecorator
def say_hello():
    print("hello")

say_hello()
# decorator called
# Excuting say_hello
# hello