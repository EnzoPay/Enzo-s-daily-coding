# 1、ASCII码
print(ord('0'))  # 0的ASCII码是48 阿拉伯数字往后以此类推
print(ord('A'))  # A的ASCII码是65 大写字母往后以此类推
print(ord('a'))  # a的ASCII码是97 小写字母往后以此类推

# 2、list
list = [1, 2, 3, 4, 5]
print([a for a in reversed(list)])
print(list[::2])  # [1,3,5]
print(list[::-1])
print("----------------------------------------------------")

# 3、列表字符排序
list_s = ['AB', "ab", 'ABC', 'ABDC', "ABB"]  # 与元素长度无关 只与元素各位ASCII码有关
list_s.sort()  # 默认从小到大排序 reverse参数复制为True可调为从大到小
print(list_s)
print("----------------------------------------------------")

# 4、字典
dict = {'name': 'enzo', 'age': 15, 'city': 'Beijing'}
print(max(dict), min(dict))  # 按字典键的ASCII码排序
print("----------------------------------------------------")

# 5、列表生成式，range step步长
print([i for i in range(0, 8, 2)])
for index, value in enumerate([i for i in range(0, 8, 2)]):  # 用enumerate方法可以很简单的获取下标与值
    print(index, value)
print("----------------------------------------------------")

# 6、保留两位小数
print(round(2.345, 2))
print('%.2f' % 2.345)
print('{:.2f}'.format(2.345))
