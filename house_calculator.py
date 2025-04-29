import streamlit as st

# Page Config
st.set_page_config(page_title="House Sale Calculator", page_icon="🏡", layout="centered")

# Main Title
st.title("🏡 House Sale and Purchase Calculator")
st.write("Easily calculate your equity, debts, and remaining cash after buying your new home!")

# Inputs - nicely spaced
st.header("Enter Your Details:")

sale_price = st.number_input("🏷️ House Sale Price (£)", value=475000, step=1000)
mortgage_balance = st.number_input("🏦 Remaining Mortgage (£)", value=298000, step=1000)
debts_and_fees = st.number_input("💳 Debts + Fees (£)", value=56000, step=1000)
deposit_amount = st.number_input("💰 Deposit for New House (£)", value=80000, step=1000)

# Calculations
equity = sale_price - mortgage_balance
after_debts = equity - debts_and_fees
remaining_cash = after_debts - deposit_amount

# Results
st.header("Results 📊")
st.success(f"**Equity after Mortgage:** £{equity:,.0f}")
st.success(f"**Equity after Debts & Fees:** £{after_debts:,.0f}")
st.success(f"**Cash Remaining after Deposit:** £{remaining_cash:,.0f}")

# Warning if cash
