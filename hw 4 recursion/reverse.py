def reverse_(input):
    rev=''
    i=len(input)-1
    while i>=0:
        rev+=input[i]
        i-=1
    return rev 
#print(reverse_('hello'))

def _reverse(input):
    input = str(input)
    if len(input) == 0:
        return ""
    else:
        return input[-1] + _reverse(input[:-1])

print(_reverse(12345)) 
