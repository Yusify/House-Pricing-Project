import streamlit as st

st.title("🏠 Boston House Price Predictor")
st.write("Adjust the values below to predict a house price:")

crim = st.slider("Crime Rate (crim)", 0.0, 90.0, 3.6)
zn = st.slider("Residential Zone Percentage (zn)", 0.0, 100.0, 11.0)
indus = st.slider("Industrial Area Percentage (indus)", 0.0, 28.0, 11.0)
chas = st.selectbox("Near River? (chas)", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
dis = st.slider("Distance to Work Centers (dis)", 1.0, 13.0, 3.8)
rad = st.slider("Highway Access Index (rad)", 1, 24, 9)
lstat = st.slider("Low Income Population % (lstat)", 1.0, 38.0, 12.0)
rm = st.slider("Number of Rooms (rm)", 3.0, 9.0, 6.3)

rm_lstat = rm / lstat

intercept = 29.08940863581039
coef = {
    "crim": -0.14720685002194883,
    "zn": 0.028678133879972423,
    "indus": -0.27435486681911614,
    "chas": 2.6359218315917654,
    "dis": -1.3641182384164037,
    "rad": -0.005294676293785439,
    "lstat": -0.35660103863655235,
    "rm_lstat": 8.436585863703709,
}

prediction = (
    intercept
    + coef["crim"] * crim
    + coef["zn"] * zn
    + coef["indus"] * indus
    + coef["chas"] * chas
    + coef["dis"] * dis
    + coef["rad"] * rad
    + coef["lstat"] * lstat
    + coef["rm_lstat"] * rm_lstat
)

if st.button("🔮 Predict Price"):
    if prediction < 0:
        st.error("⚠️ Invalid combination — try adjusting the values.")
    else:
        st.success(f"🏠 Predicted House Price: ${prediction * 1000:,.0f}")
        st.info(f"Model explains 74.6% of price variation (R² = 0.746)")