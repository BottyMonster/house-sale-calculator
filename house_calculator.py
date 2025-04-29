import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="House Sale Calculator", page_icon="🏡", layout="centered")

st.title("🏡 House Sale & Purchase Calculator")
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

# Excel download
def to_excel(data_dict):
    df = pd.DataFrame(data_dict.items(), columns=["Item", "Amount"])
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name="Results")
    processed_data = output.getvalue()
    return processed_data

st.markdown("### 📥 Download Your Results")
excel_data = to_excel(results)
st.download_button(
    label="⬇️ Download as Excel File",
    data=excel_data,
    file_name="house_sale_calculator.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")


