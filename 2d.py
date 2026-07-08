def soma(x, y, z):
    if z == '+':
        return (x+y)
    elif z == '-':
        return (x-y)
    elif z == '*':
         return (x*y)
    elif z == '/':
         return (x/y)
txt1 = soma(50,2,'+')
print (txt1)
txt2 = soma(50,2,'-')
print (txt2)
txt3 = soma(50,2,'*')
print (txt3)
txt4 = soma(50,2,'/')
print (txt4)
