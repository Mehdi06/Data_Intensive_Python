def fib():
    a, b = 0, 1
    while 1 : 
        yield b 
        a, b = b, a+b

f = fib()
print(next(f)) 
print(next(f)) 
print(next(f)) 
print(next(f)) 
print(next(f)) 


def CollatzGenerator():
    val = 23
    while 1 :
        yield val

        if val % 2 == 0:
            val = val /2
        else :
            val = val*3+1


collatz = CollatzGenerator()
n = 0
while n != 1 :
    n = next(collatz) 
    print(n)
