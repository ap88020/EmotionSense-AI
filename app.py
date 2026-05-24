import streamlit as st
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model
model = tf.keras.models.load_model("emotion_model.h5")

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Load label encoder
with open("label_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# Max length used during training
max_len = 100

# UI
st.title("😊 Human Emotion Detection")

st.write("Enter a sentence and detect emotion.")

user_input = st.text_area("Enter Text")

if st.button("Predict Emotion"):

    # Convert text to sequence
    sequence = tokenizer.texts_to_sequences([user_input])

    # Padding
    padded = pad_sequences(sequence, maxlen=max_len)

    # Prediction
    prediction = model.predict(padded)

    # Get highest probability
    predicted_class = prediction.argmax(axis=1)[0]

    # Convert label back to emotion
    emotion = encoder.inverse_transform([predicted_class])[0]

    # Confidence
    confidence = prediction.max() * 100

    st.success(f"Predicted Emotion: {emotion}")
    st.info(f"Confidence: {confidence:.2f}%")