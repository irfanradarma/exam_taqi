import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

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

    st.title("📋 SATOE-52 Alumni Directory")

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

    # --- Filtering Logic ---
    filtered_df = st.session_state.database.copy()

    if 'ALL' not in st.session_state.kelas:
        filtered_df = filtered_df[filtered_df['KELAS'].isin(st.session_state.kelas)]

    if 'ALL' not in st.session_state.okupasi:
        filtered_df = filtered_df[filtered_df['OKUPASI'].isin(st.session_state.okupasi)]

    if st.session_state.nama.strip():
        filtered_df = filtered_df[filtered_df['NAMA'].str.contains(st.session_state.nama.strip(), case=False, na=False)]

    filtered_df = filtered_df.drop_duplicates(subset=['NAMA', 'KELAS', 'OKUPASI', 'INSTANSI', 'DOMISILI']).reset_index(drop=True)
    filtered_df['No'] = filtered_df.index + 1
    filtered_df = filtered_df[['No', 'NAMA', 'KELAS', 'OKUPASI', 'INSTANSI', 'DOMISILI']]

    # --- Show Table ---
    st.dataframe(filtered_df, use_container_width=True, hide_index=True, height=423,
                 column_config={
                     'No': st.column_config.NumberColumn(
                            width="small",
                            help="Nomor"
                     ),
                     'NAMA': st.column_config.TextColumn(
                            width="large",
                            help="Nama Lengkap"
                     ),
                     'KELAS': st.column_config.TextColumn(
                            width="small",
                            help="Kelas"
                     ),
                     'OKUPASI': st.column_config.TextColumn(
                            width="medium",
                            help="Pekerjaan / Profesi"
                     ),
                     'INSTANSI': st.column_config.TextColumn(
                            width="large",
                            help="Nama Instansi / Perusahaan / Usaha Bisnis"
                     ),
                     'DOMISILI': st.column_config.TextColumn(
                            width="medium",
                            help="Kota Domisili"
                     )
                 })
    st.markdown('---')

    st.subheader("Rekap Data per Kelas")
    kelas_counts = st.session_state.database['KELAS'].value_counts()
    kelas_counts = kelas_counts.reset_index()
    kelas_counts.columns = ['KELAS', 'JUMLAH']
    kelas_counts['BAR'] = kelas_counts['JUMLAH']
    kelas_counts = kelas_counts.sort_values(by='KELAS').reset_index(drop=True)
    st.dataframe(kelas_counts, use_container_width=False, hide_index=True,
                 column_config={
                     'KELAS': st.column_config.TextColumn(
                            width="small",
                            help="Kelas"
                     ),
                        'JUMLAH': st.column_config.NumberColumn(
                                width="small",
                                help="Jumlah"
                        ),
                     'BAR': st.column_config.ProgressColumn(
                            width="large",
                            help="Jumlah",
                            format=" ",
                            max_value=48,
                            min_value=0,
                     )
                 })
    st.markdown('---')

if __name__ == "__main__":
    main()
