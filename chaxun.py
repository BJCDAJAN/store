def bank_chaxun(self, user):
    sql = "select * from user  where  account = %s"
    param = [user.getAccount()]
    data = select(sql, param)
    # 账号存在
    i = 0
    for c in data:
        if c[0] == user.getAccount():
            i = i + 1
            password = input("请输入密码：")
            password = int(password)
            if password == c[2]:
                print("前账号：", user.getAccount())
                print("密码：******")
                print("余额：", c[7])
                print("用户居住地址：", c[3], c[4], c[5], c[6])
                print("当前账户的开户行：", c[9])
            else:
                print("密码不正确")
    if i == 0:
        print("账户不存在")