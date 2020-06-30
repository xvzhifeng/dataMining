"""
    @Author:sumu
    @Date:2020-05-25 11:00
    @Email:xvzhifeng@126.com

"""

import math

def dic(x1,y1,x2,y2):

    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


if __name__ == "__main__":
    dic1 = dic(9.5,1.5,10.5,10)
    print(dic1)