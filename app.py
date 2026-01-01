import streamlit as st
from sklearn.tree import DecisionTreeClassifier

st.title("AI Exam Predictor")

# Training data
X = [[1], [2], [3], [4], [5], [6], [7]]
y = [0, 0, 0, 1, 1, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

hours = st.number_input("Enter hours studied:", min_value=0, max_value=24)

if st.button("Predict"):
    result = model.predict([[hours]])
    if result[0] == 1:
        st.success("Prediction: PASS ")
    else:
        st.error("Prediction: FAIL ")
