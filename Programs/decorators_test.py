# Write your code here :-)

def mydec(myfunc):

    def wrapper(a,b):
        #a = args[0]
        #b= args[1]
        if a<b:
            a,b = b,a
        return myfunc(a,b)

    return wrapper

def new_decor(myfunc):
    def inner_func(*args,**kwargs):
        print(*args)
        print(*kwargs)
        return myfunc(*args,**kwargs)
    return inner_func


@new_decor
def div(x,y):
    print('hello')
    print(x/y)

#div(8,4)

@mydec
def div(x,y):
    print(x/y)

div(2,4)


"""
def decorator_func(original_func):

    def wrapper_func():
        print('wrapper executed the function: {}'.format(original_func.__name__))
        return original_func()
    return wrapper_func

@decorator_func
def display():
    print('displaying display func')

display()

"""

