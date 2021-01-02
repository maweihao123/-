import random


if __name__ == "__main__":
    a, b, c = 0, 0, 0
    for i in range(10000):
        r = int(random.random() * 360)
        if 0 <= r < 10:
            a += 1
        elif 10 <= r < 120:
            b += 1
        elif 120 <= r < 360:
            c += 1
    print("一等奖{}个，二等奖{}个，三等奖{}个。".format(a, b, c))
