import shutil, os


def searchFileType(str):
    targetFiles = []
    path = os.path.abspath(".")
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            dirPath = os.path.join(dirpath, dirname)
            print("文件夹:{}".format(dirPath))

        for filename in filenames:
            filePath = os.path.join(dirpath, filename)
            print("文件:{}".format(filePath))
            if filePath.endswith(str):
                targetFiles.append(filePath)
    return targetFiles


def copyFileType(targetFiles):
    path = os.path.abspath(".")

    targetPath = os.path.join(path, "targetType")
    try:
        os.mkdir(targetPath)
    except FileExistsError:
        print("文件夹已存在，跳过创建")
    for targetFile in targetFiles:
        print(targetFile)
        dir_path, file_name = os.path.split(targetFile)

        move_to_the_path = os.path.join(targetPath, file_name)
        shutil.copyfile(targetFile, move_to_the_path)
        print(move_to_the_path)


copyFileType(searchFileType("pdf"))
