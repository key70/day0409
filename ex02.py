#연습) Data/i_have_a_dream.txt 파일의 내용을 읽어 들여
#           화면에 출력해 봅니다.

#wordcloud
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib import font_manager, rc

# font_mask =  np.array(Image.open("../Data/world_map.png"))


#
# f = open("../Data/i_have_a_dream.txt")
# data = f.read()
# f.close()
# print(data)
#
# #단어별 빈도수를 워드클라우드로 표현해 봅시다.
# colud1 = WordCloud().generate(data) #문자열 데이터를 갖고 워드클라우드 객체생성
#
#
# # print(colud1)
# # print(type(colud1))
# plt.imshow(colud1)      #워드클라우드 객체에 해당하는 이미지 생성
#
# #워드클라우드에서는 차트의 축을 없애는것이 보기 좋을 거 같아요
# plt.axis('off')         #차트의 x,y축을 없애 주세요
# plt.show()              #워드클라우드를 보여주세요


#연습)
#문재인 대통령의 연설문을 워드클라우드로 표현해 봅니다.

f = open("../Data/mun.txt",encoding='utf-8')
data = f.read()
# data=data.replace("것입니다","")
# data=data.replace("우리가","")
# data=data.replace("함께","")
# data=data.replace("우리는","")
# data=data.replace("우리","")

# delWord = ['것입니다','우리가','함께','우리는','우리', '있습니다']
# for dw in delWord:
#     data = data.replace(dw,'')
#
# cloud1 = WordCloud(font_path="C:/Windows/Fonts/batang.ttc").generate(data)
#
#
#
# rc("font",family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())
# plt.imshow(cloud1)
# plt.title("문재인 대통령 연설문 시각화")
# plt.axis('off')
# plt.show()

# 워드클라우드 생성시 한글이 깨어짐니다. 도움말을 이용하여 매개변수가 필요한지 확인합시다.
# help(plt.imshow)
# help(WordCloud)
#차트의 제목에는 한글글꼴 확장자 ttf만 적용되어요.



#연습)위의 연설문에서  데이터 분석에 의미 없는 단어를 모두 제거하고
#           다시 워드클라우드로 표현해 봅니다.


f = open("../Data/mun.txt",encoding='utf-8')
data = f.read()
# data=data.replace("것입니다","")
# data=data.replace("우리가","")
# data=data.replace("함께","")
# data=data.replace("우리는","")
# data=data.replace("우리","")

# delWord = ['것입니다','우리가','함께','우리는','우리', '있습니다']
# for dw in delWord:
#     data = data.replace(dw,'')
#
# cloud1 = WordCloud(font_path="C:/Windows/Fonts/batang.ttc").generate(data)
#
#
#
# rc("font",family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())
# plt.imshow(cloud1)
# plt.title("문재인 대통령 연설문 시각화")
# plt.axis('off')
# plt.show()


#단어별 빈도수를 먼저 파악하고 빈도수별 내림차순 정렬하여
#필요없는 단어를 파악하고 싶어요.
#것입니다:25, 우리가:17, ...

# cloud = WordCloud(font_path="C:/Windows/Fonts/batang.ttc")
# word_count = cloud.process_text(data)
# print(word_count)
#
#
# #dictionary의 value를 기준으로 정렬하려면 operator
# import operator
# sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1))[::-1]
# sorted_word_count = sorted_word_count[:20]
# print(sorted_word_count)
# # delWord = ['것입니다', '우리는','함께','새로운','우리가','있습니다','우리의','국민의','한반도의','위해','것이','바로','있는','한반도','우리']
# delWord = ['것입니다', '우리는','함께','새로운','우리가','있습니다','우리의','국민의','위해','것이','바로','있는','우리']
#
# #동의어 처리
# data = data.replace('100년은','100년')
# data = data.replace('한반도의','한반도')
#
#
# for dw in delWord:
#     data = data.replace(dw,'')
#
#
# cloud1 =  cloud.generate(data)
# plt.imshow(cloud1)
# plt.show()



# WorldCloud 객체생성시에 옵션을 확인해 봅시다.
#           차트의 모양을 결정하는 무엇이 있는지 알아봅시다.

# help(WordCloud)

# contour_color="red"           윤곽색   별차이없음.

# cloud = WordCloud(font_path="C:/Windows/Fonts/batang.ttc",
#                     min_font_size=10,
#                   max_font_size=100,
#                   font_step=10,
#                   max_words=100,
#                   background_color="pink",
#                   mask=font_mask,
#                   stopwords="한반도")


from PIL import Image

#이미지를 기반으로 mask를 만들어요.
font_mask =  np.array(Image.open("../Data/mask_circle.png"))

cloud = WordCloud(font_path="C:/Windows/Fonts/batang.ttc",
                  mask=font_mask,
                  background_color='white',
                  stopwords="한반도")
word_count = cloud.process_text(data)


print(word_count)


#dictionary의 value를 기준으로 정렬하려면 operator
import operator
sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1))[::-1]
sorted_word_count = sorted_word_count[:20]
print(sorted_word_count)
# delWord = ['것입니다', '우리는','함께','새로운','우리가','있습니다','우리의','국민의','한반도의','위해','것이','바로','있는','한반도','우리']
delWord = ['것입니다', '우리는','함께','새로운','우리가','있습니다','우리의','국민의','위해','것이','바로','있는','우리']

#동의어 처리
data = data.replace('100년은','100년')
data = data.replace('한반도의','한반도')


for dw in delWord:
    data = data.replace(dw,'')


cloud1 =  cloud.generate(data)
plt.imshow(cloud1)
plt.show()








