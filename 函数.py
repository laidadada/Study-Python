# -*- encoding:utf-8 -*-

# def get_user(Uersname):
#     """显示简单的问候语"""
#     print("hello " + Uersname.title() + "!")
#
# get_user("daming")

def describe_pet(animal_type,pet_name = 'cat'):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('兔子','黑寡妇')
describe_pet('dog', 'happy')
describe_pet('大明')
describe_pet()