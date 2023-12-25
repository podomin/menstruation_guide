import streamlit as st
import pandas as pd
from PIL import Image
#st.set_page_config(layout="centered")
  
st.title("생리대 (패드형 생리용품)")

cols = st.columns(2)
with cols[0]:
    st.error("생리대: 팬티에 부착해서 사용하는 일회용 생리용품")
    st.error("사용법이 간단해서 생리용품 사용이 처음이라면 생리대를 추천해요. ")
    st.error("다양한 사이즈 및 용도별(오버나이트, 입는형) 등 다양한 옵셜 별 제품이 있음")
    st.error("위생상 3~4시간 주기로 교체 권장")
with cols[1]:
    st.image("./data/pad_illust.png")    

st.markdown("### 생리대 리뷰 워드클라우드")
st.markdown("➡️ 워드클라우드는 자료의 빈도를 시각적으로 나타내는 데이터 시각화 방법 중 하나입니다.")
if st.toggle("### 워드클라우드 시각화 보기"):
    image = Image.open('./data/pad_wc.png')
    st.image(image, width=700)
    
    
st.markdown("### 브랜드 별 생리대 Boxplot 시각화")
st.markdown("➡️ Boxplot은 데이터들의 통계 정보, 분포, 이상치를 시각적으로 보여주는 시각화 차트입니다.")
if st.toggle("### Boxplot 보기"):
    image = Image.open('./data/pad_box.png')
    st.image(image, width=800)
    st.markdown("( 해당 데이터는 생리대 만족도 리뷰의 흡수도(1,2,3점), 촉감(1,2,3점), 자극(1,2,3점) 점수의 평균을 기준으로 측정한 그래프입니다 )")
    
    st.markdown("🧐** 타 브랜드와 비교했을 때, 이너시아의 평균 점수는 확실히 높은 편이다. \
        하지만 눈에 보이는 것이 다가 아닐 수 있다. 타 브랜드와 이너시아와의 평균 차이가 통계적으로도 \
        유의미하게 맞는 결과인지 아래에서 더 자세히 살펴보자 **")

st.markdown("### 이너시아 VS 좋은느낌")
st.write("🧐 위 박스플롯 그래프 속 이너시아의 높은 평균 점수가 사실인지 확인하기 위해 t-test를 진행해보겠습니다.\
    좋은 느낌 평균 점수와 비교를 해볼 건데 좋은느낌을 비교 대상으로 선택한 이유는 최근에 등장한 이너시아와 달리 역사가 오래된 생리용품 브랜드이고 리뷰 수 차이가 \
    가장 높았던 브랜드였기 때문입니다.")
st.markdown("< t-test 결과 확인하기 >")
st.image("./data/inersia_ttest.png")
st.write("위 이미지 속 p-value의 가장 마지막에 있는 값이 0.000~ 으로 유의수준 0.05보다 작기 때무에 \
    귀무가설(H0)을 기각하고 대립가설(H1)을 채택할 수 있습니다. \
    즉, 생리대 부문에서 이너시아 평균 점수가 좋은느낌 평균 점수보다 통계적으로도 분명히 높다고 볼 수 있습니다.")

st.markdown("### (국내) 유기농본 VS (해외) 라엘")
st.write(" 🧐 위 박스플롯 그래프 속 평균 점수 분포가 상위에 위치에 있는 브랜드는 \
    라엘, 이너시아 그리고 유기농본입니다. 이 중에서 국내 브랜드인 유기농본과 \
    해외 브랜드인 라엘의 만족도 평균 점수가 통계적으로 유의미한 차이가 있을지 t-test를 통해 살펴보겠습니다. ")
st.markdown("< t-test 결과 확인하기 >")
st.image("./data/pad_ttest.png")
st.write("위 이미지 속 p-value의 가장 마지막에 있는 값이 유의수준 0.05보다 작기 때문에\
    귀무가설(H0)을 기각하고 대립가설(H1)을 채택할 수 있습니다.\
    즉, 라엘 생리대 만족도 평균 점수가 유기농본 생리대 만족도 평균 점수보다 통계적으로도 높다라고 할 수 있습니다.")


st.markdown("### 브랜드 별 키워드 비율 시각화")
if st.toggle("### 바그래프 보기"):
    image = Image.open('./data/pad_p.png')
    st.image(image, use_column_width=True)
    st.markdown("위 그래프는 브랜드 별 생리대 리뷰에서 로 생리용품과 관련된 키워드의 빈도수를 시각화한 바그래프입니다.  ")

cols = st.columns(4)
with cols[0]:
    with st.expander(label=f"**Keyword - '흡수'**"):
        st.write("생리대 리뷰에서 '흡수' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 이너시아 ")
        df= pd.DataFrame({'흡수':[0.358]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '편하다'**"):
        st.write("생리대 리뷰에서 '편하다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 좋은느낌 ")
        df= pd.DataFrame({'편하다':[0.242]})
        st.dataframe(df)
        
with cols[1]:
    with st.expander(label=f"**Keyword - '좋다'**"):
        st.write("생리대 리뷰에서 '좋다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 쏘피 ")
        df= pd.DataFrame({'좋다':[0.994]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '불편'**"):
        st.write("생리대 리뷰에서 '불편' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 쏘피 ")
        df= pd.DataFrame({'불편':[0.128]})
        st.dataframe(df)

with cols[2]:
    with st.expander(label=f"**Keyword - '재구매'**"):
        st.write("생리대 리뷰에서 '재구매' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 아임오 ")
        df= pd.DataFrame({'재구매':[0.151]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '나쁘다'**"):
        st.write("생리대 리뷰에서 '나쁘다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 쏘피 ")
        df= pd.DataFrame({'나쁘다':[0.038]})
        st.dataframe(df)

with cols[3]:
    with st.expander(label=f"**Keyword - '가성비'**"):
        st.write("생리대 리뷰에서 '가성비' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 쏘피 ")
        df= pd.DataFrame({'가성비':[0.0895]})
        st.dataframe(df)
        


st.markdown("### '흡수력' 삼대장 생리대 제품")
st.markdown("패드형 생리대에서 흡수율은 굉장히 중요하죠. 생리대의 가장 필수적인 역할이기도 하고요.\
    그래서 '흡수력'를 키워드로 잡았을 때 해당 키워드가 리뷰에서 가장 자주 등장했던 \
    제품 TOP 3개를 소개하려고 합니다.  \
    ")

cols = st.columns(3)
with cols[0]:
    with st.expander(label=f"**1. 제품이름**"):
        st.image('data/inersia.png',  use_column_width=True)
        st.write("가격: 7000원")
        st.write(" < 제품 상세 설명 >")
        
with cols[1]:
    with st.expander(label=f"**2. 제품이름**"):
        st.image('data/inersia.png',  use_column_width=True)
        st.write("가격: 7000원")
        st.write(" < 제품 상세 설명 >")
        
with cols[2]:
    with st.expander(label=f"**3. 제품이름**"):
        st.image('data/inersia.png',  use_column_width=True)
        st.write("가격: 7000원")
        st.write(" < 제품 상세 설명 >")
