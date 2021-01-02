import random


if __name__ == "__main__":
    r = random.random() * 360
    if 0 <= r < 10:
        print("一等奖")
    elif 10 <= r < 120:
        print("二等奖")
    elif 120 <= r < 360:
        print("三等奖")

