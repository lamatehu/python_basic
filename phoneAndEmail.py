import re
import pyperclip


def getPhoneNumberAndEmail(text):
    getPhoneNumber = re.compile(
        r"""(\d{3}|\(\d{3}\))? # area_code
                    (\s|-|\.)? # 空格 - 或者.
                    (\d{3}) # 前三位
                    (\s|-|\.)? # 空格 - 或者.
                    (\d{4})
                    (\s*(ext|x|ext./)\s*(\d{2,5}))?#分机号 
                """,
        re.VERBOSE,
    )  # 可加注释
    getEmail = re.compile(
        r"""([A-Za-z0-9._%+-]+
        @
        [A-Za-z0-9.-]+
        (\.[a-zA-Z]{2,4})
        )""",
        re.VERBOSE,
    )

    match = []

    for groups in getPhoneNumber.findall(text):
        phoneNum = "-".join([groups[0], groups[2], groups[4]])
        print(groups)
        if groups[7] != "":
            phoneNum = phoneNum + " x" + groups[7]
        match.append(phoneNum)

    for emails in getEmail.findall(text):
        print(emails)
        match.append(emails[0])
    return match


def cut_copy_paste_board():
    str1 = pyperclip.paste()
    matchs = getPhoneNumberAndEmail(str1)
    if matchs != None:
        pyperclip.copy("\n".join(matchs))
        print(matchs)
    else:
        print("不好意思没有匹配项")


cut_copy_paste_board()
