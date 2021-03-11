#实现输入10个数字，并打印10个数的求和结果
'''
ten = 0
all = 0
while ten < 10:
    once = int(input("请输入数字： "))
    all = all + once
    ten = ten + 1
print ("合计结果: ",all)
'''
#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''
ten = 0
all = 0
every = 0
while ten < 10:
    once = int(input("请输入数字： "))
    if once > every:
        every= once
    all = all + once
    ten = ten + 1
print ("最大值:  ",every)
print ("合计结果: ",all)
print ("平均值为: ",all / 10)
'''
#使用random模块，如何产生 50~150之间的数？
'''
import  random
num =random.randint(50,150)
print(num)
'''
#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
# （结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
a = 0
b = 0
c = 0
a = int(input("请输入三角形a边边长: "))
b = int(input("请输入三角形b边边长: "))
c = int(input("请输入三角形c边边长: "))
if a==0 or b==0 or c==0:
        print("结果：你家三角形能有一条边为0？")
elif a+b <= c or a+c<= b or b+c <=a:#不能构成三角形
        print ("结果：不能形成三角形")
elif a * a + b * b == c * c or a * a + c * c == b * b or b * b +c * c == a * a:#直角三角形
        print("结果：构成直角三角形")
elif a == b == c:#等边三角形
        print("结果：构成等边三角形")
elif a == b or a == c or b==c:#等腰三角形
        print("结果：构成等腰三角形")
elif a + b > c or a + c > b or b + c > a:  # 普通三角形
        print("结果：构成普通三角形")

#有以下两个数，使用+，-号实现两个数的调换
'''
'''
a = 56
b = 78
c = 0
while True:
    c = input("请输入+、-号来调整数字大小:")
    if c == "+":
        a = a + b
        b = a - b
        a = a - b
        print("a的数值为：", a)
        print("b的数值为：", b)
    elif c == "-":
        a = a + b
        b = a - b
        a = a - b
        print("a的数值为：",a)
        print("b的数值为：",b)
    else:
        print("输入字符非法，您只能输入+或-")
        break
'''
#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）

# id  = "root"
# pa = "admin"
# check = 0
# while True:
#     id_int = input("请输入用户名：")
#     pa_int = input("请输入密码：")
#     if id_int != id or pa_int != pa:
#         print("登录失败，用户名与密码不匹配！")
#         check = check + 1
#         if check == 3:
#             print("登录系统失败，程序已锁定，请您动动脑子")
#     else:
#         print("登录成功！")
#         break

#编程实现下列图形的打印
'''
for i in range(8):
    for j in range(0, 10 - i):
        print(end=" ")
    for k in range(10 - i, 10):
        print("*", end=" ")
    print("")
'''
#使用while循环实现99乘法表的打印。
'''
a=1
b=1
while a<=9:
    while b<=9:
        print(a,"*",b,"=",a*b)
        b += 1
    b=1
    a+=1
'''
#编程实现99乘法表的倒叙打印
'''
a=9
b=9
while a>0:
    while b>0:
        print(a,"*",b,"=",a*b)
        b -= 1
    b=1
    a-=1
'''
# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
'''
high = 20
morn = -3
nigh = 2
out = 0
while high <= 20:
     high += morn
     if high == 0:
         break
     high += nigh
     if high == 0:
         break
     out+=1
print ("这青蛙花费了",out,"天，个人推荐下回别上来了。")
'''
# import random
# 
# rannum = random.randint(1,2)
# tnum = 20
# while True:
#     print("\t")
#     print("-当前剩余次数：",tnum,"-")
#     num = input("请输入您要猜的数字：")
#     num = int(num)
# 
#     if num > rannum:
#         print("\t")
#         print("---当前剩余次数:",tnum, "---")
#         print("--猜大了!!失去一次机会--")
#         tnum-=1
#     elif num < rannum:
#         print("\t")
#         print("---当前剩余次数:",tnum, "---")
#         print("--猜小了!!失去一次机会--")
#         tnum-=1
#     else:
#         if tnum == 0:
#             print("你好菜啊，别玩了")
#         elif tnum >= 17:
#             print("恭喜您在3次之内成功猜到数字")
#             print("系统将奖励您2000金币")
#             print("正确数字为：", rannum)
#         else:
#             print("恭喜您，猜对了！正确数字为：", rannum)
#         break
#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
'''
b=1
c=0
while a<20:
    while b<=a:
        print(a," ",b)
        c=c+(a*b)
        b+=1
    b=1
    a+=1
print(c)
'''