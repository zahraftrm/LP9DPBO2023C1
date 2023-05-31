from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas, lokasi):
        super().__init__("Rumah", jml_penghuni, jml_kamar, luas)
        self.nama_pemilik = nama_pemilik
        self.lokasi = lokasi

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    # memberi method baru, yaitu method lokasi
    def get_lokasi(self):
        return self.lokasi
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nLuas Bangunan : " + str(self.luas) + "\nLokasi rumah : " + str(self.lokasi) + "\n"
   