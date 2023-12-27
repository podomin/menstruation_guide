import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(layout="wide")
  
st.title("생리대 (패드형 생리용품)")

cols = st.columns(2)
with cols[0]:
    st.error("🩸 생리대 : 팬티에 부착해서 사용하는 일회용 생리용품")
    st.error("🩸 사용법이 간단해서 생리용품 사용이 처음이라면 생리대를 추천해요. ")
    st.error("🩸 다양한 사이즈 및 용도(오버나이트, 입는형) 등 다양한 옵셜 별 제품이 있어요")
    st.error("🩸 위생상 3~4시간 주기로 교체하는 것을 권장해요")
    st.error("🩸 피부가 민감하거나 알러지가 있다면 주의해서 사용하세요")
with cols[1]:
    st.image("./data/pad_ill.png") 

st.write("")
st.markdown("------------------")
st.write("")

st.warning("해당 데이터는 2023년 12월 20일 기준으로 수집한 데이터입니다. 올리브영의 '패드형 생리대' 범주에서 인기순 top 20 제품과 '탐폰 & 생리컵' 범주에서의 \
        모든 제품의 리뷰 데이터를 분석한 자료임을 참고해주세요") 

st.write("")
 
st.markdown("### 생리대 키워드 - 브랜드 3대장 🏆")
st.markdown(" 생리대 구매 시 어떤 걸 가장 중요하게 생각하시나요? \
    '흡수'는 생리대의 가장 필수적인 역할이죠. '재구매' 여부는 다른 소비자가 제품을 구매할 때 큰 영향을 줄 수 있는 키워드죠 \
    '가성비'는 저희의 통장이 텅장이 되지 않도록 도와주는 키워드이고요.  \
    그래서 '흡수', '재구매', '가성비' 키워드가 생리대 리뷰 데이터에서 가장 자주 등장했던\
    브랜드를 찾아 소개하려고 합니다.  \
    ")

cols = st.columns(3)
with cols[0]:
    with st.expander(label=f"**1. 흡수**"):
        st.image('data/inersia.png',  use_column_width=True)
        st.markdown(" #### 흡수 💘 이너시아 ")
        st.write(" 리뷰 분석 결과, '흡수' 키워드 등장 비율이 가장 높았던 브랜드는 바로 이너시아였습니다! ")
        
with cols[1]:
    with st.expander(label=f"**2. 재구매**"):
        st.image('data/imo.png',  use_column_width=True)
        st.markdown(" #### 재구매 💘 아임오 ")
        st.write(" 리뷰 분석 결과, '재구매' 키워드 등장 비율이 가장 높았던 브랜드는 바로 아임오아였습니다! ")
        
with cols[2]:
    with st.expander(label=f"**3. 가성비**"):
        st.image('data/sofy.png',  use_column_width=True)
        st.markdown(" #### 가성비 💘 쏘피 ")
        st.write(" 리뷰 분석 결과, '가성비' 키워드 등장 비율이 가장 높았던 브랜드는 바로 쏘피였습니다! ")
    
st.write("")
st.write("")
   
st.markdown("### 생리대 브랜드 별 키워드 비율 더 자세히 알아보기")
st.markdown("➡️ 올리브영 입점 브랜드 17개의 리뷰 웹클로링, 전처리, 형태소 분석기로 토큰화 작업을 거친 후,\
    생리대 관련 키워드의 빈도수를 측정 및 시각화를 진행한 그래프입니다.")
if st.toggle("🧐 그래프 보기"):
    image = Image.open('./data/pad_p.png')
    st.image(image, use_column_width=True)
    st.markdown("위 그래프는 브랜드 별 생리대 리뷰에서 로 생리대와 관련된 키워드의 빈도수를 시각화한 바그래프입니다.  ")

cols = st.columns(4)
with cols[0]:
    with st.expander(label=f"**Keyword - '흡수'**"):
        st.write("😍 생리대 리뷰에서 '흡수' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 이너시아 ")
        df= pd.DataFrame({'흡수':[0.358]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '편하다'**"):
        st.write("😍 생리대 리뷰에서 '편하다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 좋은느낌 ")
        df= pd.DataFrame({'편하다':[0.242]})
        st.dataframe(df)
        
with cols[1]:
    with st.expander(label=f"**Keyword - '좋다'**"):
        st.write("😍 생리대 리뷰에서 '좋다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 쏘피 ")
        df= pd.DataFrame({'좋다':[0.994]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '불편'**"):
        st.write("😭 생리대 리뷰에서 '불편' 키워드 빈도수가 가장 높았던 브랜드는...")
        st.markdown("#### 쏘피 ")
        df= pd.DataFrame({'불편':[0.128]})
        st.dataframe(df)

with cols[2]:
    with st.expander(label=f"**Keyword - '재구매'**"):
        st.write("😍 생리대 리뷰에서 '재구매' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 아임오 ")
        df= pd.DataFrame({'재구매':[0.151]})
        st.dataframe(df)
        
    with st.expander(label=f"**Keyword - '나쁘다'**"):
        st.write("😭생리대 리뷰에서 '나쁘다' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 쏘피 ")
        df= pd.DataFrame({'나쁘다':[0.038]})
        st.dataframe(df)

with cols[3]:
    with st.expander(label=f"**Keyword - '가성비'**"):
        st.write("😍 생리대 리뷰에서 '가성비' 키워드 빈도수가 가장 높았던 브랜드는... ")
        st.markdown("#### 쏘피 ")
        df= pd.DataFrame({'가성비':[0.0895]})
        st.dataframe(df)
        
st.write("")
st.write("")   

st.markdown("### 생리대 리뷰 워드클라우드")
st.markdown("➡️ 워드클라우드는 자료의 빈도를 시각적으로 나타내는 데이터 시각화 방법 중 하나입니다.")
if st.toggle("## 🧐 워드클라우드 보기"):
    image = Image.open('./data/pad_wc.png')
    st.image(image, width=700)
st.markdown("- 위의 시각화 자료를 살펴보면 글자 크기를 기준으로 사용자의 \
    니즈를 한 눈에 파악할 수 있다. ")
st.markdown("- 생리대를 구매할 때 가장 중요하게 생각하는 부분은 \
    ‘부드럽‘고 ‘흡수력‘이 좋아야하며 ‘피부‘에 ‘자극’이 덜한 \
    제품인 것으로 예상해볼 수 있다. 또한 피부에 닿는 면이 \
    유기농 순면인 제품을 조금 더 선호하는 것 같고, \
    생리대가 다른 생활용품에 비해 가격이 있는 편이라 \
    세일할 때 구매하는 것을 중요하게 생각하는 것으로 보인다.")
st.markdown("- 생리대에서 가장 많이 등장한 브랜드는 ‘좋은느낌‘과 ‘쏘피’ 이었다.")


st.write("")
st.markdown("------------------")
st.write("")  
    
st.markdown("### 브랜드 별 생리대 Boxplot")
st.markdown("➡️ Boxplot은 데이터들의 통계 정보, 분포, 이상치를 시각적으로 보여주는 시각화 차트입니다.")
st.markdown(" ( 해당 데이터는 올리브영 생리대 리뷰에 포함된\
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

if st.toggle("## 🧐 박스플롯 보기"):
    image = Image.open('./data/pad_box.png')
    st.image(image, width=600)
st.write("")
st.markdown(" ##### 📌박스플롯 파헤치기")
st.markdown("- 타 브랜드와 비교했을 때, 이너시아의 평균 점수가 확실히 높은 편이다. \
        하지만 눈에 보이는 것이 다가 아닐 수 있습니다. 타 브랜드와 이너시아와의 평균 차이가 통계적으로도 \
        유의미하게 맞는 결과인지 아래에서 더 자세히 살펴보겠습니다.")
st.markdown("- 박스플롯 그래프 속 평균 점수 분포가 가장 상위에 위치에 있는 국내 브랜드는 \
        이너시아, 유기농본이고 해외 브랜드는 라엘입니다. 국내와 해외 브랜드의 평균 차이가 통계적으로도 사실일지\
        아래에서 더 자세히 살펴보겠습니다.")

st.write("")
st.write("")

st.markdown("### 이너시아 VS 좋은느낌 t-test")
st.markdown("➡️ t-test는 두 집단 간의 평균 차이가 유의미한지 검증하는 통계 방법입니다.")
with st.expander(label=f"**루키 브랜드 VS 원조 브랜드**"): 
    st.write("📌 위 박스플롯 그래프 속 이너시아의 높은 평균 점수가 사실인지 확인하기 위해 t-test를 진행해보겠습니다.\
        좋은느낌 평균 점수와 비교를 해볼 건데 좋은느낌을 비교 대상으로 선택한 이유는 최근에 등장한 이너시아와 달리 역사가 오래된 생리용품 브랜드이고 리뷰 수 차이가 \
        가장 높았던 브랜드였기 때문입니다.")
    st.markdown("< t-test 결과 확인하기 >")
    st.image("./data/inersia_ttest.png")
    st.write("위 이미지 속 p-value의 가장 마지막에 있는 값이 0.000~ 으로 유의수준 0.05보다 작기 때무에 \
        귀무가설(H0)을 기각하고 대립가설(H1)을 채택할 수 있습니다. \
        즉, 생리대 부문에서 이너시아 평균 점수가 좋은느낌 평균 점수보다 통계적으로도 분명히 높다고 볼 수 있습니다.")
    st.markdown(" ##### 결론 : 루키 인기 브랜드인 이너시아의 평균 점수가 \
        원조격 브랜드인 좋은 느낌의 평균 점수보다 높은 것은 사실이다.")

st.write("")
st.write("")

st.markdown("### 유기농본 VS 라엘 t-test")
with st.expander(label=f"**국내 브랜드 VS 해외 브랜드**"): 
    st.write(" 📌위 박스플롯 그래프 속 평균 점수 분포가 상위에 위치에 있는 브랜드 \
        중에서 국내 브랜드인 유기농본과 해외 브랜드인 라엘의 평균 점수가 \
        통계적으로 유의미한 차이가 있을지 t-test를 통해 살펴보겠습니다. ")
    st.markdown("< t-test 결과 확인하기 >")
    st.image("./data/pad_ttest.png")
    st.write("위 이미지 속 p-value의 가장 마지막에 있는 값이 0.465~로 유의수준 0.05보다 작기 때문에\
        귀무가설(H0)을 기각할 수 없습니다.\
        즉, 라엘 생리대 리뷰 평균과 유기농본 생리대 리뷰 \
        평균이 통계적으로도 같다고 할 수 있습니다.")
    st.markdown(" ##### 결론 : 해외 브랜드인 라엘의 평균 점수와 국내 브랜드인 유기농본의 평균 점수는 같다.")




