# python 装饰器

'''
输出之前输出type
'''
def add_type(func):
    def wrapper(something):  # 指定一毛一样的参数
        print('#' + '-' * 10 + "[DEBUG]: type: {}".format(type(something)) + '-' * 10 + '#')

        return func(something)

    return wrapper  # 返回包装过函数


@add_type
def my_print(someting):
    print(someting)
