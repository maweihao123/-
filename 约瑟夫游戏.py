def move(players,step):
    num =step-1
    while num>0:
        tmp=players.pop(0)
        players.append(tmp)
        num=num-1
    return players

def play(players,step,alive):
    list1=[i for i in range(1,players+1)]
    while len(list1)>alive:
       # num =step-1
       # while num>0:
        #    tmp=list1.pop(0)
         #   list1.append(tmp)
          #  num=num-1
        list1  = move(list1,step)  
        list1.pop(0)
        
        
    return list1  
players_num=int(input("请输入参加游戏的人数"))
step_num=int(input("请输入淘汰的数字"))
alive_num=int(input("请输入幸存人数"))

alive_list=play(players_num,step_num,alive_num)
print(alive_list)