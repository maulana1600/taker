# Bot Aktivasi Miner Taker Protocol (Modifikasi dengan API)

Bot Python untuk mengotomatiskan interaksi dengan Taker Protocol. Bot ini menggunakan kombinasi panggilan API off-chain (untuk login, mendapatkan status mining, dan memulai/mengkonfirmasi mining) dan transaksi on-chain (untuk fungsi `active()`) untuk beberapa wallet.

**PERINGATAN KERAS / DISCLAIMER:**
* **GUNAKAN DENGAN RISIKO ANDA SENDIRI.** Skrip ini berinteraksi dengan private key, API eksternal, dan transaksi blockchain. Pastikan Anda memahami cara kerjanya.
* **KEAMANAN PRIVATE KEY SANGAT PENTING.** Jangan pernah membagikan file `private_keys.txt` Anda atau private key Anda kepada siapa pun. Simpan file tersebut dengan aman. Sebaiknya gunakan wallet baru khusus untuk bot ini dengan dana secukupnya hanya untuk gas fee.
* Penulis tidak bertanggung jawab atas kehilangan dana atau masalah lain yang mungkin timbul dari penggunaan skrip ini.

## Fitur
* Login ke API Taker Protocol menggunakan penandatanganan pesan.
* Mengecek status/waktu aktivasi miner terakhir melalui API.
* Melakukan transaksi on-chain `active()` jika diperlukan.
* Melakukan panggilan API off-chain `startMining` untuk aktivasi awal atau setelah reaktivasi on-chain.
* Mendukung multi-wallet dari file `private_keys.txt`.
* Interval aktivasi per wallet sekitar 24 jam.
* Jeda antar pemrosesan wallet yang berbeda.

## Prasyarat
* Python 3.7+
* Pip (Python package installer)

## Setup & Instalasi

1.  **Clone atau Unduh Repositori:**
    Jika Anda sudah membuat repositori di GitHub, clone:
    ```bash
    git clone [URL_REPO_ANDA_DARI_GITHUB.git]
    cd nama-direktori-repo-anda
    ```
    Jika belum, buat direktori baru dan salin file `taker_bot.py`, `requirements.txt`, dan `.gitignore` ke dalamnya.

2.  **Buat Virtual Environment (Sangat Direkomendasikan):**
    ```bash
    python3 -m venv venv
    ```
    Aktifkan virtual environment:
    * Windows: `venv\Scripts\activate`
    * macOS/Linux: `source venv/bin/activate`

3.  **Install Dependencies:**
    Pastikan Anda memiliki file `requirements.txt` dengan konten yang sudah diperbarui.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Buat File Private Keys:**
    * Buat file bernama `private_keys.txt` di direktori yang sama dengan `taker_bot.py`.
    * Masukkan private key Anda ke dalam file ini, **satu private key per baris**. Pastikan setiap private key diawali dengan `0x` dan memiliki panjang 66 karakter.
        ```
        0xPRIVATEKEYWALLET1................
        0xPRIVATEKEYWALLET2................
        ```
    * **JANGAN UNGGAH FILE INI KE GITHUB.** File `.gitignore` sudah dikonfigurasi untuk mengabaikannya.

5.  **Konfigurasi Skrip (Jika Perlu):**
    * Buka file `taker_bot.py`.
    * Parameter utama seperti `RPC_URL`, `CHAIN_ID`, `CONTRACT_ADDRESS_ONCHAIN`, `BASE_API_URL`, dan `REF_CODE` sudah diisi. Anda bisa mengubah `REF_CODE` dengan kode referral Anda jika diinginkan.
    * Anda juga bisa menyesuaikan `GAS_LIMIT`, `SLEEP_INTERVAL_PER_WALLET_SECONDS`, dan `DELAY_BETWEEN_DIFFERENT_WALLETS` jika diperlukan.

## Menjalankan Bot
Setelah semua setup selesai, jalankan bot dari terminal atau command prompt (pastikan virtual environment sudah aktif):
```bash
python3 taker_bot.py
