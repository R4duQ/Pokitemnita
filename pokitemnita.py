# ----------------------------- IMPORTS -----------------------------
import os
import random
import pygame
import itertools
from collections import Counter


# ----------------------------- INITIALIZATION -----------------------------
pygame.init()

# ----------------------------- CONSTANTS -----------------------------
MUSIC_GAME = 0.5
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CRIMSON = (220, 20, 60)

# ----------------------------- ASSETS -----------------------------
icon = pygame.image.load("pokitemnita icon.png")
background = pygame.image.load("background.jpg")
logo_image = pygame.image.load("pokitemnita without background.png")
dealer1 = pygame.image.load("Steli varianta cartoon fara background.png")
dealer2 = pygame.image.load("raul fara backgorund cartoon.png")
pokertable = pygame.image.load("poker table without background 2.png")
panti = pygame.image.load("panti cartoon fara background.png")
patronu = pygame.image.load("Patronu fara background si fara barba.png")
eu = pygame.image.load("eu cartoon style fara background.png")
tomus = pygame.image.load("Tomus cartoon fara background.png")

pygame.display.set_icon(icon)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokitemnita")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

# ----------------------------- UI ELEMENTS -----------------------------
block = pygame.Rect(240, 50, 800, 50)
buton_start = pygame.Rect(235, 300, 200, 50)
settings = pygame.Rect(865, 300, 200, 50)
quit_button = pygame.Rect(535, 400, 200, 50)
fullscreen_button = pygame.Rect(130, 300, 400, 50)
back_to_main_menu_button = pygame.Rect(430, 300, 400, 50)
turn_off_the_music = pygame.Rect(740, 300, 400, 50)
change_song_button = pygame.Rect(740, 400, 400, 50)
credits_button = pygame.Rect(130, 200, 400, 50)
back_to_settings_button = pygame.Rect(430, 600, 400, 50)
dealer1_button = pygame.Rect(240, 150, 200, 50)
dealer2_button = pygame.Rect(840, 150, 200, 50)
button_camera = pygame.Rect(240, 300, 200, 50)
music_select_button = pygame.Rect(740, 200, 400, 50)
pause_button = pygame.Rect(1050, 30, 200, 50)
continue_button = pygame.Rect(420, 200, 400, 50)
raise_button = pygame.Rect(550, 650, 200, 50)
call_button = pygame.Rect(300, 650, 200, 50)
fold_button = pygame.Rect(800, 650, 200, 50)
titlegamescreen_button = pygame.Rect(450, 50, 400, 50)
username_input_box = pygame.Rect(430, 100, 400, 50)
input_box = pygame.Rect(520, 600, 200, 50)
volume_slider = pygame.Rect(540, 630, 200, 10)
volume_handle = pygame.Rect(630, 620, 20, 30)
bet_input_box = pygame.Rect(500, 600, 250, 40)
play_again_button = pygame.Rect(1000, 50, 200, 50)


# ----------------------------- GAME VARIABLES -----------------------------
selected_dealer = None
is_full_screen = False
current_song = ""
username_text = ""
username_active = False
max_characters = 20
active = False
show_bet_input = False
initial_bet_placed = False
initial_bet_button_clicked = False
music_folder = "music"
card_design = "Cards"
pokercard_back = "pokitemnita_card_back_128x128.png"
drums_effect = "Music_effect"
switcher = "Switcher_64x64.png"
songs = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
song_titles = [os.path.splitext(song)[0] for song in songs]
color_inactive = RED
color_active = CRIMSON
color = color_inactive
is_dragging = False
is_dragging1 = False
start_screen = True
main_menu_active = False
game_screen_active = False
settings_active = False
credits_active = False
game_active = False
game1_active = False
camera_active = False
player_select = False
music_selection = False
pause_active = False
winner_screen_active = False
running = True
is_paused = False
music_playing = True
selected_index = 0
button_pressed = False
countdown_time = 0
start_ticks = None
current_tip = None
game_phase = "betting"
current_player_turn = 0
current_bet = 0
player_balances = [1000, 1000, 1000, 1000]
player_bets = [0, 0, 0, 0]
bot_names = ["Tomus", "Panti", "Patronu"]
player_ok = [True, True, True, True]
player_actions = ["", "", "", ""]
bet_input_active = False
bet_input_text = ""
only_one = 0
winner_countdown_start = None
slider_visible = False
slider_start_time = None
slider_x = -300
slider_width = 300
slider_height = 50
slider_y = 10
slider_speed = 5
blink_start_time = pygame.time.get_ticks()
blink_interval = 500
show_text = True


# ----------------------------- CARD DATA -----------------------------
card_games_poker = [
    "Ace - Hearts",
    "2 - Hearts",
    "3 - Hearts",
    "4 - Hearts",
    "5 - Hearts",
    "6 - Hearts",
    "7 - Hearts",
    "8 - Hearts",
    "9 - Hearts",
    "10 - Hearts",
    "J - Hearts",
    "Q - Hearts",
    "K - Hearts",
    "Ace - Diamonds",
    "2 - Diamonds",
    "3 - Diamonds",
    "4 - Diamonds",
    "5 - Diamonds",
    "6 - Diamonds",
    "7 - Diamonds",
    "8 - Diamonds",
    "9 - Diamonds",
    "10 - Diamonds",
    "J - Diamonds",
    "Q - Diamonds",
    "K - Diamonds",
    "Ace - Clubs",
    "2 - Clubs",
    "3 - Clubs",
    "4 - Clubs",
    "5 - Clubs",
    "6 - Clubs",
    "7 - Clubs",
    "8 - Clubs",
    "9 - Clubs",
    "10 - Clubs",
    "J - Clubs",
    "Q - Clubs",
    "K - Clubs",
    "Ace - Spades",
    "2 - Spades",
    "3 - Spades",
    "4 - Spades",
    "5 - Spades",
    "6 - Spades",
    "7 - Spades",
    "8 - Spades",
    "9 - Spades",
    "10 - Spades",
    "J - Spades",
    "Q - Spades",
    "K - Spades",
]
RANK_ORDER = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "Ace": 14,
}

random_tips_stelian = ["ceva"]
random_tips_raul = ["altceva"]


# ----------------------------- FUNCTIONS -----------------------------
def read_player_data(player_index):
    save_folder = "player_data"
    save_file = os.path.join(save_folder, f"player_{player_index + 1}_data.txt")
    if os.path.exists(save_file):
        with open(save_file, "r") as file:
            data = file.readlines()
            bet_line = data[0].strip()
            balance_line = data[1].strip()
            bet = int(bet_line.split(": ")[1])
            balance = float(balance_line.split(": ")[1])
            print(f"Player {player_index + 1} Bet: {bet}, Balance: {balance}")
            return bet, balance
    else:
        print(f"No data found for Player {player_index + 1}.")
        return None, None


def parse_card(card_str):
    rank, suit = card_str.split(" - ")
    return rank, suit


def evaluate_hand(cards):
    hand = [parse_card(card) for card in cards]
    ranks = [rank for rank, _ in hand]
    suits = [suit for _, suit in hand]
    rank_counts = Counter(ranks)
    most_common = rank_counts.most_common()
    flush = len(set(suits)) == 1
    rank_values = sorted([RANK_ORDER[rank] for rank in ranks], reverse=True)
    is_straight = len(set(rank_values)) == 5 and (
        max(rank_values) - min(rank_values) == 4
    )
    if set([14, 2, 3, 4, 5]).issubset(set(rank_values)):
        is_straight = True
        rank_values = [5, 4, 3, 2, 1]
    if is_straight and flush:
        return "Straight Flush", rank_values
    if most_common[0][1] == 4:
        return "Four of a Kind", rank_values
    if most_common[0][1] == 3 and most_common[1][1] == 2:
        return "Full House", rank_values
    if flush:
        return "Flush", rank_values
    if is_straight:
        return "Straight", rank_values
    if most_common[0][1] == 3:
        return "Three of a Kind", rank_values
    if most_common[0][1] == 2 and most_common[1][1] == 2:
        return "Two Pair", rank_values
    if most_common[0][1] == 2:
        return "One Pair", rank_values
    return "High Card", rank_values


def best_combination(player_hand, community_cards):
    all_cards = player_hand + community_cards
    best = None
    for combo in itertools.combinations(all_cards, 5):
        hand_type, value = evaluate_hand(combo)
        if not best or (hand_strength(hand_type), value) > (
            hand_strength(best[0]),
            best[1],
        ):
            best = (hand_type, value)
    return best


def hand_strength(hand_type):
    hand_rank = {
        "High Card": 1,
        "One Pair": 2,
        "Two Pair": 3,
        "Three of a Kind": 4,
        "Straight": 5,
        "Flush": 6,
        "Full House": 7,
        "Four of a Kind": 8,
        "Straight Flush": 9,
    }
    return hand_rank.get(hand_type, 0)


def compare_hands(hand1, hand2):
    hand1_type, hand1_value = hand1
    hand2_type, hand2_value = hand2
    strength1 = hand_strength(hand1_type)
    strength2 = hand_strength(hand2_type)
    if strength1 > strength2:
        return 1
    elif strength1 < strength2:
        return -1
    else:
        if hand1_value > hand2_value:
            return 1
        elif hand1_value < hand2_value:
            return -1
        else:
            return 0


def poker_deck():
    deck = card_games_poker.copy()
    random.shuffle(deck)
    return deck


def poker_deal(deck, num_cards=5):
    hand = [deck.pop(0) for _ in range(num_cards)]
    return hand, deck


def poker_player(deck, num_cards=2):
    hand_player = [deck.pop(0) for _ in range(num_cards)]
    return hand_player, deck


def save_username_to_file(username):
    with open("username.txt", "w") as file:
        file.write(username)


def choose_random_song():
    global current_song
    current_song = random.choice(song_titles)
    print(f"Now playing: {current_song}")


def play_music():
    choose_random_song()
    song_filename = os.path.join(music_folder, f"{current_song}.mp3")
    pygame.mixer.music.load(song_filename)
    pygame.mixer.music.set_volume(MUSIC_GAME)
    pygame.mixer.music.play(-1)


def draw_button(rect, text, is_hovered):
    button_color = (220, 20, 60) if not is_hovered else (139, 0, 0)
    text_color = (255, 255, 255)
    pygame.draw.rect(screen, button_color, rect, border_radius=10)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)


def toggle_music():
    global music_playing
    if music_playing:
        pygame.mixer.music.stop()
        music_playing = False
        print("Music turned off.")
    else:
        play_music()
        music_playing = True
        print("Music turned on.")


def render_songs(selected_index):
    screen.blit(background, (0, 0))
    for index, song in enumerate(songs):
        color = BLACK
        if index == selected_index:
            color = (0, 100, 255)
        text = font.render(song, True, color)
        screen.blit(text, (50, 50 + index * 40))
    pygame.display.flip()


def handle_player_bet_input(events, input_active, bet_input_text):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                input_active = not input_active
            else:
                input_active = False
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                print(f"Player bet: {bet_input_text}")
                return int(bet_input_text), False
            elif event.key == pygame.K_BACKSPACE:
                bet_input_text = bet_input_text[:-1]
            else:
                bet_input_text += event.unicode
    return bet_input_text, input_active


def draw_slider():
    pygame.draw.rect(screen, (139, 0, 0), volume_slider)
    pygame.draw.rect(screen, WHITE, volume_handle)
    volume_text = font.render(f"Volume: {int(MUSIC_GAME * 100)}%", True, WHITE)
    screen.blit(volume_text, (535, 585))


def bot_decision(balance, current_bet):
    if balance <= current_bet:
        return "call"

    # Realistic AI simulation
    confidence = random.random()  # 0 to 1

    # If pot is small and AI is confident, raise
    if confidence > 0.7 and current_bet < balance * 0.2:
        raise_amount = random.randint(int(balance * 0.05), int(balance * 0.2))
        return "raise", raise_amount

    # Moderate confidence, likely to call
    if 0.4 <= confidence <= 0.7:
        return "call"

    # Low confidence, fold more often
    if confidence < 0.4:
        return random.choices(["fold", "call"], weights=[0.7, 0.3])[0]

    return "call"


def all_bets_equal():
    active_bets = [player_bets[i] for i in range(len(player_ok)) if player_ok[i]]
    return len(set(active_bets)) == 1


def load_card_image(card_name):
    # Convert "2 - Clubs" to "2_Clubs.png"
    card_file = os.path.join(card_design, f"{card_name.replace(' - ', '_')}.png")
    if os.path.exists(card_file):
        return pygame.image.load(card_file)
    else:
        print(f"Warning: Image for {card_name} not found.")
        return None


def draw_cards(cards, x, y, is_bot=False, reveal_count=None, show_front_only=False):
    for i, card in enumerate(cards):
        offset = 50 if i < 3 else 55
        if show_front_only or (
            not is_bot and (reveal_count is None or i < reveal_count)
        ):
            card_image = load_card_image(card)
        else:
            card_image = pygame.image.load(pokercard_back)
            card_image = pygame.transform.scale(card_image, (40, 64))
        if card_image:
            screen.blit(card_image, (x + i * offset, y))


def save_poker_hands(player_hands, dealer_hand):
    with open("poker_hands.txt", "w") as file:
        for i, hand in enumerate(player_hands, start=1):
            file.write(f"Player {i} Hand: {', '.join(hand)}\n")
        file.write(f"Dealer Hand: {', '.join(dealer_hand)}\n")
        print("Poker hands saved to poker_hands.txt")


def get_max_bet(player_bets):
    max_bet = max(player_bets)
    max_bet_player_index = player_bets.index(max_bet)
    return max_bet, max_bet_player_index


def on_key_press(char):
    print(f"Funcția activată! Tasta apăsată: '{char}'")


# ----------------------------- GAME LOGIC -----------------------------
deck = poker_deck()
print("Deck of cards:")
for card in deck:
    print(card)

poker_player1 = poker_player(deck, 2)
poker_player2 = poker_player(deck, 2)
poker_player3 = poker_player(deck, 2)
poker_player4 = poker_player(deck, 2)

player1_hand = poker_player1[0]
player2_hand = poker_player2[0]
player3_hand = poker_player3[0]
player4_hand = poker_player4[0]
dealer_hand = poker_deal(deck, 5)[0]

# ----------------------------- MAIN GAME LOOP -----------------------------
play_music()

while running:
    screen.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()
    is_hovered_start = buton_start.collidepoint(mouse_pos)
    is_hovered_settings = settings.collidepoint(mouse_pos)
    is_hovered_full_screen = fullscreen_button.collidepoint(mouse_pos)
    is_hovered_back_to_main_menu = back_to_main_menu_button.collidepoint(mouse_pos)
    is_hovered_music = turn_off_the_music.collidepoint(mouse_pos)
    is_hovered_change_song = change_song_button.collidepoint(mouse_pos)
    is_hovered_credits = credits_button.collidepoint(mouse_pos)
    is_hovered_back_to_settings_button = back_to_settings_button.collidepoint(mouse_pos)
    is_hovered_quit_button = quit_button.collidepoint(mouse_pos)
    is_hovered_dealer1 = dealer1_button.collidepoint(mouse_pos)
    is_hovered_dealer2 = dealer2_button.collidepoint(mouse_pos)
    is_hovered_button_camera = button_camera.collidepoint(mouse_pos)
    is_hovered_username_input = username_input_box.collidepoint(mouse_pos)
    is_hovered_music_selected_button = music_select_button.collidepoint(mouse_pos)
    is_hovered_pause_button = pause_button.collidepoint(mouse_pos)
    is_hovered_contiune_button = continue_button.collidepoint(mouse_pos)
    is_hovered_raise_button = raise_button.collidepoint(mouse_pos)
    is_hovered_fold_button = fold_button.collidepoint(mouse_pos)
    is_hovered_call_button = call_button.collidepoint(mouse_pos)
    is_hovered_bet_input_box = bet_input_box.collidepoint(mouse_pos)
    is_hovered_play_again_button = play_again_button.collidepoint(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game1_active and selected_dealer == "Stelian" or selected_dealer == "Raul":
            pause_button = pygame.Rect(1050, 30, 200, 50)
            draw_button(pause_button, "Pause", is_hovered_pause_button)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button.collidepoint(mouse_pos):
                    game1_active = False
                    pause_active = True

                if (
                    game_phase == "next_round"
                    or game_phase == "next_round2"
                    or game_phase == "final_phase"
                    and current_player_turn == 0
                ):
                    if fold_button.collidepoint(event.pos):
                        player_ok[0] = False
                        player_actions[0] = "fold"
                        winner_screen_active = True
                        game1_active = False
                        game_phase = None
                        winner_name = "You"
                        winner_hand_type = "Folded"
                        print("You folded. You lose!")
                        current_player_turn += 1

                    elif call_button.collidepoint(event.pos):
                        player_bets[0] = current_bet
                        player_balances[0] -= current_bet
                        player_actions[0] = "call"
                        current_player_turn += 1

                    elif raise_button.collidepoint(event.pos):
                        if not bet_input_active:
                            bet_input_active = True
                            bet_input_text = ""
                        elif bet_input_text.isdigit():
                            raise_amount = int(bet_input_text)
                            max_bet, max_bet_player_index = get_max_bet(player_bets)
                            total_bet = max_bet + raise_amount
                            max_raise = player_balances[0] + player_bets[0] - max_bet

                            if raise_amount <= 0:
                                print("Raise amount must be greater than 0.")
                            elif (
                                raise_amount
                                > player_balances[0] + player_bets[0] - max_bet
                            ):
                                print(
                                    f"You do not have enough balance to raise this amount. Maximum raise: {player_balances[0] + player_bets[0] - max_bet}."
                                )
                            elif total_bet <= max_bet:
                                print(
                                    f"Raise amount must exceed the current highest bet of {max_bet}."
                                )
                            else:
                                current_bet = total_bet
                                player_bets[0] = total_bet
                                player_balances[0] -= total_bet - max_bet
                                player_actions[0] = f"raise {raise_amount}"
                                print(
                                    f"You raised by {raise_amount}. Current bet is now {current_bet}."
                                )
                                current_player_turn += 1
                                max_bet, max_bet_player_index = get_max_bet(player_bets)
                                if max_bet_player_index == 0:
                                    print(f"You made the highest bet of {max_bet}.")
                                else:
                                    print(
                                        f"{bot_names[max_bet_player_index - 1]} made the highest bet of {max_bet}."
                                    )
                            bet_input_active = False

                if game_phase == "betting" and current_player_turn == 0:
                    if bet_input_box.collidepoint(event.pos):
                        bet_input_active = True
                    else:
                        bet_input_active = False

            elif event.type == pygame.KEYDOWN and bet_input_active:
                if event.key == pygame.K_BACKSPACE:
                    bet_input_text = bet_input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if bet_input_text.isdigit():
                        raise_amount = int(bet_input_text)
                        max_bet, max_bet_player_index = get_max_bet(player_bets)
                        total_bet = max_bet + raise_amount
                        max_raise = player_balances[0] + player_bets[0] - max_bet

                        if raise_amount <= 0:
                            print("Raise amount must be greater than 0.")
                        elif (
                            raise_amount > player_balances[0] + player_bets[0] - max_bet
                        ):
                            print(
                                f"You do not have enough balance to raise this amount. Maximum raise: {player_balances[0] + player_bets[0] - max_bet}."
                            )
                        elif total_bet <= max_bet:
                            print(
                                f"Raise amount must exceed the current highest bet of {max_bet}."
                            )
                        else:
                            current_bet = total_bet
                            player_bets[0] = total_bet
                            player_balances[0] -= total_bet - max_bet
                            player_actions[0] = f"raise {raise_amount}"
                            print(
                                f"You raised by {raise_amount}. Current bet is now {current_bet}."
                            )
                            current_player_turn += 1
                            max_bet, max_bet_player_index = get_max_bet(player_bets)
                            if max_bet_player_index == 0:
                                print(f"You made the highest bet of {max_bet}.")
                            else:
                                print(
                                    f"{bot_names[max_bet_player_index - 1]} made the highest bet of {max_bet}."
                                )
                        bet_input_active = False
                elif event.unicode.isdigit():
                    bet_input_text += event.unicode

            if (
                game_phase == "next_round"
                and current_player_turn > 0
                and current_player_turn <= 3
            ):
                i = current_player_turn
                if player_ok[i]:
                    decision = bot_decision(player_balances[i], current_bet)
                    if decision == "fold":
                        player_ok[i] = False
                        player_actions[i] = "fold"
                    elif decision == "call":
                        player_bets[i] = current_bet
                        player_balances[i] -= current_bet
                        player_actions[i] = "call"
                    elif isinstance(decision, tuple) and decision[0] == "raise":
                        raise_amount = decision[1]
                        current_bet += raise_amount
                        player_bets[i] = current_bet
                        player_balances[i] -= current_bet
                        player_actions[i] = f"raise {raise_amount}"
                current_player_turn += 1

            if game_phase == "next_round" and current_player_turn >= 4:
                if all_bets_equal():
                    print("Proceeding to the next phase")
                    game_phase = "next_round2"
                    current_player_turn = 0
                else:
                    current_player_turn = 0

            if (
                game_phase == "next_round2"
                and current_player_turn > 0
                and current_player_turn <= 3
            ):
                i = current_player_turn
                if player_ok[i]:
                    decision = bot_decision(player_balances[i], current_bet)
                    if decision == "fold":
                        player_ok[i] = False
                        player_actions[i] = "fold"
                    elif decision == "call":
                        player_bets[i] = current_bet
                        player_balances[i] -= current_bet
                        player_actions[i] = "call"
                    elif isinstance(decision, tuple) and decision[0] == "raise":
                        raise_amount = decision[1]
                        current_bet += raise_amount
                        player_bets[i] = current_bet
                        player_balances[i] -= current_bet
                        player_actions[i] = f"raise {raise_amount}"
                current_player_turn += 1

            if game_phase == "next_round2" and current_player_turn >= 4:
                if all_bets_equal():
                    print("Proceeding to the final phase")
                    game_phase = "final_phase"
                    current_player_turn = 0
                else:
                    current_player_turn = 0

            if (
                game_phase == "final_phase"
                and current_player_turn > 0
                and current_player_turn <= 3
            ):
                i = current_player_turn
                if player_ok[i]:
                    decision = bot_decision(player_balances[i], current_bet)
                    if decision == "fold":
                        player_ok[i] = False
                        player_actions[i] = "fold"
                    elif decision == "call":
                        player_bets[i] = current_bet
                        player_balances[i] -= current_bet
                        player_actions[i] = "call"
                    elif isinstance(decision, tuple) and decision[0] == "raise":
                        raise_amount = decision[1]
                        current_bet += raise_amount
                        player_bets[i] = current_bet
                        player_balances[i] -= current_bet
                        player_actions[i] = f"raise {raise_amount}"
                current_player_turn += 1

            if game_phase == "final_phase" and current_player_turn >= 4:
                if all_bets_equal():
                    print("Proceeding to the winner")
                    game_phase = "winner"
                    current_player_turn = 0
                else:
                    current_player_turn = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                button_pressed = True
                if volume_slider.collidepoint(mouse_pos):
                    is_dragging = True

                if game_screen_active:
                    if dealer1_button.collidepoint(mouse_pos):
                        selected_dealer = "Stelian"
                        game_screen_active = False
                        game_active = True
                        print("Stelian selected")
                        current_tip = random.choice(random_tips_stelian)

                    elif dealer2_button.collidepoint(mouse_pos):
                        selected_dealer = "Raul"
                        game_screen_active = False
                        game_active = True
                        print("Raul selected")
                        current_tip = random.choice(random_tips_raul)

                if username_input_box.collidepoint(mouse_pos):
                    username_active = True
                else:
                    username_active = False

                if pause_active:
                    if continue_button.collidepoint(mouse_pos):
                        pause_active = False
                        game1_active = True
                        print("Game continued")

        elif event.type == pygame.KEYDOWN:
            if username_active:
                if event.key == pygame.K_BACKSPACE:
                    username_text = username_text[:-1]
                elif len(username_text) < max_characters:
                    username_text += event.unicode

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and button_pressed:
                button_pressed = False
                is_dragging = False

                if main_menu_active:
                    if buton_start.collidepoint(mouse_pos):
                        player_select = True
                        main_menu_active = False
                        print("Am apasat Start, merg spre ecranul de Joc")
                        if not music_playing:
                            music_playing = False

                    elif settings.collidepoint(mouse_pos):
                        main_menu_active = False
                        settings_active = True
                        print("Am apasat Options, merg spre ecranul de Setari")

                    elif quit_button.collidepoint(mouse_pos):
                        running = False

                elif game_screen_active:
                    if back_to_main_menu_button.collidepoint(mouse_pos):
                        game_screen_active = False
                        game_active = False
                        main_menu_active = True
                        print("Inapoi spre Main Menu")

                elif settings_active:
                    if fullscreen_button.collidepoint(mouse_pos):
                        is_full_screen = not is_full_screen
                        if is_full_screen:
                            pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                        else:
                            pygame.display.set_mode((WIDTH, HEIGHT))

                    if (
                        back_to_main_menu_button.collidepoint(mouse_pos)
                        and settings_active
                    ):
                        settings_active = False
                        main_menu_active = True
                        print("Inapoi spre Main Menu")

                    elif turn_off_the_music.collidepoint(mouse_pos):
                        toggle_music()

                    elif change_song_button.collidepoint(mouse_pos):
                        choose_random_song()
                        play_music()
                        print(f"Song changed to: {current_song}")

                    elif credits_button.collidepoint(mouse_pos):
                        settings_active = False
                        credits_active = True

                    if music_select_button.collidepoint(mouse_pos):
                        settings_active = False
                        music_selection = True

                elif player_select:
                    if back_to_main_menu_button.collidepoint(mouse_pos):
                        player_select = False
                        main_menu_active = True
                        print("Back to Main Menu from Player Select")

                elif music_selection:
                    if back_to_main_menu_button.collidepoint(mouse_pos):
                        music_selection = False
                        settings_active = True
                        print("Back to Settings from Music Selection")

        elif event.type == pygame.MOUSEMOTION and is_dragging:
            volume_handle.x = max(
                volume_slider.x,
                min(
                    event.pos[0],
                    volume_slider.x + volume_slider.width - volume_handle.width,
                ),
            )

            MUSIC_GAME = (volume_handle.x - volume_slider.x) / (
                volume_slider.width - volume_handle.width
            )
            pygame.mixer.music.set_volume(MUSIC_GAME)
            pygame.draw.rect(screen, (220, 20, 60), volume_handle)

            text_surface = font.render(
                f"{int(MUSIC_GAME * 100)}%", True, (255, 255, 255)
            )
            text_rect = text_surface.get_rect(center=volume_handle.center)
            screen.blit(text_surface, text_rect)
        if music_selection:
            screen.blit(background, (0, 0))
            back_to_main_menu_button = pygame.Rect(430, 600, 400, 50)
            draw_button(
                back_to_main_menu_button,
                "Back to Settings",
                is_hovered_back_to_main_menu,
            )

            songs_per_page = 5
            table_x, table_y = 130, 50
            table_width, table_height = 900, 300
            row_height = 50

            slider_x = table_x + table_width + 20
            slider_y = table_y
            slider_width = 20
            slider_height = table_height
            slider_handle_height = max(20, slider_height * songs_per_page // len(songs))
            slider_handle_y = slider_y + (
                selected_index * (slider_height - slider_handle_height)
            ) // max(1, len(songs) - songs_per_page)

            pygame.draw.rect(
                screen,
                (200, 200, 200),
                (table_x, table_y, table_width, table_height),
                border_radius=10,
            )
            pygame.draw.rect(
                screen,
                (150, 150, 150),
                (slider_x, slider_y, slider_width, slider_height),
                border_radius=10,
            )
            pygame.draw.rect(
                screen,
                (100, 100, 255),
                (slider_x, slider_handle_y, slider_width, slider_handle_height),
                border_radius=10,
            )

            start_index = max(0, selected_index - selected_index % songs_per_page)
            end_index = min(len(songs), start_index + songs_per_page)

            for i, song in enumerate(songs[start_index:end_index]):
                color = (0, 255, 0) if start_index + i == selected_index else (0, 0, 0)
                text = font.render(song[:-4], True, color)
                screen.blit(text, (table_x + 10, table_y + i * row_height + 40))

            for i, song in enumerate(songs[start_index:end_index]):
                song_rect = pygame.Rect(
                    table_x, table_y + i * row_height + 40, table_width, row_height
                )
                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and event.button == 1
                    and song_rect.collidepoint(mouse_pos)
                ):
                    selected_index = start_index + i
                    selected_song = songs[selected_index]
                    song_filename = os.path.join(music_folder, selected_song)
                    pygame.mixer.music.load(song_filename)
                    pygame.mixer.music.play(-1)
                    current_song = selected_song[:-4]

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pygame.Rect(
                    slider_x, slider_handle_y, slider_width, slider_handle_height
                ).collidepoint(mouse_pos):
                    is_dragging1 = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                is_dragging1 = False
            elif event.type == pygame.MOUSEMOTION and is_dragging1:
                slider_handle_y = max(
                    slider_y,
                    min(event.pos[1], slider_y + slider_height - slider_handle_height),
                )
                selected_index = (
                    (slider_handle_y - slider_y)
                    * (len(songs) - songs_per_page)
                    // max(1, slider_height - slider_handle_height)
                )
                selected_index = min(max(0, selected_index), len(songs) - 1)

    if main_menu_active:
        screen.blit(background, (0, 0))
        logo_rect = logo_image.get_rect(center=(block.centerx, block.centery + 150))
        screen.blit(logo_image, logo_rect)

        quit_button = pygame.Rect(535, 400, 200, 50)
        draw_button(buton_start, "Start", is_hovered_start)
        draw_button(settings, "Options", is_hovered_settings)
        draw_button(quit_button, "Quit", is_hovered_quit_button)

        song_text = font.render(f"Now Playing: {current_song}", True, WHITE)
        screen.blit(song_text, (10, 680))
        if (
            not game_screen_active
            and main_menu_active
            and not pygame.mixer.music.get_busy()
        ):
            if music_playing:
                play_music()
        selected_dealer = None

    if game_screen_active:
        screen.blit(background, (0, 0))
        text = font.render("Game Screen", True, WHITE)
        back_to_main_menu_button = pygame.Rect(430, 600, 400, 50)
        draw_button(
            back_to_main_menu_button, "Back to Main Menu", is_hovered_back_to_main_menu
        )
        screen.blit(text, (10, 680))

        if music_playing:
            pygame.mixer.music.stop()

        dealer1_resized = pygame.transform.scale(dealer1, (400, 350))
        dealer1_rect = dealer1_resized.get_rect(
            center=(block.centerx - 300, block.centery + 300)
        )
        screen.blit(dealer1_resized, dealer1_rect)

        dealer2_resized = pygame.transform.scale(dealer2, (300, 320))
        dealer2_rect = dealer2_resized.get_rect(
            center=(block.centerx + 300, block.centery + 300)
        )
        screen.blit(dealer2_resized, dealer2_rect)

        draw_button(titlegamescreen_button, "Choose your dealer", False)
        draw_button(dealer1_button, "Stelian", is_hovered_dealer1)
        draw_button(dealer2_button, "Raul", is_hovered_dealer2)

    if settings_active:
        screen.blit(background, (0, 0))
        text = font.render("Settings", True, WHITE)
        back_to_main_menu_button = pygame.Rect(130, 400, 400, 50)
        screen.blit(text, (10, 680))

        draw_button(fullscreen_button, "Fullscreen Mode", is_hovered_full_screen)
        draw_button(
            back_to_main_menu_button, "Back to Main Menu", is_hovered_back_to_main_menu
        )

        if music_playing:
            draw_button(turn_off_the_music, "Turn Off the Music", is_hovered_music)
        else:
            draw_button(turn_off_the_music, "Turn On the Music", is_hovered_music)

        draw_button(change_song_button, "Change Song", is_hovered_change_song)
        draw_slider()
        draw_button(credits_button, "Credits", is_hovered_credits)

        draw_button(
            music_select_button, "Music Select", is_hovered_music_selected_button
        )

    if credits_active:
        screen.blit(background, (0, 0))
        text = font.render(
            "Game Title: Pokitemnita (Poker in Politemnita)", True, WHITE
        )
        screen.blit(text, (250, 100))
        text2 = font.render("Developer: Moldovan Radu-Lucian", True, WHITE)
        screen.blit(text2, (350, 150))
        text3 = font.render("Libraries: Pygame, Pyinstaller", True, WHITE)
        screen.blit(text3, (380, 200))
        text4 = font.render("Coordonator: Nicola Stelian, Brumar Raul", True, WHITE)
        screen.blit(text4, (300, 250))
        draw_button(
            back_to_settings_button,
            "Back to Options",
            is_hovered_back_to_settings_button,
        )
        if (
            back_to_settings_button.collidepoint(mouse_pos)
            and event.type == pygame.MOUSEBUTTONDOWN
        ):
            settings_active = True
            credits_active = False
            print("Back to Settings clicked")

    if game_active:
        screen.blit(background, (0, 0))
        if selected_dealer:
            selection_text = font.render(
                f"Selected Dealer: {selected_dealer}", True, WHITE
            )
            screen.blit(selection_text, (420, 250))
        if start_ticks is None:
            start_ticks = pygame.time.get_ticks()

        seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
        countdown = max(0, countdown_time - int(seconds_passed))

        if current_tip:
            small_font = pygame.font.Font(None, 30)
            tip_text = small_font.render(f"Tip: {current_tip}", True, WHITE)
            screen.blit(tip_text, (20, 680))

        if countdown > 0:
            countdown_text = font.render(f"Countdown: {countdown}", True, WHITE)
        else:
            countdown_text = font.render("Time's up!", True, RED)
            game1_active = True
            game_active = False

        screen.blit(countdown_text, (500, 300))

    if game1_active:
        screen.blit(background, (0, 0))
        pokertable_resized = pygame.transform.scale(pokertable, (820, 520))
        screen.blit(pokertable_resized, (230, 100))

        if selected_dealer == "Stelian":
            if (
                player_ok[1] is False
                and player_ok[2] is False
                and player_ok[3] is False
            ):
                winner_screen_active = True
                game1_active = False
                print("Player 1 won the game!")

            dealer1_resized = pygame.transform.scale(dealer1, (156, 156))

            panti_resized = pygame.transform.scale(panti, (130, 156))
            screen.blit(panti_resized, (105, 140))
            panti_nume = "Panti"
            panti_nume = font.render(panti_nume, True, WHITE)
            screen.blit(panti_nume, (125, 300))

            patronu_resized = pygame.transform.scale(patronu, (250, 250))
            screen.blit(patronu_resized, (970, 95))
            patronu_nume = "Patronu"
            patronu_nume = font.render(patronu_nume, True, WHITE)
            screen.blit(patronu_nume, (1030, 305))
            screen.blit(dealer1_resized, (550, 10))

            eu_resized = pygame.transform.scale(eu, (130, 170))
            screen.blit(eu_resized, (110, 450))

            tomus_resized = pygame.transform.scale(tomus, (150, 180))
            screen.blit(tomus_resized, (1010, 440))
            name1 = "Tomus"
            name1 = font.render(name1, True, WHITE)
            screen.blit(name1, (1035, 630))

            draw_button(pause_button, "Pause", is_hovered_pause_button)

            draw_cards(player1_hand, 360, 450)

            if game_phase != "winner":
                draw_cards(player2_hand, 780, 450, is_bot=True)
                draw_cards(player3_hand, 360, 190, is_bot=True)
                draw_cards(player4_hand, 780, 190, is_bot=True)

            if game_phase == "betting":
                draw_cards(dealer_hand, 500, 320, is_bot=True)
            elif game_phase == "next_round":
                draw_cards(dealer_hand, 500, 320, reveal_count=3)
            elif game_phase == "next_round2":
                draw_cards(dealer_hand, 500, 320, reveal_count=4)
            elif game_phase == "final_phase":
                draw_cards(dealer_hand, 500, 320)
            elif game_phase == "winner":
                draw_cards(player2_hand, 780, 450, is_bot=False)
                draw_cards(player3_hand, 360, 190, is_bot=False)
                draw_cards(player4_hand, 780, 190, is_bot=False)
                draw_cards(dealer_hand, 500, 320)

            if only_one == 0:
                save_poker_hands(
                    [player1_hand, player2_hand, player3_hand, player4_hand],
                    dealer_hand,
                )
                only_one = 1

            with open("username.txt", "r") as read_username_file:
                text = read_username_file.read()
                shorter_text = text[:-1]
                shorter_text = font.render(shorter_text, True, WHITE)
                screen.blit(shorter_text, (130, 630))

            if (
                game_phase == "betting"
                and current_player_turn > 0
                and current_player_turn <= 3
            ):
                i = current_player_turn
                if player_ok[i]:
                    decision = bot_decision(player_balances[i], current_bet)
                    if decision == "fold":
                        player_ok[i] = False
                        player_actions[i] = "fold"

                    elif decision == "call":
                        player_bets[i] = current_bet
                        player_balances[i] -= current_bet
                        player_actions[i] = "call"
                    elif isinstance(decision, tuple) and decision[0] == "raise":
                        raise_amount = decision[1]
                        current_bet += raise_amount
                        player_bets[i] = current_bet
                        player_balances[i] -= current_bet
                        player_actions[i] = f"raise {raise_amount}"
                current_player_turn += 1

            if game_phase == "betting" and current_player_turn >= 4:
                if all_bets_equal():
                    print("Next round")
                    game_phase = "next_round"
                    current_player_turn = 0
                else:
                    current_player_turn = 0

            for i, action in enumerate(player_actions):
                if i == 0:
                    player_name = "You"
                    status_you = font.render(f"{player_name}: {action}", True, WHITE)
                    screen.blit(status_you, (30, 10))
                else:
                    player_name = bot_names[i - 1]
                    status = font.render(f"{player_name}: {action}", True, WHITE)
                    screen.blit(status, (30, 10 + i * 30))

            if game_phase == "betting" and current_player_turn == 0:
                pygame.draw.rect(screen, (220, 20, 60), bet_input_box, border_radius=10)
                if is_hovered_bet_input_box:
                    pygame.draw.rect(
                        screen, (139, 0, 0), bet_input_box, border_radius=10
                    )
                else:
                    pygame.draw.rect(
                        screen, (220, 20, 60), bet_input_box, border_radius=10
                    )
                    font = pygame.font.Font(None, 40)
                    text_surface = font.render(bet_input_text, True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=bet_input_box.center)
                    screen.blit(text_surface, text_rect)

            if game_phase == "next_round" and current_player_turn == 0:
                if bet_input_active:
                    pygame.draw.rect(
                        screen, (220, 20, 60), bet_input_box, border_radius=10
                    )
                    text_surface = font.render(bet_input_text, True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=bet_input_box.center)
                    screen.blit(text_surface, text_rect)
                else:
                    draw_button(call_button, "Call", is_hovered_call_button)
                    draw_button(raise_button, "Raise", is_hovered_raise_button)
                    draw_button(fold_button, "Fold", is_hovered_fold_button)

            if game_phase == "next_round2" and current_player_turn == 0:
                if bet_input_active:
                    pygame.draw.rect(
                        screen, (220, 20, 60), bet_input_box, border_radius=10
                    )
                    text_surface = font.render(bet_input_text, True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=bet_input_box.center)
                    screen.blit(text_surface, text_rect)
                else:
                    draw_button(call_button, "Call", is_hovered_call_button)
                    draw_button(raise_button, "Raise", is_hovered_raise_button)
                    draw_button(fold_button, "Fold", is_hovered_fold_button)

            if game_phase == "final_phase" and current_player_turn == 0:
                if bet_input_active:
                    pygame.draw.rect(
                        screen, (220, 20, 60), bet_input_box, border_radius=10
                    )
                    text_surface = font.render(bet_input_text, True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=bet_input_box.center)
                    screen.blit(text_surface, text_rect)
                else:
                    draw_button(call_button, "Check", is_hovered_call_button)
                    draw_button(raise_button, "Raise", is_hovered_raise_button)
                    draw_button(fold_button, "Fold", is_hovered_fold_button)

            if game_phase == "winner":
                if winner_countdown_start is None:
                    winner_countdown_start = pygame.time.get_ticks()

                elapsed_time = (pygame.time.get_ticks() - winner_countdown_start) / 1000
                countdown = max(0, 8 - int(elapsed_time))

                if countdown > 0:
                    countdown_text = font.render(
                        f"Winner will be revealed in: {countdown}", True, WHITE
                    )
                    screen.blit(countdown_text, (450, 600))
                    if not pygame.mixer.music.get_busy():
                        drums_folder = "Music_effect"
                        drums_song = [
                            f for f in os.listdir(drums_folder) if f.endswith(".mp3")
                        ]
                        if drums_song:
                            drums = os.path.join(drums_folder, drums_song[0])
                            pygame.mixer.music.load(drums)
                            pygame.mixer.music.play(-1)
                else:
                    best_hands = []
                    player_hands = [
                        player1_hand,
                        player2_hand,
                        player3_hand,
                        player4_hand,
                    ]

                    for i, hand in enumerate(player_hands):
                        if player_ok[i]:
                            full_hand = hand + dealer_hand
                            best_hand = best_combination(full_hand, [])
                            best_hands.append((i, best_hand))

                    winner_index, winner_hand = max(
                        best_hands, key=lambda x: (hand_strength(x[1][0]), x[1][1])
                    )
                    winner_name = (
                        "You" if winner_index == 0 else bot_names[winner_index - 1]
                    )
                    winner_hand_type = winner_hand[0]
                    pygame.mixer.music.stop()

                    winner_screen_active = True
                    game1_active = False
                    game_phase = None
                    winner_countdown_start = None

        elif selected_dealer == "Raul":
            if (
                player_ok[1] is False
                and player_ok[2] is False
                and player_ok[3] is False
            ):
                winner_screen_active = True
                game1_active = False
                print("Player 1 won the game!")

            dealer2_resized = pygame.transform.scale(dealer2, (130, 130))

            panti_resized = pygame.transform.scale(panti, (130, 156))
            screen.blit(panti_resized, (105, 140))
            panti_nume = "Panti"
            panti_nume = font.render(panti_nume, True, WHITE)
            screen.blit(panti_nume, (125, 300))

            patronu_resized = pygame.transform.scale(patronu, (250, 250))
            screen.blit(patronu_resized, (970, 95))
            patronu_nume = "Patronu"
            patronu_nume = font.render(patronu_nume, True, WHITE)
            screen.blit(patronu_nume, (1030, 305))
            screen.blit(dealer2_resized, (530, 10))

            eu_resized = pygame.transform.scale(eu, (130, 170))
            screen.blit(eu_resized, (110, 450))

            tomus_resized = pygame.transform.scale(tomus, (150, 180))
            screen.blit(tomus_resized, (1010, 440))
            name1 = "Tomus"
            name1 = font.render(name1, True, WHITE)
            screen.blit(name1, (1035, 630))

            draw_button(pause_button, "Pause", is_hovered_pause_button)

            draw_cards(player1_hand, 360, 450)

            if game_phase != "winner":
                draw_cards(player2_hand, 780, 450, is_bot=True)
                draw_cards(player3_hand, 360, 190, is_bot=True)
                draw_cards(player4_hand, 780, 190, is_bot=True)

            if game_phase == "betting":
                draw_cards(dealer_hand, 500, 320, is_bot=True)
            elif game_phase == "next_round":
                draw_cards(dealer_hand, 500, 320, reveal_count=3)
            elif game_phase == "next_round2":
                draw_cards(dealer_hand, 500, 320, reveal_count=4)
            elif game_phase == "final_phase":
                draw_cards(dealer_hand, 500, 320)
            elif game_phase == "winner":
                draw_cards(player2_hand, 780, 450, is_bot=False)
                draw_cards(player3_hand, 360, 190, is_bot=False)
                draw_cards(player4_hand, 780, 190, is_bot=False)
                draw_cards(dealer_hand, 500, 320)

            if only_one == 0:
                save_poker_hands(
                    [player1_hand, player2_hand, player3_hand, player4_hand],
                    dealer_hand,
                )
                only_one = 1

            with open("username.txt", "r") as read_username_file:
                text = read_username_file.read()
                shorter_text = text[:-1]
                shorter_text = font.render(shorter_text, True, WHITE)
                screen.blit(shorter_text, (130, 630))

            if (
                game_phase == "betting"
                and current_player_turn > 0
                and current_player_turn <= 3
            ):
                i = current_player_turn
                if player_ok[i]:
                    decision = bot_decision(player_balances[i], current_bet)
                    if decision == "fold":
                        player_ok[i] = False
                        player_actions[i] = "fold"
                    elif decision == "call":
                        player_bets[i] = current_bet
                        player_balances[i] -= current_bet
                        player_actions[i] = "call"
                    elif isinstance(decision, tuple) and decision[0] == "raise":
                        raise_amount = decision[1]
                        current_bet += raise_amount
                        player_bets[i] = current_bet
                        player_balances[i] -= current_bet
                        player_actions[i] = f"raise {raise_amount}"
                current_player_turn += 1

            if game_phase == "betting" and current_player_turn >= 4:
                if all_bets_equal():
                    print("Next round")
                    game_phase = "next_round"
                    current_player_turn = 0
                else:
                    current_player_turn = 0

            for i, action in enumerate(player_actions):
                if i == 0:
                    player_name = "You"
                    status_you = font.render(f"{player_name}: {action}", True, WHITE)
                    screen.blit(status_you, (30, 10))
                else:
                    player_name = bot_names[i - 1]
                    status = font.render(f"{player_name}: {action}", True, WHITE)
                    screen.blit(status, (30, 10 + i * 30))

            if game_phase == "betting" and current_player_turn == 0:
                pygame.draw.rect(screen, (220, 20, 60), bet_input_box, border_radius=10)
                if is_hovered_bet_input_box:
                    pygame.draw.rect(
                        screen, (139, 0, 0), bet_input_box, border_radius=10
                    )
                else:
                    pygame.draw.rect(
                        screen, (220, 20, 60), bet_input_box, border_radius=10
                    )
                    font = pygame.font.Font(None, 40)
                    text_surface = font.render(bet_input_text, True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=bet_input_box.center)
                    screen.blit(text_surface, text_rect)

            if game_phase == "next_round" and current_player_turn == 0:
                if bet_input_active:
                    pygame.draw.rect(
                        screen, (220, 20, 60), bet_input_box, border_radius=10
                    )
                    text_surface = font.render(bet_input_text, True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=bet_input_box.center)
                    screen.blit(text_surface, text_rect)
                else:
                    draw_button(call_button, "Call", is_hovered_call_button)
                    draw_button(raise_button, "Raise", is_hovered_raise_button)
                    draw_button(fold_button, "Fold", is_hovered_fold_button)

            if game_phase == "next_round2" and current_player_turn == 0:
                if bet_input_active:
                    pygame.draw.rect(
                        screen, (220, 20, 60), bet_input_box, border_radius=10
                    )
                    text_surface = font.render(bet_input_text, True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=bet_input_box.center)
                    screen.blit(text_surface, text_rect)
                else:
                    draw_button(call_button, "Call", is_hovered_call_button)
                    draw_button(raise_button, "Raise", is_hovered_raise_button)
                    draw_button(fold_button, "Fold", is_hovered_fold_button)

            if game_phase == "final_phase" and current_player_turn == 0:
                if bet_input_active:
                    pygame.draw.rect(
                        screen, (220, 20, 60), bet_input_box, border_radius=10
                    )
                    text_surface = font.render(bet_input_text, True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=bet_input_box.center)
                    screen.blit(text_surface, text_rect)
                else:
                    draw_button(call_button, "Check", is_hovered_call_button)
                    draw_button(raise_button, "Raise", is_hovered_raise_button)
                    draw_button(fold_button, "Fold", is_hovered_fold_button)

            if game_phase == "winner":
                if winner_countdown_start is None:
                    winner_countdown_start = pygame.time.get_ticks()

                elapsed_time = (pygame.time.get_ticks() - winner_countdown_start) / 1000
                countdown = max(0, 8 - int(elapsed_time))

                if countdown > 0:
                    countdown_text = font.render(
                        f"Winner will be revealed in: {countdown}", True, WHITE
                    )
                    screen.blit(countdown_text, (450, 600))
                    if not pygame.mixer.music.get_busy():
                        drums_folder = "Music_effect"
                        drums_song = [
                            f for f in os.listdir(drums_folder) if f.endswith(".mp3")
                        ]
                        if drums_song:
                            drums = os.path.join(drums_folder, drums_song[0])
                            pygame.mixer.music.load(drums)
                            pygame.mixer.music.play(-1)
                else:
                    best_hands = []
                    player_hands = [
                        player1_hand,
                        player2_hand,
                        player3_hand,
                        player4_hand,
                    ]

                    for i, hand in enumerate(player_hands):
                        if player_ok[i]:
                            full_hand = hand + dealer_hand
                            best_hand = best_combination(full_hand, [])
                            best_hands.append((i, best_hand))

                    winner_index, winner_hand = max(
                        best_hands, key=lambda x: (hand_strength(x[1][0]), x[1][1])
                    )
                    winner_name = (
                        "You" if winner_index == 0 else bot_names[winner_index - 1]
                    )
                    winner_hand_type = winner_hand[0]
                    pygame.mixer.music.stop()

                    winner_screen_active = True
                    game1_active = False
                    game_phase = None
                    winner_countdown_start = None

    if player_select:
        if music_playing:
            pygame.mixer.music.stop()
        screen.blit(background, (0, 0))
        back_to_main_menu_button = pygame.Rect(430, 600, 400, 50)
        draw_button(
            back_to_main_menu_button, "Back to Main Menu", is_hovered_back_to_main_menu
        )

        pygame.draw.rect(screen, (220, 20, 60), username_input_box, border_radius=10)
        if is_hovered_username_input:
            pygame.draw.rect(screen, (139, 0, 0), username_input_box, border_radius=10)
        else:
            pygame.draw.rect(
                screen, (220, 20, 60), username_input_box, border_radius=10
            )

        input_surface = font.render(username_text, True, WHITE)
        screen.blit(
            input_surface, (username_input_box.x + 10, username_input_box.y + 10)
        )
        label = font.render("Enter your username:", True, WHITE)
        screen.blit(label, (430, 50))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                save_username_to_file(username_text)
                print(f"Username saved: {username_text}")
                game_screen_active = True
                player_select = False
                is_hovered_username_input = False

    if music_selection:
        screen.blit(background, (0, 0))
        back_to_main_menu_button = pygame.Rect(430, 600, 400, 50)
        draw_button(
            back_to_main_menu_button, "Back to Settings", is_hovered_back_to_main_menu
        )

        songs_per_page = 5
        table_x, table_y = 130, 50
        table_width, table_height = 900, 300
        row_height = 50

        slider_x = table_x + table_width + 20
        slider_y = table_y
        slider_width = 20
        slider_height = table_height
        slider_handle_height = max(
            20, slider_height * songs_per_page // max(1, len(songs))
        )
        slider_handle_y = slider_y + (
            selected_index * (slider_height - slider_handle_height)
        ) // max(1, len(songs) - songs_per_page)

        pygame.draw.rect(
            screen,
            (200, 200, 200),
            (table_x, table_y, table_width, table_height),
            border_radius=10,
        )
        pygame.draw.rect(
            screen,
            (150, 150, 150),
            (slider_x, slider_y, slider_width, slider_height),
            border_radius=10,
        )
        pygame.draw.rect(
            screen,
            (100, 100, 255),
            (slider_x, slider_handle_y, slider_width, slider_handle_height),
            border_radius=10,
        )

        start_index = max(0, selected_index - selected_index % songs_per_page)
        end_index = min(len(songs), start_index + songs_per_page)

        for i, song in enumerate(songs[start_index:end_index]):
            color = (0, 255, 0) if start_index + i == selected_index else (0, 0, 0)
            text = font.render(song[:-4], True, color)
            screen.blit(text, (table_x + 10, table_y + i * row_height + 40))

        for i, song in enumerate(songs[start_index:end_index]):
            song_rect = pygame.Rect(
                table_x, table_y + i * row_height + 40, table_width, row_height
            )
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and song_rect.collidepoint(mouse_pos)
            ):
                selected_index = start_index + i
                selected_song = songs[selected_index]
                song_filename = os.path.join(music_folder, selected_song)
                pygame.mixer.music.load(song_filename)
                pygame.mixer.music.play(-1)
                current_song = selected_song[:-4]

    if pause_active:
        screen.blit(background, (0, 0))
        draw_button(continue_button, "Continue", is_hovered_contiune_button)
        quit_button = pygame.Rect(420, 300, 400, 50)
        draw_button(quit_button, "Quit", is_hovered_quit_button)

        if event.type == pygame.MOUSEBUTTONUP:
            if quit_button.collidepoint(mouse_pos):
                running = False

        back_to_main_menu_button = pygame.Rect(420, 400, 400, 50)
        draw_button(
            back_to_main_menu_button, "Back to Main Menu", is_hovered_back_to_main_menu
        )
        if event.type == pygame.MOUSEBUTTONUP:
            if back_to_main_menu_button.collidepoint(mouse_pos):
                main_menu_active = True
                game_screen_active = False
                settings_active = False
                credits_active = False
                game_active = False
                game1_active = False
                camera_active = False
                player_select = False
                music_selection = False
                pause_active = False

    if winner_screen_active:
        screen.blit(background, (0, 0))
        play_again_button = pygame.Rect(430, 500, 400, 50)
        back_to_main_menu_button = pygame.Rect(430, 600, 400, 50)
        if not pygame.mixer.music.get_busy():
            winner_songs_folder = "winner_song_player"
            winner_songs = [
                f for f in os.listdir(winner_songs_folder) if f.endswith(".mp3")
            ]
            if winner_songs:
                random_song = random.choice(winner_songs)
                random_song_path = os.path.join(winner_songs_folder, random_song)
                pygame.mixer.music.load(random_song_path)
                pygame.mixer.music.play(-1)

        if not player_ok[0]:
            text_loser = font.render("You lose! You folded.", True, WHITE)
            screen.blit(text_loser, (500, 300))
        elif all(not player_ok[i] for i in range(1, 4)):
            text_winner = font.render("You win!", True, WHITE)
            screen.blit(text_winner, (600, 300))
        else:
            winner_display_text = font.render(
                f"Winner: {winner_name} with {winner_hand_type}", True, WHITE
            )
            screen.blit(winner_display_text, (400, 300))
        draw_button(play_again_button, "Play Again", is_hovered_play_again_button)
        draw_button(
            back_to_main_menu_button, "Back to Main Menu", is_hovered_back_to_main_menu
        )

        if event.type == pygame.MOUSEBUTTONUP:
            if back_to_main_menu_button.collidepoint(mouse_pos):
                winner_screen_active = False
                game1_active = False
                game_phase = None
                winner_countdown_start = None
                main_menu_active = True
                pygame.mixer.music.stop()

            if play_again_button.collidepoint(mouse_pos):
                winner_screen_active = False
                game1_active = False
                game_phase = "betting"
                winner_countdown_start = None
                deck = poker_deck()

                poker_player1 = poker_player(deck, 2)
                poker_player2 = poker_player(deck, 2)
                poker_player3 = poker_player(deck, 2)
                poker_player4 = poker_player(deck, 2)

                player1_hand = poker_player1[0]
                player2_hand = poker_player2[0]
                player3_hand = poker_player3[0]
                player4_hand = poker_player4[0]
                dealer_hand = poker_deal(deck, 5)[0]
                save_poker_hands(
                    [player1_hand, player2_hand, player3_hand, player4_hand],
                    dealer_hand,
                )
                current_player_turn = 0
                current_bet = 0
                player_balances = [1000, 1000, 1000, 1000]
                player_bets = [0, 0, 0, 0]
                player_ok = [True, True, True, True]
                player_actions = ["", "", "", ""]
                bet_input_active = False
                bet_input_text = ""
                game_active = False
                game_screen_active = True
                pygame.mixer.music.stop()

    if start_screen:
        pygame.mixer.music.stop()
        screen.blit(background, (0, 0))
        text = font.render("Intro", True, WHITE)
        logo_rect = logo_image.get_rect(center=(block.centerx, block.centery + 150))
        screen.blit(logo_image, logo_rect)

        elapsed_time = pygame.time.get_ticks() - blink_start_time
        if elapsed_time >= blink_interval:
            show_text = not show_text
            blink_start_time = pygame.time.get_ticks()

        if show_text:
            blinking_text = font.render("Press any key to continue", True, WHITE)
            screen.blit(blinking_text, (470, 500))

        back_to_main_menu_button = pygame.Rect(430, 600, 400, 50)

        if event.type == pygame.KEYDOWN:
            on_key_press(event.unicode)
            start_screen = False
            main_menu_active = True

    pygame.display.flip()
    clock.tick(120)
