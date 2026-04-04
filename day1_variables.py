# 变量、输入输出练习

# 练习1：个人信息打印
name="欧阳思琦"
age=17
major="网络安全"
print(f"我叫{name},今年{age},专业{major}")

# 练习2：圆面积计算
import math
radius=float(input("输入圆面积："))
area=math.pi*radius**2
print(f"半径{radius}圆面积{area:.2f}")

# 变量与输入输出笔记
'''
## input() 和 print()
input() 读取用户输入，返回字符串。
print() 输出内容，可以拼接多个字符串。

## 格式化字符串
f"...{变量}..."直接在字符串中嵌入变量，方便清晰。
{变量:.2f} 控制浮点数小数位数。

## 练习1 要点
变量定义直接赋值即可。
print 可以输出多个内容，用逗号分隔，但 f-string 更直观。

## 练习2 要点
float(input()) 将输入转为浮点数。
math.pi 是圆周率，需要先 import math。
计算面积公式 `πr²`，用 `**` 表示乘方。

## 易错点
- 忘记转换类型，直接 radius = input() 会导致乘法出错。
- 格式化输出时漏掉f前缀，变量不会替换。
'''