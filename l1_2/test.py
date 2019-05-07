# C:\Users\User\Desktop\univer\bigdata\bigdata\l1_2
from l1_2 import controller, view

# a = controller.Animation(r'C:\Users\User\Desktop\univer\bigdata\bigdata\l1_2\test.json', 100000)
# a = controller.Animation(r'C:\Users\User\Desktop\univer\bigdata\lab2\file3_1000_563.json', 10000000)
a = controller.Animation(r'C:\Users\User\Desktop\univer\bigdata\lab2\file2_500_500.json', 1000000)
# a = controller.Animation(r'C:\Users\User\Desktop\univer\bigdata\lab2\file1_30_30.json', 1000000)
d = view.Drawer(a)
d.draw()
