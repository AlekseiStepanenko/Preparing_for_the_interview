
class Stack:

    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0


    def push(self, el):
        self.stack.append(el)



    def pop(self):
        if len(self.stack) == 0:
            return None
        remove_el = self.stack.pop()
        return remove_el


    def peek(self):
        return self.stack[-1]



    def size(self):
        return len(self.stack)




def add_elements_and_verification_stack(elements: str, name_stack: str):
    name_stack = Stack()
    for el in elements:
        name_stack.push(el)

    test_stack = []
    is_good = True
    for i in elements:
        if i in '({[':
            test_stack.append(i)
        elif i in ')}]':
            open_bracket = test_stack.pop()
            if open_bracket == '(' and i == ')':
                continue
            if open_bracket == '{' and i == '}':
                continue
            if open_bracket == '[' and i == ']':
                continue
            is_good = False
            break
    if is_good:
        print('Сбалансированно')
    else:
        print('Несбалансированно')





add_elements_and_verification_stack('(((([{}]))))', 's')


