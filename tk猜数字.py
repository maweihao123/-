import tkinter  as  tk
import random
import logging
logger = logging.getLogger('mylogger') 
logger.setLevel(logging.DEBUG)


 
fh = logging.FileHandler('test.log') 
fh.setLevel(logging.DEBUG) 
 

ch = logging.StreamHandler() 
ch.setLevel(logging.ERROR) 
 

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
 

fh.setFormatter(formatter) 
ch.setFormatter(formatter) 
 
 
logger.addHandler(fh) 
logger.addHandler(ch)
 
logger.debug("请输入数字")









root = tk.Tk()

root.title('猜数字游戏')

tk.Label(root, text="请输入一个1——100之间的整数：").grid(row=0, column=0)

entry1 = tk.Entry(root) 
entry1.grid(row=0, column=1, padx=10, pady=10)


random_num = random.randint(1, 100)              
var_猜数字 =  tk.StringVar()
var_猜数字_text = tk.StringVar()          

var_猜数字_text.set('无')


def count():
    guess_num = float(entry1.get())
    temp_猜数字=guess_num
    var_猜数字.set(str(temp_猜数字))
  
    if guess_num > random_num:
            var_猜数字_text.set('您猜的数字大了，请重新猜测！')
    elif guess_num < random_num:
            var_猜数字_text.set('您猜的数字小了，请重新猜测！')
    elif guess_num == random_num:
            var_猜数字_text.set('恭喜您答对了！')

tk.Label(root, text="结果").grid(row=2, column=0)
tk.Label(root, textvariable=var_猜数字_text).grid(row=2, column=1)



tk.Button(root, text="猜一猜", width=10, command=count).grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)

tk.mainloop()