#84 File

#file object = open(file_name[,access_model][,buffering])
read = open("file.txt","r")
for line in read.readlines():
    line = line.strip()
    print(line)
read.close()


#http://ithelp.ithome.com.tw/articles/10161708

