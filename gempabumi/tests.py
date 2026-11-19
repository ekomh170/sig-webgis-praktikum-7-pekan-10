import io
import json
from unittest import mock

from django.core.cache import cache
from django.test import TestCase

from .views import kategori_kedalaman, olah_gempa

CONTOH = {
    "Tanggal": "17 Nov 2026", "Jam": "04:11:20 WIB",
    "DateTime": "2026-11-16T21:11:20+00:00", "Coordinates": "-6.03,131.62",
    "Lintang": "6.03 LS", "Bujur": "131.62 BT", "Magnitude": "7.1",
    "Kedalaman": "115 km", "Wilayah": "130 km BaratDaya MALUKUTENGGARA",
    "Potensi": "Tidak berpotensi tsunami",
}


class OlahDataTest(TestCase):
    def test_kategori_kedalaman(self):
        self.assertEqual(kategori_kedalaman(10), "dangkal")
        self.assertEqual(kategori_kedalaman(69), "dangkal")
        self.assertEqual(kategori_kedalaman(70), "menengah")
        self.assertEqual(kategori_kedalaman(300), "menengah")
        self.assertEqual(kategori_kedalaman(465), "dalam")

    def test_olah_gempa_mengubah_teks_menjadi_angka(self):
        g = olah_gempa(CONTOH)
        self.assertEqual((g["lat"], g["lon"]), (-6.03, 131.62))
        self.assertEqual(g["magnitude"], 7.1)
        self.assertEqual(g["kedalaman"], 115)
        self.assertEqual(g["kategori"], "menengah")


class ViewTest(TestCase):
    def setUp(self):
        cache.clear()

    @mock.patch("gempabumi.views.urllib.request.urlopen")
    def test_halaman_hanya_menampilkan_15_gempa(self, urlopen):
        isi = json.dumps({"Infogempa": {"gempa": [CONTOH] * 20}})
        urlopen.return_value.__enter__.return_value = io.StringIO(isi)
        resp = self.client.get("/gempabumi/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context["gempa"]), 15)

    @mock.patch("gempabumi.views.urllib.request.urlopen", side_effect=OSError("timeout"))
    def test_bmkg_gagal_tidak_membuat_error_500(self, urlopen):
        resp = self.client.get("/gempabumi/")
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Data BMKG gagal diambil")
