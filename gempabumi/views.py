import json
import urllib.request

from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

JUMLAH_GEMPA = 15          # jumlah gempa yang ditampilkan
CACHE_KEY = "bmkg_gempaterkini"
CACHE_DETIK = 60           # cache 60 detik (batas BMKG: 60 req/menit)


def kategori_kedalaman(km):
    """Klasifikasi kedalaman hiposenter yang dipakai BMKG."""
    if km < 70:
        return "dangkal"
    if km <= 300:
        return "menengah"
    return "dalam"


def olah_gempa(item):
    """Ubah satu objek gempa BMKG (semua nilai teks) menjadi data siap pakai."""
    lat, lon = (float(x) for x in item["Coordinates"].split(","))
    kedalaman = int(item["Kedalaman"].split()[0])      # "115 km" -> 115
    return {
        "tanggal": item["Tanggal"],
        "jam": item["Jam"],
        "datetime": item["DateTime"],
        "lat": lat,
        "lon": lon,
        "lintang": item["Lintang"],
        "bujur": item["Bujur"],
        "magnitude": float(item["Magnitude"]),
        "kedalaman": kedalaman,
        "kategori": kategori_kedalaman(kedalaman),
        "wilayah": item["Wilayah"],
        "potensi": item.get("Potensi", "-"),
    }


def ambil_data_bmkg():
    """Ambil 15 gempa terakhir dari BMKG. Hasil disimpan di cache 60 detik."""
    data = cache.get(CACHE_KEY)
    if data is not None:
        return data

    req = urllib.request.Request(settings.BMKG_GEMPA_URL,
                                 headers={"User-Agent": "webumkm-webgis/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        mentah = json.load(resp)

    daftar = mentah["Infogempa"]["gempa"][:JUMLAH_GEMPA]
    data = {
        "gempa": [olah_gempa(g) for g in daftar],
        "diambil": timezone.localtime().strftime("%H.%M.%S"),
    }
    cache.set(CACHE_KEY, data, CACHE_DETIK)
    return data


def gempaterkini(request):
    try:
        data = ambil_data_bmkg()
        error = None
    except Exception as e:  # jaringan putus, BMKG down, format berubah
        data = {"gempa": [], "diambil": "-"}
        error = f"Data BMKG gagal diambil: {e}"
    context = {
        "gempa": data["gempa"],
        "diambil": data["diambil"],
        "jumlah": len(data["gempa"]),
        "error": error,
    }
    return render(request, "gempabumi/gempaterkini.html", context)


def api_gempaterkini(request):
    """Endpoint JSON untuk tombol 'Muat ulang' (dipanggil lewat fetch)."""
    if request.GET.get("segar"):
        cache.delete(CACHE_KEY)
    try:
        return JsonResponse(ambil_data_bmkg())
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=502)
