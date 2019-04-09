#난수만들기
#random을 이용할 수도 있고
#numpy를 이용할 수도 있습니다.

import numpy as np
import matplotlib.pyplot as plt
import random



#0~10사이의 난수를 발생해줘
# x = np.random.randint(10)
# print(x)

# x2 = random.randint(0,10)
# print(x2)


#100에서 1000사이의 난수 5개 만들어줘
# x = np.random.randint(100,1000,5)
# print(x)

# x = np.random.randint(100,1000,10)
# print(x)


#이미 있는 데이터들 중에 임의로 하나를 선택하고 싶어요         random==>choice
# data = [9,7,2,1,100,3]
# x = random.choice(data)
# print(x)
#
#
# #이미 있는 데이터들을 섞어서 중복없이 임의로 여러개 뽑고 싶어요           random==>sample
# x2 = random.sample(data, 3)
# print(x2)


#0~100사이의 난수 1개 만들어줘

# print(x)

# x = np.random.randint(0,1000,100)
# print(x)


# x = np.random.rand()    #0~1 사이의 실수 1개 발생
# print(x)


# 0~100사의 정수 1개 만들어 줘
# x = np.random.randint(100)

#0~1사이의 실수 100개 발생
x = np.random.rand(100)
y = np.random.rand(100)

# print(x)
# print(y)

#데이터의 흩어진 정도를 점을찍어 파악하고자 할 때 ==> scatter
# # plt.scatter(x,y)
# plt.scatter(x,y,c='r')
# # plt.plot(x,y)
# plt.show()


# 연습) data1,data2배열을 만들고
# data1에는 난수100개를 발생시켜 담도록 합니다. (단, 난수의 범위는 -1,0,1 으로 합니다.)
# data2에는 data1의 요소를 누적한 합이 담기도록 합니다.
# data1과 data2를 각각 하나의 figure에 위아래로 분할하여 plot으로 나타내 봅니다.

'''
data1 = [-1,1,1,1]
data2 = [-1,0,1,2]
'''

# data1=[]
# data2=[]
# temp = 0
# for _ in range(100):
#     a = np.random.randint(3)-1
#     temp = temp + a
#     data1.append(a)
#     data2.append(temp)
#
# # print(data1)
# # print(data2)
#
# plt.subplot(211)
# plt.plot(data1)
# plt.subplot(212)
# plt.plot(data2)
# plt.show()



#위의 실습을 좀 더 간단하게 해 봅시다.
# data1 = np.random.randint(-1,2,100)
# data2 = np.cumsum(data1)
# # print(data1)
# # print(data2)
# plt.subplot(211)
# plt.plot(data1)
# plt.subplot(212)
# plt.plot(data2)
# plt.show()


#차트가 예쁘지 않아요
#사용가능한 차트의 종류를 확인 해 봅시다.
# print(plt.style.available)
# ['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight',
# 'ggplot', 'grayscale', 'seaborn-bright', 'seaborn-colorblind',
# 'seaborn-dark-palette', 'seaborn-dark', 'seaborn-darkgrid',
# 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
# 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster',
# 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid',
# 'seaborn', 'Solarize_Light2', 'tableau-colorblind10', '_classic_test']

# print(len(plt.style.available))


#위의 예제를 ggplt 스타일을 적용시켜 차트를 그려봅시다.
data1 = np.random.randint(-1,2,100)
data2 = np.cumsum(data1)
# print(data1)
# print(data2)

# with plt.style.context('_classic_test'):
#     plt.subplot(211)
#     plt.plot(data1)
#     plt.subplot(212)
#     plt.plot(data2)
#     plt.show()



#연습)data2의 내용을 한화면에  _classic_test 를 제외한 25개의 스타일별로 나타내도록 합니다.

styles = plt.style.available;
styles = styles[:-1]

i = 1
for style in styles:
    with plt.style.context(style):
        plt.subplot(5,5,i)
        plt.plot(data2)
        plt.title(style)
    i = i + 1
plt.savefig("plot_styles.png")
plt.show()



#
# x = [1,2,3,4,5]
# y = x.copy()
#
# x[0] = 100
# print(x)
# print(y)





























