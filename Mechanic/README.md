## Information
|   name   |  category  | solves | score |   solver   |
|:--------:|:----------:|:------:|:-----:|:----------:|
| Mechanic | Easy-Peasy |  109   |  50   | Killua4564 |

## Description
Mechanic’s ‘post-quantum’ lock is so easy, even Schrödinger’s cat could crack it, alive and dead.

## Writeup
* 給你 40 個有序的 skey，只有其中 22 個是真的，並對 flag 圖片做了加密
* 看起來是背包問題，但其實放入不對的 skey 會噴 `CipherVerifyError`
* 所以倒序著每個試試看即可，最後拿到 flag.png

## Flag
`CCTF{k3y_3NcAp5uL4t!0n_M3cH4n1Sms!}`
