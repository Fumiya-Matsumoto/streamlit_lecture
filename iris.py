from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

def predict(method, train_data, labels, columns=None):
    if method == "fisher":
        # インスタンス生成
        lda = LinearDiscriminantAnalysis(
            solver="svd", 
            shrinkage=None, 
            n_components=None
        )
        # 学習
        lda.fit(train_data, labels)
        # 推論
        predicted_labels = lda.predict(train_data)
        score = lda.score(train_data, labels)
    elif method=="logistic":
        # インスタンス生成
        lr = LogisticRegression(
            penalty="l2", 
            C=1.0, 
            random_state=0, 
            solver="liblinear"
        )
        # 学習
        lr.fit(train_data, labels)
        # 推論
        predicted_labels = lr.predict(train_data)
        score = lr.score(train_data, labels)
    elif method=="svc":
        # インスタンス生成
        svm = SVC(kernel="rbf", C=1, gamma=0.5, random_state=0)
        # 学習
        svm.fit(train_data, labels)
        # 推論
        predicted_labels = svm.predict(train_data)
        score = svm.score(train_data, labels)
    elif method=="decision_tree":
        # インスタンス生成
        dtree = DecisionTreeClassifier(
            criterion="gini", 
            max_depth=3, 
            random_state=0
        )
        # 学習
        dtree.fit(train_data, labels)
        # 推論
        predicted_labels = dtree.predict(train_data)
        score = dtree.score(train_data, labels)
    elif method=="kneighbors":
        # インスタンス生成
        knn = KNeighborsClassifier(n_neighbors=5, p=2, metric="minkowski")
        # 学習
        knn.fit(train_data, labels)
        # 推論
        predicted_labels = knn.predict(train_data)
        score = knn.score(train_data, labels)
    
    return predicted_labels, score