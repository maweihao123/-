f1=open('demo.py.ipynb','r').readlines()
f=open('demo_new.py','w')
s=1
for a in f1:
    a=f1.replace('\n','#'+str(s)+'\n')
    s+=1
    f.write(a)

f1.close()
f.close()
