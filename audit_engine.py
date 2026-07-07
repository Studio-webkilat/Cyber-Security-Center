import subprocess
import json
import os

def run_audit(target):
    print(f"[*] Memulai audit terhadap: {target}")
    
    # Menjalankan nuclei dan menyimpan output ke file scan_result.json
    output_file = "scan_result.json"
    cmd = ["nuclei", "-target", target, "-json", "-o", output_file]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"[+] Audit selesai. Hasil disimpan di {output_file}")
        
        # Membaca hasil untuk dihitung skornya
        with open(output_file, 'r') as f:
            findings = [json.loads(line) for line in f]
        
        return findings
    except Exception as e:
        print(f"[!] Terjadi kesalahan: {e}")
        return []

# Contoh penggunaan (Uji coba pada domain target)
# target_input = input("Masukkan URL target: ")
# hasil = run_audit(target_input)

