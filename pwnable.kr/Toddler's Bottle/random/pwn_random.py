from pwn import *

shell = ssh('random', 'pwnable.kr', password='guest', port=2222)

payload = "3039230856"

process = shell.process(executable='./random', argv=['random'])
process.sendline(payload)

print(process.recvall().decode('utf-8', 'replace'))

process.close()
shell.close()