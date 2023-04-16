from operator import le
import re, shutil, os

datePatern = re.compile(
    r"""
           (.*?)
           ((1|2)?\d)-
           ((0?[1-9])|([12]\d)|(3[01]))-
           ((19|20)\d{2})
           (.*?)$
           """,
    re.VERBOSE,
)

# 查看文件目录
dirs = os.listdir("D:\\learning code\\python\\")
print(dirs)
for file1 in dirs:
    mo = datePatern.search(file1)

    if mo == None:
        continue
    zichuan = re.findall(datePatern, file1)
    print(zichuan)
    print("hahaha")
    frontzi = mo.group(1)
    mm = mo.group(2)
    dd = mo.group(4)
    yy = mo.group(8)
    behindzi = mo.group(10)

    print(mm, dd, yy)
    # 转换为dd mm yy
    targetDirs = "D:\\learning code\\python\\target\\"
    buiddir = "D:\\learning code\\python"
    try:
        os.mkdir(targetDirs)
    except FileExistsError:
        print("目录存在")
    newfile1 = frontzi + dd + "-" + mm + "-" + yy + behindzi
    shutil.copy(os.path.join(buiddir, file1), targetDirs + newfile1)
