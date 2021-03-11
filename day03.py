# a = ["北京","上海","广东"]
# a.append("天津")
# a.append("重庆")
# a.append("哈尔滨")
# a.append("银川")
# a.append("郑州")
# a.append("济南")
# a.append("太原")
# a.append("合肥")
# a.append("长春")
# a.append("沈阳")
# a.append("呼和浩特")
# a.append("石家庄")
# a.append("乌鲁木齐")
# a.append("兰州")
# a.append("西宁")
# a.append("西安")
# a.append("长沙")
# a.append("武汉")
# a.append("南京")
# a.append("成都")
# a.append("贵阳")
# a.append("昆明")
# a.append("南宁")
# a.append("拉萨")
# a.append("杭州")
# a.append("南昌")
# a.append("广州")
# a.append("福州")
# a.append("台北")
# a.append("海口")
# a.append("香港")
# a.append("澳门")
# 2)	广东成为第二大发达城市，将广东排在上海前面
# a.remove("广东")
# a.insert(1,"广东")
# print(a)
#请统计前8城市的GDP总和，平均GDP
# GDP = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# zh = 0
# pj = 0
# cs = 0
# while cs<8:
#      zh = zh + GDP[cs]
#      cs += 1
# print(round(zh,2),round(zh/8,2))
# 有以下一个列表，求其中是5的倍数的和
# a = [1,5,21,30,15,9,30,24]
# cs = 0
# z = 0
# while cs < 8:
#     if a[cs]%5 == 0:
#         z = z + a[cs]
#     cs = cs + 1
# print(z)
#有下列列表，请编程实现列表的数据翻转
# list = [1,2,3,4,5,6,7,8,9]
# num = 8
# newlist = []
# while True:
#     if num >= 0:
#         list.append(list[num])
#         list.remove(list[num])
#         num -= 1
#     elif num <0:
#         break
#     print(list)
#请编程统计列表中的每个数字出现的次数
# a = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# c=1
# while c<=10:
#     print("数字",c,"出现的次数为：",a.count(c))
#     c+=1












