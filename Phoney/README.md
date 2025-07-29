## Information
|  name  |   category   | solves | score | solver |
|:------:|:------------:|:------:|:-----:|:------:|
| Phoney | Brain Buster |   25   |  159  |        |

## Description
Phoney laughs! Until you unpick its multi-prime RSA and random message lock.

## Writeup
* 已知 p, q, r 是 512, 576, 640 bits 的質數，給
  * $n = p * q * r$
  * $s = inverse(p, q * r) + p$
  * $q_0 = q \mod {p}$
* 首先把 $p$ 求出來
  * $s = inverse(p, q * r) + p$
  * $s - p = p ^ {-1} \mod (q * r)$
  * $p * (s - p) - 1 = k * q * r = k * \frac{n}{p}$
  * $p ^ {3} - s * p ^ {2} + p = 0 \mod {n}$
  * 在 `Zmod(n)` 底下造出多項式用 `beta=1` 和 `epsilon=1/32` 拿到 $p$
* 再來是 $q$
  * $q_0 = q \mod {p}$
  * $q = k * p + q_0$
  * 在 `Zmod(n / p)` 底下造出 `monic` 多項式用 `X=1<<80` 和 `beta=0.4` 拿到 $q$ (個人覺得蠻暴力的)
* 接下來拿 `e` 和 `c` 算回 flag 即可

## Flag
`CCTF{c0UlD_b3_ReCoVEr3d_v!4_Coppersmiths_m3ThOd?}`
