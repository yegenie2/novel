import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.header('소설 봇', divider='rainbow')
st.title('	:heartpulse: :rainbow[AI 동화] :heartpulse:')

content = st.text_input('동화의 주제를 제시해주세요.')

if st.button('동화 작성 요청하기'):
    with st.spinner('동화 작성 중...'):
        result = chat_model.predict(content + "에 대한 동화 작성해줘 글자수는 1000자 미만으로 ")
        st.write(result)











