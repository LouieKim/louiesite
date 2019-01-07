print("test01")

f = open("test01.txt", 'w')
for i in range(1, 11):
    data = "%d line.\n" % i
    f.write(data)
f.close()