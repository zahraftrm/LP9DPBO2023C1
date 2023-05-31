from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas, lokasi):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, luas)
        self.nama_pemilik = nama_pemilik
        self.lokasi = lokasi

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    # memberi method baru, yaitu method lokasi
    def get_lokasi(self):
        return self.lokasi
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nLuas Apartement : " + str(self.luas) + "\nLokasi Apartement : " + str(self.lokasi) + "\n"