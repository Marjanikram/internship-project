  #  AI-Powered PDF Report Generator using Python

This internship project uses Python to analyze feedback using sentiment analysis and generate a professional PDF report automatically. It helps demonstrate how AI and automation can work together.


# Tools & Libraries Used

- Python 3.13
- `pandas`
- `textblob`
- `matplotlib`
- `fpdf`
- `os`


# Project Files

- `project.py` → Main Python file to generate the PDF report
- `AI_Feedback_Report.pdf` → The output PDF
- `sentiment_chart.png` → The chart used in the PDF (auto-deleted)
- `screenshots/` → Folder with output images
- `Report.pdf` → Final report with explanation
- `README.md` → This file



# How to Set It Up and Run

# Step 1: Install Libraries

Open terminal (PowerShell) and run:

python -m pip install pandas fpdf textblob matplotlib --user
# internship-project


# Step 2: Run the Python File

Navigate to the project folder in terminal:
```powershell
cd "D:\semester 2\internship project"
python project.py
After successful execution, a file named AI_Feedback_Report.pdf will be created in the same folder.

You will also briefly see a chart image (sentiment_chart.png) — this is used in the PDF and then automatically deleted.

#  Explanation of Commands
# Command	*  What it Does
cd "D:\..."	Goes to your project folder
python project.py	Runs the Python script
AI_Feedback_Report.pdf	Final report file generated
sentiment_chart.png	Chart added to the PDF and auto-deleted

# What the Script Does
Collects predefined feedback

Analyzes sentiment using TextBlob

Generates a bar chart of sentiment types

Creates a PDF report with summary, chart, and detailed feedback

# Challenges Faced
Faced module import errors (like fpdf, pandas)

Solved by using --user flag in pip install

Some path issues were fixed by giving full folder path with quotes

# Internship Info
This project was completed as part of my internship tasks to demonstrate Python automation using AI and reporting tools.

# Author
Name: Marjan Ikram
Project: Internship Task – AI-Powered Report Generator
Date:  27 July 2025

# Step 3: Output Location

After running the code:

- A file named **`AI_Feedback_Report.pdf`** is created automatically.
- It is saved in the **same folder** where your `project.py` file is located.
- You may also see a temporary image file `sentiment_chart.png`, which is deleted after being added to the PDF.


# Example Output Location

If your script is in:

Then the report will be saved at:
D:\semester 2\internship project\AI_Feedback_Report.pdf

## Step 4: Explanation of What the Project Does

This project performs sentiment analysis on feedback data and creates a PDF report with the results.

---

###  How It Works (in simple terms):

1. **Takes sample feedback** from users.
2. Uses **TextBlob** to analyze if feedback is positive, negative, or neutral.
3. Plots a **sentiment chart** using `matplotlib`.
4. Adds feedback and chart into a **PDF report** using `fpdf`.
5. Deletes the chart image after inserting it into the PDF.
6. Saves the final PDF in the same folder as the code.

---

## Example Output in Report

- Positive Feedback: “The product is excellent...”
- Negative Feedback:  “Not satisfied, the product was broken.”
- Final Report Name: `AI_Feedback_Report.pdf`

### Step 5: Challenges Faced

  **Python version issues**  
I was using Python 3.13, and some modules like `pip` were missing at first. I fixed it by using `python -m pip install` instead of just `pip`.

  **Module not found error**  
At the start, modules like `pandas`, `textblob`, and `fpdf` were not found. I solved this by installing them using:


python -m pip install pandas fpdf textblob matplotlib --user

File not saving in the right folder
The PDF was saving in the wrong place. I fixed this by giving the full path:

pdf.output(r"D:\semester 2\internship project\AI_Feedback_Report.pdf")
 Temporary image not deleting
I added this line at the end to delete the chart image after the PDF is made:

os.remove("sentiment_chart.png")

### ✅ Step 6: Final Notes

- This project was created as part of an internship task to demonstrate basic **AI + Python automation**.
- The PDF generation shows how we can combine **sentiment analysis**, **data visualization**, and **reporting**.
- All the outputs are auto-generated — no manual editing is needed.
- The temporary chart is removed after use to keep the folder clean.

---

### 📎 Files in This Project

| File | Description |
|------|-------------|
| `project.py` | Main code for report generation |
| `AI_Feedback_Report.pdf` | Final PDF output |
| `README.md` | Instructions and explanation |
| `Report.pdf` | Separate project explanation (if submitted) |



