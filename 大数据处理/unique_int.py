import numpy as np
mark = np.zeros((2.5*(10**8),2),dtype=np.bool)
def get_unique_int():
    with open('data.txt') as f:
        for num in f:
            if mark[num][0] == False and mark[num][1] == False:  #这个数第一次出现
                mark[num][0] = True
                mark[num][1] = False
            else:
                mark[num][0] = True                              #出现了不止一次的数据，那么同意赋值 1 1
                mark[num][1] = True

    with open('data.txt') as f:
        for num in f:
            if mark[num][0] == True and mark[num][1] == False:
                yield num

if __name__ == "__main__":
    unique_list = list(get_unique_int())#返回的是一个迭代器对象,通过list


