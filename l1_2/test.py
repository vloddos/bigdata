# C:\Users\User\Desktop\univer\bigdata\bigdata\l1_2
from l1_2 import controller, view

# a = controller.Animation(r'C:\Users\User\Desktop\univer\bigdata\bigdata\l1_2\test.json', 100000)
# a = controller.Animation(r'C:\Users\User\Desktop\univer\bigdata\lab2\file3_1000_563.json', 10000000)
a = controller.Animation(r'C:\Users\User\Desktop\univer\bigdata\lab2\file2_480_368.json', 1000000)
d = view.Drawer(a)
print(d.coords)
d.draw()
