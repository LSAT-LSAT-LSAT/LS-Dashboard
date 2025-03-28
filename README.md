# ⚖️ ABA J.D. Program Dashboard

An interactive Streamlit dashboard for exploring ABA-accredited online and hybrid J.D. programs, focusing on:

- 💸 Tuition (lowest full-time costs)
- 🧪 LSAT (most accessible entry scores)
- 🎓 Bar Passage Rates (highest performing schools)
- 📊 Interactive visualizations with Plotly

## 🚀 Features

- Sidebar filters for Program Type, Tuition, and LSAT
- Visual comparisons: tuition, LSAT, bar passage, and program types
- Program links for more info or to apply
- Responsive layout powered by Streamlit and Plotly

## 📁 File Structure

```
.
├── app.py                      # Streamlit dashboard
├── ABA_Online_JD_Programs_2025_Styled.xlsx  # Excel data
├── generate_jd_data.py         # Script to regenerate the dataset (optional)
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview and instructions
```

## 🧪 Getting Started (Locally)

1. Clone the repo or download the files
2. Create a virtual environment (optional but recommended)
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the dashboard:

```bash
streamlit run app.py
```

---

## 🌐 Deploy on Streamlit Community Cloud

### Step-by-Step:

1. Create a GitHub repo (e.g. `jd-dashboard`)
2. Upload these files:
   - `app.py`
   - `ABA_Online_JD_Programs_2025_Styled.xlsx`
   - `requirements.txt`
   - `README.md`

3. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
4. Sign in with GitHub and click **New App**
5. Select your repo and set:
   - **Main file:** `app.py`

6. Click **Deploy** — done! 🎉

---

## 💬 Questions or Contributions

Pull requests are welcome. For suggestions or enhancements, open an issue!

---

© 2025 ABA J.D. Explorer Team
