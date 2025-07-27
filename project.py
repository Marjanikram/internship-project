# AI-Powered PDF Report Generator Using Python

# === STEP 1: Import required libraries ===
import pandas as pd
from fpdf import FPDF
from textblob import TextBlob
import matplotlib.pyplot as plt
import os

# === STEP 2: Load or collect data ===
data = pd.DataFrame({
    'Feedback': [
        "The product is excellent and delivery was fast.",
        "I had a terrible experience, support was unhelpful.",
        "Amazing quality and very reliable.",
        "Not satisfied, the product was broken.",
        "Pretty decent, could be better."
    ]
})

# === STEP 3: Analyze sentiment ===
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

data['Sentiment Score'] = data['Feedback'].apply(get_sentiment)
data['Sentiment Type'] = data['Sentiment Score'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')

# === STEP 4: Plot a sentiment chart ===
sentiment_counts = data['Sentiment Type'].value_counts()
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Number of Feedbacks')
plt.tight_layout()
plt.savefig("sentiment_chart.png")
plt.close()

# === STEP 5: Create PDF report ===
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="AI-Powered Feedback Report", ln=1, align='C')
pdf.ln(10)

# Summary
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Total Feedback: {len(data)}", ln=1)
pdf.cell(200, 10, txt=f"Positive: {sentiment_counts.get('Positive', 0)}", ln=1)
pdf.cell(200, 10, txt=f"Negative: {sentiment_counts.get('Negative', 0)}", ln=1)
pdf.cell(200, 10, txt=f"Neutral: {sentiment_counts.get('Neutral', 0)}", ln=1)
pdf.ln(10)

# Insert Chart
try:
    pdf.image("sentiment_chart.png", x=10, y=None, w=180)
except RuntimeError as e:
    print("⚠️ Error inserting image into PDF:", e)

# Detailed Feedback
pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, txt="Detailed Feedback", ln=1)
pdf.set_font("Arial", size=11)

for index, row in data.iterrows():
    pdf.multi_cell(0, 10, txt=f"{index+1}. {row['Feedback']} (Sentiment: {row['Sentiment Type']})")

# === STEP 6: Save PDF ===
pdf.output("AI_Feedback_Report.pdf")
print("Report generated.")
print("Saved at: D:\\semester 2\\internship project\\AI_Feedback_Report.pdf")



# Clean up
if os.path.exists("sentiment_chart.png"):
    os.remove("sentiment_chart.png")
