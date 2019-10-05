from pwn import *
from time import sleep

import hashlib
import sys

def solve(prefix, difficulty):
    zeros = '0' * difficulty

    def is_valid(digest):
        digest = [ord(i) for i in digest]
        bits = ''.join(bin(i)[2:].zfill(8) for i in digest)
        return bits[:difficulty] == zeros

    i = 0
    while True:
        i += 1
        s = prefix + str(i)
        if is_valid(hashlib.sha256(s.encode()).digest()):
            return str(i)

conn = remote('52.201.239.96', 9487)
sleep(0.5)
gg = conn.recv()
print gg

index = gg.find("prefix = \"") + 10
rindex = gg.find("\"", index)

res = solve(gg[index:rindex], 23)
print res
conn.sendline(res)
sleep(1)
p1 = "[print(sum(map(int,input().split())))for _ in[0]*int(input())]"
conn.sendline(p1)
print conn.recvuntil("Congrats")
print conn.recv()
p2 = "[[[z.__setitem__(j,max(z[j],z[c+j]+v))for _ in[0]*n for v,c in[map(int,input().split())]for j in range(w-c)],print(z[0])]for(n,w),z in[(map(int,input().split()),[0]*3001)]]"
conn.sendline(p2)
print conn.recvuntil("Congrats")
print conn.recv()
p3 = "[[[d.__setitem__(i+1,d[int(e)]+1)for i, e in enumerate(input().split()[1:])],print(max(d))]for d in[[0]*int(input())]]"
conn.sendline(p3)
print conn.interactive()
