## Information
|    name     |   category    | solves | score |   solver   |
|:-----------:|:-------------:|:------:|:-----:|:----------:|
| ASIS Primes | Getting There |   40   |  110  | Killua4564 |

## Description
ASIS Primes is a cryptography challenge requiring primes with printable, meaningful bytes; can you generate such primes effectively?

## Writeup
* 這題就單純找質數，如果符合他一堆條件的話就讓你設定客製化的 p, q
* 如果輸入的值會出意外，則會幫你把 nbit 調高，如果正常的數字但只是沒痛過驗證的話則不會
* 我自己是設定 nbit 要是 640，所以先故意輸入了 640 - 512 次的錯誤值，然後不斷地抽獎嘗試把 p, q 塞進去
* 最後要注意加密的 e ^ 1 會變成 65536，所以拿到 enc_flag 解回來後要去處理開模方的問題
* 幸運抽中就能拿到 flag 啦～

## Flag
`CCTF{3AzY_RSA_cH4l13n9E_!n_ASIS_CTF!!}`
