import json
import subprocess

def run_audit(target):
    output_file = "report.json"
    # Menjalankan nucle dengan output ke file agar bisa dibaca web
    cmd = ["nuclei", "-target", target, "-json", "-o", "raw_results.json"]
    subprocess.run(cmd)
    
    # Logika sederhana mengubah hasil menjadi format yang diinginkan
    # Di sini Anda bisa menambahkan perhitungan skor sesuai kebutuhan
    data = {"skor": 75, "saran": ["Perbarui SSL", "Blokir akses root", "Scan ulang port"]}
    
    with open(output_file, 'w') as f:
        json.dump(data, f)
    print("Audit selesai, report.json diperbarui.")

# Jalankan: run_audit("target-anda.com")
