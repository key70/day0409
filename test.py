#연습) Data/i_have_a_dream.txt 파일의 내용을 읽어 들여
#           화면에 출력해 봅니다.

#wordcloud

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib import font_manager, rc


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



f = open("../Data/mun.txt", encoding='utf-8')
data = f.read()
f.close()
print(data)

#단어별 빈도수를 워드클라우드로 표현해 봅시다.
# colud1 = WordCloud().generate(data) #문자열 데이터를 갖고 워드클라우드 객체생성
font_path = "C:/Windows/Fonts/malgun.ttf"
cloud1 = WordCloud( font_path = font_path).generate(data)

rc("font",family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())

# print(colud1)
# print(type(colud1))
plt.imshow(cloud1)      #워드클라우드 객체에 해당하는 이미지 생성


help(WordCloud)



#워드클라우드에서는 차트의 축을 없애는것이 보기 좋을 거 같아요


plt.axis('off')         #차트의 x,y축을 없애 주세요
plt.show()              #워드클라우드를 보여주세요
















