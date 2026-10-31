# ✍️ LinkedIn Post Generator

An AI-powered LinkedIn content generation tool that helps users create engaging, topic-specific LinkedIn posts using Large Language Models (LLMs) and Few-Shot Prompting.

Built using **Python, Streamlit, LangChain, and Groq API**, the application generates posts based on user-selected topics and length preferences. It uses a curated dataset of sample LinkedIn posts to guide the LLM's writing style and produce more relevant, structured content.

The project also implements an LLM-powered data preprocessing pipeline that extracts metadata, identifies relevant tags, and normalizes similar categories to improve example selection during generation.

---

## 🚀 Key Features

- **AI-Powered Post Generation:** Generate LinkedIn posts using Groq-hosted LLMs.
- **Topic-Based Generation:** Select a topic from available categories such as Job Search, Motivation, Mental Health, and more.
- **Customizable Post Length:** Choose between Short, Medium, and Long posts.
- **Few-Shot Prompting:** Use relevant sample LinkedIn posts to guide the LLM's writing style and output.
- **Intelligent Example Selection:** Filter sample posts based on topic, language, and length before passing them to the LLM.
- **Automated Metadata Extraction:** Extract word count, language, and relevant tags from existing LinkedIn posts.
- **Tag Normalization:** Merge similar tags into unified categories using LLM-based processing.
- **Interactive Interface:** Generate posts through a simple Streamlit application.

---

## 🎯 Problem Statement

Creating consistent and engaging LinkedIn content can be challenging.

Users often struggle with:
- Finding the right way to communicate their ideas.
- Maintaining a professional yet engaging writing style.
- Structuring posts according to their intended length.
- Finding relevant hashtags and content categories.
- Generating fresh content without sounding repetitive.

General-purpose AI text generation can produce generic content that does not always match the desired writing style.

**LinkedIn Post Generator addresses this problem through example-driven content generation.**

Instead of relying only on a generic prompt, the system retrieves relevant sample posts and uses them as few-shot examples to guide the LLM's response.

---

## 🧠 How It Works

The application follows a two-stage architecture:

### Stage 1: Data Preprocessing & Enrichment

The objective is to prepare a structured dataset of LinkedIn posts that can be used for few-shot prompting.

**Workflow:**

Raw LinkedIn Posts (JSON)  
↓  
Text Extraction  
↓  
LLM-Based Metadata Extraction  
↓  
Word Count + Language + Tags  
↓  
Tag Normalization & Unification  
↓  
Processed JSON Dataset

**Key operations:**

1. **Metadata Extraction:** Use an LLM to extract word count, language, and up to two relevant tags from each post.
2. **Tag Unification:** Identify similar tags and merge them into standardized categories.

   Example:

   | Original Tags | Unified Tag |
   |---|---|
   | Jobseekers | Job Search |
   | Job Hunting | Job Search |
   | Motivation | Motivation |
   | Inspiration | Motivation |
   | Personal Development | Personal Growth |

3. **Structured Storage:** Save the enriched posts in JSON format for efficient filtering and retrieval.

### Stage 2: Post Generation

The processed dataset is used to retrieve relevant examples and generate new LinkedIn content.

**Workflow:**

User Input  
↓  
Topic + Length + Language  
↓  
Filter Relevant Sample Posts  
↓  
Few-Shot Prompt Construction  
↓  
Groq LLM  
↓  
Generated LinkedIn Post

**Generation process:**

1. The user selects a topic, post length, and language.
2. The system filters existing posts based on the selected parameters.
3. Relevant examples are added to the prompt using few-shot prompting.
4. The prompt is passed to the configured Groq LLM.
5. The LLM generates a new LinkedIn post.

---

## 🎯 Few-Shot Prompting

A key concept implemented in this project is **Few-Shot Prompting**.

Few-shot prompting is a prompt engineering technique where an LLM is provided with a few examples of the expected output before generating a response.

Instead of simply asking:

> Generate a LinkedIn post about Job Search.

The application provides relevant sample posts so the LLM can understand the desired writing style and structure.

### How the implementation works

- Load previously processed LinkedIn posts.
- Categorize posts into Short, Medium, and Long based on word count.
- Filter posts by topic, language, and length.
- Select up to two relevant examples.
- Include the examples in the generation prompt.

This helps guide the LLM toward outputs that are more consistent with the selected examples.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive application interface |
| Groq API | LLM inference |
| GPT-OSS-20B | Configured language model |
| LangChain | Prompt templates and LLM integration |
| Pandas | Data manipulation and filtering |
| JSON | Dataset storage and processing |
| Python-dotenv | Environment variable management |

---

## 📂 Project Structure

```text
LinkedinPostGenerator/
│
├── data/
│   ├── raw_posts.json
│   └── processed_posts.json
│
├── main.py                 # Streamlit application
├── postGenerator.py        # LinkedIn post generation
├── few_shots.py            # Example filtering and selection
├── preprocess.py           # Metadata extraction and tag unification
├── llm_helper.py           # Groq LLM configuration
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10 or later
- pip
- Groq API key

### 1. Clone the Repository

```bash
git clone https://github.com/Pranjalshivhare06/LinkedinPostGenerator.git

cd LinkedinPostGenerator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).

Never commit your `.env` file or expose your API credentials.

### 5. Prepare the Dataset

Place your raw LinkedIn post dataset in:

```text
data/raw_posts.json
```

Run the preprocessing pipeline:

```bash
python preprocess.py
```

This generates the enriched dataset:

```text
data/processed_posts.json
```

The processed dataset is used by the application for example selection.

### 6. Run the Application

```bash
streamlit run main.py
```

Open the local URL displayed in your terminal to access the application.



