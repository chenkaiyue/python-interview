# 内容多的原因还是在于不能一次read一个大文件，所以readline之后分别存在1000个文件中，这样的话
# 每个小文件的内容就可以一次读入，进行处理

import os
from collections import Counter

source_file=r'bigdata.txt'
temp_files = 'C:/Users/Administrator/Desktop/most_ip/temp/'
top_1000ip = []
def hash_file():
    temp_path_list=[]
    if not os.path.exists(temp_files):
        os.makedirs(temp_files)
    for i in range(1000):
        temp_path_list.append(open(temp_files+str(i)+".txt",'w'))
    with open(source_file) as f:
        for line in f:#把ip分别写到1000个文件中去
            temp_path_list[hash(str(line))%1000].write(line)
            # print line
    for i in range(1000):
        temp_path_list[i].close()

def cal_query_frequency():
    for root,dirs,files in os.walk(temp_files):
        for file in files:
            real_path = os.path.join(root,file)
            ip_list = []
            with open(real_path,'r') as f:
                for line in f:
                    ip_list.append(line.replace('\n',''))
                try:
                    top_1000ip.append(Counter(ip_list).most_common()[0])
                except:
                    pass
    # print top_1000ip

def get_ip():
    return (sorted(top_1000ip,key=lambda a:a[1],reverse=True)[0])[0]

if __name__ == "__main__":
    hash_file()
    cal_query_frequency()
    print(get_ip())
