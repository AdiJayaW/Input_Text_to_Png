from PIL import Image
from PIL.PngImagePlugin import PngInfo
import os

def sembunyikan_metadata_interaktif():
    print("=== Alat Penyisip Teks Rahasia ke PNG ===")
    
    # 1. Meminta user memasukkan nama file gambar asli
    file_input = input("Masukkan nama file gambar sumber (contoh: gambar.png): ")
    
    # Mengecek apakah file gambar tersebut benar-benar ada
    if not os.path.exists(file_input):
        print("Error: File gambar tidak ditemukan! Pastikan nama dan lokasinya benar.")
        return # Menghentikan program jika file tidak ada

    # 2. Meminta user memasukkan nama file output
    file_output = input("Masukkan nama untuk file gambar hasil (contoh: rahasia.png): ")
    
    # 3. Meminta user menginputkan teks rahasia mereka sendiri
    print("\n--- Masukkan Data Rahasia ---")
    prompt_user = input("Ketikkan Prompt      : ")
    referensi_user = input("Ketikkan Referensi   : ")
    
    try:
        # Proses membuka gambar dan menyiapkan metadata
        gambar = Image.open(file_input)
        metadata = PngInfo()
        
        # Menyisipkan inputan user ke dalam metadata PNG
        metadata.add_text("Prompt", prompt_user)
        metadata.add_text("Referensi", referensi_user)
        
        # Menyimpan gambar dengan metadata baru
        gambar.save(file_output, pnginfo=metadata)
        
        print("\n[+] SUKSES!")
        print(f"Data rahasia milikmu berhasil disembunyikan di dalam file '{file_output}'.")
        
    except Exception as e:
        print(f"\n[-] Terjadi kesalahan saat memproses gambar: {e}")

# Menjalankan fungsi
if __name__ == "__main__":
    sembunyikan_metadata_interaktif()