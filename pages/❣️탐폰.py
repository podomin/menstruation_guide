import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(layout="wide")

st.title("탐폰 (삽입형 생리용품)")

cols = st.columns(2)
with cols[0]:
    st.error("🩸 탐폰: 질내에 삽입해서 사용하는 일회용 생리용품")
    st.error("🩸 4시간 주기로 교체하는 것을 권장해요! ")
    st.error("🩸 7~8시간 이상 장시간 사용시 독성 쇼크 증후군 위험이 있어요!")
    st.error("🩸 외부 접촉이 없어서 피부나 냄새에 민감하다면 추천해요")
    st.error("🩸 활동성 UP! 수영할 때도 사용 가능해요")
with cols[1]:
    st.image("./data/tampon_ill.png")  

st.write("")
st.markdown("------------------")
st.write("")

st.warning("해당 데이터는 2023년 12월 20일 기준으로 수집한 데이터입니다. 올리브영의 '패드형 생리대' 범주에서 인기순 top 20 제품과 '탐폰 & 생리컵' 범주에서의 \
        모든 제품의 리뷰 데이터를 분석한 자료임을 참고해주세요") 

st.write("") 

st.markdown("### 탐폰 키워드 - 브랜드 3대장 🏆")
st.markdown(" 탐폰 구매 시 어떤 걸 가장 중요하게 생각하시나요? \
    '흡수력'는 탐폰의 가장 필수적인 역할이죠. '재구매' 여부는 다른 소비자가 제품을 구매할 때 큰 영향을 줄 수 있는 키워드죠 \
    '편하다'는 탐폰의 착용 만족도를 알 수 있는 키워드이고요.  \
    그래서 '흡수력', '재구매', '편하다' 키워드가 탐폰 리뷰 데이터에서 가장 자주 등장했던\
    브랜드를 찾아 소개하려고 합니다.  \
    ")

cols = st.columns(3)
with cols[0]:
    with st.expander(label=f"**1. 흡수력**"):
        st.image('data/sunsu.png',  use_column_width=True)
        st.markdown(" #### 흡수력 💘 순수한면 ")
        st.write(" 리뷰 분석 결과, '흡수력' 키워드 등장 비율이 가장 높았던 브랜드는 바로 순수한면입니다! ")
        
with cols[1]:
    with st.expander(label=f"**2. 재구매**"):
        st.image('data/natra.png',  use_column_width=True)
        st.markdown(" #### 재구매 💘 나트라케어 ")
        st.write(" 리뷰 분석 결과, '재구매' 키워드 등장 비율이 가장 높았던 브랜드는 바로 나트라케어였습니다! ")
        
with cols[2]:
    with st.expander(label=f"**3. 편하다**"):
        st.image('data/tempo.png',  use_column_width=True)
        st.markdown(" #### 편하다 💘 템포 ")
        st.write(" 리뷰 분석 결과, '편하다' 키워드 등장 비율이 가장 높았던 브랜드는 바로 템포였습니다! ")
    
st.write("")
st.write("")

st.markdown("### 탐폰 브랜드 별 키워드 비율 더 자세히 알아보기")
st.markdown("➡️ 올리브영 입점 브랜드 17개의 리뷰 웹클로링, 전처리, 형태소 분석기로 토큰화 작업을 거친 후,\
    생리용품 관련 키워드의 빈도수를 측정 및 시각화를 진행한 그래프입니다.")
if st.toggle("🧐 그래프 보기"):
    image = Image.open('./data/tampon_p.png')
    st.image(image, use_column_width=True)
    st.markdown("위 그래프는 브랜드 별 탐폰 리뷰에서 탐폰과 관련된 키워드의 빈도수를 시각화한 바그래프입니다.  ")

cols = st.columns(4)
with cols[0]:
    with st.expander(label=f"**Keyword - '좋다'**"):
        st.write("😍 탐폰 리뷰에서 '좋다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 나트라케어 ")
        df= pd.DataFrame({'흡수력':[0.799]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '흡수력'**"):
        st.write("😍 탐폰 리뷰에서 '흡수력' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 순수한면 ")
        df= pd.DataFrame({'흡수력':[0.448]})
        st.dataframe(df)
        
with cols[1]:
    with st.expander(label=f"**Keyword - '재구매'**"):
        st.write("😍 탐폰 리뷰에서 '재구매' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 라엘 ")
        df= pd.DataFrame({'재구매':[0.0988]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '나쁘다'**"):
        st.write("😭 탐폰 리뷰에서 '나쁘다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 순수한면 ")
        df= pd.DataFrame({'나쁘다':[0.472]})
        st.dataframe(df)

with cols[2]:      
    with st.expander(label=f"**Keyword - '편하다'**"):
        st.write("😍 탐폰 리뷰에서 '편하다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 템포 ")
        df= pd.DataFrame({'편하다':[0.301]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '아프다'**"):
        st.write("😭 탐폰 리뷰에서 '아프다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 나트라케어 ")
        df= pd.DataFrame({'아프다':[0.799]})
        st.dataframe(df)

with cols[3]:
    with st.expander(label=f"**Keyword - '어렵다'**"):
        st.write("😭 탐폰 리뷰에서 '어렵다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 나트라케어 ")
        df= pd.DataFrame({'어렵다':[0.0799]})
        st.dataframe(df)
        

st.markdown("### 탐폰 리뷰 워드클라우드")
st.markdown("➡️ 워드클라우드는 자료의 빈도를 시각적으로 나타내는 데이터 시각화 방법 중 하나입니다.")
if st.toggle("🧐 워드클라우드 보기"):
    image = Image.open('./data/tampon_wc.png')
    st.image(image, width=700) 
st.markdown("- 위의 시각화 자료를 살펴보면 글자 크기를 기준으로 사용자의 \
    니즈를 한 눈에 파악할 수 있다. ")
st.markdown("- 탐폰을 구매할 때 가장 중요하게 생각하는 부분은\
    '흡수력'이 정도와 '편한'지 '불편'한지에 대한 '느낌'과 '자극'에 대한 여부 \
    이며 추가적으로 탐폰의 '사이즈'와 '세일'유무도 사용자가 제품을 구매하는데 큰 영향을  \
    미칠 것이라고 예상해볼 수 있다.")
st.markdown("- 탐폰에서 가장 많이 등장한 브랜드는 ‘템포‘와 ‘해피문데이’ 이었다.")

st.write("")
st.markdown("------------------")
st.write("")   
    

st.markdown("### 브랜드 별 탐폰 Boxplot 시각화")
st.markdown("➡️ Boxplot은 데이터들의 통계 정보, 분포, 이상치를 시각적으로 보여주는 시각화 차트입니다.")
st.markdown("( 해당 데이터는 올리브영 탐폰 리뷰에 포함된\
    흡수력, 촉감, 자극 리뷰를 점수화 한 값의 평균을 기준으로 측정한 그래프입니다 )")
with st.expander(label=f"**측정 기준 자세히 보기**"):
    cols = st.columns(3)
    with cols[0]:
        st.write("흡수력 점수 측정 기준")
        df= pd.DataFrame({
                    '아주 만족해요': '3점',
                    '보통이에요': '2점',
                    '다소 아쉬워요': '1점'}, index=['점수'])
        st.dataframe(df)
        
    with cols[1]:
        st.write("자극도 점수 측정 기준")
        df= pd.DataFrame({
                    '자극없이 순해요': '3점',
                    '보통이에요': '2점',
                    '자극이 느껴져요': '1점'}, index=['점수'])
        st.dataframe(df)
    
    with cols[2]:
        st.write("촉감 점수 측정 기준")
        df= pd.DataFrame({
                    '부드러워요': '3점',
                    '보통이에요': '2점',
                    '거친 편이에요': '1점'}, index=['점수'])
        st.dataframe(df)


if st.toggle("### Boxplot 보기"):
    image = Image.open('./data/tampon_box.png')
    st.image(image, width=600)
st.write("")
st.markdown(" ##### 📌박스플롯 파헤치기")   
st.markdown("- 위 박스플롯 그래프를 살펴보면 해피문데이의 만족도 평균 점수 분포가 가장\
        상위권에 위치해 있다는 것을 확인할 수 있습니다. 타 브랜드에 비해 높은 해피문데이의 평균 점수가 \
        통계적으로 사실인지 확인하기 위해 아래에서 t-test를 진행해보겠습니다")
st.markdown("- 생리대 때와 마찬가리로 해외 브랜드인 라엘과 가장 리뷰 점수가 높은 국내 탐폰 브랜드 \
        해피문데이를 비교해보겠습니다. 국내와 해외 브랜드의 평균 차이가 통계적으로도 사실일지\
        아래에서 더 자세히 살펴보겠습니다.")

st.write("")
st.write("")

st.markdown("### 해피문데이 VS 템포 t-test")
st.markdown("➡️ t-test는 두 집단 간의 평균 차이가 유의미한지 검증하는 통계 방법입니다.")
with st.expander(label=f"**리뷰 점수 가장 높은 브랜드 VS 리뷰 많은 브랜드**"): 
    st.write("📌 위 박스플롯 그래프 속 해피문데이의 높은 평균 점수가 사실인지 확인하기 위해 t-test를 진행해보겠습니다.\
        템포가 탐폰 부문에서 리뷰 수가 가장 많았기 때문에 템포의 평균 점수와 비교를 해보도록 하겠습니다.")
    st.markdown("< t-test 결과 확인하기 >")
    st.image("./data/moon_ttest.png")
    st.write("위 이미지 속 p-value의 가장 마지막에 있는 값이 유의수준 0.05보다 작기 때문에\
        귀무가설(H0)을 기각하고 대립가설(H1)을 채택할 수 있습니다.\
    즉, 해피문데이 탐폰 리뷰의 만족도 평균 점수가 템포 탐폰 리뷰의 만족도 평균 점수보다 통계적으로도 높다고 할 수 있습니다.")
    st.markdown(" ##### 결론 : 평점 높은 브랜드인 해피문데이의 평균 점수가 \
        리뷰 수가 압도적으로 많은 브랜드인 템포의 평균 점수보다 높은 것은 사실이다.")

st.write("")
st.write("")

st.markdown("### 해피문데이 VS 라엘 t-test")
with st.expander(label=f"**국내 브랜드 VS 해외 브랜드**"): 
    st.write(" 📌 이번에는 국내 브랜드인 해피문데이 만족도 평균 점수와 생리대 부문에서 상위권에 속해 있었던 해외 브랜드 라엘의 \
        탐폰 만족도 평균 점수 차이의 통계적으로 비교해보기 위해 t-test를 진행해보겠습니다. ")
    st.image("./data/tampon_ttest.png")
    st.write("위 이미지 속 p-value의 가장 마지막에 있는 값이 유의수준 0.05보다 크기 때문에\
        귀무가설(H0)을 기각할 수 없어 대립가설(H1)을 채택해야 합니다.\
        즉, 해피문데이 탐폰 리뷰의 평균 점수와 라엘 탐폰 리뷰의 평균 점수는 통계적으로 같다.")
    st.markdown(" ##### 결론 : 국내 브랜드인 해피문데이의 평균 점수가 \
        해외 브랜드인 라엘의 평균 점수보다 높은 것은 사실이 아니며 둘의 평균은 같다.")

