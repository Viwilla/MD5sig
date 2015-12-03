info.txt:存放MD5信息
vt.py : VirusTotal检测脚本，需要到官网上注册https://www.virustotal.com/，然后将脚本倒数第二行“yourkey”换为你的key
MD5Sig.py: 读取info.txt里的MD5，用vt脚本检测，记录检测信息到Sampleinfo.txt，未检测到的记录到NotDetected.txt'，方便以后再次检测
deleteRe.py:文件去重