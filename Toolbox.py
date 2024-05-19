import math

def welcome():
    while True:
        print("---------------欢迎使用工具箱(made by Pimeng)---------------")
        print("1. BMI计算工具")
        print("2. 简易方程计算器")
        print("* 输入 exit 退出本工具箱")
        choose = input("请输入你需要干的事：").strip().lower()
        if choose == "1":
            bmic()
        elif choose == "2":
            equation()
        elif choose == "exit":
            print("再见")
            break
        else:
            print("无效输入，请选择 1，2 或者输入 exit 退出。")

def bmic():
    print("---------------------BMI计算器---------------------")
    while True:
        confirm = input("输入 exit 退出，输入其他继续操作:").strip().lower()
        if confirm == "exit":
            return
        else:
            try:
                tall = float(input("请输入身高（单位：m）："))
                height = float(input("请输入体重(单位：kg)："))
                bmi1 = height / tall**2
                print("您的BMI计算结果为：", "%.2f" % bmi1)
                if bmi1 < 10:
                    print("您是人吗？")
                elif 10 <= bmi1 < 18.5:
                    print("您的BMI指数过低，请注意！")
                elif 18.5 <= bmi1 < 23.9:
                    print("您的BMI指数正常")
                elif 24 <= bmi1 < 27.9:
                    print("你的BMI超标，请注意")
                elif bmi1 >= 28:
                    print("您的BMI指数已经严重超标！")
            except ValueError:
                print("无效输入，请输入数字值。")
    print("BMI程序退出，欢迎再次使用！")

def equation():
    while True:
        print("------------------简易方程计算器----------------")
        print("1. 一元一次方程(形如 ax + b = c)")
        print("2. 二元一次方程(形如 ax² + bx + c = d 的形式)")
        print("* 输入 exit 来退出本计算器")
        choice = input("请选择方程类型：").strip().lower()
        if choice == "1":
            equation1()
        elif choice == "2":
            equation2()
        elif choice == "exit":
            return
        else:
            print("无效输入，请选择 1，2 或者输入 exit 退出。")

def equation1():
    print("当前编辑的方程为：ax + b = c")
    try:
        a = float(input("请输入 a 的值："))
        print(f"方程：{a}x + b = c，请继续输入各项值")
        b = float(input("请输入 b 的值："))
        print(f"方程：{a}x + {b} = c，请继续输入各项值")
        c = float(input("请输入 c 的值："))
        print(f"方程：{a}x + {b} = {c}")

        while True:
            print("方程是否正确？(回答 是 或 否)")
            ans = input().strip().lower()
            if ans == "是":
                print("计算中...")
                s1 = c - b
                s2 = s1 / a
                print(f"计算出的 X 的值为：{s2}")
                break
            elif ans == "否":
                print("请重新输入方程参数...")
                return equation1()
            else:
                print("无效输入，请输入 '是' 或 '否'。")
    except ValueError:
        print("无效输入，请输入数字值。")

def equation2():
    print("当前编辑的方程为：ax² + bx + c = d")
    try:
        a = float(input("请输入 a 的值："))
        print(f"方程：{a}x² + bx + c = d，请继续输入各项值")
        b = float(input("请输入 b 的值："))
        print(f"方程：{a}x² + {b}x + c = d，请继续输入各项值")
        c = float(input("请输入 c 的值："))
        print(f"方程：{a}x² + {b}x + {c} = d，请继续输入各项值")
        d = float(input("请输入 d 的值："))
        print(f"方程：{a}x² + {b}x + {c} = {d}")

        while True:
            print("方程是否正确？(回答 是 或 否)")
            ans = input().strip().lower()
            if ans == "是":
                print("计算中...")
                s1 = b**2 - 4*a*(c-d)
                if s1 < 0:
                    print("该方程无解。请重新输入参数...")
                    return equation2()
                else:
                    x1 = (-b + math.sqrt(s1)) / (2*a)
                    x2 = (-b - math.sqrt(s1)) / (2*a)
                    print(f"计算出的 X1 的值为：{x1}，计算出的 X2 的值为：{x2}")
                    break
            elif ans == "否":
                print("请重新输入方程参数...")
                return equation2()
            else:
                print("无效输入，请输入 '是' 或 '否'。")
    except ValueError:
        print("无效输入，请输入数字值。")

# 启动程序
welcome()