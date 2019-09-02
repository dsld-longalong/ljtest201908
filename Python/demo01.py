print("你好，浪晋")
print(23333)
print('哈哈，字符串需要加引号， wo haishi key shuo english!22222222222')
print(100)
print(2.333,"哈哈哈","嘻嘻嘻")


yuanzu = (2,4,5,"哈哈哈","哈哈哈",False,None,2.333,"xixi","4444")

xiabiao = yuanzu.index("哈哈哈")
print(xiabiao)

shuliang = yuanzu.count("不存在")
print(shuliang)



print("---------------------------")


shuzu = [1,2,3,"哈哈","数组","喵喵喵","???","2333",2333,2333]
print(shuzu)
shuzu.append("这是新插入的值")  # 向数组中插入数据
print(shuzu)

shuzu.insert(3,"这是控制了位置的数据")
print(shuzu)

a = shuzu.pop(3)  # 取走
print(a)
print(shuzu)

'''
shuzu.clear()
print(shuzu)
'''
b = shuzu.copy()
print(b)

shuzu.remove(2333)
shuzu.remove(2333)
print(shuzu)

# shuzu.extend([1,2,3,4])
# print(shuzu)
c = shuzu + [1,2,3,4]
print(c)


print("-------------------------------")

zidian = {
    0:"哈哈哈",
    "name":"张三",
    5:"绥滨",
    "high":"175cm"
    }  # 键值对  key:value


print(zidian)

zidian["new"] = "刘莹"
print(zidian)

zidian["name"] = "李四"
print(zidian)

del zidian["name"]
print(zidian)


del shuzu[0]