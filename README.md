
Blog Generation using LLM
This repository provides a simple Streamlit application for generating blogs using a Large Language Model (LLM). The application allows users to input a blog topic, specify the number of words, and choose the style of the blog, then generates the blog content accordingly.

How to Use
Prerequisites
Python 3.9
Streamlit
langchain
langchain_community
asyncio

Installation
Clone this repository:

git clone https://github.com/your-username/blog-generator-llm.git
cd blog-generator-llm

Install the required packages:

pip install streamlit langchain langchain_community asyncio
Make sure to have the Llama model (llama-2-7b-chat.ggmlv3.q8_0.bin) in the models directory.

Running the Application

Start the Streamlit application:

streamlit run app.py
Open the provided URL in your web browser.

Application Usage
Enter the Blog Topic: Provide the topic for which you want to generate a blog.

Specify Number of Words: Use the number input to specify the desired length of the blog.

Select Blog Style: Choose the style of the blog from the dropdown menu (e.g., Researchers, Data Scientist, Common People).

Generate Blog: Click the "Generate" button to create the blog.

Save Blog: After the blog is generated, click the "Save Blog" button to save the content to a .txt file.

Troubleshooting
Ensure the model file is correctly placed in the models directory.
Check for any errors in the Streamlit logs for troubleshooting.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributions
Feel free to open issues or pull requests for improvements or bug fixes.

Happy Blogging!
