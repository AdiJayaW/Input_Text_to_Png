from PIL import Image
import os

def ekspor_otomatis_ke_notepad():
    print("=== Alat Ekspor Data Rahasia PNG Otomatis ===")
    
    # 1. User CUKUP memasukkan nama gambar saja
    file_gambar = input("Masukkan nama file gambar PNG (contoh: rahasia.png): ")
    
    if not os.path.exists(file_gambar):
        print("[-] Error: File gambar tidak ditemukan!")
        return
        
    try:
        gambar = Image.open(file_gambar)
        
        # Mengecek apakah gambar memiliki metadata
        if gambar.info:
            
            # 2. Membuat nama file .txt secara otomatis berdasarkan nama gambar
            # Contoh: "rahasia.png" akan dipecah menjadi "rahasia" dan otomatis ditambah ".txt"
            nama_asli = os.path.splitext(file_gambar)[0]
            file_output = f"{nama_asli}.txt"
            
            # 3. Proses menulis data ke file .txt dengan jarak
            with open(file_output, 'w', encoding='utf-8') as f:
                f.write("=====================================\n")
                f.write("      HASIL EKSTRAKSI DATA PNG       \n")
                f.write("=====================================\n")
                f.write(f"Nama File Sumber: {file_gambar}\n\n")
                
                # Menulis data secara spesifik agar rapi dan berjarak
                # Jika metadata Prompt ada, tulis dengan jarak
                if "Prompt" in gambar.info:
                    f.write("--- PROMPT ---\n")
                    f.write(f"{gambar.info['Prompt']}\n\n") # \n\n memberikan jarak baris kosong
                    
                # Jika metadata Referensi ada, tulis di bawahnya
                if "Referensi" in gambar.info:
                    f.write("--- REFERENSI ---\n")
                    f.write(f"{gambar.info['Referensi']}\n\n")
                    
                # Mengambil sisa metadata lain (jika ada flag, dll)
                for key, value in gambar.info.items():
                    if key not in ["Prompt", "Referensi"]:
                        f.write(f"--- {key.upper()} ---\n")
                        f.write(f"{value}\n\n")
                    
                f.write("=====================================\n")
            
            print(f"\n[+] BERHASIL!")
            print(f"Data diekstraksi dan otomatis disimpan sebagai '{file_output}'.")
            
        else:
            print("\n[-] Gagal: Tidak ada data teks rahasia di dalam gambar ini.")
            
    except Exception as e:
        print(f"\n[-] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    ekspor_otomatis_ke_notepad()