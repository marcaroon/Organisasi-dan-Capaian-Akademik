import pickle
import streamlit as st
import sklearn

# Load the model
mhs_model = pickle.load(open('modelnew.sav', 'rb'))

# Function to map IPK to numerical values


def map_ipk(ipk):
    if ipk is None:
        return None
    elif ipk >= 1.00 and ipk <= 1.50:
        return 0
    elif ipk > 1.50 and ipk <= 2.00:
        return 1
    elif ipk > 2.00 and ipk <= 2.50:
        return 2
    elif ipk > 2.50 and ipk <= 3.00:
        return 3
    elif ipk > 3.00 and ipk <= 3.50:
        return 4
    elif ipk > 3.50 and ipk <= 4.00:
        return 5
    else:
        return None

# Function to map Jabatan to numerical values


def map_jabatan(jabatan):
    if jabatan == 'Ketua':
        return 6
    elif jabatan == 'Wakil Ketua':
        return 5
    elif jabatan == 'Sekretaris/Bendahara':
        return 4
    elif jabatan == 'Kepala Bagian/Departemen/Bidang':
        return 3
    elif jabatan == 'Kepala Sub Bagian/Divisi':
        return 2
    elif jabatan == 'Staff':
        return 1
    else:
        return 0


# Title
st.title('Prediksi Kepuasan Mahasiswa')

# User input
IPK = st.number_input('IPK saat ini', value=None, placeholder="Masukkan IPK")
Jumlah_Organisasi = st.number_input('Jumlah organisasi yang diikuti', value=None,
                                    placeholder="Masukkan jumlah organisasi yang diikuti semester ini")
Jumlah_Kepanitiaan = st.number_input('Jumlah kepanitiaan yang diikuti', value=None,
                                     placeholder="Masukkan jumlah kepanitiaan yang diikuti semester ini")
Jabatan_Organisasi = st.selectbox('Jabatan tertinggi dalam organisasi', ('Ketua', 'Wakil Ketua', 'Sekretaris/Bendahara',
                                  'Kepala Bagian/Departemen/Bidang', 'Kepala Sub Bagian/Divisi', 'Staff', '-'), index=None, placeholder="Pilih salah satu")
Jabatan_Kepanitiaan = st.selectbox('Jabatan tertinggi dalam kepanitiaan', ('Ketua', 'Wakil Ketua', 'Sekretaris/Bendahara',
                                   'Kepala Bagian/Departemen/Bidang', 'Kepala Sub Bagian/Divisi', 'Staff', '-'), index=None, placeholder="Pilih salah satu")

# Map categorical values to numerical values

if IPK is not None and (IPK > 4.00 or IPK < 0.00):
    st.warning('Masukkan IPK yang valid')

mapped_ipk = map_ipk(IPK)
mapped_jabatan_org = map_jabatan(Jabatan_Organisasi)
mapped_jabatan_kep = map_jabatan(Jabatan_Kepanitiaan)


# Make prediction using the model
if mapped_ipk is not None and Jumlah_Organisasi is not None and Jumlah_Kepanitiaan is not None and Jabatan_Organisasi is not None and Jabatan_Kepanitiaan is not None:

    prediction_input = [[mapped_ipk, Jumlah_Organisasi,
                         Jumlah_Kepanitiaan, mapped_jabatan_org, mapped_jabatan_kep]]
    kepuasan = mhs_model.predict(prediction_input)[0]

    # Map Result
    if kepuasan == 4:
        kepuasan = "Sangat Tidak Puas"
    elif kepuasan == 3:
        kepuasan = "Tidak Puas"
    elif kepuasan == 2:
        kepuasan = "Puas"
    elif kepuasan == 1:
        kepuasan = "Sangat Puas"

    # Display result
    st.write('Hasil Prediksi Kepuasan Mahasiswa:', kepuasan)
