alien_0 = {}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#更改字典信息
alien_0 = {'color': 'green'}
print("The alien is now " + alien_0['color'] + "!")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + "!")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
alien_0['speed'] = "fast"
# 向右移动外星人
# 据外星人当前速度决定将其移动多
if alien_0['speed'] == 'slow':
 x_increment = 1
elif alien_0['speed'] == 'medium':
 x_increment = 2
else:
 x_increment = 3
# 新位置等于઻位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#删除
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
friends = ['jen','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name not in friends:
        print("hi " + name.title() +",  I see your favorite language is " + favorite_languages[name].title())

#遍历字典中的所有值
#使用方法values（）,它返回一个值列表，而不包含任何键
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())

# 按顺序遍历字典中的所有键：
# 要以特定的顺序返回元素，一种办法是在for循环中对返回的建进行排序。为此，可使用函数sorted（）来获得特定顺序排序的键列表的副本
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
 print(name.title() + ", thank you for taking the poll.")

#为了剔除重复项，可以使用集合set（）
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
 print(language.title())

