# 😊 EmotionSense-AI  
### Human Emotion Detection from Text using Deep Learning & LSTM

<p align="center">
  <img src="https://img.shields.io/badge/DeepLearning-LSTM-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/NLP-EmotionDetection-green?style=for-the-badge">
</p>

---

## 🚀 Project Overview

EmotionSense-AI is a Deep Learning based NLP project that detects human emotions from text using **LSTM (Long Short-Term Memory)** networks.

The application analyzes user input sentences and predicts emotions such as:

- 😊 Joy
- 😢 Sadness
- 😡 Anger
- 😨 Fear
- ❤️ Love
- 😲 Surprise

This project demonstrates:
- Natural Language Processing (NLP)
- Tokenization & Padding
- Deep Learning with LSTM
- Emotion Classification
- Streamlit Web App Deployment

---

# 🖥️ Application UI

## 🎯 Home Interface

<p align="center">
  ![alt text](image.png)
</p>

<p align="center">
  ![alt text](image-1.png)
</p>

---

## 📊 Emotion Prediction Output

<p align="center">
  <img width="900" src="https://miro.medium.com/v2/resize:fit:1400/1*J8kh2x2oG89eN5GdS4z0lw.png">
</p>

---

# 🧠 Deep Learning Architecture

```text
Input Text
     ↓
Tokenizer
     ↓
Padding Sequences
     ↓
Embedding Layer
     ↓
LSTM Layer
     ↓
Dropout Layer
     ↓
Dense Layer
     ↓
Softmax Output
     ↓
Predicted Emotion
```

---

# 🛠️ Tech Stack

| Technology | Usage |
|------------|------|
| Python | Programming Language |
| TensorFlow / Keras | Deep Learning |
| LSTM | Sequence Learning |
| NLTK | Text Preprocessing |
| Streamlit | Web Application |
| Scikit-learn | Label Encoding |
| Pandas & NumPy | Data Handling |

---

# 📂 Project Structure

```bash
EmotionSense-AI/
│
├── app.py
├── emotion_model.h5
├── tokenizer.pkl
├── label_encoder.pkl
├── requirements.txt
├── README.md
│
├── data/
│   ├── train.txt
│   ├── test.txt
│   └── val.txt
│
├── notebooks/
│   └── training.ipynb
│
└── screenshots/
```

---

# 📦 Dataset

Dataset used:

🔗 https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp

Dataset contains labeled emotional text samples for training and testing NLP models.

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/EmotionSense-AI.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd EmotionSense-AI
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Streamlit App

```bash
streamlit run app.py
```

---

# 🧪 Example Predictions

| Input Text | Predicted Emotion |
|------------|------------------|
| I feel amazing today | 😊 Joy |
| I am very nervous | 😨 Fear |
| I miss my old memories | 😢 Sadness |
| I am furious right now | 😡 Anger |

---

# 📈 Model Performance

| Metric | Score |
|--------|------|
| Training Accuracy | 92% |
| Validation Accuracy | 90% |
| Test Accuracy | 89% |

---

# 🔥 Features

✅ Real-Time Emotion Detection  
✅ LSTM Deep Learning Model  
✅ Streamlit Interactive UI  
✅ Text Preprocessing Pipeline  
✅ Tokenization & Padding  
✅ Softmax Probability Prediction  
✅ Clean & Responsive Interface  

---

# 🧠 Concepts Used

- Natural Language Processing (NLP)
- Tokenization
- Padding Sequences
- Embedding Layer
- LSTM Networks
- Dropout Regularization
- Dense Neural Networks
- Backpropagation
- Adam Optimizer
- Softmax Activation

---

# 📸 Future Improvements

- 🔊 Voice Emotion Detection
- 🤖 Transformer/BERT Fine-Tuning
- 📊 Emotion Probability Graphs
- 🌐 Deploy on Streamlit Cloud
- 📱 Mobile Responsive UI

---

# 💻 Sample Code

```python
prediction = model.predict(padded_sequence)

predicted_class = prediction.argmax(axis=1)[0]

emotion = encoder.inverse_transform([predicted_class])[0]
```

---

# 🌟 Streamlit Interface

```python
st.title("😊 EmotionSense-AI")
st.text_area("Enter Your Text")
```

---

# 📚 Learning Outcomes

Through this project, I learned:

- Deep Learning fundamentals
- NLP preprocessing techniques
- Sequence modeling using LSTM
- TensorFlow model training
- Streamlit deployment
- Real-world AI application development

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:
- Fork the repository
- Create a new branch
- Submit a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Akash Patel

Passionate about:
- Deep Learning
- NLP
- Generative AI
- AI Engineering

---

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?lines=Deep+Learning+Project;Emotion+Detection+Using+LSTM;Built+With+TensorFlow+%26+Streamlit;NLP+%7C+AI+%7C+Deep+Learning&center=true&width=900&height=45">
</p>

---

<p align="center">
⭐ If you liked this project, don't forget to star the repository!
</p>