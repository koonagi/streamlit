import streamlit as st
import pandas as pd
import base64

df = pd.DataFrame([['東京', 'とうきょう'], ['大阪', 'おおさか'], ['北海道', 'ほっかいどう']],columns=['漢字', 'ひらがな'])

st.table(df)
csv = df.to_csv(index=False)  

# utf-8
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:application/octet-stream;base64,{b64}" download="result_utf-8.csv">Download Link</a>'
st.markdown(f"CSVファイルのダウンロード(utf-8):  {href}", unsafe_allow_html=True)

# utf-8(BOM)
b64 = base64.b64encode(csv.encode('utf-8-sig')).decode()
href = f'<a href="data:application/octet-stream;base64,{b64}" download="result_utf-8-sig.csv">Download Link</a>'
st.markdown(f"CSVファイルのダウンロード(utf-8 BOM):  {href}", unsafe_allow_html=True)
