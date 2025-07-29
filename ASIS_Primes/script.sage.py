import ast
import itertools
import string

import tqdm
from Crypto.Util.number import bytes_to_long, getPrime, inverse, long_to_bytes
from pwn import remote
from sage.all import Zmod, gcd, is_prime

E = string.printable[:63].encode() + b'_'

nbit = 640
conn = remote('65.109.189.98', '13737')

def generate_init_prime(init):
    for k in itertools.count(1):
        for item in itertools.product(E, repeat=k):
            init_prime = bytes_to_long(init + bytes(item) + b'}')
            if is_prime(init_prime):
                return init_prime
    return None

for _ in tqdm.trange(nbit - 512):
    conn.sendlineafter(b'[Q]uit', b'S')
    conn.sendlineafter(b'Please submit the primes p, q: ', b'Quack')
    conn.recvuntil(b'The input you provided is not valid! Try again!!')

while True:
    conn.sendlineafter(b'[Q]uit', b'S')
    conn.recvuntil(b': ')
    pinit = ast.literal_eval(conn.recvuntil(b'\n').decode())
    conn.recvuntil(b': ')
    qinit = ast.literal_eval(conn.recvuntil(b'\n').decode())

    p = generate_init_prime(pinit)
    q = generate_init_prime(qinit)

    conn.sendlineafter(b': ', f'{p},{q}'.encode())
    print((9 * p * q).bit_length())
    if (9 * p * q).bit_length() == 2 * nbit:
        break

conn.sendlineafter(b'[Q]uit', b'E')
conn.recvuntil(b' = ')
c = int(conn.recvuntil(b'\n').decode())

e = 65536
phi = (p - 1) * (q - 1)
l = gcd(e, phi)
d = inverse(e // l, phi // l)
m = pow(c, d, p * q)

while l > 1:
    m = (int(Zmod(p)(m).sqrt()) * inverse(q, p) * q + int(Zmod(q)(m).sqrt()) * inverse(p, q) * p) % (p * q)
    l //= 2

print(long_to_bytes(m).decode())
