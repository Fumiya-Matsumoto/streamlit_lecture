import streamlit as st
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import plotly.graph_objects as go

import sys
sys.path.append("../")
import iris

@st.cache
def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target_names[iris.target]
    return df

# ページ設定
st.set_page_config(
    page_title="irisデータセットで試す",
    page_icon="🌺",
    layout="wide",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
    }
)

df = load_data()
targets = list(df.target.unique())

st.title("Irisデータセットで試す")

st.markdown("### データの可視化")
selected_targets = st.multiselect('ターゲットを選んでください', targets, default=targets)
df = df[df.target.isin(selected_targets)]

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### データフレーム")
    st.dataframe(df.style.highlight_max(axis=0))
with col2:
    st.markdown("#### 統計量")
    st.dataframe(df.describe())

col3, col4 = st.columns(2)
with col3:
    st.markdown("#### ターゲット割合")
    fig_target = go.Figure(data=[go.Pie(labels=df.target,hole=.3)])
    st.plotly_chart(fig_target, use_container_width=True)
with col4:
    st.markdown("#### 散布図")
    selected_x = st.selectbox('x軸のカラムを選んでください', df.columns)
    selected_y = st.selectbox('y軸のカラムを選んでください', df.columns)
    fig = plt.figure()
    for target in selected_targets:
        x = df[df["target"] == target][selected_x]
        y = df[df["target"] == target][selected_y]
        plt.scatter(x, y, label=target)
    plt.xlabel(selected_x)
    plt.ylabel(selected_y)
    plt.tight_layout()
    plt.legend()
    st.pyplot(fig)

st.markdown("---")
st.markdown("### 機械学習の実装")

train_data = df.drop("target", axis=1)
labels = df.target
methods = ["-","fisher", "logistic", "svc", "decision_tree", "kneighbors"]

method = st.selectbox('機械学習の手法を選んでください', methods)

if method:
    if method != "-":
        predicted_labels, score = iris.predict(method, train_data, labels)
        st.write(f"正答率：{score}")
