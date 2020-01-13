# LeetCode-in-Python
[![LeetCode 排名](https://img.shields.io/badge/{{.Username}}-{{.Ranking}}-blue.svg)](https://leetcode.com/{{.Username}}/)
 [![Python](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/)

LeetCode在线提交测试速度很慢，在做的的过程中发现调试很不方便，特别是有时候没注意到的`Syntax error`，要浪费很多时间，就打算把做过的题目全部可以本地化，希望能提高一些效率。

有些题目需要自定义一些数据结构，集中放在了`datastruct`目录下。

## 使用pytest进行本地调试

 已解决的题目都包含了本地测试用例，无需使用网络就可以进行测试。测试用例如下：

```python
tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 7, 0, 1], 3, [0, 2]),
        ]
```
每一行为一个用例，`tuple`的前几个为输入的参数，最后一个为期望结果。



测试所有题目：

`pytest solutions`

测试数据结构：

`pytest datastruct`

