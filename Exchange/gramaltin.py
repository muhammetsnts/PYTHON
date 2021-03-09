import sys
from PyQt5 import QtGui

import requests
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QPushButton,QApplication,QWidget,QLineEdit,QLabel
from bs4 import BeautifulSoup
from PyQt5.QtGui import QIcon

class Investing(QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.tryusd=QLabel("TRY-USD")
        self.trygbp=QLabel("TRY-GBP")
        self.tryeur=QLabel("TRY-EUR")
        self.eurusd=QLabel("EUR-USD")
        self.altin=QLabel("GRAM ALTIN")

        self.cevap1=QLineEdit()
        self.cevap2=QLineEdit()
        self.cevap3=QLineEdit()
        self.cevap4=QLineEdit()
        self.cevap5=QLineEdit()
        self.cevap1.setFixedSize(130, 20)
        self.cevap2.setFixedSize(130, 20)
        self.cevap3.setFixedSize(130, 20)
        self.cevap4.setFixedSize(130, 20)
        self.cevap5.setFixedSize(130, 20)

        self.getir=QPushButton("YENİLE")

        h_box1=QHBoxLayout()
        h_box1.addWidget(self.tryusd)
        h_box1.addWidget(self.cevap1)

        h_box2=QHBoxLayout()
        h_box2.addWidget(self.trygbp)
        h_box2.addWidget(self.cevap2)

        h_box3=QHBoxLayout()
        h_box3.addWidget(self.tryeur)
        h_box3.addWidget(self.cevap3)

        h_box4 = QHBoxLayout()
        h_box4.addWidget(self.eurusd)
        h_box4.addWidget(self.cevap4)

        h_box5 = QHBoxLayout()
        h_box5.addWidget(self.altin)
        h_box5.addWidget(self.cevap5)

        v_box=QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)
        v_box.addWidget(self.getir)

        self.setLayout(v_box)
        self.bul()
        self.getir.clicked.connect(self.bul)

        self.setWindowTitle("DÖVİZ")
        self.setWindowIcon(QIcon("logo.png"))
        self.show()

    def bul(self):

        try:
            url = "https://yorumlar.altin.in/tum/gram-altin"
            response = requests.get(url)
            html_içeriği = response.content
            soup = BeautifulSoup(html_içeriği, "html.parser")
            dolar = soup.find_all("h2", {"id": "dfiy"})
            self.cevap1.setText(dolar[0].text)
            sterlin= soup.find_all("h2", {"id": "sfiy"})
            self.cevap2.setText(sterlin[0].text)
            euro=soup.find_all("h2", {"id": "efiy"})
            self.cevap3.setText(euro[0].text)
            parite=soup.find_all("h2", {"id": "pfiy"})
            self.cevap4.setText(parite[0].text)
            altin=soup.find_all("li",{"class": "midrow satis"})
            self.cevap5.setText(altin[0].text)

        except:

            self.getir.setText("Lütfen bağlantınızı kontrol edip tekrar deneyiniz!")


app=QApplication(sys.argv)
investing=Investing()
sys.exit(app.exec_())