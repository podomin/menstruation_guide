import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(layout="wide")

st.title("생리용품 브랜드")         
 
st.markdown("### 올리브영 인기 생리용품 브랜드 살펴보기 ")
st.warning("해당 데이터는 2023년 12월 20일 기준으로 수집한 데이터입니다")
st.warning("올리브영의 '패드형 생리대' 범주에서 인기순 top 20 제품과 '탐폰 & 생리컵' 범주에서의 \
        모든 제품의 리뷰 데이터를 분석한 자료임을 참고해주세요")


st.markdown("### 생리용품 브랜드 17가지")

st.write("")
st.markdown("------------------")
st.write("")

cols = st.columns(2)
with cols[0]:
    with st.expander(label=f"**1. 라엘**"): 
        st.image('data/raeel.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 라엘은 미국 아마존 생리대 부문 1위를 찍고 한국으로 건너온 브랜드입니다. \
            100% 유기농 순면을 사용하고 있고 생리대, 탐폰, 생리컵, 면생리대 등 \
            다양한 타입의 생리용품 및 건강 식품도 함께 판매하고 있습니다.     ''', unsafe_allow_html=True)
        st.write('''< 라엘 생리대 키워드 >''', unsafe_allow_html=True)
        st.write('''라엘 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top5를 표로 뽑아봤어요. \
            사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        
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
            '편하다':[0.11],
            '재구매':[0.10],
            })
        st.dataframe(df_t)
        
        st.write('''< 라엘 생리컵 키워드 >''', unsafe_allow_html=True)
        df_c= pd.DataFrame({
            '좋다':[1.19],
            '편하다':[0.71],
            '추천':[0.48],
            '불편':[0.43],
            '쉽다':[0.19],
            })
        st.dataframe(df_c)
        
        
    with st.expander(label=f"**3. 좋은느낌**"):
        st.image('data/goodf.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 좋은느낌은 유한킴벌리의 국내에서 오랜 기간 함께해 온 생리용품 브랜드로 안정된 품질과 가성비 뿐만 아니라 \
            마트, 편의점 및 공중 화장실 자판기에도 판매하는 등 접근성이 가장 좋다는 것이 큰 장점입니다 ''', unsafe_allow_html=True)
        st.write('''< 좋은느낌 생리대 키워드 >''', unsafe_allow_html=True)
        st.write('''좋은느낌 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        
        df= pd.DataFrame({
            '좋다':[1.01],
            '편하다':[0.24],
            '유기농':[0.15],
            '순면':[0.14],
            '흡수':[0.10],
            })
        st.dataframe(df)
        
        st.write('''< 좋은느낌 탐폰 키워드 >''', unsafe_allow_html=True)
        df_t= pd.DataFrame({
            '좋다':[0.55],
            '편하다':[0.27],
            '추천':[0.08],
            '자극':[0.06],
            '흡수력':[0.06],
            })
        st.dataframe(df_t)
        
    with st.expander(label=f"**5. 해피문데이**"):
        st.image('data/happymoon.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 해피문데이는 여성의 입장에 서서 문제점과 니즈를 파악해 생리대, 탐폰(어플리케이터, 디지털), 생리컵 등 월경용품의 다채로운 선택지를 제공하고 있습니다.\
            순면 100%는 물론이고 종이 포장지와 사탕수수 어플리케이터를 사용해 친환경 및 지속 가능성을 위해 노력하고 있습니다.
            실제로 국내 최초로 라이트 사이즈 탐폰을 출시했고 월경 주기를 기록 및 관리해줘 \
            내 월경 주기에 맞게 월경용품을 정기 배송을 해주는 어플리케이션 서비스도 제공하고 있습니다.  \
              ''', unsafe_allow_html=True)
        st.write('''< 해피문데이 탐폰 키워드 >''', unsafe_allow_html=True)
        st.write('''해피문데이 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df_t= pd.DataFrame({
            '좋다':[0.77],
            '흡수+흡수력':[0.30],
            '편하다':[0.17],
            '추천':[0.11],
            '자극':[0.11],
            })
        st.dataframe(df_t)

    with st.expander(label=f"**7. 나트라케어**"):
        st.image('data/natra.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 나트라케어는 여성 건강과 환경이라는 철학 아래에 유기농 순면 100%, \
            생분해 소재, 자연 유래 펄프, 환경호르몬 걱정 없는 무연소표백 등 안심할 수 있는 생리용품을 향해 노력하고 있습니다.\
            특히, 몇 년 전까지만 해도 국내에 탐폰 제품의 형태 다양성과 사용감이 부족했을 때 한 줄기의 빛이 되었던 유럽 브랜드이다.''', unsafe_allow_html=True)
        st.write('''< 나트라케어 탐폰 키워드 >''', unsafe_allow_html=True)
        st.write('''나트라케어 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df_t= pd.DataFrame({
            '좋다':[0.80],
            '흡수력':[0.20],
            '편하다':[0.19],
            '자극':[0.13],
            '추천':[0.13],
            })
        st.dataframe(df_t)
        
    with st.expander(label=f"**9. 예지미인**"):
        st.image('data/yeji.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 예지미인은 유기농 순면 커버, 에어핏 커버, 더블파워 흡수케어로 보송하고 산뜻한 착용감과 함께 \
            안심하고 사용할 수 있는 브랜드입니다. 생리용품이지만 귀여운 캐릭터와 콜라보도 진행하면서 \
            MZ세대의 구매욕과 트렌디함을 사로잡기 위해 노력하는 브랜드입니다. ''', unsafe_allow_html=True)
        st.write('''< 예지미인 생리대 키워드 >''', unsafe_allow_html=True)
        st.write('''예지미인 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df= pd.DataFrame({
            '좋다':[0.77],
            '유기농':[0.15],
            '순면':[0.13],
            '흡수':[0.12],
            '편하다':[0.08],
            })
        st.dataframe(df)
        
    with st.expander(label=f"**11. 템포**"):
        st.image('data/tempo.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 템포는 동아제약에서 1977년부터 여성의 고민을 함께해 온 생리용품 브랜드입니다. \
            유기농 순면 100% 흡수체, 체내 맞춤형 슬림 어플리케이터 등 사용자 중심의 편의성을 중심으로 생각합니다. \
            무엇보다, 탐폰이 보편적이지 않던 시절부터 탐폰 제품을 연구 및 출시해온 국내 브랜드입니다.''', unsafe_allow_html=True)
        st.write('''< 템포 탐폰 키워드 >''', unsafe_allow_html=True)
        st.write('''템포 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df_t= pd.DataFrame({
            '좋다':[0.69],
            '편하다':[0.30],
            '흡수력':[0.15],
            '자극':[0.14],
            '추천':[0.12],
            })
        st.dataframe(df_t)

    with st.expander(label=f"**13. 라네이처**"):
        st.image('data/nature.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 라네이처는 유한킴벌리의 생리용품 브랜드 중 하나로 건강과 지구를 생각하는 에코라이프를 항상 생각하면서 \
            천연 원료, 친환경 섬유 인증, 플라스틱 대신 식물유래 바이오매스를 사용한 포장재 등 지속 가능한 미래를 위해 노력하고 있습니다..  ''', unsafe_allow_html=True)
        st.write('''< 라네이처 생리대 키워드 >''', unsafe_allow_html=True)
        st.write('''라네이처 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df= pd.DataFrame({
            '좋다':[0.69],
            '편하다':[0.07],
            '흡수':[0.06],
            '추천':[0.05],
            '재구매':[0.05],
            })
        st.dataframe(df)
        
    with st.expander(label=f"**15. 순수한면**"):
        st.image('data/sunsu.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 순수한면은 깨끗한 나라에서 만든 월경용품 브랜드이며 100% 유기농 순면 커버, 유연한 패드/어플리케이터, \
            이중 라인 및 시어버터 코팅 날개로 샘 없이 안심하고 사용할 수 있는 순면 생리대 브랜드입니다.
            ''', unsafe_allow_html=True)
        st.write('''< 순수한면 탐폰 키워드 >''', unsafe_allow_html=True)
        st.write('''순수한면 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df_t= pd.DataFrame({
            '좋다':[0.77],
            '흡수+흡수력':[0.45],
            '편하다':[0.22],
            '자극':[0.14],
            '재구매':[0.10],
            })
        st.dataframe(df_t)

    with st.expander(label=f"**17. 유기농본**"):
        st.image('data/bon.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 유기농본은 국내 최초 유기농 순면 커버 사업을 시작했고 미국 텍사스산 순면을 사용해 \
            피부에 자극이 적고 부드럽고 순한 생리대를 만드는 브랜드입니다.''', unsafe_allow_html=True)
        st.write('''< 유기농본 생리대 키워드 >''', unsafe_allow_html=True)
        st.write('''유기농본 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df= pd.DataFrame({
            '좋다':[0.99],
            '유기농':[0.31],
            '순면':[0.12],
            '흡수':[0.11],
            '편하다':[0.11],
            })
        st.dataframe(df)
        
with cols[1]:
    with st.expander(label=f"**2. 이너시아**"):
        st.image('data/inersia.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 이너시아는 2021년에 KAIST 여성 과학자들이 만든 브랜드로 \
            수술실 지혈 소재에서 착안한 흡수 소재 100% 소재, 유기농 순면 100%, 사탕수수 바이오 백시트 등을 사용해 \
            강력한 흡수력 + 예민한 사람들도 사용할 수 있는는 과학적인 생리용품을 만들기 위해 노력하는 브랜드입니다.''', unsafe_allow_html=True)
        st.write('''< 이너시아 생리대 키워드 >''', unsafe_allow_html=True)
        st.write('''이너시아 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df= pd.DataFrame({
            '좋다':[1.31],
            '흡수':[0.36],
            '유기농':[0.34],
            '순면':[0.15],
            '편하다':[0.12],
            })
        st.dataframe(df)
        
    with st.expander(label=f"**4. 티읕**"):
        st.image('data/tcup.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 티읕은 100% 의료용 실리콘을 주성분으로 사용한 인체에 유해한 화학성분이 없는 \
            안전하고 입증된 월경컵입니다. 한국 여성에 최적화된 디자인과 사이즈를 제공하고 있으며 \
            전자레인지로 소독할 수 있는 재사용 가능한 케이스를 함께 위생적이고 휴대하기 편한 월경컵을 출시하고 있습니다. ''', unsafe_allow_html=True)
        st.write('''< 티읕 생리컵 키워드 >''', unsafe_allow_html=True)
        st.write('''티읕 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df_c= pd.DataFrame({
            '좋다':[0.71],
            '편하다':[0.30],
            '어렵다':[0.18],
            '추천':[0.16],
            '불편':[0.15],
            })
        st.dataframe(df_c)

    with st.expander(label=f"**6. 마리솜**"):
        st.image('data/marisom.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 마리솜은 편안한 일상을 위한 오가닉 순면커버 생리대를 제공하고 있으며\
            빠른 흡수력과 부드럽고 피부 자극이 적은 사용감을 가지고 있습니다. \
            인기 있는 캐릭터와 콜라보를 통해 트렌디한 이미지를 위해 노력하고 있다''', unsafe_allow_html=True)
        st.write('''< 마리솜 생리대 키워드 top5 >''', unsafe_allow_html=True)
        st.write('''마리솜 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top5를 표로 만들고 전체 키워드 비율 바그래프 형태로 뽑아봤어요. \
            사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df= pd.DataFrame({
            '좋다':[0.63],
            '유기농':[0.08],
            '순면':[0.07],
            '추천':[0.03],
            '재구매':[0.03],
            })
        st.dataframe(df)
        st.write('''< 마리솜 생리대 전체 키워드 >''', unsafe_allow_html=True)
        st.image("./data/marisom-bar.png")
        
    with st.expander(label=f"**8. 아임오**"):
        st.image('data/imo.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 아임오는 국내 최초로 칠성무당벌레를 활용한 친환경농법으로 \
            유기농 커버 생리대를 만들어 편안함은 물론 안심할 수 있고 \
            종이 패키지와 콩기름 잉크로 자연까지 생각하는 생리용품 브랜드입니다.  ''', unsafe_allow_html=True)
        st.write('''< 아임오 생리대 키워드 >''', unsafe_allow_html=True)
        st.write('''아임오 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df= pd.DataFrame({
            '좋다':[0.71],
            '재구매':[0.15],
            '추천':[0.09],
            '편하다':[0.08],
            '유기농':[0.08],
            })
        st.dataframe(df)
        
    with st.expander(label=f"**10. 한나**"):
        st.image('data/hana.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 한나는 국내 제조, 의료용 실리콘 100%, 부드러우면서도 탄성 있는 중간 경도와 \
            다양한 사이즈를 제공해 생리컵 입문자도 쉽게 사용할 수 있는 ''', unsafe_allow_html=True)
        st.write('''< 한나 생리컵 키워드 >''', unsafe_allow_html=True)
        st.write('''한나 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df_c= pd.DataFrame({
            '좋다':[0.50],
            '불편':[0.25],
            '압박':[0.25],
            '재구매':[0.25],
            '편하다':[0.12],
            })
        st.dataframe(df_c)
        
    with st.expander(label=f"**12. 쏘피**"):
        st.image('data/sofy.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 쏘피는 화학공정을 거치지 않은 무표백속커버로 \
            유기농 100% 순면커버, 무표백, 식문 유래 성분 함유 방수층으로 \
            자연에 가깝게, 내 몸에 순하게를 실천하고 있습니다.''', unsafe_allow_html=True)
        st.write('''< 쏘피 생리대 키워드 >''', unsafe_allow_html=True)
        st.write('''쏘피 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df= pd.DataFrame({
            '좋다':[0.99],
            '유기농':[0.17],
            '흡수':[0.15],
            '편하다':[0.14],
            '재구매':[0.14],
            })
        st.dataframe(df)
        
    with st.expander(label=f"**14. 루나컵**"):
        st.image('data/luna.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 루나컵은 의료용 실리콘 100%는 물론이고 착용과 제거가 쉽고 \
            독보적인 링 손잡이 디자인으로 편안하고 이물감 없는 월경컵을 연구하고 만드는 월경컵 전문 브랜드입니다. ''', unsafe_allow_html=True)
        st.write('''< 루나컵 생리컵 키워드 >''', unsafe_allow_html=True)
        st.write('''루나컵 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df_c= pd.DataFrame({
            '좋다':[0.69],
            '편하다':[0.43],
            '추천':[0.26],
            '쉽다':[0.19],
            '어렵다':[0.15],
            })
        st.dataframe(df_c)
        
    with st.expander(label=f"**16. 화이트**"):
        st.image('data/white.png',  use_column_width=True)
        st.write('''< 브랜드 소개 >''', unsafe_allow_html=True)
        st.write(''' 화이트는 유한킴벌리의 국내에서 오랜 기간 함께해 온 생리용품 브랜드로 안정된 품질과 가성비 뿐만 아니라 \
            마트, 편의점 및 공중 화장실 자판기에도 판매하는 등 접근성이 가장 좋다는 것이 큰 장점입니다 ''', unsafe_allow_html=True)
        st.write('''< 화이트 탐폰 키워드 >''', unsafe_allow_html=True)
        st.write('''화이트 리뷰에서 생리용품와 연관이 있으며 가장 자주 등장한 \
            키워드 top 5를 뽑아봤어요. 사용자가 느끼는 해당 제품에 대한 이미지가 \
            궁금하다면 참고해보세요 (비율 기준)''', unsafe_allow_html=True)
        df_t= pd.DataFrame({
            '좋다':[0.61],
            '편하다':[0.28],
            '흡수력':[0.11],
            '자극':[0.10],
            '추천':[0.06],
            })
        st.dataframe(df_t)

st.write("")  


st.write("")  
