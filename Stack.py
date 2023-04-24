
class Stack:
    def __init__(self, data_type, max_size):
        self.data_type = data_type
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top_index = -1
#   add element to the stack

    def push(self, element):
        if self.top_index == self.max_size - 1:
            print("Stack overflow")
            return
        elif type(element) != self.data_type:
            print("Invalid data type")
            return
        else:
            self.top_index += 1
            self.stack[self.top_index] = element
#   remove element from stack and return its value

    def pop(self):
        if self.top_index == -1:
            print("Stack underflow")
            return
        else:
            element = self.stack[self.top_index]
            self.stack[self.top_index] = None
            self.top_index -= 1
            return element
#   return True if stack is empty and False if not

    def isempty(self):
        return self.top_index == -1
#   return value of the element on the top of stack

    def top(self):
        if self.top_index == -1:
            print("Stack is empty")
            return
        else:
            return self.stack[self.top_index]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def add(self, string):
        for char in string:
            node = Node(char)
            if self.head is None:
                self.head = node
                self.length = 1
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node
                self.length += 1

    def check_palindrome(self):

        stack = Stack(str , self.length)
        current = self.head

        while current is not None:
            stack.push(current.data)
            current = current.next

        current = self.head

        while current is not None:
            if current.data != stack.pop():
                print("This is not a palindrom")
                return False
            current = current.next

        print("It is a palindrom")
        return True
            

def infix_to_postfix(expresion):

    importance = {'+': 2, '-': 2, '*': 1, '/': 1}

    elements = expresion.split(' ')
    elements.remove('')

    stack = Stack(type(expresion), len(elements))
    
    equation = ""

    for element in elements:
        
        if element.isdigit() or '.' in element or ('-' in element and element.replace('-','').isdigit()):
            equation += element + " "
             
        elif element == '(':
            stack.push(element)
            
        elif element == ')':
            while stack.top() != '(':
                
                equation += stack.pop() + " "
            stack.pop()
            
        else:
            while ((not stack.isempty()) and stack.top() != '(' and importance[element] <= importance[stack.top()]):
                equation += stack.pop() + " "
            stack.push(element)
            

    while not stack.isempty():
        equation += stack.pop() + " "
        
    return equation


def calculate_postfix(expresion):

    stack = Stack(type(expresion), len(expresion))

    elements = expresion.split(' ')
    
    elements.remove('')
    
    for element in elements:
        if element.isdigit() or '.' in element or ('-' in element and element.replace('-','').isdigit()):
            stack.push(element)
        else:

            a = float(stack.pop())
            b = float(stack.pop())
            
            if element == '+':
                result = a + b
            elif element == '-':
                result = b - a
            elif element == '*':
                result = a * b
            elif element == '/':
                result = b / a
            else:
                print("invalid operator")
                return
            
            stack.push(str(result))

    result = float(stack.top())

    return result


if __name__ == "__main__":

    postfix_eq = infix_to_postfix('17.23 * ( -2 + 3 )  + 4 + ( -89867 * 5 )')
    print("expresion in postfix: ", postfix_eq)
    print("its value: ", calculate_postfix(postfix_eq))
    List = LinkedList()
    List.add("antna")
    List.check_palindrome()