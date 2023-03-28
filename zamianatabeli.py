# dz = [1,2,3,4]
#
# zlyjanek = []
#
# def danilo(dz):
#     a=dz[0]
#     b=dz[1]
#     c=dz[2]
#     d=dz[3]
#
#     a1=a
#     zlyjanek.append(a1)
#
#     a2=a+b
#     zlyjanek.append(a2)
#
#     a3=a+b+c
#     zlyjanek.append(a3)
#
#     a4=a+b+c+d
#     zlyjanek.append(a4)
#
#     print(zlyjanek)
#
# print(danilo(dz))

a =[1,2,3,4]

def sumatabeli(a):
    for i in range(1,len(a)):
        a[i]=a[i-1]+a[i]
    return a



print(sumatabeli(a))


