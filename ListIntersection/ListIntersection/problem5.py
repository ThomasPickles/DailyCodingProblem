def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def first(a,b):
        return a
    return pair(first)

def cdr(pair):
    def last(a,b):
        return b
    return pair(last)

assert car(cons(1,2)) == 1
assert cdr(cons(1,2)) == 2

#Basially an easy exercise in functional programming

