# Bot Aktivasi Miner Taker Protocol (Multi-Wallet)

Bot Python sederhana untuk mengotomatiskan panggilan fungsi `active()` pada smart contract di Taker Chain untuk beberapa wallet. Bot ini akan membaca private keys dari file `private_keys.txt` dan mencoba mengaktifkan miner untuk setiap wallet dengan interval sekitar 24 jam per wallet.

**PERINGATAN KERAS / DISCLAIMER:**
* **GUNAKAN DENGAN RISIKO ANDA SENDIRI.** Skrip ini berinteraksi dengan private key dan transaksi blockchain. Pastikan Anda memahami cara kerjanya.
* **KEAMANAN PRIVATE KEY SANGAT PENTING.** Jangan pernah membagikan file `private_keys.txt` Anda atau private key Anda kepada siapa pun. Simpan file tersebut dengan aman. Sebaiknya gunakan wallet baru khusus untuk bot ini dengan dana secukupnya hanya untuk gas fee.
* Penulis tidak bertanggung jawab atas kehilangan dana atau masalah lain yang mungkin timbul dari penggunaan skrip ini.

## Fitur
* Mendukung multi-wallet dari file `private_keys.txt`.
* Interval aktivasi per wallet sekitar 24 jam.
* Jeda antar pemrosesan wallet yang berbeda untuk menghindari potensi masalah.
* Koneksi ke RPC Taker Chain.

## Prasyarat
* Python 3.7+
* Pip (Python package installer)

## Setup & Instalasi

1.  **Clone atau Unduh Repositori (Jika sudah di GitHub):**
    ```bash
    git clone https://github.com/maulana1600/taker.git
    cd taker
    ```
    Atau, jika Anda membuat file secara manual, pastikan semua file (`taker_bot.py`, `requirements.txt`, `.gitignore`) berada dalam satu direktori.

2.  **Buat Virtual Environment (Sangat Direkomendasikan):**
    ```bash
    python -m venv venv
    ```
    Aktifkan virtual environment:
    * Windows: `venv\Scripts\activate`
    * macOS/Linux: `source venv/bin/activate`

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Buat File Private Keys:**
    * Buat file bernama `private_keys.txt` di direktori yang sama dengan `taker_bot.py`.
    * Masukkan private key Anda ke dalam file ini, **satu private key per baris**. Pastikan setiap private key diawali dengan `0x` dan tidak ada spasi tambahan.
        ```
        0xPRIVATEKEYWALLET1................
        0xPRIVATEKEYWALLET2................
        ```
    * **JANGAN UNGGAH FILE INI KE GITHUB.** File `.gitignore` sudah dikonfigurasi untuk mengabaikannya.

5.  **Konfigurasi Skrip (Jika Perlu):**
    * Buka file `taker_bot.py`.
    * Parameter utama seperti `RPC_URL`, `CHAIN_ID`, `CONTRACT_ADDRESS`, dan `CONTRACT_ABI` sudah diisi berdasarkan informasi yang kita temukan untuk Taker Protocol. Jika ada perubahan di masa depan, Anda bisa menyesuaikannya di bagian atas skrip.
    * Anda juga bisa menyesuaikan `GAS_LIMIT`, `SLEEP_INTERVAL_PER_WALLET_SECONDS`, dan `DELAY_BETWEEN_DIFFERENT_WALLETS` jika diperlukan.

## Menjalankan Bot
Setelah semua setup selesai, jalankan bot dari terminal atau command prompt:
```bash
python taker_bot.py
