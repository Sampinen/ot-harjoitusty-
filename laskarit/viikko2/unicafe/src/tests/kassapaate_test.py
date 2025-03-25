import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000.0)
    
    def test_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.syodyt_lounaat(),0)
    
    def test_syo_edullisesti_kateisella_lisaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1002.4)
    
    def test_syo_edullisesti_ei_toimi_jos_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)
    def test_syo_maukkaasti_kateisella_lisaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1004.0)
    def test_syo_maukkasti_kateisella_ei_toimi_jos_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)    

    def test_edullinen_korttiosto_toimii_oikein(self):

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),True)  
    
    def test_maukas_korttiosto_toimii_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),True) 
    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_maara_ei_muutu_ostaessa_maukkaan_annoksen(self):
                self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(10)),False)
    
    def test_jos_kortilla_on_tarpeeksi_rahaa_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syodyt_lounaat(),1)  
    
    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(10))
        self.assertEqual(self.kassapaate.syodyt_lounaat(),0)  
    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_palauta_false(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(10)),False)
    
    def test_kassassa_oleva_rahamaara_ei_muutu_kortilla_ostettaessa(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(10))
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,100)
        self.assertEqual(self.maksukortti.saldo_euroina(),11.0)
    
    def test_kortille_rahaa_ladatessa_kassassa_oleva_rahamaara_kasvaa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1001.0)
    
    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)
    