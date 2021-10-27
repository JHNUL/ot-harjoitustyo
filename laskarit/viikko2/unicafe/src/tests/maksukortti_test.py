import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_alussa_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")
    
    def test_kortilta_voi_ottaa_rahaa(self):
        res = self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
        self.assertEqual(res, True)
    
    def test_kortilta_ei_voi_ottaa_rahaa_jos_ei_riita(self):
        res = self.maksukortti.ota_rahaa(15)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        self.assertEqual(res, False)