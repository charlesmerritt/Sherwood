def exception_handler(func):
    """
    Decorator to handle exceptions in functions
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"{func.__name__} raised an exception: {e}")
    return inner