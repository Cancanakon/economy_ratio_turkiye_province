import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from design import Ui_IS
import  sqlite3

baglan  = sqlite3.connect("data.db")

if baglan:
    print("data bağlandı!")
else:
    print("data bağlanmadı!")


class strt(QMainWindow):
    def __init__(self):
        super().__init__()

        # QWidget.__init__(self)
        self.ui =Ui_IS()
        self.ui.setupUi(self)

        self.ui.btn_Getir.clicked.connect(self.araClicked)
        self.ui.btn_Hesapla.clicked.connect(self.btnHesaplaClicked)

    def araClicked(self):
        cameCity =self.ui.cbox_sehir.currentIndex()
        nameCity = self.ui.cbox_sehir.currentText()
        selectedCity =str(cameCity +1)
        print(f"Şehir Numarası: {selectedCity}")
        veri = baglan.cursor()
        getir = veri.execute('SELECT * FROM ilveilce WHERE il_no=' + selectedCity + '')

        # getir = veri.execute('SELECT * FROM ilveilce WHERE il_no=(?)',(selectedCity))
        gelen = getir.fetchall()
        print(gelen)
        cameCity= int(selectedCity)
        baglan.commit()

        for i in gelen:
            print(i)
        print(i[1])
        nufus= str(i[1])
        katki= str(i[2])
        gelirYuzde= str(i[3])
        self.ui.lbl_katkiyuzde.setText(f"%{gelirYuzde}")
        self.ui.lbl_nufus.setText(nufus)
        self.ui.lbl_katki.setText(f"{katki} $")
        self.ui.lbl_sehir.setText(nameCity)
        self.ui.pb_katki.setValue(int(i[3]*3.5))
        nufusPb=int(i[1]/78000000*100)
        self.ui.pb_nufus.setValue(nufusPb*2)
        gelir= int(int(katki)/int(nufus))
        gelirHesapli = str(gelir)
        self.ui.lbl_gelir.setText(f"{gelirHesapli} $")

    def btnHesaplaClicked(self):
        gelenGelir = self.ui.edt_Gelir.text()
        gelenNufus = self.ui.edt_nufus.text()
        cgelenGelir = int(gelenGelir)
        cgelenNufus = int(gelenNufus)
        sonuc = int(cgelenGelir / cgelenNufus)
        sonucDon = str(sonuc)
        self.ui.lbl_manGelir.setText(f"{sonucDon} $ ")

uyg = QApplication([])
pen= strt()
pen.show()
uyg.exec_()