import streamlit as st
import pandas as pd
from io import BytesIO

# Page settings
st.set_page_config(page_title="Ross & Marta Wales Move", page_icon="🏡", layout="centered")

# 🌄 Add background styling
st.markdown("""
    <style>
        body {
            background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1400&q=80');
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🏡 Ross & Marta Wales Move")
st.markdown("Easily work out your equity and cash remaining when buying your new home.")

# Input section
st.header("🔢 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    sale_price = st.number_input("🏷️ Sale Price (£)", min_value=0, step=1000, help="Expected sale price of your current house")
    mortgage_balance = st.number_input("🏦 Mortgage Left (£)", min_value=0, step=1000, help="Outstanding mortgage on your current house")

with col2:
    debts_and_fees = st.number_input("💳 Debts & Legal Fees (£)", min_value=0, step=1000, help="Total of debts, conveyancing fees, stamp duty etc.")
    deposit_amount = st.number_input("💰 Deposit for New House (£)", min_value=0, step=1000, help="Deposit you're putting down on the next house")

# Only run calculations if all values are filled
if all(x > 0 for x in [sale_price, mortgage_balance, debts_and_fees, deposit_amount]):
    
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
        </div>
        """, unsafe_allow_html=True
    )

    st.divider()

    # Detailed Results
    st.subheader("📊 Full Breakdown")

    results = {
        "House Sale Price": f"£{sale_price:,.0f}",
        "Less: Mortgage Remaining": f"-£{mortgage_balance:,.0f}",
        "Equity After Mortgage": f"£{equity:,.0f}",
        "Less: Debts & Fees": f"-£{debts_and_fees:,.0f}",
        "Equity After Debts & Fees": f"£{after_debts:,.0f}",
        "Less: Deposit for New House": f"-£{deposit_amount:,.0f}",
        "Remaining Cash": f"£{remaining_cash:,.0f}",
    }

    # Show results in two columns
    colA, colB = st.columns(2)
    with colA:
        for label, value in list(results.items())[:4]:
            st.markdown(f"**{label}:** {value}")
    with colB:
        for label, value in list(results.items())[4:]:
            st.markdown(f"**{label}:** {value}")

    # MARTA's Mood
    st.markdown("---")
    st.header("🧠 MARTA's Mood")

    if remaining_cash > 15000:
        st.markdown("### 😊 MARTA is happy — you're well set!")
    elif 0 <= remaining_cash <= 15000:
        st.markdown("### 😐 MARTA is not impressed — cutting it a bit close.")
    else:
        st.markdown("### 😠 MARTA is angry — there’s not enough money after the deposit!")

# Footer
st.markdown("---")
st.caption("Made with ❤️ for Marta by Ross")

