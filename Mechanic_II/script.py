import ast
import hashlib
import itertools
import string

import tqdm
from pwn import remote

conn = remote('91.107.252.0', '11111')
conn.recvuntil(b": (b'")
head = conn.recvuntil(b"'").strip(b"'")
conn.recvuntil(b"'")
hexdigest = conn.recvuntil(b"'").strip(b"'").decode()

def pass_pow():
    for iter_item in itertools.product(string.printable[:63] + '_', repeat=4):
        tail = ''.join(iter_item).encode()
        if hashlib.sha3_256(head + tail).hexdigest() == hexdigest:
            conn.sendline(tail)
            break

pass_pow()

for index in tqdm.trange(1337):
    conn.sendlineafter(b'[Q]uit', b'R')
    conn.sendlineafter(b': ', str(index).encode())

    conn.sendlineafter(b'[Q]uit', b'D')
    conn.sendlineafter(b': ', str(index).encode())
    conn.recvuntil(b'_shasec = ')
    shasec = ast.literal_eval(conn.recvuntil(b'\n').decode())

    conn.sendlineafter(b'[Q]uit', b'D')
    conn.sendlineafter(b': ', str(index + 1337).encode())
    conn.recvuntil(b'_shasec = ')
    _shasec = ast.literal_eval(conn.recvuntil(b'\n').decode())

    if shasec == _shasec:
        secret = hashlib.sha3_256(shasec + hashlib.sha3_256(shasec + str(index).encode()).digest()).hexdigest()

        conn.sendlineafter(b'[Q]uit\n', b'S')
        conn.sendlineafter(b': ', secret.encode())
        print(conn.recvuntil(b'\n').decode())
        break
