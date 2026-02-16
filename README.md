# 🎭 AI-Based Sentiment Analysis System  
### Minor Project – Computer Engineering  

---

## 📌 Project Overview

The **AI-Based Sentiment Analysis System** is a Machine Learning application that classifies textual data as **Positive** or **Negative** using Natural Language Processing (NLP) techniques.

The system is trained on the IMDB Movie Reviews dataset and deployed using Streamlit to provide real-time sentiment analysis through a user-friendly web interface.

This project demonstrates the practical implementation of NLP, feature extraction, and supervised machine learning in a real-world application.

---

## 🎯 Objectives

- Implement sentiment classification using Machine Learning  
- Apply NLP techniques for text preprocessing  
- Use TF-IDF for feature extraction  
- Train a Logistic Regression model  
- Build an interactive web application using Streamlit  
- Display prediction confidence using probability scores  

---

## 📊 Dataset Information

- Dataset: IMDB Movie Reviews Dataset  
- Total Reviews: 50,000  
- Classes: Positive and Negative  
- Train-Test Split: 80% Training / 20% Testing  

---

## ⚙️ Methodology

### 1️⃣ Data Cleaning
- Lowercasing  
- Removing special characters  
- Removing unwanted symbols  

### 2️⃣ Text Preprocessing
- Tokenization  
- Stopword removal  
- Basic normalization  

### 3️⃣ Feature Extraction
- TF-IDF (Term Frequency – Inverse Document Frequency)

### 4️⃣ Model Training
- Logistic Regression classifier

### 5️⃣ Model Evaluation
- Accuracy score calculation  
- Probability-based confidence scoring  

---

## 📈 Model Performance

- Algorithm: Logistic Regression  
- Vectorization: TF-IDF  
- Model Accuracy: ~89%  

---

## 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- NLTK  
- Streamlit  

---

## 🏗 System Architecture

User Input  
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


---

## 🚀 Live Application

The project is deployed using **Streamlit Community Cloud** for real-time sentiment analysis.

---

## ▶️ How to Run the Project Locally

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt

### Step 2: (Optional) Train the Model
```bash
python train_model.py

### Step 3: Run the Application
```bash
streamlit run app.py



## 💡 Key Features

- Real-time sentiment prediction  
- Displays Positive or Negative classification  
- Confidence score calculation using probability values  
- Progress bar visualization for prediction confidence  
- Clean and user-friendly Streamlit interface  
- Modular code structure (separate UI and model logic)  
- TF-IDF based feature extraction  
- Logistic Regression based classification model  
- Deployment-ready on Streamlit Community Cloud  

---

## 🎓 Conclusion

The AI-Based Sentiment Analysis System successfully demonstrates the practical implementation of Natural Language Processing (NLP) and Machine Learning for real-time sentiment classification.

By integrating text preprocessing, TF-IDF vectorization, and a Logistic Regression classifier, the system efficiently predicts whether a given review expresses positive or negative sentiment.

The deployment using Streamlit enhances accessibility and usability, making the application interactive and user-friendly.  

Overall, this project showcases a complete end-to-end machine learning workflow — from data preprocessing and model training to web deployment — making it a suitable and well-structured minor project in Computer Engineering.
