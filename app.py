
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quản lý tín hiệu giao thông", layout="wide")
st.title("📊 Ứng dụng quản lý tín hiệu giao thông")

uploaded_file = st.file_uploader("Chọn file Excel", type=["xlsx", "xls"])
if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("Đọc file thành công ✅")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Lỗi khi đọc file: {e}")
