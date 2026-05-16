import streamlit as st
import pandas as pd
import time

# 1. Page Configuration
st.set_page_config(page_title="Tradata Challenge", layout="wide")

st.title("🕵️‍♂️ Tradata Booth Game")
st.markdown("Act like a Non-QM underwriter and find out the Overdraft Fee")

# 2. State management for the AI button
if 'ai_run' not in st.session_state:
    st.session_state.ai_run = False

# 3. Tradata AI Interface
col_btn, col_msg = st.columns([1, 3])

with col_btn:
    if st.button("🚀 Run Tradata AI", type="primary", use_container_width=True):
        st.session_state.ai_run = True

with col_msg:
    if st.session_state.ai_run:
        # Simulate fast AI processing
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("Scanning documents for return item fees...")
        time.sleep(0.4)
        progress_bar.progress(50)
        
        status_text.text("Mapping transaction vectors...")
        time.sleep(0.4)
        progress_bar.progress(100)
        
        status_text.markdown("✅ **Found hidden overdraft fee ($35.00) in 0.8 seconds! (Mapped to: Column 2, Row 8)**")
        time.sleep(0.2)
        progress_bar.empty()

st.markdown("---")

# 4. 30 Rows of Data (10 per column) to perfectly fit without scrolling
data = [
    # Column 1 (Rows 1-10)
    {"Date": "05/12/2026", "Description": "WHOLE FOODS MARKET", "Amount": "-$208.43"},
    {"Date": "05/21/2026", "Description": "STARBUCKS STORE #124", "Amount": "-$119.84"},
    {"Date": "05/15/2026", "Description": "HOME DEPOT", "Amount": "-$226.31"},
    {"Date": "05/17/2026", "Description": "WIRE TRANSFER IN", "Amount": "+$170.46"},
    {"Date": "05/07/2026", "Description": "COSTCO WHOLESALE", "Amount": "-$199.34"},
    {"Date": "05/17/2026", "Description": "ACH DEPOSIT - PAYROLL", "Amount": "+$190.37"},
    {"Date": "05/13/2026", "Description": "COSTCO WHOLESALE", "Amount": "-$104.61"},
    {"Date": "05/28/2026", "Description": "COSTCO WHOLESALE", "Amount": "-$125.94"},
    {"Date": "05/19/2026", "Description": "TARGET STORE", "Amount": "-$209.69"},
    {"Date": "05/24/2026", "Description": "AMAZON.COM PVMNT", "Amount": "-$94.79"},
    
    # Column 2 (Rows 11-20)
    {"Date": "05/18/2026", "Description": "WIRE TRANSFER IN", "Amount": "+$238.12"},
    {"Date": "05/06/2026", "Description": "ACH DEPOSIT - PAYROLL", "Amount": "-$41.09"},
    {"Date": "05/12/2026", "Description": "ACH DEPOSIT - PAYROLL", "Amount": "+$107.83"},
    {"Date": "05/29/2026", "Description": "MCDONALDS", "Amount": "-$238.90"},
    {"Date": "05/18/2026", "Description": "NETFLIX SUBSCRIPTION", "Amount": "-$146.10"},
    {"Date": "05/16/2026", "Description": "MCDONALDS", "Amount": "-$247.02"},
    {"Date": "05/14/2026", "Description": "ACH DEPOSIT - PAYROLL", "Amount": "+$145.58"},
    {"Date": "05/18/2026", "Description": "ACH DEPOSIT - OVERDRAFT FEES", "Amount": "-$35.00"}, 
    {"Date": "05/02/2026", "Description": "COMCAST CABLE", "Amount": "-$53.55"},
    {"Date": "05/27/2026", "Description": "STARBUCKS STORE #124", "Amount": "-$82.14"},
    
    # Column 3 (Rows 21-30)
    {"Date": "05/03/2026", "Description": "WHOLE FOODS MARKET", "Amount": "-$193.61"},
    {"Date": "05/30/2026", "Description": "NETFLIX SUBSCRIPTION", "Amount": "-$231.77"},
    {"Date": "05/07/2026", "Description": "APPLE ONLINE STORE", "Amount": "-$133.21"},
    {"Date": "05/18/2026", "Description": "WHOLE FOODS MARKET", "Amount": "-$175.88"},
    {"Date": "05/30/2026", "Description": "COSTCO WHOLESALE", "Amount": "-$176.02"},
    {"Date": "05/15/2026", "Description": "PG&E UTILITY PAYMENT", "Amount": "-$137.28"},
    {"Date": "05/27/2026", "Description": "WIRE TRANSFER IN", "Amount": "+$207.25"},
    {"Date": "05/30/2026", "Description": "MCDONALDS", "Amount": "-$41.88"},
    {"Date": "05/04/2026", "Description": "TARGET STORE", "Amount": "-$210.58"},
    {"Date": "05/23/2026", "Description": "COSTCO WHOLESALE", "Amount": "-$216.26"}
]

df = pd.DataFrame(data)

# 5. Pandas Styling to highlight the row if AI is run
def highlight_fee(row):
    if row['Amount'] == '-$35.00':
        return ['background-color: #d4edda; color: #155724; font-weight: bold'] * len(row)
    return [''] * len(row)

# Slice into 3 columns and set continuous indexes (1 to 30)
df1 = df.iloc[0:10].copy()
df1.index = range(1, 11)

df2 = df.iloc[10:20].copy()
df2.index = range(11, 21)

df3 = df.iloc[20:30].copy()
df3.index = range(21, 31)

# Apply styles conditionally
if st.session_state.ai_run:
    df1_display = df1.style.apply(highlight_fee, axis=1)
    df2_display = df2.style.apply(highlight_fee, axis=1)
    df3_display = df3.style.apply(highlight_fee, axis=1)
else:
    df1_display = df1
    df2_display = df2
    df3_display = df3

# 6. Display using st.table
c1, c2, c3 = st.columns(3)

with c1:
    st.table(df1_display)
with c2:
    st.table(df2_display)
with c3:
    st.table(df3_display)

# Reset Button
if st.session_state.ai_run:
    if st.button("Reset Challenge"):
        st.session_state.ai_run = False
        st.rerun()