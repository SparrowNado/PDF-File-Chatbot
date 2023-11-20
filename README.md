# PDF Chatbot with Custom Data 📄


An interactive AI chatbot for querying and discussing the contents of PDF documents using Streamlit and AI language models.



### Warning you need to have your OWN Open AI API KEY for this i cant provide mine because it will get cancelled

#
## About the Project 🌟

This project provides a user-friendly interface to interact with AI language models and extract information from PDF documents. It's particularly useful for researchers, students, and professionals who need to quickly access and query the content of PDF files without manually skimming through pages.

The chatbot integrates with OpenAI's language models, making it capable of answering a wide range of questions and engaging in natural language conversations about the content within the uploaded PDFs.

## Getting Started 🚀

To get started with this project, follow the steps below.

### Prerequisites 🛠️

Before using the chatbot, ensure you have the following installed:

- Python 3.x 🐍
- pip (Python package manager) 📦


### ADD the api key first 
edit this line with your key
```
os.environ["OPENAI_API_KEY"] = "Your-key"
```

then this
```
embeddings = OpenAIEmbeddings(openai_api_key="Your key")
```


### Note 

Make sure you use pycharm so that you can just install packages in one click

### Installation ⚙️
Through the terminal of pycharm 
1. Clone the repository:

   ```shell
   git clone https://github.com/SparrowNado/PDF-File-Chatbot.git
   ```

  
2. Install the required Python packages using pip:
    ```shell
    pip install -r requirements.txt
    ```

## How to Run (locally) 📋

 Execute the chatbot by entering the following command:

    ```shell
    streamlit run app.py
    ```
The chatbot interface will open in your default web browser 🌐

Upload one or more PDF files for processing 📂

Initiate a conversation by posing questions or seeking information about the PDF content 💬

The chatbot will furnish responses based on the content within the uploaded PDFs 🧠






##Features 🌈
Upload and process multiple PDF documents 📁
Interact with PDF content through natural language queries 💬
Harness the capabilities of robust language models for precise responses 💡
Enjoy a user-friendly web interface powered by Streamlit 🖥️





