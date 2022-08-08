#задание1
duration = int(input("введите число:"))
a = duration
b = a%3600
if duration > 86400:
   print(f"{int(a/86400)} дней ", end='' )

if duration > 3600:
   print(f"{int((a/3600)%24)} часов ", end='' )
  
if duration > 60:
   print(f"{int((a/60)%60)} минут ", end='' )
  
print(f"{int(a%60)} секунд ", end='' )

