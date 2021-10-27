import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_hello_world(self):
        vastaus = str(self.kortti)
        self.assertEqual(vastaus, "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        vastaus = str(self.kortti)
        self.assertEqual(vastaus, "Kortilla on rahaa 7.5 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein_2(self):
        kortti_edu = Maksukortti(2.5)
        kortti_edu.syo_edullisesti()
        vastaus = str(kortti_edu)
        self.assertEqual(vastaus, "Kortilla on rahaa 0.0 euroa")
    
    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        vastaus = str(self.kortti)
        self.assertEqual(vastaus, "Kortilla on rahaa 6 euroa")
    
    def test_syo_maukkaasti_vahentaa_saldoa_oikein_2(self):
        kortti_maku = Maksukortti(4)
        kortti_maku.syo_maukkaasti()
        vastaus = str(kortti_maku)
        self.assertEqual(vastaus, "Kortilla on rahaa 0 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_edullisesti()
        vastaus = str(self.kortti)
        self.assertEqual(vastaus, "Kortilla on rahaa 2 euroa")
    
    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        vastaus = str(self.kortti)
        self.assertEqual(vastaus, "Kortilla on rahaa 2 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")
    
    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kortti.lataa_rahaa(-5)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")
    
    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")