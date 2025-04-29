import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(page_title="Ross & Marta Wales Move", page_icon="🏡", layout="centered")

# 🌄 Wales background with dark overlay
st.markdown("""
    <style>
        body {
            background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
            url('https://images.unsplash.com/photo-1610394214304-f978ec6dfe8a?auto=format&fit=crop&w=1400&q=80');
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center;
        }
        .stApp {
            background-color: rgba(0, 0, 0, 0.5);
            color: white;
            padding: 2rem;
            border-radius: 10px;
        }
        .stNumberInput input {
            background-color: #222 !important;
            color: #fff !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🏡 Ross & Marta Wales 🐉 Move")
st.markdown("Easily work out your equity and cash remaining when buying your new home.")

# 🔢 Input section
st.header("🔢 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    sale_price = st.number_input("🏷️ Sale Price", min_value=0, step=1000, format="%d")
    st.caption(f"💬 You entered: £{sale_price:,.0f}")

    mortgage_balance = st.number_input("🏦 Mortgage Left", min_value=0, step=1000, format="%d")
    st.caption(f"💬 You entered: £{mortgage_balance:,.0f}")

with col2:
    debts_and_fees = st.number_input("💳 Debts & Legal Fees", min_value=0, step=1000, format="%d")
    st.caption(f"💬 You entered: £{debts_and_fees:,.0f}")

    deposit_amount = st.number_input("💰 Deposit for New House", min_value=0, step=1000, format="%d")
    st.caption(f"💬 You entered: £{deposit_amount:,.0f}")

# 🧮 Calculations (always run, default to 0)
equity = sale_price - mortgage_balance if sale_price and mortgage_balance else 0
after_debts = equity - debts_and_fees if equity and debts_and_fees else 0
remaining_cash = after_debts - deposit_amount if after_debts and deposit_amount else 0

# 🧾 Summary
st.markdown("### 🧾 Summary")

summary_color = "#00ff88" if remaining_cash >= 0 else "#ff4444"
st.markdown(
    f"""
    <div style='padding: 1em; border: 2px solid #888; border-radius: 10px; background-color: rgba(255,255,255,0.1);'>
        <h3 style='color: {summary_color}'>💷 Remaining Cash After Everything: <strong>£{remaining_cash:,.0f}</strong></h3>
    </div>
    """, unsafe_allow_html=True
)

st.divider()

# 📊 Breakdown
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

colA, colB = st.columns(2)
with colA:
    for label, value in list(results.items())[:4]:
        st.markdown(f"**{label}:** {value}")
with colB:
    for label, value in list(results.items())[4:]:
        st.markdown(f"**{label}:** {value}")

# 🧠 MARTA's Mood (always shown, centered)
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>🧠 MARTA's Mood</h2>", unsafe_allow_html=True)

if remaining_cash > 15000:
    st.markdown("<h3 style='text-align: center;'>😊 MARTA is happy — you're well set!</h3>", unsafe_allow_html=True)
elif 0 <= remaining_cash <= 15000:
    st.markdown("<h3 style='text-align: center;'>😐 MARTA is not impressed — cutting it a bit close.</h3>", unsafe_allow_html=True)
else:
    st.markdown("<h3 style='text-align: center;'>😠 MARTA is angry — there’s not enough money after the deposit!</h3>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Made with ❤️ for Marta by Ross")
