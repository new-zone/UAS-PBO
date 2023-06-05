import random
import time
import pygame

# Inisialisasi Pygame
pygame.init()

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (124, 252, 0)

# Ukuran layar
WIDTH = 800
HEIGHT = 600

# Daftar kata-kata untuk ditebak
kata = ['wares',
    'soup',
    'mount',
    'extend',
    'brown',
    'expert',
    'tired',
    'humidity',
    'backpack',
    'crust',
    'dent',
    'market',
    'knock',
    'smite',
    'windy',
    'coin',
    'throw',
    'silence',
    'bluff',
    'downfall',
    'climb',
    'lying',
    'weaver',
    'snob',
    'kickoff',
    'match',
    'quaker',
    'foreman',
    'excite',
    'thinking',
    'mend',
    'allergen',
    'pruning',
    'coat',
    'emerald']

# Membuat jendela game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Memuat gambar hangman
hangman_images = [
    pygame.image.load('hangman_0.png'),
    pygame.image.load('hangman_1.png'),
    pygame.image.load('hangman_2.png'),
    pygame.image.load('hangman_3.png'),
    pygame.image.load('hangman_4.png'),
    pygame.image.load('hangman_5.png'),
    pygame.image.load('hangman_6.png')
]

# Memuat suara tebakan benar
correct_sound = pygame.mixer.Sound('correct.wav')

# Memuat suara tebakan salah
wrong_sound = pygame.mixer.Sound('wrong.wav')

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def draw_hangman(attempts):
    screen.blit(hangman_images[attempts], (0, 0))

def hangman():
    # Pilih kata secara acak dari daftar kata
    words = random.choice(kata)
    guessed_letters = []
    attempts = 0

    # Mengubah kata menjadi tanda hubung
    hidden_word = ('-' + '') * len(words)

    # Font teks
    font = pygame.font.Font(None, 48)

    running = True
    while running:
        screen.fill(WHITE)
        
        # Menampilkan gambar hangman
        draw_hangman(attempts)

        draw_text("Hangman Game", font, WHITE, WIDTH // 2, 50)

        # Menampilkan kata yang harus ditebak
        draw_text(hidden_word, font, WHITE, WIDTH // 2, 200)

        # Menampilkan huruf yang telah ditebak
        draw_text("Guessed Letters:", font, WHITE, WIDTH // 2, 300)
        draw_text(','.join(guessed_letters), font, WHITE, WIDTH // 2, 350)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    guess = chr(event.key).lower()

                    # Cek apakah huruf telah ditebak sebelumnya
                    if guess in guessed_letters:
                        continue

                    guessed_letters.append(guess)

                    # Jika tebakan benar
                    if guess in words:
                        correct_sound.play()
                        new_hidden_word = ""
                        for i in range(len(words)):
                            if words[i] == guess:
                                new_hidden_word += guess
                            else:
                                new_hidden_word += hidden_word[i]
                        hidden_word = new_hidden_word

                        # Cek apakah kata telah selesai ditebak
                        if '-' not in hidden_word:
                            draw_text("YOU WIN!", font, GREEN, WIDTH // 2, 450)
                            pygame.display.flip()
                            time.sleep(2)
                            running = False
                    else:
                        wrong_sound.play()
                        attempts += 1

                        # Cek apakah kesempatan habis
                        if attempts == 6:
                            draw_text("YOU LOSE!", font, RED, WIDTH // 2, 450)
                            pygame.display.flip()
                            time.sleep(2)
                            running = False

# Memulai game
hangman()

# Menutup Pygame
pygame.quit()
