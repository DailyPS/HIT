from pwn import *
import re

process = remote("127.0.0.1", 9007)
process.recv(10024)

for i in range(100):
    condition = process.recv(1024).decode("UTF-8").strip().split(' ')    
    print(condition)

    N = int(condition[0].split("=")[1])
    C = int(condition[1].split("=")[1])

    start = 0
    end = N

    for j in range(C):
        msg = ' '.join(str(start) for start in range(start, int((start + end) / 2)))
        process.sendline(msg)
        output = int(process.recv(1024).decode("UTF-8").strip())

        if (output % 10 == 0):
            start = int((start + end) / 2)

        else:
            end = int((start + end) / 2)

    process.sendline(str(start))

    print(process.recv(1024).decode("UTF-8"))

print(process.recv(1024).decode("UTF-8"))
process.close()