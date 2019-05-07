from .stack_array import ArrayStack


def reverse_data(data):
    s = ArrayStack()
    reversed = ""

    for i in data:
        s.push(i)

    while not s.is_empty():
        reversed += s.pop()
    return reversed


def is_matched(expr):
    lefty = "({["
    righty = ")}]"

    s = ArrayStack()

    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index((s.pop())):
                return False
    return s.is_empty()
