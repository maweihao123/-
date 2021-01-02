import random
import sys


def catchme(n, m):
    list1 = []
    list2 = [-1, 1]
    rabbit_in = int(random.random() * n + 1)
    for i in range(n):
        list1.append(i + 1)
    t = 1
    while t <= m:
        if rabbit_in == 1:
            rabbit_in += 1
        elif rabbit_in == n:
            rabbit_in -= 1
        else:
            rabbit_in = rabbit_in + list2[int(random.random() * 2)]
        try:
            which_catch_in = input("这次指定几(1~{})号洞：".format(n))
            which_catch = int("".join(i for i in which_catch_in if i in "1234567890"))
        except ValueError:
            print("请输入整数！")
        else:
            if rabbit_in == which_catch:
                print("成功抓到兔子！")
                sys.exit()
            elif t == m:
                print("次数用光了也没抓到兔子！菜！")
                sys.exit()
            else:
                print("第{}次没抓到兔子！".format(t))
                t += 1


def message_in():
    try:
        holes_in = input("请输入洞口的个数：")
        holes = int("".join(i for i in holes_in if i in "1234567890"))
        times_in = input("请输入玩家游戏次数：")
        times = int("".join(i for i in times_in if i in "1234567890"))
        return holes, times
    except ValueError:
        print("请输入整数！")
        return message_in()


if __name__ == "__main__":
    catchme(*message_in())
