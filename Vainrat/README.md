## Information
|  name   |   category    | solves | score | solver |
|:-------:|:-------------:|:------:|:-----:|:------:|
| Vainrat | Getting There |   67   |  72   | Xtrimi |

## Description
Precision is key, Vainrat escapes sluggish calculators effortlessly.

## Writeup
* 看著 Xtrimi 當時的 payload 寫的
* 主要思路是，如果計算會讓精度失真，那要想辦法減少計算
* 先把 `rat` 簡化，得到遞歸數列
  * $x_1 = \frac{x_0 + y_0}{2}$
  * $y_1 = \sqrt{x_1 * y_0}$
  * $x_1 ^ 2 - y_1 ^ 2 = \frac{x_0 ^ 2 - y_0 ^ 2}{4}$
  * 也就是說 $x_{20} ^ 2 - y_{20} ^ 2 = \frac{x_0 ^ 2 - y_0 ^ 2}{4 ^ {20}}$
* $y_0$ 一開始就給了，為了程式的穩定性這邊選澤 `c=20` 去做計算，拿到 $y_{20}$ 和 $y_{21}$
  * $x_{20} = \frac{2 * y_{21} ^ 2}{y_{20}} - y_{20}$
  * $x_0 = \sqrt{(x_{20} ^ 2 - y_{20} ^ 2) * 4 ^ {20} + y_0 ^ {2}}$
* 最後用 $x_0$ 嘗試不同精度去還原 flag

## Flag
`CCTF{h3Ur1s7!c5_anD_iNv4rIanTs_iN_CryptoCTF_2025!}`
