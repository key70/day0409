from sklearn import preprocessing
import numpy as np

# 결측치에 대한 처리
# 수집한 데이터에는 결측치가 많을 수 있어요.
#   이것에 대한 처리에 대하여 알아 봅시다.
#       preprocessing의 Imputer함수를 이용하여 결측치를 원하는 값으로 설정


x= [
        [1,2],
        [np.nan,3],
        [7,6],
        [7,2],
        [2,3],
        [3,4]
]

help(preprocessing.Imputer)

#strategy ==> mean, median, most_frequent
imp = preprocessing.Imputer(missing_values="NaN", strategy="median")
x2 = imp.fit(x).transform(x)
print(x2)






