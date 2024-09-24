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
if "FIKIH" not in st.session_state:
    st.session_state.FIKIH = pd.read_csv("https://docs.google.com/spreadsheets/d/13PriSfxskOTcAlGv-gFd7WoiB2nQ2yx9hzsYQQUqJeY/export?format=csv&gid=1247484320")
if "SENI" not in st.session_state:
    st.session_state.SENI = pd.read_csv("https://docs.google.com/spreadsheets/d/13PriSfxskOTcAlGv-gFd7WoiB2nQ2yx9hzsYQQUqJeY/export?format=csv&gid=360219782")
if "ENG" not in st.session_state:
    st.session_state.ENG = pd.read_csv("https://docs.google.com/spreadsheets/d/13PriSfxskOTcAlGv-gFd7WoiB2nQ2yx9hzsYQQUqJeY/export?format=csv&gid=2130374808")

def show_soal(subject, subject_key):
    st.session_state.answers = {}
    st.session_state.nilai = 0
    st.session_state.jml_soal = len(subject)
    st.session_state.jawaban = {}
    st.session_state.salah = []
    for idx, row in subject.iterrows():
        with st.container(border=True):
            st.write(f"Question {idx+1}")
            label = str(row['Questions'])
            label = label.split("\n")
            for i in range(len(label)):
                if len(label) > 1:
                    if i < len(label):
                        y = label[i][:-2]
                else:
                    y = label[i]
                st.write(y)
            st.session_state.answers[row['No.']] = st.radio(
                label="",  # Adding the label argument here
                label_visibility="hidden",
                options=[f'a. {row['a']}', f'b. {row['b']}', f'c. {row['c']}', f'd. {row['d']}'],
                # index=['a', 'b', 'c', 'd'].index(row['answer']),
                index=None,
                key=f'question_{subject_key}_{row['No.']}'
            )
            st.session_state.jawaban[row['No.']] = row['answer']
    if st.button("Submit", key=subject_key):
        for number in subject['No.']:
            try:
                if st.session_state.answers[number][0] == st.session_state.jawaban[number]:
                    st.session_state.nilai += 1
                else:
                    st.session_state.salah.append(number)
            except:
                pass
        
        st.write(f"Jumlah betul: {st.session_state.nilai}")
        st.write(f"Nilainya adalah {st.session_state.nilai/st.session_state.jml_soal * 100:.2f}%")
        if st.session_state.nilai < 10:
            st.write(f"coba cek lagi jawaban nomor: {st.session_state.salah}")

def main():
    st.title("Latihan Ulangan")
    tab_bindo,tab_mtk, tab_pkn, tab_akidah, tab_fikih, tab_seni, tab_eng = st.tabs(["B. Indonesia", 
                                                                           "Matematika", 
                                                                           "PKN", 
                                                                           "Akidah", 
                                                                           "Fikih", 
                                                                           "Seni Rupa",
                                                                           "Bhs. Inggris"])
    with tab_mtk:
        subtab1, subtab2, subtab3 = st.tabs(["1-10", "11-20", "21-30"])
        with subtab1:
            show_soal(st.session_state.MTK[st.session_state.MTK["No."].isin(range(1,11))], "mtk1")
        with subtab2:
            show_soal(st.session_state.MTK[st.session_state.MTK["No."].isin(range(11,21))], "mtk2")
        with subtab3:
            show_soal(st.session_state.MTK[st.session_state.MTK["No."].isin(range(21,31))], "mtk3")
        # st.write(f"Jumlah betul: {st.session_state.nilai}")
        # st.write(f"Nilainya adalah {st.session_state.nilai/st.session_state.jml_soal * 100:.2f}%")
    with tab_pkn:
        show_soal(st.session_state.PKN, 'pkn')
        # st.write(f"Jumlah betul: {st.session_state.nilai}")
        # st.write(f"Nilainya adalah {st.session_state.nilai/st.session_state.jml_soal * 100:.2f}%")
    with tab_bindo:
        subtab1, subtab2, subtab3 = st.tabs(["1-10", "11-20", "21-30"])
        with subtab1:
            show_soal(st.session_state.BINDO[st.session_state.BINDO["No."].isin(range(1,11))], "bindo1")
            # st.write(f"Jumlah betul: {st.session_state.nilai}")
            # st.write(f"Nilainya adalah {st.session_state.nilai/st.session_state.jml_soal * 100:.2f}%")
        with subtab2:
            show_soal(st.session_state.BINDO[st.session_state.BINDO["No."].isin(range(11,21))], "bindo2")
            # st.write(f"Jumlah betul: {st.session_state.nilai}")
            # st.write(f"Nilainya adalah {st.session_state.nilai/st.session_state.jml_soal * 100:.2f}%")
        with subtab3:
            show_soal(st.session_state.BINDO[st.session_state.BINDO["No."].isin(range(21,31))], "bindo3")
            # st.write(f"Jumlah betul: {st.session_state.nilai}")
            # st.write(f"Nilainya adalah {st.session_state.nilai/st.session_state.jml_soal * 100:.2f}%")

    with tab_akidah:
        subtab1, subtab2, subtab3 = st.tabs(["1-10", "11-20", "21-30"])
        with subtab1:
            show_soal(st.session_state.AKIDAH[st.session_state.AKIDAH["No."].isin(range(1,11))], "akidah1")
            # st.write(f"Jumlah betul: {st.session_state.nilai}")
            # st.write(f"Nilainya adalah {st.session_state.nilai/st.session_state.jml_soal * 100:.2f}%")
        with subtab2:
            show_soal(st.session_state.AKIDAH[st.session_state.AKIDAH["No."].isin(range(11,21))], "akidah2")
            # st.write(f"Jumlah betul: {st.session_state.nilai}")
            # st.write(f"Nilainya adalah {st.session_state.nilai/st.session_state.jml_soal * 100:.2f}%")
        with subtab3:
            show_soal(st.session_state.AKIDAH[st.session_state.AKIDAH["No."].isin(range(21,31))], "akidah3")
            # st.write(f"Jumlah betul: {st.session_state.nilai}")
            # st.write(f"Nilainya adalah {st.session_state.nilai/st.session_state.jml_soal * 100:.2f}%")
    
    with tab_fikih:
        subtab1, subtab2, subtab3 = st.tabs(["1-10", "11-20", "21-30"])
        with subtab1:
            show_soal(st.session_state.FIKIH[st.session_state.FIKIH["No."].isin(range(1,11))], "fikih1")
        with subtab2:
            show_soal(st.session_state.FIKIH[st.session_state.FIKIH["No."].isin(range(11,21))], "fikih2")
        with subtab3:
            show_soal(st.session_state.FIKIH[st.session_state.FIKIH["No."].isin(range(21,31))], "fikih3")
    
    with tab_seni:
        subtab1, subtab2, subtab3 = st.tabs(["1-10", "11-20", "21-30"])
        with subtab1:
            show_soal(st.session_state.SENI[st.session_state.SENI["No."].isin(range(1,11))], "seni1")
        with subtab2:
            show_soal(st.session_state.SENI[st.session_state.SENI["No."].isin(range(11,21))], "seni2")
        with subtab3:
            show_soal(st.session_state.SENI[st.session_state.SENI["No."].isin(range(21,31))], "seni3")

    with tab_eng:
        subtab1, subtab2, subtab3 = st.tabs(["1-10", "11-20", "21-30"])
        with subtab1:
            show_soal(st.session_state.ENG[st.session_state.ENG["No."].isin(range(1,11))], "english1")
        with subtab2:
            show_soal(st.session_state.ENG[st.session_state.ENG["No."].isin(range(11,21))], "english2")
        with subtab3:
            show_soal(st.session_state.ENG[st.session_state.ENG["No."].isin(range(21,31))], "english3")

if __name__ == "__main__":
    main()
