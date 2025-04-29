import streamlit as st

st.title("🏡 House Sale and Purchase Calculator")

# User Inputs
sale_price = st.number_input("House Sale Price (£)", value=475000, step=1000)
mortgage_balance = st.number_input("Remaining Mortgage (£)", value=298000, step=1000)
debts_and_fees = st.number_input("Debts + Fees (£)", value=56000, step=1000)
deposit_amount = st.number_input("Deposit for New House (£)", value=80000, step=1000)

# Calculations
equity = sale_price - mortgage_balance
after_debts = equity - debts_and_fees
remaining_cash = after_debts - deposit_amount

# Results
st.subheader("Results 📊")
st.write(f"**Equity after Mortgage:** £{equity:,.0f}")
st.write(f"**Equity after Debts & Fees:** £{after_debts:,.0f}")
st.write(f"**Cash Remaining after Deposit:** £{remaining_cash:,.0f}")

# Warning if cash negative
if remaining_cash < 0:
    st.error("⚠️ Warning: You do not have enough funds after paying the deposit!")
