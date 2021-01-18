x = int(input("Unesi broj>>>"))
if x % 2 == 0:
    x -= 2
elif x % 2 == 1:
    x -= 1
for i in range(x,0,-2):
    print(i)

input("\nPretisni enter da izadjes")