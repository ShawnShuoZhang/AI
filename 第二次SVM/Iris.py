import numpy as np
import pandas as pd
from sklearn import datasets, model_selection, svm
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import matplotlib as mpl

if __name__ == '__main__':
    iris_dataset = load_iris()
    # 调用 load_iris 函数来加载数据
    # load_iris 返回的 iris 对象是一个 Bunch 对象，与字典非常相似，里面包含键和值
    # 了解数据
    print("keys of iris_dataset: \n{}".format(iris_dataset.keys()))
    print(iris_dataset)
    print(iris_dataset['DESCR'] + "\n..")

    print("target names: \n{}".format(iris_dataset['data']))

    print("target names: \n{}".format(iris_dataset['target_names']))

    print("Feature names: \n{}".format(iris_dataset['feature_names']))
    # 'sepal length':花萼长度 'sepal width':花萼宽度 'petal length':花瓣长度 'petal width':花瓣宽度
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        iris_dataset['data'], iris_dataset['target'], random_state=0)
    iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
    '''scikit-learn 中的 train_test_split 函数可以打乱数据集并进行拆分。这个函数将 75% 的
    行数据及对应标签作为训练集，剩下 25% 的数据及其标签作为测试集。训练集与测试集的分配比例
    可以是随意的，但使用 25% 的数据作为测试集是很好的经验法则。利用 random_state 参数指定了
    随机数生成器的种子。这样函数输出就是固定不变的，所以这行代码的输出始终相同'''

    grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
                                     hist_kwds={'bins': 20}, s=60, alpha=.8)  # 画出散点图
    plt.show()

    # KNN
    from sklearn.neighbors import KNeighborsClassifier

    knn = KNeighborsClassifier(n_neighbors=25)  # k近邻分类器
    knn.fit(X_train, y_train)
    '''想要基于训练集来构建模型，需要调用 knn 对象的 fit 方法，输入参数为 X_train 和 y_
    train，二者都是 NumPy 数组，前者包含训练数据，后者包含相应的训练标签'''

    '''
    #prediction 测试1
    X_new = np.array([[5, 2.9, 1, 0.2]])
    print("X_new.shape: {}".format(X_new.shape))

    prediction = knn.predict(X_new)
    print("Prediction: {}".format(prediction))
    print("Predicted target name: {}".format(iris_dataset['target_names'][prediction]))
    '''

    y_pred = knn.predict(X_test)
    print("Test set predictions:\n {}".format(y_pred))

    print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))

    #K-means
    iris = datasets.load_iris()

    # 2.取特征空间中的4个维度
    X = iris.data[:, :4]
    # 3.搭建模型，构造KMeans聚类器，聚类个数为3
    estimator = KMeans(n_clusters=3)
    # 开始聚类训练
    estimator.fit(X)
    # 获取聚类标签
    label_pred = estimator.labels_
    # 绘制数据分布图（数据可视化）
    plt.scatter(X[:, 0], X[:, 1], c="red", marker='o', label='see')
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.legend(loc=2)
    plt.show()
    # 绘制k-means结果
    x0 = X[label_pred == 0]
    x1 = X[label_pred == 1]
    x2 = X[label_pred == 2]
    plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')
    plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')
    plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')
    # 花瓣的长宽
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.legend(loc=2)
    plt.show()
