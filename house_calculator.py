import streamlit as st

# Page Config
st.set_page_config(page_title="House Sale Calculator", page_icon="🏡", layout="centered")

# Main Title
st.title("🏡 House Sale and Purchase Calculator")
st.write("Instantly see your house sale, mortgage payoff, and cash position!")

# Inputs grouped in two columns
colA, colB = st.columns(2)

with colA:
    sale_price = st.number_input("🏷️ House Sale Price (£)", value=475000, step=1000)
    st.caption(f"💬 Sale Price: **£{sale_price:,.0f}**")

    debts_and_fees = st.number_input("💳 Debts + Fees (£)", value=56000, step=1000)
    st.caption(f"💬 Debts & Fees: **£{debts_and_fees:,.0f}**")

with colB:
    mortgage_balance = st.number_input("🏦 Remaining Mortgage (£)", value=298000, step=1000)
    st.caption(f"💬 Mortgage: **£{mortgage_balance:,.0f}**")

    deposit_amount = st.number_input("💰 Deposit for New House (£)", value=80000, step=1000)
    st.caption(f"💬 Deposit: **£{deposit_amount:,.0f}**")

# Live Calculations
equity = sale_price - mortgage_balance
after_debts = equity - debts_and_fees
remaining_cash = after_debts - deposit_amount

st.divider()

# Results
st.header("Results 📊")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Equity after Mortgage", value=f"£{equity:,.0f}")

with col2:
    st.metric(label="Equity after Debts & Fees", value=f"£{after_debts:,.0f}")

with col3:
    st.metric(label="Cash Remaining after Deposit", value=f"£{remaining_cash:,.0f}")

if remaining_cash < 0:
    st.error("⚠️ You do not have enough funds after deposit!")

st.markdown("---")
st.caption("Created with ❤️ by [Your Name or Company]")

