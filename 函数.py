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


# def get_formatter_name(firt_name,last_name):
#     """返回整洁的名字"""
#     full_name = firt_name + last_name
#     return full_name.title()
#
# while True:
#     print("\nPlease tell me you nmae")
#     f_name = input("firt name:")
#     l_name = input("last name:")
#     musician = get_formatter_name(f_name,l_name)
#     print(musician)
#     repeat = input("\nWould you like to let another person respond?(yes/no)")
#     if repeat == "no":
#         break

# def greet_user(names):
#     """向每个用户发送问候"""
#     for name in names:
#         msg = "hello, " + name.title() + "!"
#         print(msg)
#
# usernames = ['daming','xiaoming','tony']
# greet_user(usernames)


# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
#
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)
#

#
# def print_modesls(unprinted_designs,completed_models):
#     """
#      模拟打印每个设计,直到没有未打印的设计为止
#      打印每个设计，都将其移到列表completed_models中
#      """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
# def show_completed_models(comleted_modles):
#     """显示打印ࡻ的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_modesls(unprinted_designs,completed_models)
# show_completed_models(completed_models)

def show_magicians(old_names,new_names):
    while old_names:
        new_name = old_names.pop()
        print('hello ,' + new_name.title())
        new_names.append(new_name)

def make_great(new_names):
    """对所有魔术师进行修改"""
    print("\nThey are new name is:")
    for new_name in new_names:
        msg = 'hello , the Great ' +new_name.title()
        print(msg)

old_names = [ 'Tom', 'Day', 'lai' ]
new_names = []
show_magicians(old_names[:], new_names)
make_great(new_names)
make_great(old_names)


# --158页面

