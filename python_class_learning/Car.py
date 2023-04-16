class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.__miles = 0

    def description(self):
        # 生成描述汽车信息的字符串
        long_info = f"{self.year}-{self.make}-{self.model}-{self.__miles}"
        return long_info.title()

    def updateMiles(self, miles):
        if miles < self.__miles:
            print("对不起，你不能回调公里数")
        else:
            self.__miles = miles
            print("恭喜你更新成功")


# 要创建的汽车列表
cars_data = [
    [2019, "Tesla", "Model 3"],
    [2021, "Toyota", "Camry"],
    [2018, "Honda", "Civic"],
]

# 存储所有汽车实例的列表
cars_instances = []
for car_data in cars_data:
    # 创建汽车实例并添加到列表中
    car_instance = Car(car_data[0], car_data[1], car_data[2])
    cars_instances.append(car_instance)
cars_instances[0].updateMiles(10)
# 打印每个汽车的描述信息
for car_instance in cars_instances:
    print(car_instance.description())
