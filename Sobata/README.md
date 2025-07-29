## Information
|  name  |   category    | solves | score | solver |
|:------:|:-------------:|:------:|:-----:|:------:|
| Sobata | Getting There |   44   |  102  | hokak  |

## Description
Master Sobata by dissecting ECC secrets, then tame its walk function’s hidden path.

## Writeup
https://hackmd.io/@hokak/CryptoCTF2025#sobata

* 接續上述 writeup 講的簡單解法
* 我的目光放在 (a, b) 的生成分別是 $R_{0} ^ \frac{p-1}{3}$ 和 $R_{1} ^ \frac{p-1}{2}$
* 所以 walk 的寫法如果最後沒有乘上 $c$ 的話就會是只有 6 個點的 subgroup
* 但乘上 $c$ 之後就會把 $Q$ 跳去不同的 subgroup，所以可以在 jump 輸入 -1 把他跳回來
* 也就是說 enc_flag -> jump(-1) -> jump(0) (repeat 4 times) -> flag

## Flag
`CCTF{L1n3Ari7y_iN_w4lkIn9_ECC!}`
