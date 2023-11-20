import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template, hide_st_style, footer
from langchain.llms import HuggingFaceHub
from matplotlib import style

# os.environ["OPENAI_API_KEY"] = "Your-key"

def extract_text_from_pdfs(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def split_text_into_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def create_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def create_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def process_user_input(user_question):
    if st.session_state.conversation is None:
        st.error("Please upload PDF data before starting the chat.")
        return

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="PDF Chatbot",
                    page_icon="icon.png")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Send in  your PDF file")
    user_question = st.text_input("Ask a question about your Data: Make sure you have an api key")

    with st.sidebar:
        st.subheader("PDF Files ")
        pdf_docs = st.file_uploader(
            "Upload your PDF file and then click 'Process'", accept_multiple_files=True, type=['pdf'])

        if st.button("Process"):
            if pdf_docs is None:
                st.error("You need to add at least one PDF file")
            else:
                with st.spinner("Processing"):
                    raw_text = extract_text_from_pdfs(pdf_docs)
                    text_chunks = split_text_into_chunks(raw_text)

                    # embeddings = OpenAIEmbeddings(openai_api_key="Your key")
                    vectorstore = create_vectorstore(text_chunks)
                    st.session_state.conversation = create_conversation_chain(vectorstore)
                    st.success("Your Data has been processed successfully")

    if user_question:
        process_user_input(user_question)

    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.markdown(footer, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
