def palindrome(x):
  x=x.upper()
  if len(x)==1 or len(x)==0:
    return True
  else:
    if x[0]==x[-1]:
      x=x[1:-1]
      return palindrome(x)
      
    else:
      return False

a=palindrome("racecar")
print(a)