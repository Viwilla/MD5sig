import os,sys,os.path
#import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__=="__main__":
    md5total = []
    md5 = []
    count = 0
    count1 =0
    counttotal= 0
    file1 = open ("MD5Sig.txt","r")
    file2 = open("MD5Sig2.txt","a+")
    lines = file1.readlines()
    for line in lines:
        counttotal = counttotal +1
        md5 = line[0:32]
        if md5 in md5total:
            print md5 
            count1  = count1+1
     #       data = splitlines(True)
           # del line
        else:
            md5total.append(md5.lower())
            file2.write(line)
            count = count +1
    file1.close()
    file2.close()
    
   # with open("1.txt",'w') as fout:
   #     fout.writelines(data[1:])
        
    print "End"
    print "共有%d条信息,%d条重复,有效%d条"%(counttotal,count1,count)