# flatmate_bill

📌 Project Description
Flatmates Bill is a Python-based application that calculates how much each flatmate needs to pay for a shared bill based on the number of days they stayed in the house. The program also generates a PDF report summarizing the bill details.

🚀 Features
✅ User Input: Users enter the bill amount, flatmates' names, and their stay duration.
✅ Fair Cost Distribution: The bill is split proportionally based on the days stayed.
✅ PDF Report Generation: Generates a formatted PDF with names, amounts, and billing period.
✅ Automatic PDF Opening: Opens the generated PDF file automatically.

📂 Project Structure

Flatmates_Bill/
│── main.py         # Main script to run the program
│── Flat.py         # Contains Bill & Flatmate classes
│── Reports.py      # Generates the PDF report
│── Files/          # Stores generated PDFs & assets (e.g., house.png)
│── README.md       # Project documentation
│── requirements.txt # Dependencies

🛠️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/harshithanbhat77/Flatmates-Bill.git
cd Flatmates-Bill

2️⃣ Create a Virtual Environment
python -m venv .venv
source .venv/bin/activate  # On Mac/Linux
.\.venv\Scripts\activate   # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run the Program
python main.py
🔹 Enter the total bill amount and each flatmate’s stay duration when prompted.
🔹 The program calculates the amount each flatmate has to pay.
🔹 A PDF report is generated and opened automatically.

📌 Technologies Used
Python 🐍
FPDF (for PDF generation) 📝
OS & Webbrowser Modules 🌐
