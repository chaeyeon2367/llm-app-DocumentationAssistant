# Langchain Documentation Chat Assistant 🤖

<br>

Welcome to the Langchain Documentation Chat Assistant project! This application aims to provide users with a convenient way to interact with Langchain documentation through a chat interface powered by advanced Generative AI technologies

<br>

![ScreenRecording2024-04-24at22 48 08-ezgif com-video-to-gif-converter](https://github.com/chaeyeon2367/llm-app-DocumentationAssistant/assets/63314860/8b9caed1-1212-41a5-a56d-4398ae5edbe4)


<br>

## Project Overview

The Langchain 🦜🔗 Documentation Chat Assistant allows users to ask questions about Langchain, a topic they are studying or curious about, and receive responses from a chatbot. The chatbot's responses are generated based on the information available in the Langchain documentation. To provide transparency and traceability, each response includes a source URL indicating the specific section of the Langchain documentation from which the information was derived.

<br>

### Key Features

- **GPT Model Turbo 3.5**: The chatbot is powered by the GPT model Turbo 3.5, allowing it to generate natural and contextually relevant responses to user queries.
- **Pinecone🌲 Vector Database**: Utilizes Pinecone for vector database management, enabling similarity search to extract relevant information from the vector space.
- **RetrievalQA Chain**: Implements a RetrievalQA chain for prompt augmentation, enhancing the chatbot's ability to provide accurate and informative responses.
- **Streamlit User Interface**: The frontend of the application is built using Streamlit, providing an intuitive and user-friendly interface for interacting with the chatbot.
- **LLM Memory**: Utilizes LLM memory to store chat history and maintain context, enabling the chatbot to provide coherent responses based on previous interactions. This enhances the conversational flow and improves the overall user experience.
- **Source URL Display:** The application displays the source URL of the information used to generate the answer, allowing users to verify and explore further if needed.

<br>

## Getting Started

To get started with the Langchain Documentation Chat Assistant, follow these steps:

1. Clone the repository to your local machine.
2. Install Pipenv virtual environment `pipenv install` and run Pipenv environment `pipenv shell`. You can check dependencies listed in the Pipfile
3. Run the following command to download html for a given website. Replace https://langchain.readthedocs.io/en/latest/ with a URL to your website.
   ```
   wget -r -A.html https://langchain.readthedocs.io/en/latest/
   ```

5. To run this project, you will need to add the following environment variables to your .env file
   `PINECONE_API_KEY`  `OPENAI_API_KEY`
6. Run the Streamlit application using `streamlit run main.py`.
7. Interact with the chatbot by typing your questions or queries into the chat interface.

<br>

## Contributing

Contributions to the Langchain Documentation Chat Assistant project are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue on GitHub or submit a pull request with your changes.

<br>

## Resources

https://github.com/hwchase17/chat-langchain-readthedocs

https://github.com/AI-Yash/st-chat

https://js.langchain.com/docs/get_started/introduction

https://github.com/emarco177/documentation-helper

<br>

## Links
<a href="https://www.linkedin.com/in/chaeyeonshim0930/" target="_blank"><img src="https://github.com/chaeyeon2367/llm-app-DocumentationAssistant/assets/63314860/1e8d7a85-e9da-4240-a318-143183d10fe8" width="40" height="40"></a>




