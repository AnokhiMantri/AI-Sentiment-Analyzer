# 🌍 AI-Based Multilingual Sentiment Analysis System  
### Minor Project – Computer Engineering

---

## 📌 Project Overview

The AI-Based Multilingual Sentiment Analysis System is a Machine Learning application that classifies textual data as **Positive** or **Negative** sentiment using Natural Language Processing (NLP) techniques.

The system is trained on the IMDB Movie Reviews dataset and deployed using Streamlit to provide real-time sentiment analysis through a web interface.

To improve accessibility and usability, the system supports **multilingual input** by automatically translating user text into English before performing sentiment prediction.

---

## 🎯 Objectives

- To implement sentiment classification using Machine Learning
- To apply NLP techniques for text preprocessing
- To use TF-IDF for feature extraction
- To train a Logistic Regression model for classification
- To build an interactive web application using Streamlit
- To support multilingual sentiment analysis through automatic translation

---

## 📊 Dataset Information

- Dataset Used: IMDB Movie Reviews Dataset
- Total Reviews: 50,000
- Classes: Positive and Negative
- Train-Test Split: 80% Training / 20% Testing

---

## ⚙️ Methodology

The project follows the below workflow:

### 1. Data Cleaning
- Lowercasing
- Removing special characters
- Removing unwanted symbols

### 2. Text Preprocessing
- Tokenization
- Stopword removal
- Basic normalization

### 3. Feature Extraction
- TF-IDF (Term Frequency – Inverse Document Frequency)

### 4. Model Training
- Logistic Regression classifier

### 5. Model Evaluation
- Accuracy score calculation
- Confidence score prediction using probability values

### 6. Multilingual Processing
- User input is translated to English using Google Translate
- Translated text is passed to the trained ML model

---

## 🌐 Multilingual Feature

The system allows users to enter text in any language such as:

- Hindi  
- Marathi  
- Spanish  
- French  
- etc.

### Example

Input:
Mujhe yeh film bilkul achi nhi lagi

Translated Text:
I did not like this movie at all

Prediction:
Negative Sentiment Detected

Confidence Score:
91%

---

## 📈 Model Performance

- Algorithm Used: Logistic Regression  
- Vectorization Technique: TF-IDF  
- Model Accuracy: 89%

---

## 🛠 Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- NLTK  
- Streamlit  
- Googletrans  

---

## 🏗 System Architecture

User Input  
↓  
Language Translation  
↓  
Text Preprocessing  
↓  
TF-IDF Vectorization  
↓  
Logistic Regression Model  
↓  
Sentiment Prediction  
↓  
Confidence Score Display  

---

## 📂 Project Structure
project-folder/
│
├── app.py
├── model_utils.py
├── train_model.py
├── styles.css
├── ui.py
├── requirements.txt
├── sentiment_model.pkl
└── tfidf_vectorizer.pkl


---

## 🚀 How to Run the Project

### Step 1: Install Dependencies

pip install -r requirements.txt

### Step 2: Train the Model

python train_model.py

### Step 3: Run the Application

streamlit run app.py

---

## 💡 Key Features

- Real-time sentiment prediction  
- Confidence score visualization  
- Progress bar indicator  
- Clean and interactive UI  
- Modular project structure  
- Multilingual text support  

---

## 🎓 Conclusion

The AI-Based Multilingual Sentiment Analysis System successfully demonstrates the application of Natural Language Processing and Machine Learning for real-time sentiment classification.

By integrating multilingual translation capabilities, the system improves accessibility and practical usability, making it adaptable for diverse users.

