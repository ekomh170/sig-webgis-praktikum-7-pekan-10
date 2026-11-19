from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("<h1>Selamat Datang di Situs Kami !</h1>")


# Daftar halaman untuk beranda (alamat "/"), urut sesuai modul.
HALAMAN = [
    {"url": "/welcome/", "judul": "Welcome",
     "isi": "Teks sambutan langsung dari view (HttpResponse)."},
    {"url": "/petasatu/", "judul": "Peta Indonesia",
     "isi": "Peta Leaflet dengan marker Jakarta."},
    {"url": "/petadua/", "judul": "Latihan Mandiri 1: Peta Jabodetabek",
     "isi": "Lima kota dengan panel pilih kota dan kepadatan penduduk."},
    {"url": "/gempabumi/", "judul": "Latihan Mandiri 2: Gempa Terkini BMKG",
     "isi": "15 gempa M 5.0+ terkini dari BMKG di peta."},
    {"url": "/gempabumi/api/", "judul": "API Gempa (JSON)",
     "isi": "Data gempa yang sudah diolah, dalam format JSON."},
]


def beranda(request):
    return render(request, "petaindonesia/beranda.html", {"halaman": HALAMAN})

# Create your views here.
