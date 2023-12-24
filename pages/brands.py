import streamlit as st
import pandas as pd

st.sidebar.markdown("brands")

st.title("브랜드")

tab_brand, tab_type = st.tabs(["Brand", "Type"])          

with tab_brand:
    
    st.markdown("### 올리브영 인기 생리용품 브랜드 살펴보기 🔎 ")
    st.warning("해당 데이터는 2023년 12월 20일 기준으로 수집한 데이터입니다")
    st.warning("'생리대' 범주에서 인기순 top 20 제품과 '탐폰 & 생리컵' 범주에서의 \
        모든 제품의 리뷰 데이터를 분석한 자료임을 참고해주세요")
    
    expand_faq1 = st.expander('''1. 라엘''')
    with expand_faq1:
        st.image('data/rael.jpg',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 라엘은 미국 아마존 생리대 부문 1위를 찍고 한국으로 건너온 브랜드입니다. \
            100% 유기농 순면을 사용하고 있고 생리대, 탐폰, 생리컵, 면생리대 등 \
            다양한 타입의 생리용품 및 건강 식품도 함께 판매하고 있습니다.     ''', unsafe_allow_html=True)
        st.write('''< 라엘 생리대 키워드 >''', unsafe_allow_html=True)
        st.write('''라엘 생리대 리뷰에서 생리대와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 궁금하다면 참고해보세요''', unsafe_allow_html=True)
        df= pd.DataFrame({
            '좋다':[1.01],
            '유기농':[0.23],
            '흡수':[0.17],
            '순면':[0.14],
            '추천':[0.12],
            })
        st.dataframe(df)

        st.write('''< 라엘 탐폰 키워드 >''', unsafe_allow_html=True)
        df_t= pd.DataFrame({
            '좋다':[0.50],
            '흡수력':[0.17],
            '추천':[0.13],
            '편하':[0.11],
            '재구매':[0.10],
            })
        st.dataframe(df_t)
        
    expand_faq1 = st.expander('''2. 이너시아''')
    with expand_faq1:
        st.image('data/inersia.jpg',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' " 생리대도 과학이다 " 2022년도에 등장한 KAIST 여성 과학자 4명이 연구 및 개발한 \
            과학적인 생리대!! 이너시아는 수술실 지혈 소재에서 착안한 흡수 소재 함유 + \
            100% 유기농 순면의 생리대를 판매하고 있습니다.      ''', unsafe_allow_html=True)
        st.write('''< 이너시아 생리대 키워드 >''', unsafe_allow_html=True)
        st.write('''이너시아 리뷰에서 생리용품과 연관이 있으면서 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 궁금하다면 참고해보세요''', unsafe_allow_html=True)
        df= pd.DataFrame({
            '좋다':[1.31],
            '흡수':[0.36],
            '유기농':[0.34],
            '순면':[0.15],
            '편하다':[0.12],
            })
        st.dataframe(df)
        

        
     



    
st.sidebar.markdown("🍄WHAT IS 독버섯?")
st.sidebar.markdown(
    "그냥 프로젝트성 팀인디요...🥸"  
    )    