import os
import shelve

files = ["a", "b", "c"]
for i in files:
    fileName = os.path.join("D://learning code//python", i)
    print(fileName)


# 获取当前文件夹
print()
str = os.getcwd() + "\haha\ll"
# os.makedirs(str)

# 获取绝对路径 和 相对路径
abspaht = os.path.abspath(".")
print(abspaht)
realpath = os.path.relpath(abspaht, "D:\\learning code\\")
print(realpath)

# 检查目录
size = os.path.getsize(abspaht)
ml = os.listdir(abspaht)
print(ml, size)

# 检查目录下所有文件的大小
totel = 0
for document in ml:
    totel += os.path.getsize(os.path.join(abspaht, document))

print(totel)

# 读写文件
"""
在 Python 中，读写文件有 3 个步骤：
1．调用 open()函数，返回一个 File 对象。
2．调用 File 对象的 read()或 write()方法。
3．调用 File 对象的 close()方法，关闭该文件。
"""
print(os.path.join(os.getcwd(), "1.py"))
dirsPath = os.path.abspath(".\\operaterFile")
file = os.open("D:\\learning code\\python\\1.py", os.O_RDONLY)
print(os.read(file, 20))

# 写文件
# w 写入
dirPath = os.getcwd()
fileDir = os.path.join(dirPath, "2.txt")
writeFile = open(fileDir, "w")
writeFile.write("hello open\n")
writeFile.close()
# a 添加
writeFile1 = open(fileDir, "a")
writeFile1.write("hello everyone\n")
writeFile1.close()


# 读
readFile = open(fileDir, "r")
print(readFile.read())
readFile.close()

# 用 shelve 模块保存变量
import shelve

# 获取路径
dirPath = os.path.abspath(".\\operateFile")
fileDir = os.path.join(dirPath, "mydata")

# 存储变量到shelve

# 存储变量到 shelve 文件中
animalDist = {"cat": 3, "dog": 4, "duck": 5}
with shelve.open(fileDir) as shelveFile:
    shelveFile["animalDist"] = animalDist

# 从 shelve 文件中读取变量
with shelve.open(fileDir) as shelveFile:
    print(shelveFile["animalDist"])
