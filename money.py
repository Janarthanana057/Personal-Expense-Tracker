import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

st.set_page_config(page_title="Expense Tracker", layout="centered")

st.title("💰 Personal Expense Tracker")
st.write("Track your daily expenses and view summary by category.")

# Initialize session state for storing expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Input form
with st.form("expense_form"):
    amount = st.number_input("Amount Spent (₹)", min_value=1)
    category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Utilities", "Entertainment","friends", "Other"])
    date = st.date_input("Date", value=datetime.date.today())
    submit = st.form_submit_button("Add Expense")

# Add to list
if submit:
    st.session_state.expenses.append({"Amount": amount, "Category": category, "Date": date})
    st.success(f"Added ₹{amount} to {category} on {date}")

# Convert to DataFrame
if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.subheader("📋 Expense Table")
    st.dataframe(df)

    # Show total
    total = df["Amount"].sum()
    st.metric(label="💸 Total Spending", value=f"₹{total}")

    # Show category summary
    category_summary = df.groupby("Category")["Amount"].sum().reset_index()
    fig = px.pie(category_summary, names="Category", values="Amount", title="Spending by Category")
    st.plotly_chart(fig)
else:
    st.info("No expenses yet. Add some to see the summary.")

