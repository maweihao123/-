import sys
try:
    num_in = input("请输入裁判人数：")
    num = int(''.join(i for i in num_in if i in '0123456789'))
except ValueError:
    print("请输入数字！")
    sys.exit()
else:
    list1 = []
    for i in range(num):
        try:
            m_in = input("请输入第{}个裁判的评分：".format(i + 1))
            m = int(''.join(i for i in m_in if i in '0123456789'))
            list1.append(m)
        except ValueError:
            print("请输入数字！")
            sys.exit()
    list1.remove(max(list1))
    list1.remove(min(list1))
    n = sum(list1) / float(len(list1))
    print("{:.2f}".format(n))
