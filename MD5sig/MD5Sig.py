import os,os.path
import sys
import csv
reload(sys)
sys.setdefaultencoding('utf-8')
def readcsv(csvname,file1):
    file3 = open (csvname ,'r')
    readinfo = csv.reader(file3)
    for row in readinfo :
            if row[1] =="True": 
                file1.write(md5_2.lower())
                file1.write(",1,")
                file1.write(row[2])
                file1.write("\n")    
                file1.flush()
                break           
    file3.close()
    os.remove(csvname)
    return 

def main():
    md5total = []
    countre = 0
    countmd5 = 0
    counterr = 0
    countall = 0
    count = 0
    file = open('Info.txt', 'r')
    lines = file.readlines()
    for line in lines:
        countall= countall +1       
    print "共%d条信息"%countall    
    file.close()
       
    file1 = open('SampleInfo.txt', 'a+')
    file2 = open('info.txt', 'r')
    file4 = open('NotDetected.txt','a')
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    
    for line in lines1:
        md5_1 = line[0:32]
        md5total.append(md5_1.lower())
        
    for line in lines2: 
        print "已完成%s"%(format((count *1.00) /countall,'.2%'))
        count = count +1
        md5_2=line[0:32]
        if md5_2.lower() in md5total:
            countre = countre+1
            #os.remove(line)
            continue
    
        else:
            os.system("python vt.py -s %s --csv"% md5_2 )
            try:
                countmd5 = countmd5 +1
                csvname = 'VTDL' + md5_2.lower() + '.csv' 
                readcsv(csvname,file1)
                
            except(IOError):
                counterr= counterr+1
                file4.write(line)
                continue     
        
    file1.close()
    file2.close()
    file4.close()
    print "完成 ！"
    print "一共%d 条MD5信息,有%d条已经存在,有%d条未检测到"%(countall,countre,counterr)
    print "有效分析%d条."%countmd5    
    
    
if __name__ == '__main__':
    main()
    
sys.exit()
