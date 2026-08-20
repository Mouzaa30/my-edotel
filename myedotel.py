# ==============================================================================
# PROYEK INTEGRASI (CHALLENGE): SISTEM MANAJEMEN KAMAR HOTEL "MYEDOTEL"
# Kelompok / Berpasangan Sebangku
# ==============================================================================

from abc import ABC, abstractmethod

# ==============================================================================
# 1. ABSTRACTION & ENCAPSULATION (Parent Class)
# ==============================================================================
class KamarHotel(ABC):
    def __init__(self, nama_kamar, stok, harga_dasar):
        self.nama_kamar = nama_kamar
        # Encapsulation: Menggunakan private attribute untuk melindungi data sensitif
        self.__stok = 0
        self.__harga_dasar = harga_dasar
        
        # Validasi stok awal saat objek pertama kali dibuat
        self.tambah_stok(stok)

    # Getter untuk mengakses nilai privat __harga_dasar dari luar atau class anak
    def get_harga_dasar(self):
        return self.__harga_dasar

    # Getter untuk mengakses nilai privat __stok
    def get_stok(self):
        return self.__stok

    # Setter / Method untuk mengubah data __stok dengan validasi ketat
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama_kamar}! Stok tidak boleh negatif ({jumlah}).")
            return False
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama_kamar}: {jumlah} unit.")
            return True

    # Abstract Method yang WAJIB di-override oleh seluruh class anak
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah_malam):
        pass


# ==============================================================================
# 2. INHERITANCE & POLYMORPHISM (Child Classes)
# ==============================================================================
class KamarDeluxe(KamarHotel):
    def __init__(self, nama_kamar, stok, harga_dasar, fasilitas):
        # Memanggil constructor dari Parent Class (KamarHotel)
        super().__init__(nama_kamar, stok, harga_dasar)
        self.fasilitas = fasilitas  # Atribut unik untuk tipe Kamar Deluxe

    # Polymorphism: Override method tampilkan_detail khusus tipe Deluxe
    def tampilkan_detail(self):
        pajak = self.get_harga_dasar() * 0.10
        print(f"[DELUXE] {self.nama_kamar} | Fasilitas: {self.fasilitas}")
        print(f"Harga Dasar/Malam: Rp {self.get_harga_dasar():,} | Pajak(10%): Rp {pajak:,.0f}")

    # Polymorphism: Override perhitungan harga total + Pajak 10%
    def hitung_harga_total(self, jumlah_malam):
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * 0.10
        subtotal = (harga_dasar + pajak) * jumlah_malam
        return int(subtotal)


class KamarStandard(KamarHotel):
    def __init__(self, nama_kamar, stok, harga_dasar, kapasitas):
        # Memanggil constructor dari Parent Class (KamarHotel)
        super().__init__(nama_kamar, stok, harga_dasar)
        self.kapasitas = kapasitas  # Atribut unik untuk tipe Kamar Standard

    # Polymorphism: Override method tampilkan_detail khusus tipe Standard
    def tampilkan_detail(self):
        pajak = self.get_harga_dasar() * 0.05
        print(f"[STANDARD] {self.nama_kamar} | Kapasitas: {self.kapasitas}")
        print(f"Harga Dasar/Malam: Rp {self.get_harga_dasar():,} | Pajak(5%): Rp {pajak:,.0f}")

    # Polymorphism: Override perhitungan harga total + Pajak 5%
    def hitung_harga_total(self, jumlah_malam):
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * 0.05
        subtotal = (harga_dasar + pajak) * jumlah_malam
        return int(subtotal)


# ==============================================================================
# 3. FITUR PEMESANAN (Polymorphism Function)
# ==============================================================================
def proses_transaksi(daftar_pesanan):
    print("--- STRUK PEMESANAN ---")
    total_tagihan = 0
    
    # Memproses daftar pesanan yang berisi tuple: (objek_kamar, jumlah_malam)
    for index, (kamar, malam) in enumerate(daftar_pesanan, start=1):
        print(f"{index}. ", end="")
        kamar.tampilkan_detail()
        
        subtotal = kamar.hitung_harga_total(malam)
        total_tagihan += subtotal
        print(f"Menginap: {malam} malam | Subtotal: Rp {subtotal:,}")
        
    print("-" * 40)
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,}")
    print("-" * 40)


# ==============================================================================
# 4. ALUR PROGRAM UTAMA (User Story)
# ==============================================================================
if __name__ == "__main__":
    print("--- SETUP DATA KAMAR ---")
    
    # a) Admin membuat data kamar Deluxe (stok awal langsung diisi 10)
    kamar_1 = KamarDeluxe("Kamar Deluxe Sea View", 10, 1500000, "Private Pool")
    
    # b) Admin membuat data kamar Standard dengan stok awal 0
    kamar_2 = KamarStandard("Kamar Standard Superior", 0, 500000, "2 Orang")
    
    # Admin MENCOBA mengisi stok kamar dengan angka negatif (Sistem menolak otomatis)
    kamar_2.tambah_stok(-5)
    
    # Admin menginput kembali dengan nilai stok yang valid
    kamar_2.tambah_stok(20)
    print()
    
    # c) Tamu memesan 2 malam Kamar Deluxe dan 1 malam Kamar Standard
    # Menyimpan pesanan dalam list (Polymorphism: mencampur tipe object berbeda dalam satu list)
    keranjang_pesanan = [
        (kamar_1, 2),
        (kamar_2, 1)
    ]
    
    # d) Menampilkan detail cetak struk kamar dan akumulasi total tagihan akhir
    proses_transaksi(keranjang_pesanan)