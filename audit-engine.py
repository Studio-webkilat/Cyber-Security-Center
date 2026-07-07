import json
import subprocess

def run_audit(target):
    # Simulasi hasil scan Nuclei
    data = {"skor": 75, "saran": ["Update Library X", "Aktifkan HTTPS", "Tutup Port 23"]}
    with open('report.json', 'w') as f:
        json.dump(data, f)
    print("Audit selesai. report.json diperbarui.")

if __name__ == "__main__":
    run_audit("target-anda.com")

