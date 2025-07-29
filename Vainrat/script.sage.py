from Crypto.Util.number import long_to_bytes
from pwn import remote
from sage.all import RealField, sqrt

c = 20
prec = 440
R = RealField(prec)

conn = remote("91.107.252.0", "11117")
conn.recvuntil(b"We know y0 = ")
y0 = R(conn.recvuntil(b"\n").strip().decode())

for _ in range(c-1):
    conn.sendlineafter(b"[Q]uit", b"C")

conn.sendlineafter(b"[Q]uit", b"C")
conn.recvuntil(b"y = ")
yc0 = R(conn.recvuntil(b"\n").strip().decode())

conn.sendlineafter(b"[Q]uit", b"C")
conn.recvuntil(b"y = ")
yc1 = R(conn.recvuntil(b"\n").strip().decode())

xc0 = R(2) * yc1 ** 2 / yc0 - yc0
x0 = ((xc0 ** 2 - yc0 ** 2) * R(4) ** c + y0 ** 2) ** R(0.5)

# xc1 = yc1 ** 2 / yc0
# x0_squared = ((xc1 ** 2 - yc1 ** 2) * R(4) ** (c + 1) + y0 ** 2) ** R(0.5)

for k in range(1, prec):
    flag = long_to_bytes(int(x0 * R(10) ** k))
    if flag.startswith(b"CCTF{"):
        print(flag.decode())
