import pandas as pd
import streamlit as st

if "MTK" not in st.session_state:
    st.session_state.MTK = pd.read_csv("https://docs.google.com/spreadsheets/d/13PriSfxskOTcAlGv-gFd7WoiB2nQ2yx9hzsYQQUqJeY/export?format=csv&gid=0")
if "PKN" not in st.session_state:
    st.session_state.PKN = pd.read_csv("https://docs.google.com/spreadsheets/d/13PriSfxskOTcAlGv-gFd7WoiB2nQ2yx9hzsYQQUqJeY/export?format=csv&gid=295218205")
if "BINDO" not in st.session_state:
    st.session_state.BINDO = pd.read_csv("https://docs.google.com/spreadsheets/d/13PriSfxskOTcAlGv-gFd7WoiB2nQ2yx9hzsYQQUqJeY/export?format=csv&gid=986118028")

def show_soal(subject, subject_key):
    answers = {}
    nilai = 0
    jml_soal = len(subject)+1
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
    if st.button("Submit", key=subject_key):    
        jawaban = subject['answer'].tolist()
        for idx, jwb in enumerate(jawaban):
            try:
                if answers[idx][0] == jwb:
                    nilai += 1
            except:
                pass
    return nilai, jml_soal

def main():
    st.title("Latihan Ulangan")
    tab_mtk, tab_pkn, tab_bindo = st.tabs(["Matematika", "PKN", "B. Indonesia"])
    with tab_mtk:
        nilai, jml_soal = show_soal(st.session_state.MTK, "mtk")
        st.write(f"Jumlah betul: {nilai}")
        st.write(f"Nilainya adalah {nilai/jml_soal * 100:.2f}%")
    with tab_pkn:
        nilai, jml_soal = show_soal(st.session_state.PKN, 'pkn')
        st.write(f"Jumlah betul: {nilai}")
        st.write(f"Nilainya adalah {nilai/jml_soal * 100:.2f}%")

if __name__ == "__main__":
    main()
