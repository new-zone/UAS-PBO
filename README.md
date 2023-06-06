# UAS-PBO
Anggota Kelompok : 1. Zahrah Hafizah Fakhri (G1A022046)  2. Neli Agustin (G1A022048)  3. Kevin Taqwa Abdiansyah (G1A022078)
Membuat Game Hangman.

Penjelasan Kode Secara Singkat

Kode pertama mengimpor beberapa modul yang diperlukan, termasuk modul `random`, `time`, dan `pygame`. Selanjutnya, beberapa variabel warna dan ukuran layar didefinisikan. Daftar kata-kata yang akan ditebak juga telah disediakan. Kemudian, layar permainan dibuat menggunakan fungsi `pygame.display.set_mode()`. Gambar-gambar untuk permainan hangman dimuat ke dalam daftar `hangman_images`. Suara tebakan benar dan salah juga dimuat menggunakan `pygame.mixer.Sound()`.

Ada beberapa fungsi yang didefinisikan, seperti `draw_text()` untuk menggambar teks di layar dan `draw_hangman()` untuk menggambar gambar hangman. Fungsi utama `hangman()` mengimplementasikan logika permainan. Kata yang akan ditebak dipilih secara acak, dan pemain diberikan kesempatan untuk menebak huruf-hurufnya. Saat pemain menebak huruf dengan benar, huruf tersebut ditampilkan di tempat yang sesuai dalam kata yang harus ditebak. Jika pemain menebak huruf-huruf dengan benar dan berhasil menebak seluruh kata sebelum kesempatan habis, pemain menang. Jika pemain gagal menebak kata sebelum kesempatan habis, pemain kalah.

Setelah permainan selesai, pesan "YOU WIN!" atau "YOU LOSE!" ditampilkan selama beberapa detik sebelum program keluar. Terakhir, permainan dimulai dengan memanggil fungsi `hangman()`, dan ketika permainan selesai, modul Pygame ditutup dengan `pygame.quit()`.


Tampilan Awal Game
![1](https://github.com/new-zone/UAS-PBO/assets/67883522/6d374649-0c6b-4629-ad9b-7f08c8391fda)

Tampilan Ketika Game Mulai Di Jalankan
![2](https://github.com/new-zone/UAS-PBO/assets/67883522/55439fb2-1e4c-4b87-b002-46012c587792)
![3](https://github.com/new-zone/UAS-PBO/assets/67883522/e25a0d87-9893-49ac-901b-fa4e9b31b93b)

Tampilan Ketika Kata Berhasil Ditebak
![4](https://github.com/new-zone/UAS-PBO/assets/67883522/a7ddebcf-9585-4b2e-b927-b3800ce1a126)

Tampilan Ketika Kata Tidak Berhasil Ditbeak
![5](https://github.com/new-zone/UAS-PBO/assets/67883522/383cb8ac-5c78-4403-b583-bf06ee9b0800)
