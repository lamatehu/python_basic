from cgi import print_arguments


# def spam():
#     raise Exception("这是一个错误")


# def meilin():
#     spam()


# meilin()


market_2nd = {"ns": "green", "ew": "red"}
mission_16th = {"ns": "red", "ew": "green"}


# 断言，旨在快速查找问题
def switchLights(stoplight):
    assert "red" in stoplight.values(), "Neither light is red! " + str(stoplight)
    for key in stoplight.keys():
        if stoplight[key] == "green":
            stoplight[key] = "yellow"
        elif stoplight[key] == "yellow":
            stoplight[key] = "red"
        elif stoplight[key] == "red":
            stoplight[key] = "green"


switchLights(market_2nd)

print("haah")

# 使用日志模块
import logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s- %(message)s"
)
logging.debug("start program")


def factorial(n):
    logging.info("start function")
    # 传入n
    num = 1
    for i in range(1, n + 1):
        num = i * num
    logging.debug("此时的阶乘的值为:%s" % {num})


# 不显示日志
logging.disable()
factorial(5)


print("Enter the first number to add:")
first = input()
print("Enter the second number to add:")
second = input()
print("Enter the third number to add:")
third = input()
print("The sum is " + first + second + third)


egg = "Dog"
bgg = "dog"
assert egg.lower() != bgg.lower(), "两个值相同"

assert 1 != 1
flip_a_coin