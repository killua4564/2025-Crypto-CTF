## Information
|    name     |   category   | solves | score |   solver   |
|:-----------:|:------------:|:------:|:-----:|:----------:|
| Mechanic II | Tough Cookie |   28   |  146  | Killua4564 |

## Description
Mechanic II cranks PQC to hilarious levels, bring a quantum wrench and a PhD in pain.

## Writeup
* 這題完全靠 gemini 跟我解釋 kem 的結構XDD
* 在 kem 的 skey 結構中最後 32 bytes 是 nonce，基本上不影響正常的加解密，也就是說，假設有兩組 key pair (pkey1, skey1) 和 (pkey2, skey2)，然後 skey1' 和 skey2' 是 skey1 和 skey2 換了 nonce
  * pkey1 encaps 的東西由 skey1 和 skey1' decaps 會是「一樣」的東西
  * pkey1 encaps 的東西由 skey2 和 skey2' decaps 會是「不同」的東西
  * pkey2 encaps 的東西由 skey1 和 skey1' decaps 會是「不同」的東西
* 所以我們可以透過複製第 i 把 skey 並用第 i 和 i + 1337 把 skey 去 decaps 來知道 i 是不是萬中選一的那個 r（所以可執行次數才會是 3 * 1337）
* 找到 r 之後算出 secret 就可以得到 flag 了

## Flag
`CCTF{se3D5_4R3_!mp0rTaN7_3vErY_WheRE!}`
