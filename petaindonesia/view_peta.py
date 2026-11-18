from django.shortcuts import render
from django.http import HttpResponse

# Titik pusat kota Jabodetabek. Koordinat dan atribut sama dengan dataset
# jabotabek.geojson pada Praktikum 5 (estimasi BPS pertengahan 2024).
KOTA_JABODETABEK = [
    {"nama": "Jakarta", "lat": -6.17539, "lon": 106.82711,
     "keterangan": "Provinsi DKI Jakarta (titik: Monas)",
     "populasi": 10684946, "luas": 661.53},
    {"nama": "Bogor", "lat": -6.59667, "lon": 106.79722,
     "keterangan": "Kota Bogor", "populasi": 1078351, "luas": 111.37},
    {"nama": "Depok", "lat": -6.39389, "lon": 106.82250,
     "keterangan": "Kota Depok", "populasi": 2163635, "luas": 199.91},
    {"nama": "Tangerang", "lat": -6.17028, "lon": 106.64028,
     "keterangan": "Kota Tangerang", "populasi": 1927815, "luas": 164.55},
    {"nama": "Bekasi", "lat": -6.23500, "lon": 106.99222,
     "keterangan": "Kota Bekasi", "populasi": 2644058, "luas": 213.04},
]


def petasatu(request):
    return render(request, 'petaindonesia/petasatu.html')


def petadua(request):
    # Kepadatan dihitung di view (logika), template cukup menampilkan.
    kota = []
    for k in KOTA_JABODETABEK:
        kota.append({**k, "kepadatan": round(k["populasi"] / k["luas"])})
    context = {
        "judul": "Peta Jabodetabek: Jakarta, Bogor, Depok, Tangerang, Bekasi",
        "kota": kota,
    }
    return render(request, 'petaindonesia/petadua.html', context)
