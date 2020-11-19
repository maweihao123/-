file = open(r'C:\Users\Administrator\Desktop\Walden.txt','r')
lines = file.readlines()
words = []
for line in lines:
    tmp_list =line.split(" ")
    for word in tmp_list:
        words.append(word)
word_count={}
word_set = set(words)
for word in word_set:
    count_num = words.count(word)
    word_count[word]=count_num
word_count
sorted(word_count.items(),key=lambda item:item[1],reverse=True)