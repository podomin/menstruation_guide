import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(layout="wide")

st.title("생리컵 (삽입형 생리용품)")

cols = st.columns(2)
with cols[0]:
    st.error("🩸 생리컵: 질내에 삽입해서 사용하는 다회용 생리용품")
    st.error("🩸 다회용이기 때문에 고정 비용 절감 + 환경 보호 가능해요")
    st.error("🩸 4~6시간 주기로 교체 권장하지만 11시간까지 사용 가능해요")
    st.error("🩸 사용 전과 후에 꼭 뜨거운 물로 소독 필수! ")
    st.error("🩸 위생상 2년마다 새 제품으로 교체 필요!")
with cols[1]:
    st.image("./data/cup_ill.png")   

st.write("")
st.markdown("------------------")
st.write("")

st.warning("해당 데이터는 2023년 12월 20일 기준으로 수집한 데이터입니다. 올리브영의 '패드형 생리대' 범주에서 인기순 top 20 제품과 '탐폰 & 생리컵' 범주에서의 \
        모든 제품의 리뷰 데이터를 분석한 자료임을 참고해주세요") 

st.write("") 
    
st.markdown("### 생리컵 키워드 - 브랜드 3대장 🏆")
st.markdown(" 생리컵 구매 시 어떤 요소가 가장 중요할까요? \
    '재구매' 여부는 다른 소비자가 제품을 구매할 때 큰 영향을 줄 수 있는 키워드죠 \
    '부드럽다'와 '편하다'는 생리컵 내구성과 일상 속 활동성의 자유를 줄 수 있는 중요한 키워드이고요.  \
    그래서 '재구매', '부드럽다', '편하다' 키워드가 생리컵 리뷰 데이터에서 가장 자주 등장했던\
    브랜드를 찾아 소개하려고 합니다.  \
    ")

cols = st.columns(3)
with cols[0]:
    with st.expander(label=f"**1. 재구매**"):
        st.image('data/hana.png',  use_column_width=True)
        st.markdown(" #### 재구매 💘 한나 ")
        st.write(" 리뷰 분석 결과, '재구매' 키워드 등장 비율이 가장 높았던 브랜드는 바로 한나입니다! ")
        
with cols[1]:
    with st.expander(label=f"**2. 편하다**"):
        st.image('data/raeel.png',  use_column_width=True)
        st.markdown(" #### 편하다 💘 라엘 ")
        st.write(" 리뷰 분석 결과, '편하다' 키워드 등장 비율이 가장 높았던 브랜드는 바로 라엘입니다! ")
        
with cols[2]:
    with st.expander(label=f"**3. 부드럽다**"):
        st.image('data/happymoon.png',  use_column_width=True)
        st.markdown(" #### 부드럽다 💘 해피문데이 ")
        st.write(" 리뷰 분석 결과, '부드럽다' 키워드 등장 비율이 가장 높았던 브랜드는 바로 해피문데이입니다! ")

st.write("") 
st.write("")     

st.markdown("### 생리컵 브랜드 별 키워드 비율 더 자세히 알아보기")
st.markdown("➡️ 올리브영 입점 브랜드 17개의 리뷰 웹클로링, 전처리, 형태소 분석기로 토큰화 작업을 거친 후,\
    생리용품 관련 키워드의 빈도수를 측정 및 시각화를 진행한 그래프입니다.")
if st.toggle("🧐 그래프 보기"):
    image = Image.open('./data/cup_p.png')
    st.image(image, use_column_width=True)
    st.markdown("위 그래프는 브랜드 별 생리컵 리뷰에서 생리컵과 관련된 키워드의 빈도수를 시각화한 바그래프입니다.  ")

cols = st.columns(4)
with cols[0]:
    with st.expander(label=f"**Keyword - '편하다'**"):
        st.write("😍 생리컵 리뷰에서 '편하다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 라엘 ")
        df= pd.DataFrame({'편하다':[0.714]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '어렵다'**"):
        st.write("😭 생리컵 리뷰에서 '어렵다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 해피문데이 ")
        df= pd.DataFrame({'편하다':[0.583]})
        st.dataframe(df)
        
with cols[1]:
    with st.expander(label=f"**Keyword - '좋다'**"):
        st.write("😍 생리컵 리뷰에서 '좋다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 라엘 ")
        df= pd.DataFrame({'편하다':[1.19]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '불편'**"):
        st.write("😭 생리컵 리뷰에서 '불편' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 라엘 ")
        df= pd.DataFrame({'불편':[0.429]})
        st.dataframe(df)

with cols[2]:      
    with st.expander(label=f"**Keyword - '재구매'**"):
        st.write("😍 생리컵 리뷰에서 '재구매' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 루나컵 ")
        df= pd.DataFrame({'재구매':[0.025]})
        st.dataframe(df)
        st.write(" 리뷰가 8개 뿐인 한나(0.0387)는 데이터 신뢰도? 관계로 제외")


with cols[3]:
    with st.expander(label=f"**Keyword - '부드럽다'**"):
        st.write("😍 생리컵 리뷰에서 '부드럽다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 해피문데이 ")
        df= pd.DataFrame({'부드럽다':[0.083]})
        st.dataframe(df)
    
st.markdown("### 생리컵 리뷰 워드클라우드")
st.markdown("➡️ 워드클라우드는 자료의 빈도를 시각적으로 나타내는 데이터 시각화 방법 중 하나입니다.")
if st.toggle("### 워드클라우드 시각화 보기"):
    image = Image.open('./data/cup_wc.png')
    st.image(image, width=700)
st.markdown("- 위의 시각화 자료를 살펴보면 글자 크기를 기준으로 사용자의 \
    니즈를 한 눈에 파악할 수 있다. ")
st.markdown("- 컵형에서 가장 많이 등장하는 키워드는 ‘처음’ 이다.\
    대부분 패드형을 쓰다가 환경이나 다른 요소들을 생각해서 \
    컵형으로 넘어오게 되는데, 아마 이런 이유에서 ‘처음’ 이라는 \
    키워드가 많이 등장한 것으로 보인다. 또한 생리컵은 삽입하는 방식이기 때문에 \
    ‘편함‘의 정도와 ‘사이즈‘가 제품을 고를 때 가장 중요한 키워드인 \
    것으로 예상해볼 수 있다.")
st.markdown("- 생리컵에서 가장 많이 등장한 브랜드는 ‘티읕‘과 ‘루나컵’ 이었다.")


st.write("")
st.markdown("------------------")
st.write("")

st.markdown("### 브랜드 별 생리컵 Boxplot 시각화")
st.markdown("➡️ Boxplot은 데이터들의 통계 정보, 분포, 이상치를 시각적으로 보여주는 시각화 차트입니다.")
st.markdown(" ( 해당 데이터는 올리브영 생리컵 리뷰에 포함된 생리컵 만족도 관련 키워드 등장 여부를 측정한 값의 평균을 기준으로 시각화한 그래프입니다 )")   
with st.expander(label=f"**측정 기준 자세히 보기**"):
    cols = st.columns(3)
    with cols[0]:
        st.write("사용성")
        df= pd.DataFrame({
                    '쉽다 O': '2점',
                    '어렵다 O': '1점',
                    '쉽다 X 어렵다 X': '0점'}, index=['키워드 등장'])
        st.dataframe(df)
    
    with cols[1]:
        st.write("편의성")
        df= pd.DataFrame({
                    '편하다 O': '2점',
                    '불편하다 O': '1점',
                    '편하다 X 불편하다 X ': '0점'}, index=['키워드 등장'])
        st.dataframe(df)
    
    with cols[2]:
        st.write("재구매")
        df= pd.DataFrame({
                    'O': '1점',
                    'X': '0점'}, index=['키워드 등장'])
        st.dataframe(df)
        

        
if st.toggle("### Boxplot 보기"):
    image = Image.open('./data/cup_box.png')
    st.image(image, width=600)
st.write("")
st.markdown(" ##### 📌박스플롯 파헤치기")   
st.markdown("- 위 박스플롯 그래프를 살펴보면 티읕과 라엘의 생리컵 평균 점수 분포가 거의\
    일치하는 것을 확인할 수 있습니다. 과연 두 브랜드의 평균 점수가 동일한 것이 \
    통계적으로 사실인지 확인하기 위해 아래에서 t-test를 진행해보겠습니다")

st.write("")
st.write("")

st.markdown("### 티읕 VS 라엘 t-test")
st.markdown("➡️ t-test는 두 집단 간의 평균 차이가 유의미한지 검증하는 통계 방법입니다.")
with st.expander(label=f"**리뷰 평균 점수가 동일한 브랜드 1 VS 리뷰 평균 점수가 동일한 브랜드 2**"): 
    st.write("📌 위 박스플롯 그래프에서 나타난 것처럼 티읕 생리컵과 라엘 생리컵의 \
        평균 점수 정말 동일한지 t-test를 통해 확인해보도록 하겠습니다.")
    st.markdown("< t-test 결과 확인하기 >")
    st.image("./data/cup_ttest.png")
    st.write("위 이미지 속 p-value의 가장 마지막에 있는 값이 유의수준 0.05보다 작기 때문에\
        귀무가설(H0)을 기각하고 대립가설(H1)을 채택할 수 있습니다.\
    즉, 티읕 생리컵과 라엘 생리컵의 리뷰 평균 점수의 차이는 0이 아닙니다.")
    st.markdown(" ##### 결론 : 박스플롯에서 평균 점수가 동일해 보였던 티읕과 라엘의 생리컵\
        리뷰 평균 점수는 통계적으로 동일하다고 볼 수 없다.")

st.write("")
