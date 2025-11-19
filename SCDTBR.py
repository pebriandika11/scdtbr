# 🎮 Game Labirin RPL menuju Kantin SMK Negeri Pasirian
# Tanpa library tambahan

def tampilkan_peta(peta, pemain, nyawa, level, skor, total_skor):
    print("\n" + "=" * 55)
    print(f"🏫 SMK NEGERI PASIRIAN — LEVEL {level}")
    print(f"❤️ Nyawa: {nyawa}   🏆 Skor Level: {skor}   🌟 Total Skor: {total_skor}")
    print("=" * 55)
    for y in range(len(peta)):
        for x in range(len(peta[y])):
            if (x, y) == pemain:
                print("😁", end="")
            else:
                print(peta[y][x], end="")
        print()
    print("=" * 55)


def clear():
    print("\033[H\033[J", end="")


def tampilkan_menu():
    print("=" * 60)
    print("🎮 SELAMAT DATANG DI GAME LABIRIN RPL ➡️ KANTIN 🍴")
    print("=" * 60)

    print("\n📘 **CARA BERMAIN:**")
    print("1. Kamu adalah siswa RPL yang ingin pergi ke kantin.")
    print("2. Gunakan kontrol untuk bergerak:")
    print("     W = Naik ⬆️")
    print("     S = Turun ⬇️")
    print("     A = Kiri ⬅️")
    print("     D = Kanan ➡️")
    print("3. Hindari menabrak tembok 🧱 (nyawa berkurang).")
    print("4. Setiap melangkah kamu mendapat skor +5.")
    print("5. Semakin cepat menyelesaikan level → bonus lebih besar.")
    print("6. Semakin tinggi level → semakin sulit.")
    print("7. Jika nyawamu habis → GAME OVER.")
    print("8. Selesaikan semua level untuk sampai ke 🍴 KANTIN SMK!")
    print("9. Total skor dihitung dari semua level.")
    print("10. Kalahkan semua level dan jadilah siswa RPL sejati!")

    print("\n👉 Tekan ENTER untuk memulai permainan...")
    input()
    clear()


def main_game():
    nama = input("Masukkan nama pemain: ").capitalize()

    nyawa = 3
    level = 1
    total_langkah = 0
    total_skor = 0

    # Semua level game
    level_maps = [
        {
            "peta": [
                list("🧱🧱🧱🧱🧱🧱🧱🧱"),
                list("🧱⬜⬜⬜⬜🧱🍴🧱"),
                list("🧱🧱⬜🧱⬜🧱⬜🧱"),
                list("🧱⬜⬜🧱⬜⬜⬜🧱"),
                list("🧱🧱🧱🧱🧱🧱🧱🧱")
            ],
            "start": (1, 1),
            "tujuan": (6, 1),
            "bonus": 200
        },
        {
            "peta": [
                list("🧱🧱🧱🧱🧱🧱🧱🧱🧱"),
                list("🧱⬜⬜⬜🧱⬜⬜🍴🧱"),
                list("🧱⬜🧱🧱🧱⬜🧱🧱🧱"),
                list("🧱⬜🧱🧱🧱⬜⬜⬜🧱"),
                list("🧱⬜🧱🧱🧱🧱🧱⬜🧱"),
                list("🧱⬜⬜⬜⬜⬜⬜⬜🧱"),
                list("🧱🧱🧱🧱🧱🧱🧱🧱🧱")
            ],
            "start": (1, 1),
            "tujuan": (7, 1),
            "bonus": 400
        },
        {
            "peta": [
                list("🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱"),
                list("🧱⬜⬜🧱⬜⬜⬜🧱🍴🧱"),
                list("🧱⬜⬜🧱⬜🧱⬜⬜⬜🧱"),
                list("🧱⬜🧱🧱⬜⬜🧱🧱🧱🧱"),
                list("🧱⬜⬜⬜🧱⬜⬜⬜⬜🧱"),
                list("🧱🧱🧱⬜🧱🧱🧱⬜🧱🧱"),
                list("🧱⬜⬜⬜⬜🧱🧱⬜⬜🧱"),
                list("🧱⬜🧱🧱🧱⬜🧱🧱⬜🧱"),
                list("🧱⬜⬜⬜⬜⬜⬜⬜⬜🧱"),
                list("🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱")
            ],
            "start": (1, 1),
            "tujuan": (8, 1),
            "bonus": 600
        }
    ]

    # MAIN LOOP LEVEL
    for data in level_maps:

        peta = data["peta"]
        pemain = data["start"]
        tujuan = data["tujuan"]
        langkah = 0
        skor = 0

        while True:
            clear()
            tampilkan_peta(peta, pemain, nyawa, level, skor, total_skor)
            print("🧱Tembok    ⬜ Jalur Jalan    😁 Karakter Pemain      🍴Kantin/Tujuan")
            print(f"Langkah ke-{langkah}")
            print("W = Ke Atas, A = Ke Kiri, S = Ke Bawah, D = Ke Kanan")
            gerak = input("Gerak (W/A/S/D): ").upper()

            x, y = pemain

            if gerak == "W": y -= 1
            elif gerak == "S": y += 1
            elif gerak == "A": x -= 1
            elif gerak == "D": x += 1
            else: continue

            # Keluar batas
            if y < 0 or y >= len(peta) or x < 0 or x >= len(peta[y]):
                nyawa -= 1
                print("💥 Kamu menabrak Dinding Luar!")
                if nyawa == 0:
                    print("\n💀 GAME OVER!")
                    print(f"Total skor akhir: {total_skor}")
                    return False
                continue

            # Tabrak tembok
            if peta[y][x] == "🧱":
                nyawa -= 1
                print("💥 Kamu Menabrak Tembok!")
                if nyawa == 0:
                    print("\n💀 GAME OVER!")
                    print(f"Total skor akhir: {total_skor}")
                    return False
                continue

            # Gerak valid
            pemain = (x, y)
            langkah += 1
            total_langkah += 1
            skor += 5

            # Sampai tujuan
            if pemain == tujuan:
                bonus = max(0, data["bonus"] - langkah * 10)
                skor += bonus
                total_skor += skor

                print("\n" + "=" * 55)
                print(f"🎉 {nama}, Kamu Menyelesaikan LEVEL {level}!")
                print(f"Langkah: {langkah}")
                print(f"Skor Level: {skor}")
                print(f"Total Skor: {total_skor}")
                print("=" * 55)

                input("Tekan ENTER untuk lanjut...")
                level += 1
                break

    # Semua level selesai
    print("\n" + "=" * 60)
    print(f"🏆 SELAMAT {nama.upper()}! Kamu sampai di 🍴 KANTIN!")
    print(f"🌟 TOTAL SKOR AKHIR: {total_skor}")
    print("=" * 60)

    return True  # menandakan game selesai sukses


def main():
    tampilkan_menu()

    while True:
        selesai = main_game()

        print("\n🔁 Ingin bermain lagi?")
        ulang = input("Ketik Y untuk ulang, N untuk keluar: ").upper()

        if ulang != "Y":
            print("\n👋 Terima kasih sudah bermain!")
            break

        clear()  # reset layar sebelum memulai ulang


main()