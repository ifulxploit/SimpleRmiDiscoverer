# SimpleRmiDiscoverer

## Deskripsi
`SimpleRmiDiscoverer` adalah alat sederhana yang dirancang untuk mengekstrak informasi JMX host:port endpoint dari RMI registry. Alat ini juga dapat memverifikasi keexploitan RCE (Remote Code Execution) tanpa menggunakan kredensial. Dengan alat ini, Anda dapat terhubung ke RMI Registry, mengekstrak endpoint, dan memeriksa kerentanannya tanpa kredensial.

## Kegunaan
Alat ini berguna untuk para red teamer dan profesional keamanan sistem untuk menilai kerentanan terhadap potensi eksploitasi RCE pada sistem yang menggunakan Java Management Extensions (JMX) melalui RMI registry.

## Analogi Program
Program ini dapat dibandingkan dengan seorang "pemburu harta karun" yang mencari tahu lokasi harta (JMX endpoint) dan memeriksa apakah harta tersebut dapat diambil tanpa kunci (kredensial).

## Cara Install
1. Pastikan Anda memiliki Python terinstal di sistem Anda.
2. Unduh atau salin kode `SimpleRmiDiscoverer.py`.
3. Simpan dalam direktori yang diinginkan.

## Cara Penggunaan
1. Buka terminal atau command prompt.
2. Pindah ke direktori tempat `SimpleRmiDiscoverer.py` disimpan.
3. Jalankan perintah:
   ```bash
   python SimpleRmiDiscoverer.py -H [IP_RMI_REGISTRY] -P [PORT_RMI_REGISTRY]
   ```
   Gantilah `[IP_RMI_REGISTRY]` dengan alamat IP RMI Registry yang ingin Anda periksa dan `[PORT_RMI_REGISTRY]` dengan port RMI Registry.

## Author
Nama: ifulxploit
Email: ifulxploit@gmail.com

**Pesan:**
> Tool ini disediakan sebagai bahan pembelajaran dan penggunaan yang etis. Harap digunakan dengan tanggung jawab dan sesuai dengan hukum yang berlaku. Penulis tidak bertanggung jawab atas penggunaan yang tidak etis atau melanggar hukum dari tool ini.
