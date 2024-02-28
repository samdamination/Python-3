# Using Python with the shell commands:
#    python3 -> goes into python shell
#    ^D -> goes back to zsh
#    mkdir/touch file.py -> create python file
#    nano file.py -> edit directly from terminal
#    python3 -i file.py -> allows to use contents of file and be interactive

# Sieve of Eratosthenes - finding prime numbers up to n
def sieve(n):
    A = [True]*(n + 1)
    A[1] = False # A[0] don't care
    pos = 2
    while pos <= n: # actually we can stop at sqrt(n)
        if A[pos]: # if A[p] == True same
            i = pos + pos
            while i <= n:
                A[i] = False
                i = i + pos
        pos = pos + 1
    return A

print(sieve(10))




