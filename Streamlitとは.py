import streamlit as st

# ページ設定
st.set_page_config(
    page_title="Streamlitとは",
    page_icon="☀️",
    layout="wide",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
    }
)

st.title("Stremlitとは")

st.image('./images/streamlit_01.png', use_column_width=True)

text = """
**Streamlit**は、PythonのWebアプリケーションフレームワーク

特に、データサイエンスや機械学習領域でのデータの可視化が**非常に簡単に**できる

大きな特徴としては
1. **Pythonのみ**で書ける（フロントエンドのコードが不要）
1. DataFrameなど**さまざまなライブラリ**の可視化にも対応
1. **マークダウン**での記載が可能
1. **コードの修正**が即座に反映
1. **デプロイ**が非常に簡単
"""
st.write(text)

st.markdown("### 他のWebアプリケーションフレームワークとの比較")

st.write("PythonのWebアプリケーションの他の有名なフレームワークDjango、Flaskと特徴を比較してみると、")

comparision_text = """
|フレームワーク|特徴|
|---|---|
|Django|ニュースサイトを管理する目的で開発されたフレームワーク。高速処理が強み。代表的なサービスは「Instagram」「Pinterest」|
|Flask|軽量で小規模開発に適したフレームワーク。デフォルトではDB機能を含まないなど、最小限の機能のみを提供。代表的なサービスは「Netflix」など|
|streamlit|簡単に素早くデータを可視化するためのフレームワーク。フロントエンドのコーディングが不要で開発が簡単。|
"""
st.write(comparision_text)


