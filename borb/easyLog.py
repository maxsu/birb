
def log(format, *args):
    if args:
        print(format.format(*args))
    else: print(format)