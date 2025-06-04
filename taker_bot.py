# --- LOOP UTAMA (Dimodifikasi untuk "tidak ada pengecekan saldo minimum" oleh skrip) ---
if __name__ == "__main__":
    print("🤖 Bot Aktivasi Miner Taker Protocol (Multi-Wallet) Dimulai...")
    
    private_keys_list = load_private_keys(PRIVATE_KEYS_FILE)

    if not private_keys_list:
        print("Tidak ada private key untuk diproses. Bot berhenti.")
        exit()

    print(f"Bot akan mencoba aktivasi untuk setiap wallet setiap ~{SLEEP_INTERVAL_PER_WALLET_SECONDS / 3600:.2f} jam.")
    print("Skrip TIDAK AKAN melakukan pengecekan saldo awal TAKER sebelum mencoba transaksi.")
    print("Jika saldo tidak cukup, transaksi akan gagal di level blockchain.")
    print("Tekan CTRL+C untuk menghentikan bot.")

    processed_wallets_today = {} 

    while True:
        current_timestamp = time.time()
        wallets_to_process_this_round = []

        for index, pk in enumerate(private_keys_list):
            try:
                if not pk.startswith("0x") or len(pk) != 66:
                    print(f"⚠️ Format private key ke-{index+1} tidak valid, dilewati: {pk[:10]}...")
                    continue

                wallet_address_derived = Web3.to_checksum_address(w3.eth.account.from_key(pk).address)
                
                last_processed_time = processed_wallets_today.get(wallet_address_derived, 0)
                if current_timestamp - last_processed_time > SLEEP_INTERVAL_PER_WALLET_SECONDS:
                    wallets_to_process_this_round.append({
                        "private_key": pk,
                        "address": wallet_address_derived,
                        "index": index + 1
                    })
                else:
                    remaining_time = (last_processed_time + SLEEP_INTERVAL_PER_WALLET_SECONDS) - current_timestamp
                    # Komentari atau hapus baris print ini jika Anda tidak ingin melihat pesan tunggu per wallet
                    # print(f"ℹ️ Wallet {wallet_address_derived} (ke-{index+1}) masih dalam periode tunggu. Sisa waktu: {remaining_time/3600:.2f} jam.")

            except Exception as e:
                print(f"❌ Error saat memproses private key ke-{index+1} (mungkin tidak valid): {e}")
                print(f"   Private key bermasalah (awal): {pk[:10]}...")
                continue
        
        if not wallets_to_process_this_round:
            # Komentari atau hapus baris print ini jika Anda tidak ingin melihat pesan saat tidak ada wallet yang diproses
            # print(f"\nSemua wallet sudah diproses untuk siklus ini. Tidur selama 1 jam sebelum cek lagi...")
            time.sleep(3600) 
            continue

        print(f"\nSiklus baru: Akan mencoba memproses {len(wallets_to_process_this_round)} wallet.")
        for wallet_data in wallets_to_process_this_round:
            print(f"\n--- Memproses Wallet #{wallet_data['index']}: {wallet_data['address']} ---")
            
            # BAGIAN PENGECEKAN SALDO YANG DIHILANGKAN/DIKOMENTARI:
            # try:
            #     balance_wei = w3.eth.get_balance(wallet_data['address'])
            #     balance_taker = w3.from_wei(balance_wei, 'ether')
            #     print(f"  Saldo saat ini: {balance_taker} TAKER") # Anda bisa tetap menampilkan saldo jika mau
            #     # if balance_taker == 0: # Pengecekan spesifik terhadap saldo 0 dihilangkan
            #     #     print("  ⚠️ Saldo TAKER mungkin tidak cukup untuk membayar gas fee.")
            # except Exception as e:
            #     print(f"  Tidak bisa mendapatkan saldo: {e}")

            success = activate_miner(wallet_data['address'], wallet_data['private_key'])
            if success:
                processed_wallets_today[wallet_data['address']] = time.time()
            
            if len(wallets_to_process_this_round) > 1 and wallet_data != wallets_to_process_this_round[-1]:
                print(f"\n⏳ Jeda {DELAY_BETWEEN_DIFFERENT_WALLETS} detik sebelum wallet berikutnya...")
                time.sleep(DELAY_BETWEEN_DIFFERENT_WALLETS)
        
        # Komentari atau hapus print ini jika tidak perlu
        # print(f"\nSemua wallet dalam siklus ini telah dicoba proses. Tidur selama 1 jam sebelum evaluasi siklus berikutnya...")
        time.sleep(3600)
