# LangChain Streamlit App

This application is a Streamlit-based interface that allows users to input a query and find similar items from a database using semantic search powered by OpenAI's embeddings and FAISS (Facebook AI Similarity Search).

## Features

- **Semantic Search**: Leverages OpenAI's language models for generating embeddings and FAISS for efficient similarity search.
- **User-Friendly Interface**: Built with Streamlit, offering a simple and interactive UI.
- **CSV Data Loading**: Loads data from a CSV file for search indexing.

## Installation

Before running the app, ensure you have Python installed on your system. Then, follow these steps:

1. **Clone the Repository**:

```
git clone [Your Repository URL]
cd [Your Repository Directory]
```

2. **Set Up a Python Virtual Environment** (Optional):

```
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```


3. **Install Dependencies**:
```
pip install streamlit openai langchain python-dotenv
```


4. **Environment Variables**:
- Create a `.env` file in the root directory.
- Add your OpenAI API key:
  ```
  OPENAI_API_KEY=your_api_key_here
  ```

## Usage

1. **Start the Streamlit App**:

`streamlit run app.py`


2. **Using the App**:
- Open your web browser and go to `http://localhost:8501`.
- Enter your query in the text input box.
- Click on "Find similar things in my DB" to see the results.

## Data Format

- The application expects a CSV file named `mydata.csv` in the root directory.
- Ensure the CSV is formatted correctly for the app to process the data.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](your_issues_link) if you want to contribute.

## License

[MIT](LICENSE)


