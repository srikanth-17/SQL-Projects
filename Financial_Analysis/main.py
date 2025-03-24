import mysql.connector
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mysql.connector import Error

# Database Connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="finance"
    )

# Fetch data from MySQL
def fetch_data(query):
    try:
        conn = get_connection()
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Error as e:
        st.error(f"Error: {e}")
        return pd.DataFrame()

# Streamlit App
st.set_page_config(page_title="Financial Transaction Analysis", layout="wide")

st.title("💰 Financial Transaction Analysis Dashboard")

# Sidebar Navigation
menu = st.sidebar.selectbox("Choose a Report", ["Top Customers", "Revenue vs. Expenses", 
                                                "High-Value Transactions", "Transaction Type Distribution","baloons"])

# Query for Top Customers by Transaction Volume
if menu == "Top Customers":
    st.header("🏅 Top Customers by Transaction Volume")
    
    query = """
    SELECT 
        c.customer_id, 
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        SUM(t.amount) AS total_transaction_volume
    FROM Customers c
    JOIN Accounts a ON c.customer_id = a.customer_id
    JOIN Transactions t ON a.account_id = t.account_id
    GROUP BY c.customer_id, customer_name
    ORDER BY total_transaction_volume DESC
    LIMIT 5;
    """
    
    df = fetch_data(query)

    if not df.empty:
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x='customer_name', y='total_transaction_volume', data=df, palette='viridis', ax=ax)
        plt.title("Top Customers by Transaction Volume")
        plt.xlabel("Customer")
        plt.ylabel("Transaction Volume (₹)")
        st.pyplot(fig)
    else:
        st.warning("No data available!")

# Query for Revenue vs. Expenses
elif menu == "Revenue vs. Expenses":
    st.header("📈 Monthly Revenue vs. Expenses")
    
    query = """
    SELECT 
        DATE_FORMAT(t.date, '%Y-%m') AS month,
        SUM(CASE WHEN t.transaction_type = 'Credit' THEN t.amount ELSE 0 END) AS revenue,
        SUM(CASE WHEN t.transaction_type = 'Debit' THEN t.amount ELSE 0 END) AS expenses
    FROM Transactions t
    GROUP BY month
    ORDER BY month DESC;
    """
    
    df = fetch_data(query)

    if not df.empty:
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df['month'], df['revenue'], label='Revenue', color='green', marker='o')
        ax.plot(df['month'], df['expenses'], label='Expenses', color='red', marker='x')
        plt.title("Revenue vs. Expenses")
        plt.xlabel("Month")
        plt.ylabel("Amount (₹)")
        plt.legend()
        st.pyplot(fig)
    else:
        st.warning("No data available!")

# Query for High-Value Transactions
elif menu == "High-Value Transactions":
    st.header("🚩 High-Value Transactions (₹10,000+)")

    query = """
    SELECT 
        t.transaction_id, 
        c.first_name, 
        c.last_name, 
        t.amount, 
        t.transaction_type, 
        t.date
    FROM Transactions t
    JOIN Accounts a ON t.account_id = a.account_id
    JOIN Customers c ON a.customer_id = c.customer_id
    WHERE t.amount > 10000
    ORDER BY t.amount DESC;
    """

    df = fetch_data(query)

    if not df.empty:
        st.dataframe(df)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x='first_name', y='amount', data=df, palette='magma', ax=ax)
        plt.title("High-Value Transactions")
        plt.xlabel("Customer")
        plt.ylabel("Transaction Amount (₹)")
        st.pyplot(fig)
    else:
        st.warning("No data available!")

# Query for Transaction Type Distribution
elif menu == "Transaction Type Distribution":
    st.header("🔍 Transaction Type Distribution")

    query = """
    SELECT 
        transaction_type, 
        COUNT(*) AS count 
    FROM Transactions
    GROUP BY transaction_type;
    """

    df = fetch_data(query)

    if not df.empty:
        fig, ax = plt.subplots(figsize=(8, 8))
        plt.pie(df['count'], labels=df['transaction_type'], autopct='%1.1f%%', startangle=140, colors=['#4CAF50', '#FF5733']) # type: ignore
        plt.title("Transaction Type Distribution")
        st.pyplot(fig)
    else:
        st.warning("No data available!")
elif menu=="baloons":
    st.header("Hii")
    st.balloons()
