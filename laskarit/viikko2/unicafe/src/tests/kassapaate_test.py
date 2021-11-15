import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(0)

    def test_kassapaate_luodaan_oikein(self):
        self.assertNotEqual(self.kassapaate, None)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_kassa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_syo_edullisesti_kateisella_myydyt_lounaat_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_liian_vahan_rahaa(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(takaisin, 200)

    def test_syo_maukkaasti_kateisella_kassa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_syo_maukkaasti_kateisella_myydyt_lounaat_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_liian_vahan_rahaa(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(takaisin, 300)

    def test_syo_edullisesti_kortilla_onnistuu(self):
        self.maksukortti.lataa_rahaa(1000)
        res = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(res, True)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_syo_edullisesti_kortilla_liian_vahan_rahaa(self):
        self.maksukortti.lataa_rahaa(100)
        res = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(res, False)
        self.assertEqual(self.maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_lounaiden_maara_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_lounaiden_kassa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_onnistuu(self):
        self.maksukortti.lataa_rahaa(1000)
        res = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(res, True)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_syo_maukkaasti_kortilla_liian_vahan_rahaa(self):
        self.maksukortti.lataa_rahaa(100)
        res = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(res, False)
        self.assertEqual(self.maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_lounaiden_maara_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_lounaiden_kassa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 5000)
        self.assertEqual(self.maksukortti.saldo, 5000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 105000)

    def test_lataa_rahaa_kortille_ei_lataa_jos_neg_maara(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -5000)
        self.assertEqual(self.maksukortti.saldo, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
