import streamlit as st
import pandas as pd
from sktime.datasets import load_airline

# ページ設定
st.set_page_config(
    page_title="Streamlitの基本的な使い方",
    page_icon="✏️",
    layout="wide",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
    }
)

st.title("Streamlitの基本的な使い方")

st.markdown("### インストール")

st.write("Stremlitをインストールします。")
st.code("pip install streamlit", language="bash")


st.markdown("### アプリの作り方")

st.write("streamlitインストール後は、非常に簡単な操作でアプリケーションが立ち上がります。")
st.write("1. ファイル（app.py）を作る")
code_hello = """
import streamlit as st
st.title("hello")
"""
st.code(code_hello, language="python")
st.write("2. 以下のコマンドを実行")
st.code("streamlit run app.py", language="bash")
st.write("このように、簡単にWebUIが作成できました。")
st.image("./images/code_hello.png", use_column_width=True)


st.markdown("### 基本的な使い方")

st.write("streamlitが提供する基本的な機能を紹介します。")
st.markdown("#### 汎用的な関数：st.write()")
"""
`st.write()`は任意のオブジェクトを表示することができます。
"""
st.markdown("##### 使い方")

st.markdown("###### 1. 文字列と数字")
code_write_text_integer = """
st.write('Hello, **World**! :sunglasses:')
st.write("1 + 1 = ", 2)
"""
st.code(code_write_text_integer, language="python")
st.write('Hello, **World**! :sunglasses:')
st.write("1 + 1 = ", 2)

st.markdown("###### 2. データフレーム")
code_write_dataframe = """
df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})
st.write(df)
"""
st.code(code_write_dataframe, language="python")
df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})
st.write(df)

st.markdown("###### 3. HTML")
code_write_html = '''
st.write(
    """
    <p style="
        color:blue;
        background:lightblue;
        font-size:16px;
        font-weight: bold;"
    >
        テキストを装飾しています。
    </p>
    """,
    unsafe_allow_html=True
)
'''
st.code(code_write_html, language="python")
st.write(
    """
    <p style="
        color:blue;
        background:lightblue;
        font-size:16px;
        font-weight: bold;"
    >
        テキストを装飾しています。
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("""---""")

st.markdown("#### テキスト")
st.markdown("`st.write()`以外にもテキストを表示するための様々な関数があります。")
select_method = st.selectbox(
    "関数を選んでください",
    ("st.markdown","st.title","st.header","st.subheader","st.caption","st.code","st.latex")
)
if select_method == "st.markdown":
    st.markdown("Hello World!")
elif select_method == "st.title":
    st.title("Hello World!")
elif select_method == "st.header":
    st.header("Hello World!")
elif select_method == "st.subheader":
    st.subheader("Hello World!")
elif select_method == "st.caption":
    st.caption("Hello World!")
elif select_method == "st.code":
    st.code("Hello World!", language="python")
elif select_method == "st.latex":
    st.latex("Hello World!")

st.markdown("""---""")

st.markdown("#### グラフ")
st.write("次に、グラフの表示関数をいくつか紹介します。")
y1 = load_airline()
st.markdown("##### 折れ線グラフ：line_chart")
st.line_chart(y1)
st.code("""
y1 = load_airline()
st.line_chart(y1)
""", language="python")

st.markdown("##### エリアチャート：area_chart")
st.area_chart(y1)
st.code("""
y1 = load_airline()
st.area_chart(y1)
""", language="python")

st.markdown("##### 棒グラフ：bar_chart")
st.bar_chart(y1)
st.code("""
y1 = load_airline()
st.bar_chart(y1)
""", language="python")

st.markdown("""---""")

st.markdown("#### ウィジェット")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("##### ボタン")
    clicked = st.button("Click me")
with col2:
    st.markdown("##### ダウンロード")
    text_contents = "This is some text"
    st.download_button("Download file", text_contents)
with col3:
    st.markdown("##### チェックボックス")
    selected = st.checkbox("I agree")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("##### ラジオボタン")
    choice = st.radio("Pike one", ("選択肢1", "選択肢2", "選択肢3")) 
with col5:
    st.markdown("##### セレクトボックス")
    choice = st.selectbox("Pike one", ("選択肢1", "選択肢2", "選択肢3")) 
with col6:
    st.markdown("##### マルチセレクトボックス")
    st.multiselect("メニューリスト（複数選択可）", ("選択肢1", "選択肢2", "選択肢3"))

col7, col8, col9 = st.columns(3)

with col7:
    st.markdown("##### テキスト入力")
    name = st.text_input("First name") 
with col8:
    st.markdown("##### 数字入力")
    choice = st.number_input("Pike a number", 0, 10) 
with col9:
    st.markdown("##### テキストエリア")
    st.text_area("Text to translate")

st.markdown("##### コード")
st.code("""
clicked = st.button("Click me")

text_contents = "This is some text"
st.download_button("Download file", text_contents)

selected = st.checkbox("I agree")

choice = st.radio("Pike one", ("選択肢1", "選択肢2", "選択肢3")) 

choice = st.selectbox("Pike one", ("選択肢1", "選択肢2", "選択肢3")) 

st.multiselect("メニューリスト（複数選択可）", ("選択肢1", "選択肢2", "選択肢3"))

name = st.text_input("First name") 

choice = st.number_input("Pike a number", 0, 10) 

st.text_area("Text to translate")
""", language="python")
st.markdown("""---""")