File Handler

    Driectory + File Name + Extention Listing
    Deduplication
# please engage this code
import pickle
f=open('test.txt','wb')
i = 0
while i in range (100):
    f.seek(0,0)
    pickle.dump(i,f)
    i += 1
with open('test.txt','rb') as k:
    obj=pickle.load(k)
    print(obj)
