import contextlib

from boltons import iterutils
from quantcrypt.cipher import KryptonKEM
from quantcrypt.errors import CipherVerifyError
from quantcrypt.kem import MLKEM_1024

kem = MLKEM_1024()
kry = KryptonKEM(MLKEM_1024)

with open("output.raw", "rb", encoding="utf-8") as file:
    skeys = list(iterutils.chunked_iter(file.read(), kem.param_sizes.sk_size))

count = 22
for skey in reversed(skeys):
    with contextlib.suppress(CipherVerifyError):
        kry.decrypt_to_file(skey, f'flag_{count}.enc', f'flag_{count-1}.enc')
        count -= 1
