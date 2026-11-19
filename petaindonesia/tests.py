from django.test import TestCase


class HalamanPetaTest(TestCase):
    def test_beranda_menautkan_semua_halaman(self):
        resp = self.client.get("/")
        self.assertTemplateUsed(resp, "petaindonesia/beranda.html")
        for url in ["/welcome/", "/petasatu/", "/petadua/", "/gempabumi/", "/gempabumi/api/"]:
            self.assertContains(resp, f'href="{url}"')

    def test_welcome(self):
        resp = self.client.get("/welcome/")
        self.assertContains(resp, "Selamat Datang di Situs Kami !")

    def test_petasatu_memakai_template(self):
        resp = self.client.get("/petasatu/")
        self.assertTemplateUsed(resp, "petaindonesia/petasatu.html")

    def test_petadua_mengirim_lima_kota(self):
        resp = self.client.get("/petadua/")
        self.assertEqual(len(resp.context["kota"]), 5)
        self.assertContains(resp, 'id="data-kota"')

    def test_referrer_policy_untuk_tile_osm(self):
        resp = self.client.get("/petasatu/")
        self.assertEqual(resp["Referrer-Policy"], "strict-origin-when-cross-origin")
