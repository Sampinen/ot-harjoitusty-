import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 500)
    
    def test_palauta_true_jos_tarpeeksi_saldoa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500),True)
    def test_saldo_ei_vahene_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_palauta_false_jos__ei_tarpeeksi_saldoa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500),False)