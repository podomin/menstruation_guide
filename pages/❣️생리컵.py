import streamlit as st
import pandas as pd
from PIL import Image

st.title("생리컵 (삽입형 생리용품)")

cols = st.columns(2)
with cols[0]:
    st.error("생리컵: 질내에 삽입해서 사용하는 다회용 생리용품")
    st.error("다회용이기 때문에 고정 비용 절감 + 환경 보호 가능")
    st.error("4~6시간 주기로 교체 권장하지만 12시간까지 사용 가능")
    st.error("한 번 사용하고 꼭 뜨거운 물로 소독 필수! 2년마다 새 제품으로 교체 필요!")
with cols[1]:
    st.image("./data/pad_illust.png")    
    
st.markdown("### 생리컵 리뷰 워드클라우드")
st.markdown("➡️ 워드클라우드는 자료의 빈도를 시각적으로 나타내는 데이터 시각화 방법 중 하나입니다.")
if st.toggle("### 워드클라우드 시각화 보기"):
    image = Image.open('./data/cup_wc.png')
    st.image(image, width=700)