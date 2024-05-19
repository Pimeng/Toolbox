import math
def welcome():
    print("---------------欢迎使用工具箱(made by Pimeng)---------------")
    print("1.BMI计算工具")
    print("2.简易方程计算器")
    print("*输入exit退出本工具箱")
    choose=str(input("请输入你需要干的事："))
    if choose == "1":
        bmic()
        welcome()
    elif choose == "2":
        equation()
        welcome()

def bmic():
    print("---------------------BMI计算器---------------------")
    confirm=str(input("输入exit退出，输入其他继续操作:"))
    if  confirm == "exit":
        welcome()
    else:
        tall=float(input("请输入身高（单位：m）："))
        height=float(input("请输入体重(单位：kg)："))
        bmi1=float(height / tall**2)
        print("您的BMI计算结果为：","%.2f" % bmi1)
        if bmi1 < 10:
            print("您是人吗？")
        elif 10 < bmi1 < 18.5:
            print("您的BMI指数过低，请注意！")
        elif 18.5 < bmi1 < 23.9:
            print("您的BMI指数正常")
        elif 24 < bmi1 < 27.9:
            print("你的BMI超标，请注意")
        elif bmi1 > 28:
            print("您的BMI指数已经严重超标！")
    print("BMI程序退出，欢迎再次使用！")

def equation():
    print("------------------简易方程计算器----------------")
    print("1.一元一次方程(形如ax+b=c)\n2.二元一次方程(形如ax²+bx+c=d的形式)\n*输入exit来退出本计算器")
    choice=str(input("请选择方程类型："))
    if choice == "1":
        equation1()
    elif choice == "2":
        equation2()
    elif choice == "exit":
        welcome()

def equation1():
    print("当前编辑的方程为：ax+b=c")
    a=float(input("请输入a的值："))
    print("方程：",a,"x+b=c，请继续输入各项值")
    b=float(input("请输入b的值："))
    print("方程：",a,"x+",b,"=c，请继续输入各项值")
    c=float(input("请输入c的值："))
    print("方程：",a,"x+",b,"=",c,"")
    print("方程是否正确？")
    ans=str(input("回答（是或者否）："))
    if ans == "是":
        print("计算中")
        s1=c-b
        s2=s1/a
        print("计算出的X的值为：",s2)
    elif ans == "否":
        print("正在执行返回函数...")
        equation1()
    welcome()

def equation2():
    print("当前编辑的方程为：ax²+bx+c=d")
    a=float(input("请输入a的值："))
    print("方程：",a,"x²+bx+c=d，请继续输入各项值")
    b=float(input("请输入b的值："))
    print("方程：",a,"x²+",b,"x+c=d，请继续输入各项值")
    c=float(input("请输入c的值："))
    print("方程：",a,"x²+",b,"x+",c,"=d，请继续输入各项值")
    d=float(input("请输入d的值："))
    print("方程：",a,"x²+",b,"x+",c,"=",d)
    print("方程是否正确？")
    ans=str(input("回答（是或者否）："))
    if ans == "是":
        print("计算中")
        s1=b**2-4*a*c
        if s1 < 0:
            print("无解")
            equation2()
        else:
            x1=((-b+math.sqrt(b**2-4*a*c))/(2*a))
            x2=((-b-math.sqrt(b**2-4*a*c))/(2*a))
            print("计算出的X1的值为：",x1,"，计算出的X2的值为：",x2)
    else:
        print("正在执行返回函数...")
        equation2()
        welcome()
    welcome()
welcome()
print("再见")