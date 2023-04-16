import random

print(r"ni''/\]\]abcfd")

print(
    """dear nihao
          haojiu bujian 
          ni hai hao ma 
          山高水长，再见     """
)

"""
多行注释
"""

str1 = """I am a man of constant sorrow
I've seen troubles all my day
I'm goin' back to California
Place where I was partly raised
All through this world"""

list = str1.split("\n")
print(list)
for l in list:
    print(l.center(40, "-"))


def printTable(tableData):
    len1 = 0
    for i in range(len(tableData)):
        length = len(tableData[i])
        if length > len1:
            len1 = length

    for i in range(len(tableData[0])):
        str2 = ""
        for j in range(len(tableData)):
            str2 += tableData[j][i].rjust(len1)
            str2 += " "
        print(str2)


tableData1 = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]

printTable(tableData1)

# 虽然在 Python 中使用正则表达式有几个步骤，但每一步都相当简单。
# 1．用 import re 导入正则表达式模块。
# 2．用 re.compile()函数创建一个 Regex 对象（记得使用原始字符串）。
# 3．向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Match 对象。
# 4．调用 Match 对象的 group()方法，返回实际匹配文本的字符串。

import re

phoneNumCompile = re.compile(r"\d{3}-\d{3}-\d{4}")
phoneNum = phoneNumCompile.search("我的电话号码是 112-338-4499")
print(phoneNum.group())

# 利用括号分组
import re

numberCompile = re.compile(r"(\d{3})-(\d{3}-\d{4})")
numSerch = numberCompile.search("我的电话号码是 112-338-4499")
print(numSerch.group(1))
print(numSerch.groups())

# 匹配区号
import re

the_area_code = re.compile(r"(\(\d{3}\))-\d{3}-\d{4}")
numse = the_area_code.search("我的电话号码是 (112)-338-4499")
print(numse.group())

# 管道 |  如果要匹配 | 就\|
batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())

# ？ 可选的 如果要匹配 ？ 就用\?
question_compile = re.compile(r"(\(\d\d\d\)-)?\d\d\d-\d{4}")
qc = question_compile.search("我的电话号码是 338-4499")
print(qc.group())

# * 匹配0次或多次

# + 匹配一次或多次

# {}匹配次数
print(re.compile(r"(哈哈哈){0,5}").match("哈哈哈哈哈哈哈哈哈"))

# 贪心匹配，贪心匹配只会匹配最长的字符串
"""
Python 的正则表达式默认是“贪心”的，这表示在有二义的情况下，它们会尽
可能匹配最长的字符串。花括号的“非贪心”版本匹配尽可能最短的字符串，即在
结束的花括号后跟着一个问号。

"""

print(re.compile(r"(哈哈哈){0,5}?").match("哈哈哈哈哈哈哈哈哈").group(0))


"""
作为 findall()方法的返回结果的总结，请记住下面两点：
1．如果调用在一个没有分组的正则表达式上，例如\d\d\d-\d\d\d-\d\d\d\d，方法
findall()将返回一个匹配字符串的列表，例如['415-555-9999', '212-555-0000']。
2．如果调用在一个有分组的正则表达式上，例如(\d\d\d)-(\d\d\d)-(\d\d\d\d)，方
法 findall()将返回一个字符串的元组的列表（每个分组对应一个字符串），例如[('415',
'555', '1122'), ('212', '555', '0000')]。
"""
print(re.compile(r"(哈哈哈){0,5}?").findall("哈哈哈哈哈哈哈哈哈"))

# 字符分类
print(re.compile(r"[aeiouAEIOU]").findall("how are you today"))
# 非方框内字符
print(re.compile(r"[^aeiouAEIOU]").findall("how are you today"))

# 连续匹配方式
print(re.compile(r"[a-eB-C]").findall("how are you today"))

# ^开始 $结束
# 插入符号在前面，美元符号在后面。
print(re.compile(r"y$").search("how are you today"))


# 通配字符 .
atRegex = re.compile(r".at")
red = atRegex.findall("The cat in the hat sat on the flat mat.")
print(red)

# .* 匹配 所以字符
# 它使用贪心算法，尽可能的匹配最长的字符串
nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = nameRegex.search("First Name: Al Last Name: Sweigart")
print(mo.group(2))


# sub 替换
namesRegex = re.compile(r"Agent \w+")
ee = namesRegex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob.")

print(ee)
