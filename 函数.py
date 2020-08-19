# -*- encoding:utf-8 -*-

# def get_user(Uersname):
#     """显示简单的问候语"""
#     print("hello " + Uersname.title() + "!")
#
# get_user("daming")

# def describe_pet(animal_type,pet_name = 'cat'):
#     """显示宠物信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
# describe_pet('兔子','黑寡妇')
# describe_pet('dog', 'happy')
# describe_pet('大明')
# describe_pet()

# def get_formatted_name(firt_name,last_name,middle_name =''):
#     """返回整洁的名字"""
#     if middle_name:
#         full_name = firt_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = firt_name + ' ' + last_name
#     return full_name.title()
#
# musician = get_formatted_name('jimi','hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


def get_formatter_name(firt_name,last_name):
    """返回整洁的名字"""
    full_name = firt_name + last_name
    return full_name.title()

while True:
    print("\nPlease tell me you nmae")
    f_name = input("firt name:")
    l_name = input("last name:")
    musician = get_formatter_name(f_name,l_name)
    print(musician)
    repeat = input("\nWould you like to let another person respond?(yes/no)")
    if repeat == "no":
        break

