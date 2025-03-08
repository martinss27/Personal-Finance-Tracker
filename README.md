
# 📌 Personal Finance Tracker  

A **simple CLI-based expense and income tracker** that allows users to log transactions, view them **sorted by date (using Merge Sort)**, search by category, and save data persistently using **CSV file handling**.  

---

## 🚀 Features  
✅ **Add Transactions** – Log expenses or income with date, amount, and category.  
✅ **View Transactions (Sorted by Date)** – Uses **Merge Sort** to display transactions chronologically.  
✅ **Search Transactions by Category** – Quickly filter transactions using **list comprehension**.  
✅ **Persistent Data Storage** – Saves transactions in a **CSV file** to retain data across sessions.  
✅ **User-Friendly CLI Menu** – Simple and intuitive interface for managing finances.  

---

### 📌 **File Explanations**  

- **`finance_tracker.py`** → The main script that runs the Personal Finance Tracker. It contains all the logic for sorting transactions, searching, and managing the menu.  
- **`transactions.csv`** → Stores user-entered transactions (date, amount, category) so data persists between sessions.  
- **`README.md`** → Provides an overview of the project, including features, setup instructions, and future improvements.  
- **`requirements.txt`** *(Optional)* → If you use any external libraries (like `pandas` or `matplotlib` in the future), this file helps install them using `pip install -r requirements.txt`.  


---

## 🛠️ Technologies Used  
- **Python** (Core language)  
- **Merge Sort** (For sorting transactions by date)  
- **CSV File Handling** (For saving/loading data)  
- **Lists & Dictionaries** (For transaction storage)  

---

## 💻 Installation & Usage  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/Personal-Finance-Tracker.git
cd Personal-Finance-Tracker

#Make sure you have Python installed, then run:
python finance_tracker.py

##Follow the CLI Menu  
1. Add Transaction
2. View Transactions (Sorted by Date)
3. Search by Category
4. Exit

