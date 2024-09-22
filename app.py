import pandas as pd
import streamlit as st

if "MTK" not in st.session_state:
    st.session_state.MTK = pd.read_csv("https://docs.google.com/spreadsheets/d/13PriSfxskOTcAlGv-gFd7WoiB2nQ2yx9hzsYQQUqJeY/export?format=csv&gid=0")
if "PKN" not in st.session_state:
    st.session_state.PKN = pd.read_csv("https://docs.google.com/spreadsheets/d/13PriSfxskOTcAlGv-gFd7WoiB2nQ2yx9hzsYQQUqJeY/export?format=csv&gid=295218205")
if "BINDO" not in st.session_state:
    st.session_state.BINDO = pd.read_csv("https://docs.google.com/spreadsheets/d/13PriSfxskOTcAlGv-gFd7WoiB2nQ2yx9hzsYQQUqJeY/export?format=csv&gid=986118028")
if "AKIDAH" not in st.session_state:
    st.session_state.AKIDAH = pd.read_csv("https://docs.google.com/spreadsheets/d/13PriSfxskOTcAlGv-gFd7WoiB2nQ2yx9hzsYQQUqJeY/export?format=csv&gid=1866255283")

def show_soal(subject, subject_key):
    if "submit" not in st.session_state:
        st.session_state.submit = False
    answers = {}
    nilai = 0
    jml_soal = len(subject)
    jawaban = subject['answer'].tolist()
    for idx, row in subject.iterrows():
        with st.container(border=True):
            st.write(f"Question {row['No.']}")
            answers[idx] = st.radio(
                label=f"{row['Questions']}",  # Adding the label argument here
                options=[f'a. {row['a']}', f'b. {row['b']}', f'c. {row['c']}', f'd. {row['d']}'],
                # index=['a', 'b', 'c', 'd'].index(row['answer']),
                index=None,
                key=f'question_{subject_key}_{idx}'
            )
            if st.session_state.submit == True:
                try:
                    if answers[idx][0] == jawaban[idx]:
                        st.success("betul")
                    else:
                        st.error(f"jawaban yang benar: {jawaban[idx]}")
                except:
                    st.error("belum dijawab")
    if st.button("Submit", key=subject_key):    
        st.session_state.submit = True
        for idx, jwb in enumerate(jawaban):
            try:
                if answers[idx][0] == jwb:
                    nilai += 1
            except:
                pass
    return nilai, jml_soal

def main():
    st.title("Latihan Ulangan")
    tab_bindo, tab_akidah, tab_mtk, tab_pkn = st.tabs(["B. Indonesia", "Akidah","Matematika", "PKN"])
    with tab_mtk:
        nilai, jml_soal = show_soal(st.session_state.MTK, "mtk")
        st.write(f"Jumlah betul: {nilai}")
        st.write(f"Nilainya adalah {nilai/jml_soal * 100:.2f}%")
    with tab_pkn:
        nilai, jml_soal = show_soal(st.session_state.PKN, 'pkn')
        st.write(f"Jumlah betul: {nilai}")
        st.write(f"Nilainya adalah {nilai/jml_soal * 100:.2f}%")
    with tab_bindo:
        subtab1, subtab2, subtab3 = st.tabs(["Satu", "Dua", "Tiga"])
        with subtab1:
            nilai, jml_soal = show_soal(st.session_state.BINDO[st.session_state.BINDO["No."].isin(range(1,11))], "bindo1")
            st.write(f"Jumlah betul: {nilai}")
            st.write(f"Nilainya adalah {nilai/jml_soal * 100:.2f}%")
        with subtab2:
            nilai, jml_soal = show_soal(st.session_state.BINDO[st.session_state.BINDO["No."].isin(range(11,21))], "bindo2")
            st.write(f"Jumlah betul: {nilai}")
            st.write(f"Nilainya adalah {nilai/jml_soal * 100:.2f}%")
        with subtab3:
            nilai, jml_soal = show_soal(st.session_state.BINDO[st.session_state.BINDO["No."].isin(range(21,31))], "bindo3")
            st.write(f"Jumlah betul: {nilai}")
            st.write(f"Nilainya adalah {nilai/jml_soal * 100:.2f}%")
    with tab_akidah:
        subtab1, subtab2, subtab3 = st.tabs(["Satu", "Dua", "Tiga"])
        with subtab1:
            nilai, jml_soal = show_soal(st.session_state.AKIDAH[st.session_state.AKIDAH["No."].isin(range(1,11))], "akidah1")
            st.write(f"Jumlah betul: {nilai}")
            st.write(f"Nilainya adalah {nilai/jml_soal * 100:.2f}%")
        with subtab2:
            nilai, jml_soal = show_soal(st.session_state.AKIDAH[st.session_state.AKIDAH["No."].isin(range(11,21))], "akidah2")
            st.write(f"Jumlah betul: {nilai}")
            st.write(f"Nilainya adalah {nilai/jml_soal * 100:.2f}%")
        with subtab3:
            nilai, jml_soal = show_soal(st.session_state.AKIDAH[st.session_state.AKIDAH["No."].isin(range(21,31))], "akidah3")
            st.write(f"Jumlah betul: {nilai}")
            st.write(f"Nilainya adalah {nilai/jml_soal * 100:.2f}%")

if __name__ == "__main__":
    main()
