import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# PHẦN 1: XỬ LÝ DỮ LIỆU (PANDAS)
# ==========================================

data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [9.0, 8.5, 7.0, 9.5, 6.0, 8.0, 8.5, 9.0, 7.5, 10.0],
    'Giữa kỳ': [8.0, 7.5, 6.5, 9.0, 5.5, 7.0, 8.0, 8.5, 6.0, 9.5],
    'Cuối kỳ': [8.5, 8.0, 7.0, 8.5, 5.0, 7.5, 8.0, 9.0, 6.5, 9.0]
}
df = pd.DataFrame(data)

df['Tong_ket'] = 0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']
df['Tong_ket'] = df['Tong_ket'].round(2)

def tinh_xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(tinh_xep_loai)

diem_tb_lop = df['Tong_ket'].mean()
sv_max = df[df['Tong_ket'] == df['Tong_ket'].max()]
sv_min = df[df['Tong_ket'] == df['Tong_ket'].min()]
so_sv_dat = len(df[df['Tong_ket'] >= 5.0])

# ==========================================
# PHẦN 2: GIAO DIỆN WEB APP (STREAMLIT)
# ==========================================

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.write("### Bảng điểm của 10 sinh viên:")
st.dataframe(df, use_container_width=True)

st.write(f"👉 **Điểm tổng kết trung bình của lớp:** {diem_tb_lop:.2f}")
st.write(f"👉 **Số sinh viên đạt (Điểm tổng kết ≥ 5):** {so_sv_dat} sinh viên")

st.write(f"🥇 **Sinh viên có điểm tổng kết cao nhất:** {', '.join(sv_max['Họ và tên'])} ({sv_max['Tong_ket'].values} điểm)")
st.write(f"🥉 **Sinh viên có điểm tổng kết thấp nhất:** {', '.join(sv_min['Họ và tên'])} ({sv_min['Tong_ket'].values} điểm)")

st.markdown("---")

st.write("### Tra cứu chi tiết sinh viên:")
chon_ten = st.selectbox("Chọn một sinh viên:", df['Họ và tên'].tolist())

if chon_ten:
    dong_sv = df[df['Họ và tên'] == chon_ten].iloc[0]
    st.info(f"**{chon_ten}** | Chuyên cần: {dong_sv['Chuyên cần']} | Giữa kỳ: {dong_sv['Giữa kỳ']} | Cuối kỳ: {dong_sv['Cuối kỳ']} | Tổng kết: {dong_sv['Tong_ket']} | Xếp loại: {dong_sv['Xep_loai']}")

st.markdown("---")

st.write("### Biểu đồ trực quan hóa:")
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(df['Họ và tên'], df['Tong_ket'], color='dodgerblue', height=0.5)
ax.set_title("Biểu đồ điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Điểm số")
ax.set_ylabel("Tên sinh viên")
ax.set_xlim(0, 10)
ax.invert_yaxis() 
st.pyplot(fig)

st.markdown("---")

st.markdown(
    "<p style='text-align: center; font-size: 12px; color: gray;'>Người tạo ứng dụng: Lê Bảo - MSSV: 060208010755</p>", 
    unsafe_allow_html=True
)