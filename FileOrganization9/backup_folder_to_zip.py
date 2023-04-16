from enum import Flag
import os, zipfile
from pickle import TRUE


def backup_folder():
    # 将要备份的路径
    path = os.path.abspath(".")
    # 备份文件存放位置
    backupPath = os.path.abspath(".") + "\\backup"
    try:
        os.mkdir(backupPath)
    except FileExistsError:
        print("文件存在")
    num = 1
    backup_file = os.path.join(backupPath, str(num) + ".zip")
    while True:
        backup_file = os.path.join(backupPath, str(num) + ".zip")
        if not os.path.exists(backup_file):
            break
        num = num + 1
    # 创建zip
    zipfiles = zipfile.ZipFile(backup_file, "w")
    backup_zip(zipfiles)
    zipfiles.close()


# 具体操作
def backup_zip(zipfiles):
    path = os.path.abspath(".")
    added_files = set()  # 存储已经添加的文件名
    for foldername, subfolders, filenames in os.walk(path):
        # 添加文件夹到 zip
        print("add folder to %s" % (foldername))
        zipfiles.write(foldername)

        for file in filenames:
            print(file)
            if file not in added_files:  # 如果文件没有被添加过，则添加到 ZIP 文件中
                if file.endswith(".zip"):
                    continue
                print("add file to %s" % (file))
                print(file)
                zipfiles.write(os.path.join(foldername, file))
                added_files.add(file)


backup_folder()

file_search_and_replication