# /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
# |  Lifeline.py - Version 1.0                           |
# |  Last updated: 2024-11-10                            |
# |  by jasperredis                                      |
# |  This is the main source code file for Lifeline.py!  |
# \______________________________________________________/

import pygame
import sys
import json
import os
import time
import random
import tkinter as tk
from tkinter import messagebox
import requests
import socket
import webbrowser

version = 1.0

# *Initialize pygame
pygame.init()
pygame.mixer.init()

# *Load saved data
print("opening saved.json...")
try:
    with open("saved.json", 'r') as file:
        saved_info = json.load(file)
        print("opened and saved to variable")
except Exception as e: # Close the program upon error and provide reason
    print("Error", f"Could not load saved.json because of provided reason: {e}", 5)

# *Set settings to preferences (previous settings)
bg = saved_info['bg'] # The background colour, defaulted to 7 (pink)
# A list of all background numbers and their corresonding colours can be found in the main loop where the background is rendered
window = saved_info['window'] # Controls whether the window is windowed borderless or fullscreen, defaulted to windowed borderless
mute = saved_info['mute'] # Controls whether audio is muted or not, defaulted to false
movmod = saved_info['movemode'] # Controls whether the player moves with WASD or their mouse, defaulted to WASD
highscore = saved_info['highscore'] # Highscore, self-explanatory.
totalscore = saved_info['totalscore'] # All scores ever gotten, added together.
gamesplayed = saved_info['gamesplayed'] # How many games the user has played.

# *Set up the display
if window == "b": # b stands for borderless
    screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)  # 800x600 window
else: # else is to prevent unnesecary use of an elif and a possible fallback
    screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)  # 800x600 window
pygame.display.set_caption("Lifeline.py")

# *Load Images
bg_r = pygame.image.load("assets\\images\\bg\\red.png")
bg_o = pygame.image.load("assets\\images\\bg\\orange.png")
bg_y = pygame.image.load("assets\\images\\bg\\yellow.png")
bg_g = pygame.image.load("assets\\images\\bg\\green.png")
bg_gg = pygame.image.load("assets\\images\\bg\\greener green.png")
bg_b = pygame.image.load("assets\\images\\bg\\blue.png")
bg_db = pygame.image.load("assets\\images\\bg\\dark blue.png")
bg_pi = pygame.image.load("assets\\images\\bg\\pink.png")
bg_pu = pygame.image.load("assets\\images\\bg\\purple.png")
bg_mg = pygame.image.load("assets\\images\\bg\\mint green.png")
bg_gr = pygame.image.load("assets\\images\\bg\\grey.png")
lll_img = pygame.image.load("assets\\images\\title\\other\\lifeline logo.png")
opts_t_img = pygame.image.load("assets\\images\\title\\buttons\\opts\\true.png")
opts_f_img = pygame.image.load("assets\\images\\title\\buttons\\opts\\false.png")
start_t_img = pygame.image.load("assets\\images\\title\\buttons\\start\\true.png")
start_f_img = pygame.image.load("assets\\images\\title\\buttons\\start\\false.png")
bar_img = pygame.image.load("assets\\images\\ingame\\bar.png")
plr_img = pygame.image.load("assets\\images\\ingame\\plr.png")
L1_img = pygame.image.load("assets\\images\\ingame\\life\\1.png")
L2_img = pygame.image.load("assets\\images\\ingame\\life\\2.png")
L3_img = pygame.image.load("assets\\images\\ingame\\life\\3.png")
L4_img = pygame.image.load("assets\\images\\ingame\\life\\4.png")
L5_img = pygame.image.load("assets\\images\\ingame\\life\\5.png")
enemy_img = pygame.image.load("assets\\images\\ingame\\enemy.png")
heal_img = pygame.image.load("assets\\images\\ingame\\heal.png")
stop_img = pygame.image.load("assets\\images\\ingame\\stop.png")
pause_1_img = pygame.image.load("assets\\images\\ingame\\pause\\1.png")
pause_2_img = pygame.image.load("assets\\images\\ingame\\pause\\2.png")
pause_3_img = pygame.image.load("assets\\images\\ingame\\pause\\3.png")
pause_barcontent = pygame.image.load("assets\\images\\bars\\bottom\\ingame\\pause.png")
dif_1_t_img = pygame.image.load("assets\\images\\title\\difficulty\\1\\true.png")
dif_1_f_img = pygame.image.load("assets\\images\\title\\difficulty\\1\\false.png")
dif_2_t_img = pygame.image.load("assets\\images\\title\\difficulty\\2\\true.png")
dif_2_f_img = pygame.image.load("assets\\images\\title\\difficulty\\2\\false.png")
dif_3_t_img = pygame.image.load("assets\\images\\title\\difficulty\\3\\true.png")
dif_3_f_img = pygame.image.load("assets\\images\\title\\difficulty\\3\\false.png")
bg_t_img = pygame.image.load("assets\\images\\title\\buttons\\bg\\true.png")
bg_f_img = pygame.image.load("assets\\images\\title\\buttons\\bg\\false.png")
gameover_img = pygame.image.load("assets\\images\\ingame\\life\\0.png")
vol_10 = pygame.image.load("assets\\images\\bars\\top\\vol\\1.png")
vol_08 = pygame.image.load("assets\\images\\bars\\top\\vol\\0.8.png")
vol_06 = pygame.image.load("assets\\images\\bars\\top\\vol\\0.6.png")
vol_04 = pygame.image.load("assets\\images\\bars\\top\\vol\\0.4.png")
vol_02 = pygame.image.load("assets\\images\\bars\\top\\vol\\0.2.png")
vol_00 = pygame.image.load("assets\\images\\bars\\top\\vol\\0.png")
protected_eff = pygame.image.load("assets\\images\\bars\\top\\effects\\protected.png")
gameover_barcontent = pygame.image.load("assets\\images\\bars\\bottom\\ingame\\gameover.png")
autosave1 = pygame.image.load("assets\\images\\other\\autosave\\f1.png")
autosave2 = pygame.image.load("assets\\images\\other\\autosave\\f2.png")
autosave3 = pygame.image.load("assets\\images\\other\\autosave\\f3.png")
autosave4 = pygame.image.load("assets\\images\\other\\autosave\\f4.png")
autosave5 = pygame.image.load("assets\\images\\other\\autosave\\f5.png")
autosave6 = pygame.image.load("assets\\images\\other\\autosave\\f6.png")
autosave7 = pygame.image.load("assets\\images\\other\\autosave\\f7.png")
autosave8 = pygame.image.load("assets\\images\\other\\autosave\\f8.png")
jris_img = pygame.image.load("assets\\images\\other\\intro\\jris.png")
updates_t_img = pygame.image.load("assets\\images\\title\\buttons\\updates\\true.png")
updates_f_img = pygame.image.load("assets\\images\\title\\buttons\\updates\\false.png")
updates_content = pygame.image.load("assets\\images\\title\\updates\\contentbox.png")
nointernet_img = pygame.image.load("assets\\images\\title\\updates\\no internet.png")
fetchingdata_img = pygame.image.load("assets\\images\\title\\updates\\fetching data.png")
updates_barcontent = pygame.image.load("assets\\images\\bars\\bottom\\title\\updates.png")
upd_button = pygame.image.load("assets\\images\\title\\updates\\button.png")
back_t_img = pygame.image.load("assets\\images\\title\\buttons\\back\\true.png")
back_f_img = pygame.image.load("assets\\images\\title\\buttons\\back\\false.png")
windicon = pygame.image.load("windicon.png")

# Set window icon
pygame.display.set_icon(windicon)

# *Declare Sounds
move_sel_sfx = pygame.mixer.Sound("assets\\audio\\sfx\\move_sel.wav")
sel_sfx = pygame.mixer.Sound("assets\\audio\\sfx\\sel.wav")
screenshot_sfx = pygame.mixer.Sound("assets\\audio\\sfx\\screenshot.wav")
lostlife_sfx = pygame.mixer.Sound("assets\\audio\\sfx\\lostlife.wav")
heal_sfx = pygame.mixer.Sound("assets\\audio\\sfx\\heal.wav")
intro1_sfx = pygame.mixer.Sound("assets\\audio\\sfx\\jris1.wav")
intro2_sfx = pygame.mixer.Sound("assets\\audio\\sfx\\jris3.wav")
main_ost = pygame.mixer.Sound("assets\\audio\\ost\\main.wav")
gameplay_ost = pygame.mixer.Sound("assets\\audio\\ost\\gameplay.wav")

# *Scale Images so that they render at the correct size ingame
s_bg_r = pygame.transform.scale(bg_r, (800, 512))
s_bg_o = pygame.transform.scale(bg_o, (800, 512))
s_bg_y = pygame.transform.scale(bg_y, (800, 512))
s_bg_g = pygame.transform.scale(bg_g, (800, 512))
s_bg_gg = pygame.transform.scale(bg_gg, (800, 512))
s_bg_b = pygame.transform.scale(bg_b, (800, 512))
s_bg_db = pygame.transform.scale(bg_db, (800, 512))
s_bg_pi = pygame.transform.scale(bg_pi, (800, 512))
s_bg_pu = pygame.transform.scale(bg_pu, (800, 512))
s_bg_mg = pygame.transform.scale(bg_mg, (800, 512))
s_bg_gr = pygame.transform.scale(bg_gr, (800, 512))
s_lll_img = pygame.transform.scale(lll_img, (512, 192))
s_opts_t_img = pygame.transform.scale(opts_t_img, (172, 20))
s_opts_f_img = pygame.transform.scale(opts_f_img, (172, 20))
s_start_t_img = pygame.transform.scale(start_t_img, (124, 20))
s_start_f_img = pygame.transform.scale(start_f_img, (124, 20))
s_bar_img = pygame.transform.scale(bar_img, (640, 15))
s_plr_img = pygame.transform.scale(plr_img, (15, 5))
s_L1_img = pygame.transform.scale(L1_img, (140, 20))
s_L2_img = pygame.transform.scale(L2_img, (140, 20))
s_L3_img = pygame.transform.scale(L3_img, (140, 20))
s_L4_img = pygame.transform.scale(L4_img, (140, 20))
s_L5_img = pygame.transform.scale(L5_img, (140, 20))
s_enemy_img = pygame.transform.scale(enemy_img, (15, 5))
s_heal_img = pygame.transform.scale(heal_img, (15, 5))
s_pause_1_img = pygame.transform.scale(pause_1_img, (256, 140))
s_pause_2_img = pygame.transform.scale(pause_2_img, (256, 140))
s_pause_3_img = pygame.transform.scale(pause_3_img, (256, 140))
s_pause_barcontent = pygame.transform.scale(pause_barcontent, (760, 36))
s_dif_1_t_img = pygame.transform.scale(dif_1_t_img, (244, 80))
s_dif_1_f_img = pygame.transform.scale(dif_1_f_img, (244, 80))
s_dif_2_t_img = pygame.transform.scale(dif_2_t_img, (244, 80))
s_dif_2_f_img = pygame.transform.scale(dif_2_f_img, (244, 80))
s_dif_3_t_img = pygame.transform.scale(dif_3_t_img, (244, 80))
s_dif_3_f_img = pygame.transform.scale(dif_3_f_img, (244, 80))
s_bg_t_img = pygame.transform.scale(bg_t_img, (292, 20))
s_bg_f_img = pygame.transform.scale(bg_f_img, (292, 20))
s_gameover_img = pygame.transform.scale(gameover_img, (212, 20))
s_vol_10 = pygame.transform.scale(vol_10, (160, 32))
s_vol_08 = pygame.transform.scale(vol_08, (160, 32))
s_vol_06 = pygame.transform.scale(vol_06, (160, 32))
s_vol_04 = pygame.transform.scale(vol_04, (160, 32))
s_vol_02 = pygame.transform.scale(vol_02, (160, 32))
s_vol_00 = pygame.transform.scale(vol_00, (160, 32))
s_protected_eff = pygame.transform.scale(protected_eff, (28, 28))
s_gameover_barcontent = pygame.transform.scale(gameover_barcontent, (348 ,36))
s_autosave1 = pygame.transform.scale(autosave1, (30, 30))
s_autosave2 = pygame.transform.scale(autosave2, (30, 30))
s_autosave3 = pygame.transform.scale(autosave3, (30, 30))
s_autosave4 = pygame.transform.scale(autosave4, (30, 30))
s_autosave5 = pygame.transform.scale(autosave5, (30, 30))
s_autosave6 = pygame.transform.scale(autosave6, (30, 30))
s_autosave7 = pygame.transform.scale(autosave7, (30, 30))
s_autosave8 = pygame.transform.scale(autosave8, (30, 30))
s_jris_img = pygame.transform.scale(jris_img, (150, 150))
s_updates_t_img = pygame.transform.scale(updates_t_img, (172, 20))
s_updates_f_img = pygame.transform.scale(updates_f_img, (172, 20))
s_updates_content = pygame.transform.scale(updates_content, (676, 272))
s_nointernet_img = pygame.transform.scale(nointernet_img, (500, 152))
s_fetchingdata_img = pygame.transform.scale(fetchingdata_img, (316, 20))
s_updates_barcontent = pygame.transform.scale(updates_barcontent, (188, 36))
s_upd_button = pygame.transform.scale(upd_button, (156, 76))
s_back_t_img = pygame.transform.scale(back_t_img, (100, 20))
s_back_f_img = pygame.transform.scale(back_f_img, (100, 20))

# *Declare variables
state = "intro" # The state of the game, so, title screen, game, ect.
sel = 1 # The selected title screen option
area = 1 # The menu of the title screen, as of right now, options or main menu
fillc = 0, 0, 0 # The fill colour of the background, defaulted to black
dif = 2 # Sets the difficulty
fps_font = pygame.font.SysFont("Open Sans", 25) # Sets the font for FPS
updt_font = pygame.font.SysFont("Open Sans", 40)
updd_font = pygame.font.SysFont("Open Sans", 20)
updv_font = pygame.font.SysFont("Open Sans", 18)
current_music = None
plrx = screen.get_width() // 2
autosaving = False
autosavei = 1
autos_tick = 0
jrot = 0
introtick = 0
jx = 0
jtxt_alpha = 0
played_jris2 = False
intropart = 1
propre_alpha = 0
url = "https://raw.githubusercontent.com/Jasperredis/lifelinepy.github.io/refs/heads/main/website/updates.json" #! This is a placeholder!
score = 0

# *Set up time related variables
clock = pygame.time.Clock() # Sets up the Pygame clock
# Title screen key delay and last key press time
key_delay = 200
last_key_press_time = 0
# Screenshot key delay and last key press time
key_delay_f2 = 200
last_key_press_time_f2 = 0
# Volume key delay and last key press time
vol_last_key_press_time = 0
vol_key_delay = 200

running = True
intro2_sfx.play()

def modifySave():
    global bg, window, mute, movmod, highscore, totalscore, gamesplayed
    with open('saved.json', 'w') as file:
        rewrite = {
            "bg": bg,
            "window": window,
            "mute": mute,
            "movemode": movmod,
            "highscore": highscore,
            "totalscore": totalscore,
            "gamesplayed": gamesplayed
        }
        json.dump(rewrite, file, indent=4)

def enemy():
    ex_x = random.randint(85, 700)
    ex_y = 298
    enemies.append([ex_x, ex_y]) 

def heal():
    h_x = random.randint(85, 700)  # Random x position
    h_y = 298
    heals.append([h_x, h_y])       # Add both x and y to the list

def fetchUpdates():
    global s_fetchingdata_img
    img_rect = s_fetchingdata_img.get_rect()
    img_rect.centerx = screen.get_width() // 2
    img_rect.centery = screen.get_height() // 2
    screen.blit(s_fetchingdata_img, (img_rect))
    pygame.display.flip()
    global url_loaded
    global upd
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        upd = response.json()       # Parse JSON data
        url_loaded = True
    except requests.exceptions.RequestException as e:
        print(f"error fetching data: {e}")

def is_connected():
    try:
        # Attempt to connect to Google's public DNS server
        socket.create_connection(("8.8.8.8", 53), timeout=5) # Check Google's public DNS server to see if the user is connected to the internet
        return True
    except OSError:
        return False

def initGame():
    global plrx, paused, gameover, enemies, heals, life, protection, last_prot, score, state, l_tick, hsu
    plrx = screen.get_width() // 2
    paused = False
    gameover = False
    enemies = []
    heals = []
    life = 5
    protection = False
    last_prot = 0
    score = 0
    state = "game"
    l_tick = pygame.time.get_ticks()
    hsu = False

# *Main Loop
while running:
    # Update dynamic variables
    mouse_x, mouse_y = pygame.mouse.get_pos()
    current_time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    fps = int(clock.get_fps())

    # *Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            modifySave()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and (pygame.key.get_mods() & pygame.KMOD_ALT):
                continue

    # *Screenshot script
    if keys[pygame.K_F2] and (current_time - last_key_press_time_f2 >= key_delay_f2):
        ssf = f"screenshots\\{int(time.time())}.png"
        pygame.image.save(screen, ssf)
        last_key_press_time_f2 = current_time
        screenshot_sfx.play()
        img_rect = s_dif_1_f_img.get_rect()
        img_rect.centerx = screen.get_width() // 2.5
        img_rect.centery = screen.get_height() // 3
        ssh = pygame.image.load(ssf)
        s_ssh = pygame.transform.scale(ssh, (400, 300))
        screen.blit(s_ssh, (img_rect))
        pygame.display.flip()
        time.sleep(0.2)

    # *Fill screen
    if state == "game": # Check if the state is in gamplay to make colour changes
        if life == 3 or life == 4 or life == 5:
            fillc = 0, 0, 0 # Use black if life is 3 or more
        elif life == 2:
            fillc = 25, 0, 0 # Use a dark red if life is 2
        elif life == 1:
            fillc = 50, 0, 0 # Use a brighter, yet still dark red if life is critically low at 1
    else:
        fillc = 0, 0, 0 # Stay at black when not in gameplay
    screen.fill((fillc)) # Finally, fill the screen with the chosen colour

    text_surface = fps_font.render(f"FPS: {fps}", True, (255, 255, 255))
    screen.blit(text_surface, (730, 0))

    # *Render background
    #! Having a number not in this below list results in no background.
    # 1 = r(ed)
    # 2 = o(range)
    # 3 = y(ellow)
    # 4 = g(reen)
    # 5 = b(lue)
    # 6 = pu(rple)
    # 7 = pi(nk)
    # 8 = g(reener)g(reen)
    # 9 = d(ark)b(lue)
    # 10 = m(int)g(reen)
    # 11 = gr(ey)
    if not state == "intro": # Allows the black background in the intro
        if bg == 1:
            screen.blit(s_bg_r, (0, 44))
        elif bg == 2:
            screen.blit(s_bg_o, (0, 44))
        elif bg == 3:
            screen.blit(s_bg_y, (0, 44))
        elif bg == 4:
            screen.blit(s_bg_g, (0, 44))
        elif bg == 5:
            screen.blit(s_bg_b, (0, 44))
        elif bg == 6:
            screen.blit(s_bg_pu, (0, 44))
        elif bg == 7:
            screen.blit(s_bg_pi, (0, 44))
        elif bg == 8:
            screen.blit(s_bg_gg, (0, 44))
        elif bg == 9:
            screen.blit(s_bg_db, (0, 44))
        elif bg == 10:
            screen.blit(s_bg_mg, (0, 44))
        elif bg == 11:
            screen.blit(s_bg_gr, (0, 44))
    
    # *Intro loop
    if state == "intro": #! Possibly not done yet
        introtick += 1
        if intropart == 1:
            if not introtick >= 150: # Rotate if 150 ticks have not passed
                jrot += 5
            if not introtick >= 150:
                rs_jris_img = pygame.transform.rotate(s_jris_img, jrot) # Rotate the image
                # Get a rect centered around a fixed position
                img_rect = rs_jris_img.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)) # Make img_rect
                jx = img_rect.x
                # Blit the rotated image at this position
                screen.blit(rs_jris_img, img_rect)

            if introtick >= 150: # Begin second part if 150 ticks have passed
                if played_jris2 == False:
                    intro1_sfx.play()
                    played_jris2 = True
                if not jtxt_alpha >= 255:
                    jtxt_alpha += 15 # Change alpha value of text
                jtxt = pygame.image.load("assets\\images\\other\\intro\\txt.png").convert_alpha() # Load new text
                jtxt.set_alpha(jtxt_alpha)
                s_jtxt = pygame.transform.scale(jtxt, (427, 108))
                if not jx <= 150:
                    jx_div = jx // 10
                    jx -= jx_div
                    if jx == 4:
                        jx = 0
                img_rect = rs_jris_img.get_rect(center=(jx, screen.get_height() // 2))
                screen.blit(rs_jris_img, (img_rect))
                screen.blit(s_jtxt, (200, 260))
            if introtick == 340:
                intropart = 2
                introtick = 0
        else:
            proudlypresents = pygame.image.load("assets\\images\\other\\intro\\proudlypresents.png").convert_alpha()
            s_proudlypresents = pygame.transform.scale(proudlypresents, (496, 236))
            propre_alpha += 10
            s_proudlypresents.set_alpha(propre_alpha)
            img_rect = s_proudlypresents.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(s_proudlypresents, (img_rect))
            if introtick >= 200:
                state = "title"

    # *Title Screen Loop
    if state == "title":
        if not sel == 3 and area == 1:
            url_loaded = False
            global verfcon
            verfcon = False
        
        # *Render buttons
        img_rect = s_lll_img.get_rect()
        img_rect.centerx = screen.get_width() // 2
        img_rect.y = 70
        screen.blit(s_lll_img, (img_rect))
        if area == 1: # 1 is the main menu screen
            # Render start button
            img_rect = s_start_t_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.y = 270
            if sel == 1:
                screen.blit(s_start_t_img, (img_rect))
            else:
                screen.blit(s_start_f_img, (img_rect))
            # Render options button
            img_rect = s_opts_t_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.y = 300
            if sel == 2:
                screen.blit(s_opts_t_img, (img_rect))
            else:
                screen.blit(s_opts_f_img, (img_rect))
            # Render updates button
            img_rect = s_updates_t_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.y = 330
            if sel == 3:
                screen.blit(s_updates_t_img, (img_rect))
            else:
                screen.blit(s_updates_f_img, (img_rect))
        elif area == 2: # 2 is options
            # Render background colour button
            img_rect = s_bg_t_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.y = 270
            if sel == 1:
                screen.blit(s_bg_t_img, (img_rect))
            else:
                screen.blit(s_bg_f_img, (img_rect))
            # Render back button
            img_rect = s_back_t_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.y = 300
            if sel == 2:
                screen.blit(s_back_t_img, (img_rect))
            else:
                screen.blit(s_back_f_img, (img_rect))
        elif area == 3: # *Special, but 3 is updates, which renders a box instead of the regular buttons. This also renders the entirety of area 3.
            img_rect = s_updates_content.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.y = 270
            screen.blit(s_updates_content, (img_rect))
            if not verfcon:
                verfcon = True
                connection = is_connected()
            else:
                if connection:
                    if not url_loaded:
                        fetchUpdates()
                    text_surface = updt_font.render(upd['title'], True, (255, 255, 255))
                    screen.blit(text_surface, (70, 280))
                    text_surface = updd_font.render(upd['description'], True, (255, 255, 255))
                    screen.blit(text_surface, (70, 310))
                    text_surface = updv_font.render(f"{upd['version']} - {upd['date']}", True, (255, 255, 255))
                    screen.blit(text_surface, (70, 520))
                    if version < float(upd['version']):
                        screen.blit(s_upd_button, (570, 450))
                        if keys[pygame.K_u]:
                            open_url = "https://google.com" #! This is a placeholder!
                            webbrowser.open(open_url)
            if not connection:
                img_rect = s_nointernet_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 320
                screen.blit(s_nointernet_img, (img_rect))
            screen.blit(s_updates_barcontent, (20, 560))
            if keys[pygame.K_ESCAPE]:
                area = 1
                sel_sfx.play()

        # *Menu Navigation
        # Scroll up
        if keys[pygame.K_UP] and (current_time - last_key_press_time >= key_delay): # Avoid repeatedly triggering
            if not area == 3:
                sel -= 1
                if sel < 1: # Make sure that sel (selected option) doesn't exceed limits
                    sel = 1
                move_sel_sfx.play()
                last_key_press_time = current_time
        # Scroll down
        if keys[pygame.K_DOWN] and (current_time - last_key_press_time >= key_delay): # Avoid repeatedly triggering
            if not area == 3:
                sel += 1
                if area == 1 and sel >= 5: # Make sure that sel (selected option) doesn't exceed limits
                    sel = 1
                elif area == 2 and sel >= 3: # Make sure that sel (selected option) doesn't exceed limits
                    sel = 2
                move_sel_sfx.play()
                last_key_press_time = current_time
        # Select options
        if keys[pygame.K_RETURN] and (current_time - last_key_press_time >= key_delay): # Avoid repeatedly triggering
            if sel == 1 and area == 1: # Start button
                initGame()
            if sel == 2 and area == 1: # Background colour
                area = 2
                sel = 1
            if sel == 3 and area == 1:
                area = 3
                sel = 1
            elif sel == 2 and area == 2:
                area = 1
            sel_sfx.play()
            last_key_press_time = current_time
        # Navigate other option for option buttons
        if keys[pygame.K_RIGHT] and (current_time - last_key_press_time >= key_delay): # Avoid repeatedly triggering
            if sel == 4 and area == 1: # Difficulty
                dif += 1
                if dif == 4: # Make sure that the selected option doesn't exceed limits
                    dif = 3
                if not dif == 2:
                    messagebox.showinfo("Warning", "The Normal (yellow heart) difficulty has attempted to strike a balance in gameplay. Other difficulties disturb this balance and do not make optimal gameplay. Work will be done in future updates to fix this.")
                move_sel_sfx.play()
                last_key_press_time = current_time
            if sel == 1 and area == 2: # Background colour
                bg += 1
                if bg == 12:  # Make sure that the selected option doesn't exceed limits
                    bg = 1
                move_sel_sfx.play()
                last_key_press_time = current_time

        if keys[pygame.K_LEFT] and (current_time - last_key_press_time >= key_delay): # Avoid repeatedly triggering
            if sel == 4 and area == 1: # Difficulty
                dif -= 1
                if dif == 0:   # Make sure that the selected option doesn't exceed limits
                    dif = 1
                if not dif == 2:
                    messagebox.showinfo("Warning", "The Normal (yellow heart) difficulty has attempted to strike a balance in gameplay. Other difficulties disturb this balance and do not make optimal gameplay.")
                move_sel_sfx.play()
                last_key_press_time = current_time
            if sel == 1 and area == 2: # Background colour
                bg -= 1
                if bg == 0:   # Make sure that the selected option doesn't exceed limits
                    bg = 11
                move_sel_sfx.play()
                last_key_press_time = current_time

        # Render difficulty
        if area == 1:
            img_rect = s_dif_1_f_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.y = 360
            if sel == 4:
                if dif == 1:
                    screen.blit(s_dif_1_t_img, (img_rect))
                elif dif == 2:
                    screen.blit(s_dif_2_t_img, (img_rect))
                elif dif == 3:
                    screen.blit(s_dif_3_t_img, (img_rect))
            else:
                if dif == 1:
                    screen.blit(s_dif_1_f_img, (img_rect))
                elif dif == 2:
                    screen.blit(s_dif_2_f_img, (img_rect))
                elif dif == 3:
                    screen.blit(s_dif_3_f_img, (img_rect))
    
    # *Game Loop
    if state == "game":
        # Bar display script
        img_rect = s_bar_img.get_rect()
        img_rect.centerx = screen.get_width() // 2
        img_rect.centery = screen.get_height() // 2
        screen.blit(s_bar_img, (img_rect))
        img_rect = s_plr_img.get_rect()

        # Change life
        if pygame.time.get_ticks() - l_tick >= 2000 and gameover == False and paused == False:
            life -= 1
            score += 50 # Add 50 to score every time life ticks down
            l_tick = pygame.time.get_ticks()
            if life < 1:
                gameover = True
                totalscore += score

        # Movement script
        if gameover == False:
            if movmod == "mouse":
                if mouse_x > 700:
                    plrx = 700
                elif mouse_x < 85:
                    plrx = 85
                else:
                    plrx = mouse_x
            else:
                if keys[pygame.K_d]:
                    plrx += 10
                    if plrx > 700:
                        plrx = 700
                elif keys[pygame.K_a]:
                    plrx -= 10
                    if plrx < 85:
                        plrx = 85

        # Player display script
        plr_rect = s_plr_img.get_rect()
        plr_rect.x = plrx
        plr_rect.centery = screen.get_height() // 2
        screen.blit(s_plr_img, (plr_rect))

        # Check protection script
        if protection == True:
            if current_time - last_prot >= 500:
                protection = False

        # Effects display script
        img_rect = s_plr_img.get_rect()
        img_rect.centerx = screen.get_width() // 2
        img_rect.y = 5
        if protection == True:
            screen.blit(s_protected_eff, img_rect)

        # Life display script
        if life < 1:
            img_rect = s_gameover_img.get_rect()
            img_rect.centerx = screen.get_width() // 5
            img_rect.y = screen.get_height() // 2 + 20
            screen.blit(s_gameover_img, (img_rect))
        else:
            img_rect = s_L5_img.get_rect()
            img_rect.centerx = screen.get_width() // 5
            img_rect.y = screen.get_height() // 2 + 20
            if life == 5:
                screen.blit(s_L5_img, (img_rect))
            elif life == 4:
                screen.blit(s_L4_img, (img_rect))
            elif life == 3:
                screen.blit(s_L3_img, (img_rect))
            elif life == 2:
                screen.blit(s_L2_img, (img_rect))
            elif life == 1:
                screen.blit(s_L1_img, (img_rect))
        
        # Spawn script
        if paused == False and gameover == False:
            if random.randint(0, 20) == 10:
                if dif == 2:
                    if random.randint(1, 2) == 1:
                        enemy()
                    else:
                        heal()
                elif dif == 1:
                    if random.randint(1, 4) == 2:
                        enemy()
                    else:
                        heal()
                elif dif == 3:
                    if random.randint(1, 4) == 2:
                        heal()
                    else:
                        enemy()

        # Enemy script
        for en in enemies:
            ex, ey = en
            screen.blit(s_enemy_img, (ex, ey))
            en_rect = pygame.Rect(ex, ey, s_enemy_img.get_width(), s_enemy_img.get_height())

            if plr_rect.colliderect(en_rect) and protection == False:
                enemies.remove(en)
                life -= 1
                last_prot = current_time
                protection = True
                lostlife_sfx.play()
                if life < 1:
                    gameover = True
                    totalscore += score

        # Heal script
        for h in heals:
            hx, hy = h
            screen.blit(s_heal_img, (hx, hy)) 
            h_rect = pygame.Rect(hx, hy, s_heal_img.get_width(), s_heal_img.get_height())

            if plr_rect.colliderect(h_rect):
                heals.remove(h)
                life += 1
                heal_sfx.play()
                if life > 5:
                    life = 5

        # Activate pause
        if keys[pygame.K_ESCAPE] and paused == False and gameover == False:
            paused = True
            sel = 1
            sel_sfx.play()
        
        # *Pause script
        if paused == True and gameover == False:
            img_rect.centerx = screen.get_width() // 10
            img_rect.y = 560
            screen.blit(s_pause_barcontent, (img_rect))

            img_rect.centerx = screen.get_width() // 2.5
            img_rect.centery = screen.get_height() // 2.5
            if sel == 1:
                screen.blit(s_pause_1_img, (img_rect))
            elif sel == 2:
                screen.blit(s_pause_2_img, (img_rect))
            elif sel == 3:
                screen.blit(s_pause_3_img, (img_rect))

            if keys[pygame.K_DOWN] and (current_time - last_key_press_time >= key_delay):
                sel += 1
                if sel > 3:
                    sel = 3
                move_sel_sfx.play()
                last_key_press_time = current_time

            if keys[pygame.K_UP] and (current_time - last_key_press_time >= key_delay):
                sel -= 1
                if sel < 1:
                    sel = 1
                move_sel_sfx.play()
                last_key_press_time = current_time

            if keys[pygame.K_RETURN] and (current_time - last_key_press_time >= key_delay):
                if sel == 1:
                    paused = False
                elif sel == 2:
                    result = messagebox.askyesno("Confirm", "Are you sure you want to restart the game?")
                    if result:  # User pressed "Yes"
                        initGame()
                elif sel == 3:
                    state = "title"
                    paused = False
                    sel = 1
                sel_sfx.play()
                last_key_press_time = current_time
        
        # Gameover script
        if gameover == True:
            screen.blit(s_gameover_barcontent, (20, 560))
            if score > highscore or hsu:
                text_surface = fps_font.render(f"New Highscore of {score}! Total Score: {totalscore}", True, (255, 255, 255))
                highscore = score
                hsu = True
            else:
                text_surface = fps_font.render(f"Score: {score}, Total Score: {totalscore}", True, (255, 255, 255))
            screen.blit(text_surface, (0, 0))
            if keys[pygame.K_r]:
                sel_sfx.play()
                initGame()
        else: # If there isnt a gameover, display the score
            if score > highscore:
                highscore = score
            text_surface = fps_font.render(f"Score: {score}, Highscore: {highscore}", True, (255, 255, 255))
            screen.blit(text_surface, (0, 0))

    # *Autosave animation
    autos_tick += 1
    if autos_tick >= 5:
        autosavei += 1 # Increase frame
        if autosavei > 8: # Return to first if past frame count
            autosavei = 1
        autos_tick = 0
    # Render autosave icon
    if autosaving == True:
        if autosavei == 1:
            screen.blit(s_autosave1, (5, 5))
        elif autosavei == 2:
            screen.blit(s_autosave2, (5, 5))
        elif autosavei == 3:
            screen.blit(s_autosave3, (5, 5))
        elif autosavei == 4:
            screen.blit(s_autosave4, (5, 5))
        elif autosavei == 5:
            screen.blit(s_autosave5, (5, 5))
        elif autosavei == 6:
            screen.blit(s_autosave6, (5, 5))
        elif autosavei == 7:
            screen.blit(s_autosave7, (5, 5))
        elif autosavei == 8:
            screen.blit(s_autosave8, (5, 5))

    # Update the screen
    pygame.display.flip()

    # Play music
    if not mute:
        if state == "title" and current_music != "title":
            gameplay_ost.stop()
            main_ost.play(loops=-1)
            current_music = "title"
        elif state == "game" and current_music != "game":
            main_ost.stop()
            gameplay_ost.play(loops=-1)
            current_music = "game"
        elif state not in ["title", "game"]:
            main_ost.stop()
            gameplay_ost.stop()
            current_music = None

    # Set the frame rate
    clock.tick(60)
# Quit pygame
pygame.quit()
sys.exit()