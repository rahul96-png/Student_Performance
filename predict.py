import pickle
import pandas as pd

# -----------------------------
# Load Trained Model
# -----------------------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Sample Student Data
# -----------------------------
student_data = pd.DataFrame([{
    "studytime": 3,
    "failures": 0,
    "absences": 5,
    "G1": 15,
    "G2": 16
}])

# -----------------------------
# Predict Final Grade (G3)
# -----------------------------
prediction = model.predict(student_data)

print("=" * 50)
print("Student Performance Prediction")
print("=" * 50)
print(f"Predicted Final Grade (G3): {prediction[0]:.2f}")

# -----------------------------
# Performance Level
# -----------------------------
if prediction[0] >= 16:
    print("🌟 Excellent Performance")
elif prediction[0] >= 10:
    print("👍 Average Performance")
else:
    print("📚 Needs Improvement")