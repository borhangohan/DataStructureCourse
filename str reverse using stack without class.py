def size(stack):
    return len(stack)

def isempty(stack):
    if size(stack)==0:
        return True
    else:
        return False

def push(stack, item):
    stack.append(item)

def pop(stack):
    if isempty(stack):
        print('Stack is empty')
    else:
        return stack.pop()

def peek(stack):
    if isempty(stack):
        print('Stack is empty')
    else:
        return stack[-1]

def revstring(str):
    for ch in str:
        push(stack, ch)
    for i in stack:
        print(i, end='')
    print()
    rev=''
    for i in range(0, size(stack)):
        ch=peek(stack)
        rev+=ch
        pop(stack)
    return rev

stack=[]

print(revstring('WATERMELON'))


'''
push(stack, 'W')
push(stack, 'A')
push(stack, 'T')
push(stack, 'E')
push(stack, 'R')
push(stack, 'M')
push(stack, 'E')
push(stack, 'L')
push(stack, 'O')
push(stack, 'N')
push(stack, 'Watermelon')
for i in stack:
    print(i, end='')
print()
print('peeked:',peek(stack))
'''






    