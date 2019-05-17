# for idle/st/etc...
import sys

p = r'C:/Users/User/Desktop/univer/bigdata/bigdata'
if p not in sys.path:
    sys.path.append(p)

from l2_boosted import controller, view

# a = controller.Animation(r'C:\Users\User\Desktop\univer\bigdata\lab2\file1_400_400.json', 1000000)
a = controller.Animation(r'C:\Users\User\Desktop\univer\bigdata\lab2\file2_100_100.json', 1000000)
# a = controller.Animation(r'C:\Users\User\Desktop\univer\bigdata\lab2\file2_500_500.json', 1000000)
# a = controller.Animation(r'C:\Users\User\Desktop\univer\bigdata\lab2\file2_480_368.json', 1000000)
d = view.Drawer(a)
# d.draw_PIL()
d.draw_mpl()
