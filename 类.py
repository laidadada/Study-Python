# -*- encoding:utf-8 -*-


# class Dog():
#     """一次模拟小狗的简单尝试"""
#
#     def __init__(self, name, age):
#         """初始化属性，name，age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """模拟小狗被命令蹲下的指令"""
#         print(self.name.title() + " is now sitting")
#
#     def roll_over(self):
#         """模拟小狗被命令打滚"""
#         print(self.name.title() + " roll over ")
#
# my_dog = Dog('willie', 6)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
#
# my_dog.sit()
# my_dog.roll_over()


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的信息"""
        # self.odometer_reading = 23
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
         将里程表读数设置为指定的值
         禁止将里程表读数往回调
         """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将૛程表读数增加指定的量"""
        self.odometer_reading += miles

    """给子类定义属性的方法"""
class ElectricCar(Car):

    def __init__(self, make, modle, year):
        """初始化父类属性"""
        super().__init__(make, modle, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(2)
# my_new_car.read_odometer()
#
# my_new_car.increment_odometer(10)
# my_new_car.read_odometer()
















