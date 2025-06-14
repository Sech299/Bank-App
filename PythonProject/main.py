import streamlit as st
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount

# --- Streamlit UI ---

st.set_page_config(page_title="Bank App", page_icon="🏦")
st.title("🏦 Bank App")
st.write("Welcome! Choose account type and perform transactions.")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #9370DB;  /* Medium Purple*/
    }
    </style>
    """,
    unsafe_allow_html=True
    )

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #000080;  /* Navy Blue */
        color: white;               /* White text color */
        border: None;               /* Remove button border */
        border-radius: 8px;         /* Round the corners */
        padding: 10px 20px;         /* Button padding */
        font-size: 16px;            /* Button text size */
    }
    .stButton>button:hover {
        background-color: #6a006a; /* Darker purple when hovered */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Initialize accounts
if "savings" not in st.session_state:
    st.session_state.savings = SavingsAccount("Divine", 10000.0)
if "current" not in st.session_state:
    st.session_state.current = CurrentAccount("Divine", 15000.0)

# UI Options
account_type = st.selectbox("Select Account Type", ["Savings Account", "Current Account"])
transaction_type = st.radio("Choose Transaction Type", ["Deposit", "Withdraw"])
amount = st.number_input("Enter amount", min_value=0.0, step=100.0)

# Logic for Savings
if account_type == "Savings Account":
    account = st.session_state.savings
    st.subheader("💼 Savings Account")
    st.write(f"**Balance:** ₦{account.balance:.2f}")
    if transaction_type == "Deposit":
        if st.button("Deposit"):
            st.success(account.deposit(amount))
    elif transaction_type == "Withdraw":
        st.info(f"Note: Max withdrawal per transaction is ₦{account.withdrawal_limit:.2f}")
        if st.button("Withdraw"):
            st.warning(account.withdraw(amount))

# Logic for Current
elif account_type == "Current Account":
    account = st.session_state.current
    st.subheader("💳 Current Account")
    st.write(f"**Balance:** ₦{account.balance:.2f}")
    if transaction_type == "Deposit":
        if st.button("Deposit"):
            st.success(account.deposit(amount))
    elif transaction_type == "Withdraw":
        if st.button("Withdraw"):
            st.warning(account.withdraw(amount))

