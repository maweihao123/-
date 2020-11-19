import random 
print("下面是猜数字游戏环节！")
random_num = random.randint(1, 100)
print("游戏开始！请输入一个1——100之间的整数！")
for i in range(5, 0, -1):
    print("您还有%d次机会" % i)
    guess_num = int(input("请输入你要猜的数字："))
    if guess_num > random_num:
        print("您猜的数字大了，请重新猜测！")
    elif guess_num < random_num:
        print("您猜的数字小了，请重新猜测！")
    elif guess_num == random_num:
        print("恭喜您答对了，正确的数字为%d！" % random_num)
        break
else:
    print("您已经没有机会了，游戏失败！")