import streamlit as st

# Page Config
st.set_page_config(page_title="House Sale Calculator", page_icon="🏡", layout="centered")

# Main Title
st.title("🏡 House Sale and Purchase Calculator")
st.write("Easily calculate your equity, debts, and remaining cash after buying your new home!")

# Inputs
st.header("Enter Your Details:")

# Sale Price
sale_price = st.number_input("🏷️ House Sale Price (£)", value=475000, step=1000)
st.caption(f"Formatted: £{sale_price:,.0f}")

# Mortgage
mortgage_balance = st.number_input("🏦 Remaining Mortgage (£)", value=298000, step=1000)
st.caption(f"Formatted: £{mortgage_balance:,.0f}")

# Debts and Fees
debts_and_fees = st.number_input("💳 Debts + Fees (£)", value=56000, step=1000)
st.caption(f"Formatted: £{debts_and_fees:,.0f}")

# Deposit
deposit_amount = st.number_input("💰 Deposit for New House (£)", value=80000, step=1000)
st.caption(f"Formatted: £{deposit_amount:,.0f}")

# Calculations
equity = sale_price - mortgage_balance
after_debts = equity - debts_and_fees
remaining_cash = after_debts - deposit_amount

# Results
st.header("Results 📊")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Equity after Mortgage", value=f"£{equity:,.0f}")

with col2:
    st.metric(label="Equity after Debts & Fees", value=f"£{after_debts:,.0f}")

with col3:
    st.metric(label="Cash Remaining after Deposit", value=f"£{remaining_cash:,.0f}")

# Warning if cash negative
if remaining_cash < 0:
    st.error("⚠️ Warning: You do not have enough funds after paying the deposit!")

# Footer
st.markdown("---")
st.caption("Created with ❤️ by [Your Name or Company]")
