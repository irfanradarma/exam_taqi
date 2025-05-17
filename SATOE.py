import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        .main-title {
            font-size: 36px;
            font-weight: bold;
            color: #2c3e50;
            padding-bottom: 10px;
            border-bottom: 2px solid #e0e0e0;
        }
        .filter-box {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #ddd;
            margin-bottom: 20px;
        }
        .dataframe th {
            background-color: #f0f0f0;
            color: #333;
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 3rem;
            padding-right: 3rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Load Sheet ---
sheet_url = "https://docs.google.com/spreadsheets/d/1wYHIvmtuKeHHZeOgrrSTu1mkDsQsIc419XAUlfzQLoY/export?format=csv&gid=742196418"

@st.cache_data
def load_data(sheet_url):
    try:
        df = pd.read_csv(sheet_url)
        df = df[['NAMA LENGKAP', 'KELAS', 'PEKERJAAN / PROFESI SAAT INI',
                 'NAMA INSTANSI / PERUSAHAAN / USAHA BISNIS',
                 'Silahkan Isi Kota Domisili saat ini (Contoh: Kota Tangerang)']]
        df.columns = ['NAMA', 'KELAS', 'OKUPASI', 'INSTANSI', 'DOMISILI']
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# --- Main App ---
def main():
    if 'database' not in st.session_state:
        st.session_state.database = load_data(sheet_url)

    st.markdown("<div class='main-title'>📋 SATOE Alumni Directory</div>", unsafe_allow_html=True)

    # Filter container
    with st.container():
        st.markdown("<div class='filter-box'>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([2, 2, 3])
        with col1:
            st.session_state.kelas = st.multiselect(
                label='KELAS',
                options=['ALL'] + sorted(st.session_state.database['KELAS'].dropna().unique().tolist()),
                default='ALL'
            )
        with col2:
            st.session_state.okupasi = st.multiselect(
                label='OKUPASI',
                options=['ALL'] + sorted(st.session_state.database['OKUPASI'].dropna().unique().tolist()),
                default='ALL'
            )
        with col3:
            st.session_state.nama = st.text_input("Cari berdasarkan NAMA (bebas huruf besar/kecil):")
        st.markdown("</div>", unsafe_allow_html=True)

    # --- Filtering Logic ---
    filtered_df = st.session_state.database.copy()

    if 'ALL' not in st.session_state.kelas:
        filtered_df = filtered_df[filtered_df['KELAS'].isin(st.session_state.kelas)]

    if 'ALL' not in st.session_state.okupasi:
        filtered_df = filtered_df[filtered_df['OKUPASI'].isin(st.session_state.okupasi)]

    if st.session_state.nama.strip():
        filtered_df = filtered_df[filtered_df['NAMA'].str.contains(st.session_state.nama.strip(), case=False, na=False)]

    filtered_df = filtered_df.drop_duplicates(subset=['NAMA', 'KELAS', 'OKUPASI', 'INSTANSI', 'DOMISILI']).reset_index(drop=True)

    # --- Show Table ---
    st.dataframe(filtered_df, use_container_width=True)

    # Footer separator
    st.markdown('---')

if __name__ == "__main__":
    main()
