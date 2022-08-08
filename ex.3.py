a = []
b = range(1000)
for x in b:
  if x%2 !=0:
    a.append(x**3)
    
print(a)

sum = 0
for x in a:
  s = 0
  while (x != 0):
    s = s + x % 10
    x = x // 10
  if s%7 == 0:
    print(s)
