class Kendaraan:
    """
    Kelas dasar untuk semua jenis kendaraan.
    """
    def __init__(self, jumlah_roda, bahan_bakar, warna):
        self.jumlah_roda = jumlah_roda
        self.bahan_bakar = bahan_bakar
        self.warna = warna
    
    def info(self):
        return f"Kendaraan dengan {self.jumlah_roda} roda, berbahan bakar {self.bahan_bakar}, berwarna {self.warna}"
    
    def bergerak(self):
        return "Kendaraan bergerak"


class Mobil(Kendaraan):
    """
    Kelas untuk jenis kendaraan Mobil.
    """
    def __init__(self, bahan_bakar, warna, model, jumlah_pintu):
        super().__init__(4, bahan_bakar, warna)
        self.model = model
        self.jumlah_pintu = jumlah_pintu
    
    def info(self):
        return f"{super().info()}. Model: {self.model}, Jumlah pintu: {self.jumlah_pintu}"
    
    def bergerak(self):
        return "Mobil melaju di jalan raya"
    
    def klakson(self):
        return "Tin Tin!"


class Motor(Kendaraan):
    """
    Kelas untuk jenis kendaraan Motor.
    """
    def __init__(self, bahan_bakar, warna, jenis_stang, tipe_motor):
        super().__init__(2, bahan_bakar, warna)
        self.jenis_stang = jenis_stang
        self.tipe_motor = tipe_motor
    
    def info(self):
        return f"{super().info()}. Tipe: {self.tipe_motor}, Jenis stang: {self.jenis_stang}"
    
    def bergerak(self):
        return "Motor melaju dengan lincah"
    
    def wheelie(self):
        return "Motor melakukan wheelie!"


class Truk(Kendaraan):
    """
    Kelas untuk jenis kendaraan Truk.
    """
    def __init__(self, bahan_bakar, warna, muatan_maksimum, jumlah_roda=6):
        if jumlah_roda < 4:
            raise ValueError("Truk harus memiliki minimal 4 roda!")
        super().__init__(jumlah_roda, bahan_bakar, warna)
        self.muatan_maksimum = muatan_maksimum
        self.muatan_saat_ini = 0
    
    def info(self):
        return f"{super().info()}. Muatan maksimum: {self.muatan_maksimum} kg, Muatan saat ini: {self.muatan_saat_ini} kg"
    
    def bergerak(self):
        return "Truk berjalan dengan berat"
    
    def muat(self, berat):
        if berat < 0:
            return "Berat muatan tidak boleh negatif!"
        if self.muatan_saat_ini + berat <= self.muatan_maksimum:
            self.muatan_saat_ini += berat
            return f"Berhasil memuat {berat} kg. Total muatan sekarang: {self.muatan_saat_ini} kg"
        else:
            return f"Gagal memuat! Muatan akan melebihi kapasitas maksimum {self.muatan_maksimum} kg"
    
    def bongkar(self, berat):
        if berat < 0:
            return "Berat bongkar tidak boleh negatif!"
        if berat <= self.muatan_saat_ini:
            self.muatan_saat_ini -= berat
            return f"Berhasil membongkar {berat} kg. Total muatan sekarang: {self.muatan_saat_ini} kg"
        else:
            return f"Gagal membongkar! Tidak cukup muatan (muatan saat ini: {self.muatan_saat_ini} kg)"


class ManajemenKendaraan:
    """
    Kelas untuk mengelola koleksi kendaraan
    """
    def __init__(self):
        self.kendaraan = []
    
    def tambah_kendaraan(self, kendaraan):
        self.kendaraan.append(kendaraan)
        return f"{type(kendaraan).__name__} berhasil ditambahkan ke sistem"
    
    def lihat_semua_kendaraan(self):
        if not self.kendaraan:
            return "Belum ada kendaraan yang terdaftar"
        
        hasil = "=== Daftar Kendaraan ===\n"
        for idx, kendaraan in enumerate(self.kendaraan, 1):
            hasil += f"{idx}. {type(kendaraan).__name__}: {kendaraan.info()}\n"
        return hasil


def buat_mobil():
    print("\n=== Tambah Mobil Baru ===")
    bahan_bakar = input("Masukkan jenis bahan bakar: ")
    warna = input("Masukkan warna: ")
    model = input("Masukkan model mobil: ")
    
    while True:
        try:
            jumlah_pintu = int(input("Masukkan jumlah pintu: "))
            return Mobil(bahan_bakar, warna, model, jumlah_pintu)
        except ValueError:
            print("Error: Masukkan angka untuk jumlah pintu!")


def buat_motor():
    print("\n=== Tambah Motor Baru ===")
    bahan_bakar = input("Masukkan jenis bahan bakar: ")
    warna = input("Masukkan warna: ")
    jenis_stang = input("Masukkan jenis stang (standar/clip-on/dll): ")
    tipe_motor = input("Masukkan tipe motor (sport/bebek/matic/dll): ")
    
    return Motor(bahan_bakar, warna, jenis_stang, tipe_motor)


def buat_truk():
    print("\n=== Tambah Truk Baru ===")
    bahan_bakar = input("Masukkan jenis bahan bakar: ")
    warna = input("Masukkan warna: ")
    
    while True:
        try:
            muatan_maksimum = float(input("Masukkan muatan maksimum (kg): "))
            jumlah_roda = int(input("Masukkan jumlah roda (minimal 4): "))
            return Truk(bahan_bakar, warna, muatan_maksimum, jumlah_roda)
        except ValueError:
            print("Error: Masukkan angka yang valid!")


def main():
    sistem = ManajemenKendaraan()
    
    while True:
        print("\n=== MANAJEMEN KENDARAAN ===")
        print("1. Tambah Mobil")
        print("2. Tambah Motor")
        print("3. Tambah Truk")
        print("4. Lihat Semua Kendaraan")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            mobil = buat_mobil()
            print(sistem.tambah_kendaraan(mobil))
            
        elif pilihan == "2":
            motor = buat_motor()
            print(sistem.tambah_kendaraan(motor))
            
        elif pilihan == "3":
            truk = buat_truk()
            print(sistem.tambah_kendaraan(truk))
            
        elif pilihan == "4":
            print(sistem.lihat_semua_kendaraan())
            
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program!")
            break
            
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
