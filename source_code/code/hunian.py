class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, luas = 0):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.luas = luas

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    # memberi method baru, yaitu method luas
    def get_luas(self):
        return self.luas

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang."