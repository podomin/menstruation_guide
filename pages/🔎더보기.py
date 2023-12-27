import streamlit as st
import pandas as pd
import os
st.set_page_config(layout="centered")

st.title("More Information")

tab_message, tab_archive = st.tabs(["메시지", "아카이브"])  
        

with tab_message:
    
        
    if 'past' not in st.session_state:
        st.session_state['past'] = []
    
  
    st.markdown("#### 🙃 가이드북이 유용했나요? 🥺 당신의 의견을 남겨주세요 ")
    with st.form('form', clear_on_submit=True):
        radio = st.radio(label = '가이드북이 얼마나 도움이 됐다고 생각하시나요?', options = ['매우', '보통', '별루'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        msg_input = st.text_input('메시지 입력 : ', '')
        submitted = st.form_submit_button('전송')
        if submitted and msg_input and radio:
            st.session_state.past.append([radio, msg_input])
            # with open("./data/oliveyoung_opinion.csv", "a", encoding="utf-8") as fa:
            #     writer = csv.writer(fa)
            #     writer.writerow(st.session_state['past'])


with tab_archive:
    st.markdown("#### < 프로젝트 발표자료 >")
    st.write('''저희 프로젝트 자료를 더 자세히 살펴보고 싶다면 링크 Click! ''')
    st.write('''[발표자료](https://github.com/podomin/menstruation_guide/blob/main/3%EC%A1%B0_%EC%98%AC%EB%A6%AC%EB%B8%8C%EC%98%81-%EB%A6%AC%EB%B7%B0-%EA%B0%90%EC%84%B1%EB%B6%84%EC%84%9D%20(3).pdf) ''', unsafe_allow_html=True)

    st.markdown("#### < 가이드북 소스코드 >")
    st.write('''가이드북 스트림릿 소스코드가 궁금하다면 링크 Click! ''')
    st.write('''[깃허브](https://github.com/podomin/menstruation_guide.git) ''', unsafe_allow_html=True)

