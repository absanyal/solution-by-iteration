#Solution of equation by iteration method
#30/05/2016

#The given equation is x**2 - 5*x + 6 = 0
#The roots are x = 2, 3

def f1(x):
    f = (-6) * (1 / (x - 5))
    return f

def f2(x):
    f = (x**2 + 6)/5
    return f

p1 = 2.99
r = 2

print ("p = " + str(p1) + "\n")

print ("Using f1")

p = p1
r = 2

k = abs((p-r))/r

i = 0

err = 10**(-10)

while (k > err):
    p = f1(p)
    k = abs((p-r))/r
    i = i + 1

print(p)
print("Converged in " + str(i) + " steps." + "\n" + "*"*20)

s1 = p

print("Using f2")

p = p1
r = 2

k = abs((p-r))/r

i = 0

while (k > err):
    p = f2(p)
    k = abs((p-r))/r
    i = i + 1

print(p)
print("Converged in " + str(i) + " steps." + "\n" + "*"*20)

s2 = p

print ("s2 - s1 = " + str(s2 - s1))