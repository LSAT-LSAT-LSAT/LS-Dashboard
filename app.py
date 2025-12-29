import streamlit as st
import pandas as pd
import plotly.express as px



@st.cache_data


SHEET_ID = "1FoTiT7dv60_Lj9xWMWYAINNJvswV1HsX"
XLSX_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=xlsx"

@st.cache_data
def load_data():
    df = pd.read_excel(XLSX_URL, sheet_name="JD_Programs_2026", engine="openpyxl")
    df["BarPassNum"] = df["Bar Passage Rate"].astype(str).str.replace("%", "").astype(float)
    df["LSAT"] = pd.to_numeric(df["Median LSAT"], errors="coerce")
    df["Tuition"] = pd.to_numeric(df["Tuition FT (USD)"], errors="coerce")
    return df

df = load_data()



import streamlit as st

st.set_page_config(page_title="PIPELINE DEVELOPER RESEARCH LAB", layout="wide")

# Optional: logo at the top
st.image("logo.png", width=220)  # if you have a logo file

st.title("PIPELINE DEVELOPER RESEARCH LAB")
st.subheader("Applied Research, Analytics, and AI-Powered Decision Tools")

st.write(
    """
    PIPELINE DEVELOPER RESEARCH LAB provides applied research, market and policy analysis,
    and custom AI dashboards for small businesses, nonprofits, and institutions.
    We design and deploy interactive tools like this ABA J.D. dashboard to support
    data-driven decisions.
    """
)

st.write("📩 To discuss a research project or tool, email: hello@pipelinedeveloperlab.com")


# Filters
with st.sidebar:
    st.header("🔍 Filter Options")
    program_types = df["Program Type"].unique().tolist()
    selected_types = st.multiselect("Program Type", program_types, default=program_types)

    tuition_limit = st.slider("Max Tuition (USD)", int(df["Tuition"].min()), int(df["Tuition"].max()), int(df["Tuition"].max()))
    lsat_limit = st.slider("Max LSAT", int(df["LSAT"].min()), int(df["LSAT"].max()), int(df["LSAT"].max()))

# Apply filters
filtered_df = df[
    (df["Program Type"].isin(selected_types)) &
    (df["Tuition"] <= tuition_limit) &
    (df["LSAT"] <= lsat_limit)
]

# 1. Lowest Tuition
lowest_tuition = filtered_df.sort_values(by="Tuition").head(10)
fig1 = px.bar(lowest_tuition, x="School Name", y="Tuition", text="Tuition", title="💸 Lowest Tuition (Full-Time)")
fig1.update_traces(texttemplate='$%{text:.0f}', textposition='outside')
fig1.update_layout(xaxis_tickangle=-45)

# 2. Tuition vs Bar Passage Rate
fig2 = px.scatter(filtered_df, x="Tuition", y="BarPassNum", size="LSAT", color="Program Type",
                  hover_name="School Name", title="🎯 Tuition vs Bar Passage Rate (Size = LSAT)")

# 3. Lowest LSAT
lowest_lsat = filtered_df.sort_values(by="LSAT").head(10)
fig3 = px.bar(lowest_lsat, x="School Name", y="LSAT", text="LSAT", title="🧪 Lowest Median LSAT")
fig3.update_traces(textposition='outside')
fig3.update_layout(xaxis_tickangle=-45)

# 4. Program Type Distribution
type_counts = filtered_df["Program Type"].value_counts().reset_index()
type_counts.columns = ["Program Type", "Count"]
fig4 = px.pie(type_counts, values="Count", names="Program Type", title="📘 Program Type Distribution")

# Layout
col1, col2 = st.columns(2)
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig3, use_container_width=True)

st.plotly_chart(fig2, use_container_width=True)

st.plotly_chart(fig4, use_container_width=True)

if st.checkbox("Show Filtered Data Table"):
    st.dataframe(filtered_df, use_container_width=True)

if st.checkbox("Show Program Links"):
    st.write(filtered_df[["School Name", "Program Link", "Apply Link"]])
