import sys
for arg in sys.argv:
        if '.' not in arg:
                ran = int(arg)
cola = [2, 5]
colb = [3, 7]
for i in range(ran):
	cola.append(cola[1] + (i + 1) * 6)
	colb.append(colb[1] + (i + 1) * 6)
c = list(set(cola).union(set(colb)))
c.sort()

expr = lambda n, x :n**2 + 2*x*n
for n in c:
        removed = {}
        for j in range(ran):
                if expr(n, j) in c and expr(n,j) <= max(c):
                        c.remove(expr(n, j))

                       
        print("For n = {0} , removed : {1}".format(n , removed))

print(c)

