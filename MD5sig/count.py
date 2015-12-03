import  sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
file= open ("MD5Sig2.txt","r")
#file= open ("info.txt","r")

lines = file.readlines()
count = 0;
for line in lines:
    count= count +1

print count 

print  count - 2