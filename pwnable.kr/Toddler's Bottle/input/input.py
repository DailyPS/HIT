from pwn import *

#stage 1
argvs = ["" for i in range (0, 100)]
argvs[65] = "\x00"
argvs[66] = "\x20\x0a\x0d"
argvs[67] = "8888"

#stage2 stderr
with open('./stderr', 'a') as f:
    f.write("\x00\x0a\x02\xff")

#stage 3
envs = {"\xde\xad\xbe\xef":'\xca\xfe\xba\xbe'}

#stage 4
with open('./\x0a', 'a') as f:
    f.write("\x00\x00\x00\x00")

target = process(executable='/home/input2/input', argv=argvs, stderr=open('./stderr'), env=envs)

#stage2 stdin
target.sendline("\x00\x0a\x00\xff")

#stage 5
conn = remote('localhost', 8888)
conn.send("\xde\xad\xbe\xef")

print(target.recvall())