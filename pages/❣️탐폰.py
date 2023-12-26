import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(layout="wide")

st.title("탐폰 (삽입형 생리용품)")

cols = st.columns(2)
with cols[0]:
    st.error("탐폰: 질내에 삽입해서 사용하는 일회용 생리용품")
    st.error("4시간 주기로 교체 권장! 7~8시간 이상 장시간 사용시 독성 쇼크 증후군 위험!")
    st.error("외부 접촉이 없어서 피부나 냄새에 민감하다면 추천")
    st.error("활동성 UP! 수영할 때도 사용 가능")
with cols[1]:
    st.image("./data/pad_illust.png")   


st.markdown("### 탐폰 리뷰 워드클라우드")
st.markdown("➡️ 워드클라우드는 자료의 빈도를 시각적으로 나타내는 데이터 시각화 방법 중 하나입니다.")
if st.toggle("### 워드클라우드 시각화 보기"):
    image = Image.open('./data/tampon_wc.png')
    st.image(image, width=700) 
    

st.markdown("### 브랜드 별 탐폰 Boxplot 시각화")
st.markdown("➡️ Boxplot은 데이터들의 통계 정보, 분포, 이상치를 시각적으로 보여주는 시각화 차트입니다.")
if st.toggle("### Boxplot 보기"):
    image = Image.open('./data/tampon_box.png')
    st.image(image, width=800)
    st.markdown("( 해당 데이터는 탐폰 만족도 리뷰의 흡수도(1,2,3점), 촉감(1,2,3점), 자극(1,2,3점) 점수의 평균을 기준으로 측정한 그래프입니다 )")
    
    st.markdown("🧐** 위 박스플롯 그래프를 살펴보면 해피문데이의 만족도 평균 점수 분포가 가장\
        상위권에 위치해 있다는 것을 확인할 수 있습니다. 타 브랜드에 비해 높은 해피문데이의 평균 점수가 \
        통계적으로 사실인지 확인하기 위해 아래에서 t-test를 진행해보겠습니다 **")
    
st.markdown("### 해피문데이 VS 템포")
st.write("🧐 위 박스플롯 그래프 속 해피문데이의 높은 평균 점수가 사실인지 확인하기 위해 t-test를 진행해보겠습니다.\
    템포가 탐폰 부문에서 리뷰 수가 가장 많았기 때문에 템포의 평균 점수와 비교를 해보도록 하겠습니다.")
st.markdown("< t-test 결과 확인하기 >")
st.image("./data/happy_ttest.png")
st.write("위 이미지 속 p-value의 가장 마지막에 있는 값이 유의수준 0.05보다 작기 때문에\
    귀무가설(H0)을 기각하고 대립가설(H1)을 채택할 수 있습니다.\
    즉, 해피문데이 탐폰 리뷰의 만족도 평균 점수가 템포 탐폰 리뷰의 만족도 평균 점수보다 통계적으로도 높다고 할 수 있습니다.")


st.markdown("### (국내) 해피문데이 VS (해외) 라엘")
st.write(" 🧐 위 박스플롯 그래프 속 평균 점수 분포가 상위에 위치에 있는 브랜드는 해피문데이입니다.\
    이번에는 국내 브랜드인 해피문데이 만족도 평균 점수와 생리대 부문에서 상위권에 속해 있었던 해외 브랜드 라엘의 \
    탐폰 만족도 평균 점수 차이의 통계적으로 비교해보기 위해 t-test를 진행해보겠습니다. ")
st.image("./data/tampon_ttest.png")
st.write("위 이미지 속 p-value의 가장 마지막에 있는 값이 유의수준 0.05보다 크기 때문에\
    귀무가설(H0)을 기각하지 않고 채택해야 합니다.\
    즉, 라엘 탐폰 리뷰의 만족도 평균 점수가 해피문데이 탐폰 리뷰의 만족도 평균 점수보다 통계적으로도 높다고 볼 수 있습니다.")

st.markdown("### 브랜드 별 키워드 비율 시각화")
if st.toggle("### 바그래프 보기"):
    image = Image.open('./data/tampon_p.png')
    st.image(image, use_column_width=True)
    st.markdown("위 그래프는 브랜드 별 탐폰 리뷰에서 로 생리용품과 관련된 키워드의 빈도수를 시각화한 바그래프입니다.  ")

cols = st.columns(4)
with cols[0]:
    with st.expander(label=f"**Keyword - '좋다'**"):
        st.write("탐폰 리뷰에서 '좋다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 나트라케어 ")
        
    with st.expander(label=f"**Keyword - '흡수력'**"):
        st.write("탐폰 리뷰에서 '흡수력' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 순수한면 ")
        df= pd.DataFrame({'흡수력':[0.448]})
        st.dataframe(df)
        
with cols[1]:
    with st.expander(label=f"**Keyword - '재구매'**"):
        st.write("탐폰 리뷰에서 '재구매' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 나트라케어 ")
        df= pd.DataFrame({'재구매':[0.799]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '나쁘다'**"):
        st.write("탐폰 리뷰에서 '나쁘다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 순수한면 ")
        df= pd.DataFrame({'나쁘다':[0.065]})
        st.dataframe(df)

with cols[2]:      
    with st.expander(label=f"**Keyword - '편하다'**"):
        st.write("탐폰 리뷰에서 '편하다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 템포 ")
        df= pd.DataFrame({'편하다':[0.301]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '아프다'**"):
        st.write("탐폰 리뷰에서 '아프다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 순수한면 ")
        df= pd.DataFrame({'아프다':[0.047]})
        st.dataframe(df)

with cols[3]:
    with st.expander(label=f"**Keyword - '어렵다'**"):
        st.write("탐폰 리뷰에서 '어렵다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 나트라케어 ")
        df= pd.DataFrame({'어렵다':[0.0798]})
        st.dataframe(df)
        
