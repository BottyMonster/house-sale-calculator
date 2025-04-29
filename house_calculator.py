import streamlit as st
import pandas as pd
from io import BytesIO

# Page settings
st.set_page_config(page_title="Ross & Marta Wales Move", page_icon="🏡", layout="centered")

# Title
st.title("🏡 Ross & Marta Wales Move")
st.markdown("Easily work out your equity and cash remaining when buying your new home.")

# Input section
st.header("🔢 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    sale_price = st.number_input("🏷️ Sale Price (£)", value=475000, step=1000, help="Expected sale price of your current house")
    mortgage_balance = st.number_input("🏦 Mortgage Left (£)", value=298000, step=1000, help="Outstanding mortgage on your current house")

with col2:
    debts_and_fees = st.number_input("💳 Debts & Legal Fees (£)", value=56000, step=1000, help="Total of debts, conveyancing fees, stamp duty etc.")
    deposit_amount = st.number_input("💰 Deposit for New House (£)", value=80000, step=1000, help="Deposit you're putting down on the next house")

# Calculations
equity = sale_price - mortgage_balance
after_debts = equity - debts_and_fees
remaining_cash = after_debts - deposit_amount

# Summary block
st.markdown("### 🧾 Summary")

summary_color = "green" if remaining_cash >= 0 else "red"
st.markdown(
    f"""
    <div style='padding: 1em; border: 2px solid #ddd; border-radius: 10px; background-color: #f9f9f9'>
        <h3 style='color: {summary_color}'>💷 Remaining Cash After Everything: <strong>£{remaining_cash:,.0f}</strong></h3>
