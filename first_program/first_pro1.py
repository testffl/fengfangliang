#斐波拉起数列
"""a,b = 0,1
while (b < 100):
    print(b,end = ',')
    a,b = b,a+b
"""
#九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
