import numpy as np
import pandas as pd
from sklearn import datasets, model_selection, svm
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    iris = datasets.load_iris()

    # 获取花萼的长(x)和宽(y)
    x = [n[0] for n in iris.data]
    y = [n[1] for n in iris.data]
    import numpy as np  # 转换成数组

    x = np.array(x).reshape(len(x), 1)
    y = np.array(y).reshape(len(y), 1)
    # 第二步 导入Sklearn机器学习扩展包中线性回归模型，然后进行训练和预测
    classifier = LinearRegression()
    # 开始训练
    classifier.fit(x, y)
    # 预测(根据花萼长来预测花萼的宽）
    pre = classifier.predict(x)

    # 第三步 画图（数据可视化）
    plt.scatter(x, y, s=100)
    plt.plot(x, pre, "r-", linewidth=4)
    # 花萼的长宽
    plt.xlabel('calycinal length')
    plt.ylabel('calycinall width')
    for idx, m in enumerate(x):
        plt.plot([m, m], [y[idx], pre[idx]], 'g-')
    plt.show()
    # 做预测，花萼长度为5.0，预测花萼宽度是多少
    print('[线性回归]花萼长度为5.0，预测花萼宽度是', classifier.predict([[5.0]]))