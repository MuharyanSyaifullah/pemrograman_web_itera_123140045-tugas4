data_mahasiswa = [
    {
        'nama': 'Budi Santoso',
        'NIM': '119140001',
        'nilai_uts': 85,
        'nilai_uas': 90,
        'nilai_tugas': 88
    },
    {
        'nama': 'Ani Lestari',
        'NIM': '119140002',
        'nilai_uts': 78,
        'nilai_uas': 70,
        'nilai_tugas': 80
    },
    {
        'nama': 'Candra Wijaya',
        'NIM': '119140003',
        'nilai_uts': 50,
        'nilai_uas': 65,
        'nilai_tugas': 55
    },
    {
        'nama': 'Dewi Anggraini',
        'NIM': '119140004',
        'nilai_uts': 92,
        'nilai_uas': 88,
        'nilai_tugas': 95
    },
    {
        'nama': 'Eka Kurniawan',
        'NIM': '119140005',
        'nilai_uts': 60,
        'nilai_uas': 45,
        'nilai_tugas': 70
    }
]

# --- Fungsi-Fungsi ---

def hitung_nilai_akhir(uts, uas, tugas):
    """
    Fungsi untuk menghitung nilai akhir berdasarkan bobot.
    (30% UTS + 40% UAS + 30% Tugas)
    """
    return (0.30 * uts) + (0.40 * uas) + (0.30 * tugas)

def tentukan_grade(nilai_akhir):
    """
    Fungsi untuk menentukan grade berdasarkan nilai akhir.
    (A: ≥80, B: ≥70, C: ≥60, D: ≥50, E: <50)
    """
    if nilai_akhir >= 80:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'

def update_data_lengkap(data_list):
    """
    Fungsi helper untuk melengkapi setiap dictionary mahasiswa
    dengan 'nilai_akhir' dan 'grade'.
    """
    for mhs in data_list:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        mhs['nilai_akhir'] = round(nilai_akhir, 2)
        mhs['grade'] = tentukan_grade(nilai_akhir)
    return data_list

def tampilkan_data(data_list):
    """
    Fungsi untuk menampilkan data dalam format tabel.
    """
    # Pastikan data sudah memiliki 'nilai_akhir' dan 'grade'
    data_list = update_data_lengkap(data_list)
    
    if not data_list:
        print("Tidak ada data untuk ditampilkan.")
        return

    print("\n" + "=" * 84)
    print(f"| {'No':<3} | {'Nama':<20} | {'NIM':<10} | {'UTS':>5} | {'UAS':>5} | {'Tugas':>5} | {'Akhir':>6} | {'Grade':>5} |")
    print("=" * 84)
    
    for i, mhs in enumerate(data_list):
        print(f"| {i+1:<3} | {mhs['nama']:<20} | {mhs['NIM']:<10} | {mhs['nilai_uts']:>5} | {mhs['nilai_uas']:>5} | {mhs['nilai_tugas']:>5} | {mhs['nilai_akhir']:>6.2f} | {mhs['grade']:>5} |")
    
    print("-" * 84)

def cari_nilai_tertinggi_terendah(data_list):
    """
    Fungsi untuk mencari mahasiswa dengan nilai akhir tertinggi dan terendah.
    """
    if not data_list:
        print("Data kosong, tidak bisa mencari nilai.")
        return
    
    data_list = update_data_lengkap(data_list)
    
    tertinggi = max(data_list, key=lambda mhs: mhs['nilai_akhir'])
    terendah = min(data_list, key=lambda mhs: mhs['nilai_akhir'])
    
    print("\n--- Nilai Tertinggi ---")
    print(f"Nama  : {tertinggi['nama']}")
    print(f"NIM   : {tertinggi['NIM']}")
    print(f"Nilai : {tertinggi['nilai_akhir']} (Grade {tertinggi['grade']})")
    
    print("\n--- Nilai Terendah ---")
    print(f"Nama  : {terendah['nama']}")
    print(f"NIM   : {terendah['NIM']}")
    print(f"Nilai : {terendah['nilai_akhir']} (Grade {terendah['grade']})")

# --- Fitur Tambahan ---

def input_data_mahasiswa_baru(data_list):
    """
    Fungsi untuk menerima input data mahasiswa baru dan menambahkannya ke list.
    """
    print("\n--- Input Data Mahasiswa Baru ---")
    try:
        nama = input("Nama: ")
        nim = input("NIM: ")
        
        # Validasi input nilai harus berupa angka
        uts = int(input("Nilai UTS: "))
        uas = int(input("Nilai UAS: "))
        tugas = int(input("Nilai Tugas: "))
        
        mahasiswa_baru = {
            'nama': nama,
            'NIM': nim,
            'nilai_uts': uts,
            'nilai_uas': uas,
            'nilai_tugas': tugas
        }
        data_list.append(mahasiswa_baru)
        print("\nData mahasiswa baru berhasil ditambahkan!")
    
    except ValueError:
        print("\nInput nilai tidak valid. Harap masukkan angka. Data tidak tersimpan.")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}. Data tidak tersimpan.")
    
    return data_list

def filter_berdasarkan_grade(data_list):
    """
    Fungsi untuk memfilter dan menampilkan mahasiswa berdasarkan grade.
    """
    if not data_list:
        print("Data kosong.")
        return
        
    grade_dicari = input("Masukkan Grade yang dicari (A/B/C/D/E): ").upper()
    
    if grade_dicari not in ['A', 'B', 'C', 'D', 'E']:
        print("Grade tidak valid. Harap masukkan A, B, C, D, atau E.")
        return

    data_list = update_data_lengkap(data_list)
    
    # Gunakan list comprehension untuk memfilter data
    hasil_filter = [mhs for mhs in data_list if mhs['grade'] == grade_dicari]
    
    if not hasil_filter:
        print(f"\nTidak ada mahasiswa dengan grade {grade_dicari}.")
    else:
        print(f"\n--- Mahasiswa dengan Grade {grade_dicari} ---")
        tampilkan_data(hasil_filter)

def hitung_rata_rata_kelas(data_list):
    """
    Fungsi untuk menghitung rata-rata nilai akhir seluruh kelas.
    """
    if not data_list:
        print("Data kosong, tidak bisa menghitung rata-rata.")
        return
        
    data_list = update_data_lengkap(data_list)
    
    # Gunakan generator expression dalam sum() untuk efisiensi
    total_nilai = sum(mhs['nilai_akhir'] for mhs in data_list)
    rata_rata = total_nilai / len(data_list)
    
    print(f"\nRata-rata nilai akhir kelas: {rata_rata:.2f}")

# --- Fungsi Utama (Menu) ---

def tampilkan_menu():
    """Menampilkan menu utama program."""
    print("\n" + "=" * 40)
    print("   Program Pengelolaan Data Nilai   ")
    print("=" * 40)
    print("1. Tampilkan Semua Data Mahasiswa")
    print("2. Tambah Data Mahasiswa Baru")
    print("3. Cari Nilai Tertinggi dan Terendah")
    print("4. Filter Mahasiswa Berdasarkan Grade")
    print("5. Hitung Rata-rata Nilai Kelas")
    print("0. Keluar")
    print("-" * 40)
    return input("Pilih menu (0-5): ")

def main():
    """
    Fungsi utama untuk menjalankan program.
    """
    # Menggunakan 'data_mahasiswa' dari scope global
    list_data = data_mahasiswa.copy() 

    while True:
        pilihan = tampilkan_menu()
        
        if pilihan == '1':
            tampilkan_data(list_data)
        elif pilihan == '2':
            list_data = input_data_mahasiswa_baru(list_data)
        elif pilihan == '3':
            cari_nilai_tertinggi_terendah(list_data)
        elif pilihan == '4':
            filter_berdasarkan_grade(list_data)
        elif pilihan == '5':
            hitung_rata_rata_kelas(list_data)
        elif pilihan == '0':
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("\nPilihan tidak valid. Silakan masukkan angka 0 sampai 5.")

# --- Titik Masuk Program ---
if __name__ == "__main__":
    main()