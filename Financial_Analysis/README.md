# 💰 **Financial Transaction Analysis Dashboard**

📊 This project is a **Streamlit-based financial transaction analysis dashboard** that connects to a **MySQL database** and visualizes financial data with **interactive charts**. The system helps in analyzing revenue, expenses, customer transactions, and detecting suspicious activities using SQL queries and Python visualizations.

---

## 🚀 **Features**

✅ **1. Top Customers by Transaction Volume**

- Displays the top 5 customers with the highest transaction volume.
- Visualized using a **bar chart**.

✅ **2. Revenue vs. Expenses**

- Monthly revenue and expenses comparison.
- Visualized using a **line chart**.

✅ **3. High-Value Transactions**

- Lists transactions above ₹10,000.
- Displays both tabular data and a **bar chart** visualization.

✅ **4. Transaction Type Distribution**

- Displays the ratio of **credit and debit transactions**.
- Visualized using a **pie chart**.

---

## 🛠️ **Tech Stack**

- **Database:** MySQL
- **Backend:** Python with Streamlit
- **Visualization:** Matplotlib, Seaborn
- **Data Manipulation:** Pandas

---

## 📦 **Installation**

1. **Clone the Repository**

```bash
git clone <repository_url>
cd financial-transaction-analysis
```

2. **Install Dependencies**

```bash
pip install streamlit mysql-connector-python pandas matplotlib seaborn
```

3. **Run the Streamlit App**

```bash
streamlit run main.py
```
