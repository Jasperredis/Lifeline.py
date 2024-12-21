
#* /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
#* |  Lifeline.py - v1.1 Beta 1.02                        |
#* |  Last updated: 12/21/2024                            |
#* |  by jasperredis                                      |
#* |  This is the main source code file for Lifeline.py!  |
#* \______________________________________________________/

# Import libraries
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
import colorama
from colorama import Fore, Back, Style, init
import gc
try:
    import plyer
    from plyer import notification
except Exception as e:
    messagebox.showinfo("Error", "Could not import plyer. Can probably resume without it.")
import platform
import subprocess
# Import modules
import assets
from assets import ld_img, ld_aud, ld_imgc, unld_img, ld_audc, unld_aud
import general
from general import sysnotif, kill_application, msgbx

def initSave():
    global window, mute, movmod, highscore, totalscore, gamesplayed, alerts, seen_upd, lazyload, bg
    bg = sinf['bg']
    # A list of all background numbers and their corresponding colours can be found in the main loop where the background is rendered
    window = sinf['window']  # Controls whether the window is windowed borderless or fullscreen, defaulted to windowed borderless
    mute = sinf['mute']  # Controls whether audio is muted or not, defaulted to false
    movmod = sinf['movemode']  # Controls whether the player moves with WASD or their mouse, defaulted to WASD
    highscore = sinf['highscore']  # Highscore, self-explanatory.
    totalscore = sinf['totalscore']  # All scores ever gotten, added together.
    gamesplayed = sinf['gamesplayed']  # How many games the user has played.
    alerts = sinf['allow_alerts']  # Whether alerts are allowed.
    seen_upd = sinf['seen_updates']
    lazyload = sinf['lazyloading']
    txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Style.RESET_ALL + "Loaded save data")
    print(txtprnt)

def modifySave():
    try:
        global window, mute, movmod, highscore, totalscore, gamesplayed, alerts, seen_upd, lazyload, bg
        txtprnt = (Fore.MAGENTA + "OPENING " + Fore.LIGHTCYAN_EX + "json/saved.json" + Style.RESET_ALL + "...")
        print(txtprnt)
        with open('json/saved.json', 'w') as file:
            txtprnt = (Fore.MAGENTA + "CREATING DICTIONARY" + Style.RESET_ALL + "...")
            print(txtprnt)
            rewrite = {
                "bg": bg,
                "window": window,
                "mute": mute,
                "movemode": movmod,
                "highscore": highscore,
                "totalscore": totalscore,
                "gamesplayed": gamesplayed,
                "allow_alerts": alerts,
                "seen_updates": seen_upd,
                "lazyloading": lazyload
            }
            txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Fore.MAGENTA + "Created dictionary!")
            print(txtprnt)
            txtprnt = (Fore.MAGENTA + "DUMPING DATA" + Style.RESET_ALL + "...")
            print(txtprnt)
            json.dump(rewrite, file, indent=4)
            txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Fore.MAGENTA + "Saved data!")
            print(txtprnt)
    except Exception as e:
        txtprnt = (Fore.LIGHTRED_EX + "ERROR: " + Fore.MAGENTA + "could not save data because: " + Fore.LIGHTRED_EX + e)
        print(txtprnt)
    
def loadSave():
    global sinf
    try:
        with open("json/saved.json", 'r') as file:
            sinf = json.load(file)
            txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Fore.LIGHTCYAN_EX + "opened json/saved.json and saved to variable" + Style.RESET_ALL + "!")
            print(txtprnt)
    except Exception as e:  # Close the program upon error and provide reason
        messagebox.showinfo("Error", f"Could not load saved.json because of provided reason: {e}")
        kill_application()
loadSave()
initSave()

def makeDisp():
    global screen
    if window == "b":  # b stands for borderless
        screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)  # 800x600 window
    else:  # else is to prevent unnecessary use of an elif and a possible fallback (this is fullscreen)
        screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)  # 800x600 window

sysnotif("Lifeline.py", "Welcome to Lifeline.py!", 5)
version = 1.0

#* Check OS
txtprnt = (Fore.MAGENTA + "CHECKING OS...")
print(txtprnt)
osnm = platform.system()
if osnm == "Windows":
    txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Style.RESET_ALL + "You are on " + Fore.LIGHTCYAN_EX + "Windows!")
    print(txtprnt)
elif osnm == "Linux":
    txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Style.RESET_ALL + "You are on " + Fore.LIGHTYELLOW_EX + "Linux!")
    print(txtprnt)
elif osnm == "Darwin":
    messagebox.showinfo("Lifeline.py", f"How are you running this game on macOS?? Lifeline.py v{version} doesnt HAVE a Mac release!! What???")
else:
    messagebox.showinfo("Lifeline.py", f"Somehow, I couldn't find what OS you're on!! Strange, right? Apparently it's some \"{osnm}\" or something.")

# *Initialize pygame
pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(False)
init(autoreset=True)

# *Load saved data
txtprnt = (Fore.MAGENTA + "OPENING:" + Fore.LIGHTCYAN_EX + " json/saved.json" + Style.RESET_ALL + "...")
print(txtprnt)
loadSave()

# *Set settings to preferences (previous settings)
txtprnt = (Fore.MAGENTA + "LOADING SAVE DATA" + Style.RESET_ALL + "...")
print(txtprnt)
if bg < 1 or bg > 11:
    bg = 7  # Default to pink if invalid
initSave()
print(txtprnt)

# *Set up the display
txtprnt = (Fore.MAGENTA + "SETTING UP WINDOW" + Style.RESET_ALL + "...")
print(txtprnt)
makeDisp()
pygame.display.set_caption("Lifeline.py - Intro")
txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Style.RESET_ALL + "Set up window")
print(txtprnt)

imaud_ind = 1
each_perc = 1.0752688172  #! This needs to be manually updated!
perc = each_perc
txtprnt = ""
ttl_assets = 93

# *Load Images by calling assets.py's functions
try:
    #* Load images needed to begin; these images will be used the entire time
    ld_imgc("init")
    #* Load images by calling assets.py's functions
    ld_imgc("ttsALL")
    ld_imgc("tts1")
    if not lazyload: # Load all other assets if lazy loading is disabled
        ld_imgc("gameplay")
        ld_imgc("autosave")
        ld_imgc("updates")
        ld_imgc("options")
        ld_imgc("controls")
    #* Announce the finishing
    txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED!" + Fore.MAGENTA + " Loaded all images!")
    print(txtprnt)
except Exception as e:
    with open("log.txt", "a") as log_file:
        log_file.write(f"Error loading images: {e}\n")
    msgbx("Error", f"Could not load images because: {e}. Saved to log.", "ok", alerts)
    kill_application()

# Set window icon
pygame.display.set_icon(assets.windicon)

# Declare Sounds
try:
    # Load the nessecary sounds to begin
    ld_audc("init")
    ld_audc("tts")
    if not lazyload: # Only immediately load gameplay sounds if lazy loading is disabled
        ld_audc("gameplay")
    txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED!" + Fore.MAGENTA + " Loaded all audio!")
    print(txtprnt)
except Exception as e:
    with open("log.txt", "a") as log_file:
        log_file.write(f"Error loading audio: {e}\n")
    messagebox.showinfo("Error", f"Could not load audio because: {e}. Saved to log.")
    kill_application()
txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED!" + Fore.MAGENTA + " Loaded all assets!")
print(txtprnt)

debug_start_in_title = False

# * Declare variables
if not debug_start_in_title:
    state = "intro"  # The state of the game, so, title screen, game, etc.
else:
    state = "title"

sel = 1  # The selected title screen option
area = 1  # The menu of the title screen, as of right now, options or main menu
fillc = 0, 0, 0  # The fill color of the background, defaulted to black
dif = 2  # Sets the difficulty
fpfont = pygame.font.SysFont("Arial", 15)  # Sets the font for FPS
updt_font = pygame.font.SysFont("Arial", 30)
updd_font = pygame.font.SysFont("Arial", 10)
updv_font = pygame.font.SysFont("Arial", 8)
controls_fnt = pygame.font.SysFont("Arial", 20)
# Guide for controls variables:
# controls_t: Controls button, selected
# controls_f: Controls button, not selected
# controls_m: Controls menu sprite
# controls_fnt: Controls font
current_music = None
plrx = screen.get_width() // 2
autosaving = False
autosavei = 1
autotick = 0
jrot = 0
introtick = 0
jx = 0
jtxt_alpha = 0
played_jris2 = False
intropart = 1
propre_alpha = 0
url = "https://raw.githubusercontent.com/Jasperredis/LifelinePyTest/refs/heads/main/updates.json"
score = 0
latestVer = True  # Tells if you're on the latest version. True by default so that update button doesn't render without Internet connection.
grid_size = 3
tick = 0
sel_kbnd = ""
gctk = 0 # Tick for garbace collection
gccount = 0 # Garbage collection count

# * Set up time-related variables
clock = pygame.time.Clock()  # Sets up the Pygame clock
# Title screen key delay and last key press time
key_delay = 200
last_key_prestime = 0
# Screenshot key delay and last key press time
key_delay_f2 = 200
last_key_prestime_f2 = 0
# Volume key delay and last key press time
vol_last_key_prestime = 0
vol_key_delay = 200

running = True
assets.intro2_sfx.play()
lnscan = 0

def enemy():
    ex_x = random.randint(148, 640)
    ex_y = 298
    enemies.append([ex_x, ex_y])

def heal():
    h_x = random.randint(148, 640)  # Random x position
    h_y = 298
    heals.append([h_x, h_y])       # Add both x and y to the list

def fetchUpdates():
    global upd, url_loaded, lnscan, txtprnt
    pygame.display.flip()
    try:
        txtprnt = (Fore.MAGENTA + "REQUESTING " + Fore.LIGHTGREEN_EX + url + Style.RESET_ALL + "...")
        print(txtprnt)
        response = requests.get(url)
        txtprnt = (Fore.MAGENTA + "CHECKING JSON AT " + Fore.LIGHTGREEN_EX + url + Style.RESET_ALL + " for errors...")
        print(txtprnt)
        response.raise_for_status()  # Check for HTTP errors
        txtprnt = (Fore.MAGENTA + "PARSING JSON AT  " + Fore.LIGHTGREEN_EX + url + Style.RESET_ALL + "...")
        print(txtprnt)
        upd = response.json()       # Parse JSON data
        txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Fore.MAGENTA + "Parsed JSON at " + url + Style.RESET_ALL + "!")
        print(txtprnt)
        url_loaded = True
        txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Fore.MAGENTA + "JSON at " + url + " " + Style.RESET_ALL + "saved to variable!")
        print(txtprnt)
    except requests.exceptions.RequestException as e:
        txtprnt = (Fore.LIGHTRED_EX + "ERROR: " + Fore.MAGENTA + f"could not fetch JSON at {url} because: " + Fore.LIGHTRED_EX + e)
        print(txtprnt)

def isconnected():
    global upd
    txtprnt = (Fore.MAGENTA + "CONNECTING TO " + Fore.LIGHTCYAN_EX + "8.8.8.8" + Style.RESET_ALL + " to verify Internet connection...")
    print(txtprnt)
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        txtprnt = (Fore.LIGHTGREEN_EX + "You are connected to the Internet!")
        print(txtprnt)
        return True
    except OSError:
        txtprnt = (Fore.LIGHTRED_EX + "Warning! " + Style.RESET_ALL + "No Intenet connection was found!")
        print(txtprnt)
        return False
        upd = {
            
        }

def dispLns():
    global lnscan, upd, lny, pg, txtprnt
    lny = 310  # Starting vertical position for text
    lnscan = 1  # Start with the first line on the page

    # Check if the current page exists in upd
    if str(pg) not in upd or 'lns' not in upd[str(pg)]:
        txtprnt = (Fore.LIGHTRED_EX + "ERROR: " + Style.RESET_ALL + f"Page \"{pg}\" os missing or malformed in UPD. Debug info (contents of UPD):\n" + Fore.LIGHTYELLOW_EX + upd)
        print(f"Error: Page {pg} data is missing or malformed in upd.")
        return
    current_page = upd[str(pg)]  # Get the dictionary for the current page
    total_lines = current_page['lns']  # Get the total number of lines for the page

    while lnscan <= total_lines:
        line_key = str(lnscan)  # Line keys are strings like "1", "2", etc.

        # Check if the line exists in the current page and is a string
        if line_key in current_page and isinstance(current_page[line_key], str):
            text_surface = updd_font.render(current_page[line_key], True, (255, 255, 255))
            screen.blit(text_surface, (70, lny))
        else:
            print(f"Skipping line {line_key}: invalid or missing text in page {pg}.")
        
        lny += 15  # Increment vertical position for the next line
        lnscan += 1

    # Display "More on the next page!" if there are additional pages
    if total_lines >= 13 and pg < int(upd['pgs']):
        text_surface = updd_font.render("More on the next page!", True, (255, 255, 255))
        screen.blit(text_surface, (70, lny))

def initGame():
    global plrx, paused, gameover, enemies, heals, life, protection, last_prot, score, state, l_tick, hsu, gamesplayed
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
    gamesplayed += 1

connection = isconnected()
if connection:
    fetchUpdates()
    txtprnt = (Fore.MAGENTA + "COMPARING VERSION TO LATEST" + Style.RESET_ALL + " ...")
    print(txtprnt)
    if float(upd['version']) > version:
        latestVer = False
        txtprnt = (Fore.LIGHTRED_EX + "Warning: " + Style.RESET_ALL + f"You are not on the latest version of Lifeline.py! Please update to " + Fore.LIGHTGREEN_EX + f"v{upd['version']}" + Style.RESET_ALL + "!")
        print(txtprnt)
    else:
        latestVer = True
        txtprnt = (Fore.LIGHTGREEN_EX + "You are on the latest version of Lifeline.py!")
        print(txtprnt)

def byebye():
    global running
    sysnotif("Lifeline.py", "Goodbye! Thanks for playing Lifeline.py!", 5)
    modifySave()
    running = False
    kill_application()

def ingnotif(imgt, imgf, pos): # pos can be tl (top left), tr (top right), bl (bottom left), or br (bottom right)
    notif_rect = imgt.get_rect()
    if pos == "tl" or pos == "bl":
        notif_rect.x = 0
    else:
        notif_rect.x = imgt.get_width() * 3
    if pos == "tl" or pos == "tr":
        notif_rect.y = 0
    else:
        notif_rect.y = 555
    if notif_rect.collidepoint(mouse_x, mouse_y):
        screen.blit(imgt, (notif_rect))
        if mb[0]:
            return True
        else:
            return False
    else:
        screen.blit(imgf, (notif_rect))
        return False
        
def play_music():
    global current_music
    if not mute:  # Only play music if it's not muted
        if state == "title" and current_music != "title":
            assets.gameplay_ost.stop()  # Stop the gameplay music
            assets.main_ost.play(loops=-1)  # Start main OST (title music)
            current_music = "title"  # Track the music that's currently playing
        elif state == "game" and current_music != "game":
            assets.main_ost.stop()  # Stop the main music
            assets.gameplay_ost.play(loops=-1)  # Start gameplay OST
            current_music = "game"  # Track the current music
        elif state not in ["title", "game"]:  # If in another state, stop both
            assets.main_ost.stop()
            assets.gameplay_ost.stop()
            current_music = None  # Reset the current music state

# *Main Loop
while running:
        # Update dynamic variables
        ogmouse_x, ogmouse_y = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        fps = int(clock.get_fps())
        mouse_x = (ogmouse_x // grid_size) * grid_size
        mouse_y = (ogmouse_y // grid_size) * grid_size
        mb = pygame.mouse.get_pressed()

        # *Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                byebye()

        if keys[pygame.K_LCTRL] and keys[pygame.K_LSHIFT] and keys[pygame.K_LALT] and keys[pygame.K_r]:
            result = subprocess.run(["bash", "/home/jaspr/CodeProjects/LifelinePy/run.sh"], capture_output=True, text=True)
            byebye()

        #* Perform garbage collection
        if gctk >= 300:
            gc.collect() # Force collection
            gctk = 0 # Reset gctk
            gccount += 1
            print(f"Performed garbage collection {gccount}!")
        else:
            gctk += 1

        # *Screenshot script
        if keys[pygame.K_F2] and (current_time - last_key_prestime_f2 >= key_delay_f2):
            ssf = f"screenshots/{int(time.time())}.png"
            pygame.image.save(screen, ssf)
            last_key_prestime_f2 = current_time
            assets.screenshot_sfx.play()

        # *Fill screen
        if state == "game":  # Check if the state is in gameplay to make colour changes
            if life == 3 or life == 4 or life == 5:
                fillc = 0, 0, 0  # Use black if life is 3 or more
            elif life == 2:
                fillc = 25, 0, 0  # Use a dark red if life is 2
            elif life == 1:
                fillc = 50, 0, 0  # Use a brighter, yet still dark red if life is critically low at 1
        else:
            fillc = 0, 0, 0  # Stay at black when not in gameplay
        screen.fill((fillc))  # Finally, fill the screen with the chosen colour

        text_surface = fpfont.render(f"FPS: {fps}", True, (255, 255, 255))
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
        bgrect = assets.bg_r.get_rect()
        bgrect.centerx = screen.get_width() // 2
        bgrect.y = 44
        if not state == "intro":  # Allows the black background in the intro
            if bg == 1:
                screen.blit(assets.bg_r, (bgrect))
            elif bg == 2:
                screen.blit(assets.bg_o, (bgrect))
            elif bg == 3:
                screen.blit(assets.bg_y, (bgrect))
            elif bg == 4:
                screen.blit(assets.bg_g, (bgrect))
            elif bg == 5:
                screen.blit(assets.bg_b, (bgrect))
            elif bg == 6:
                screen.blit(assets.bg_pu, (bgrect))
            elif bg == 7:
                screen.blit(assets.bg_pi, (bgrect))
            elif bg == 8:
                screen.blit(assets.bg_gg, (bgrect))
            elif bg == 9:
                screen.blit(assets.bg_db, (bgrect))
            elif bg == 10:
                screen.blit(assets.bg_mg, (bgrect))
            elif bg == 11:
                screen.blit(assets.bg_gr, (bgrect))

        # *Intro loop
        if state == "intro":  #! Possibly not done yet
            introtick += 1
            if intropart == 1:
                if not introtick >= 150:  # Rotate if 150 ticks have not passed
                    jrot += 5
                if not introtick >= 150:
                    rjriimg = pygame.transform.rotate(assets.jris_img, jrot)  # Rotate the image
                    # Get a rect centered around a fixed position
                    img_rect = rjriimg.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))  # Make img_rect
                    jx = img_rect.x
                    # Blit the rotated image at this position
                    screen.blit(rjriimg, img_rect)

                if introtick >= 150:  # Begin second part if 150 ticks have passed
                    if played_jris2 == False:
                        assets.intro1_sfx.play()
                        played_jris2 = True
                    if not jtxt_alpha >= 255:
                        jtxt_alpha += 15  # Change alpha value of text
                    jtxt = pygame.image.load("assets/images/other/intro/txt.png").convert_alpha()  # Load new text
                    jtxt.set_alpha(jtxt_alpha)
                    jtxt = pygame.transform.scale(jtxt, (427, 108))
                    if not jx <= 150:
                        jx_div = jx // 10
                        jx -= jx_div
                        if jx == 4:
                            jx = 0
                    img_rect = rjriimg.get_rect(center=(jx, screen.get_height() // 2))
                    screen.blit(rjriimg, (img_rect))
                    screen.blit(jtxt, (200, 260))
                if introtick == 340:
                    intropart = 2
                    introtick = 0
            else:
                proudlypresents = pygame.image.load("assets/images/other/intro/proudlypresents.png").convert_alpha()
                proudlypresents = pygame.transform.scale(proudlypresents, (496, 236))
                propre_alpha += 10
                proudlypresents.set_alpha(propre_alpha)
                img_rect = proudlypresents.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
                screen.blit(proudlypresents, (img_rect))
                if introtick >= 200:
                    state = "title"

        if state == "title":
            #! Cancled, but remains in code for hopes of help. Renders a mute music toggle.
            # music_rect = musicf.get_rect()
            # music_rect.x = 30
            # music_rect.y = 50
            # if music_rect.collidepoint(mouse_x, mouse_y):
            #     music_rect.y = 45
            #     if mb[0] and (current_time - last_key_prestime >= key_delay):  # Prevent repetitive presses
            #         if mute:
            #             mute = False
            #             play_music()  # Ensure music plays when unmuted
            #         else:
            #             mute = True
            #             main_ost.stop()  # Stop music when muted
            #             gameplay_ost.stop()
            #         last_key_prestime = current_time

            # Render the music toggle icon based on mute state
            # if mute:
            #     screen.blit(musicf, (music_rect))  # Mute icon
            # else:
            #     screen.blit(musict, (music_rect))  # Unmute icon

            # *Render buttons
            pygame.display.set_caption("Lifeline.py - Title Screen")
            img_rect = assets.lll_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.y = 70
            screen.blit(assets.lll_img, (img_rect))
            if area == 1:  # 1 is the main menu screen
                # Render start button
                img_rect = assets.start_t_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 270
                if sel == 1:
                    screen.blit(assets.start_t_img, (img_rect))
                else:
                    screen.blit(assets.start_f_img, (img_rect))
                # Render options button
                img_rect = assets.optt_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 300
                if sel == 2:
                    screen.blit(assets.optt_img, (img_rect))
                else:
                    screen.blit(assets.optf_img, (img_rect))
                # Render updates button
                img_rect = assets.updatet_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 330
                if sel == 3:
                    screen.blit(assets.updatet_img, (img_rect))
                else:
                    screen.blit(assets.updatef_img, (img_rect))
                # Render update tick if not on latest version
                if not latestVer:
                    screen.blit(assets.upd_ping, (478, 326))
                # Render difficulty
                img_rect = assets.dif_1_f_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 360
                if sel == 4:
                    if dif == 1:
                        screen.blit(assets.dif_1_t_img, (img_rect))
                    elif dif == 2:
                        screen.blit(assets.dif_2_t_img, (img_rect))
                    elif dif == 3:
                        screen.blit(assets.dif_3_t_img, (img_rect))
                else:
                    if dif == 1:
                        screen.blit(assets.dif_1_f_img, (img_rect))
                    elif dif == 2:
                        screen.blit(assets.dif_2_f_img, (img_rect))
                    elif dif == 3:
                        screen.blit(assets.dif_3_f_img, (img_rect))
            elif area == 2: # 2 is options
            # Render background colour button
                img_rect = assets.bg_t_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 270
                if sel == 1:
                    screen.blit(assets.bg_t_img, (img_rect))
                else:
                    screen.blit(assets.bg_f_img, (img_rect))
                # Render controls button
                img_rect = assets.controls_t.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 300
                if sel == 2:
                    screen.blit(assets.controls_t, (img_rect))
                else:
                    screen.blit(assets.controls_f, (img_rect))
                # Render back button
                img_rect = assets.back_t_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 330
                if sel == 3:
                    screen.blit(assets.back_t_img, (img_rect))
                else:
                    screen.blit(assets.back_f_img, (img_rect))
            elif area == 3: #* Special, but 3 is updates, which renders a box instead of the regular buttons. This also renders and makes functions of the entirety of area 3.
                if connection: # Display update contents if connected to internet
                    img_rect = assets.updatecontent.get_rect()
                    img_rect.centerx = screen.get_width() // 2
                    img_rect.y = 270
                    screen.blit(assets.updatecontent, (img_rect))
                    text_surface = updt_font.render(upd['title'], True, (255, 255, 255))
                    screen.blit(text_surface, (70, 280))
                    text_surface = updv_font.render(f"{upd['version']} - {upd['date']}", True, (255, 255, 255))
                    screen.blit(text_surface, (70, 520))
                    dispLns()
                else: # Display no internet image
                    img_rect = assets.nointernet_img.get_rect()
                    img_rect.centerx = screen.get_width() // 2
                    img_rect.y = 320
                    screen.blit(assets.nointernet_img, (img_rect))
                if not latestVer: # Display update version if not on the latest version
                    updb_rect = assets.upd_button.get_rect()
                    updb_rect.centerx = screen.get_width() // 2
                    updb_rect.y = 550
                    if updb_rect.collidepoint(mouse_x, mouse_y): # Check if mouse is touching hitbox:
                        updb_rect.y = 545
                        if mb[0] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering:
                            webbrowser.open("https://jasperredis.github.io/Lifeline.py")
                            sysnotif("Lifeline.py", "Not getting the browser window? Try opening it manually, as it may have not maximised the window.", 5)
                            last_key_prestime = current_time
                    screen.blit(assets.upd_button, (updb_rect))
                #* Add clickable buttons
                refb_rect = assets.refb.get_rect() # Display and make refresh button work
                if latestVer:
                    refb_rect.centerx = screen.get_width() // 2 + 97
                else:
                    refb_rect.centerx = screen.get_width() // 2 + 199
                refb_rect.y = 550
                if refb_rect.collidepoint(mouse_x, mouse_y): # Check if mouse is touching hitbox
                    refb_rect.y = 545
                    if mb[0] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                        connection = isconnected()
                        if connection:
                            fetchUpdates()
                            if float(upd['version']) == version and connection:
                                latestVer = True
                            else:
                                if not connection: # Tell the game that it's on the latest version so that the update button doesn't display with no connection
                                    latestVer = True
                                else:
                                    latestVer = False
                        last_key_prestime = current_time
                screen.blit(assets.refb, (refb_rect))
                
                prev_rect = assets.prev_pg.get_rect() # Display and make previous page button work
                if latestVer:
                    prev_rect.centerx = screen.get_width() // 2 - 217
                else:
                    prev_rect.centerx = screen.get_width() // 2 - 317
                prev_rect.y = 550
                if prev_rect.collidepoint(mouse_x, mouse_y): # Check if mouse is touching hitbox:
                    prev_rect.y = 545
                    if mb[0] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                        pg -= 1
                        if pg < 1:
                            pg = 1
                        assets.move_sel_sfx.play()
                        last_key_prestime = current_time
                screen.blit(assets.prev_pg, (prev_rect))

                next_rect = assets.next_pg.get_rect() # Display and make next page button work
                if latestVer:
                    next_rect.centerx = screen.get_width() // 2 + 217
                else:
                    next_rect.centerx = screen.get_width() // 2 + 317
                next_rect.y = 550
                if next_rect.collidepoint(mouse_x, mouse_y): # Check if mouse is touching hitbox
                    next_rect.y = 545
                    if mb[0] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering:
                        pg += 1
                        if pg > upd['pgs']:
                            pg = upd['pgs']
                        assets.move_sel_sfx.play()
                        last_key_prestime = current_time
                screen.blit(assets.next_pg, (next_rect))

                # Back button is last in order so that module-related bugs don't occur
                bacb_rect = assets.bacb.get_rect() # Display and make back button work
                if latestVer:
                    bacb_rect.centerx = screen.get_width() // 2 - 97
                else:
                    bacb_rect.centerx = screen.get_width() // 2 - 199
                bacb_rect.y = 550
                if bacb_rect.collidepoint(mouse_x, mouse_y): # Check if mouse is touching hitbox:
                    bacb_rect.y = 545
                    if mb[0]:
                        ld_imgc("tts1")
                        area = 1
                        unld_img("updates")
                        assets.sel_sfx.play()
                    else:
                        screen.blit(assets.bacb, (bacb_rect))
                else:
                    screen.blit(assets.bacb, (bacb_rect))

                if not seen_upd: # Show notification
                    if ingnotif(updnt, updnf, "tl"):
                        seen_upd = True

            elif area == 4: #* 4 is controls
                img_rect = assets.controls_m.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.centery = screen.get_height() // 2
                screen.blit(assets.controls_m, (img_rect))
                # Render table top
                text_surface = controls_fnt.render("Action", True, (255, 255, 255))
                screen.blit(text_surface, (85, 145))
                text_surface = controls_fnt.render("Key", True, (255, 255, 255))
                screen.blit(text_surface, (675, 145))
                # Render the actual control config
                # Render the selection bar
                if sel == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (70, 175, 656, 22))
                elif sel == 2:
                    pygame.draw.rect(screen, (255, 255, 255), (70, 195, 656, 22))
                elif sel == 3:
                    pygame.draw.rect(screen, (255, 255, 255), (70, 215, 656, 22))
                elif sel == 4:
                    pygame.draw.rect(screen, (255, 255, 255), (70, 235, 656, 22))
                elif sel == 5:
                    pygame.draw.rect(screen, (255, 255, 255), (70, 255, 656, 22))
                elif sel == 6:
                    pygame.draw.rect(screen, (255, 255, 255), (70, 275, 656, 22))
                elif sel == 7:
                    pygame.draw.rect(screen, (255, 255, 255), (70, 295, 656, 22))
                elif sel == 8:
                    pygame.draw.rect(screen, (255, 255, 255), (70, 315, 656, 22))
                elif sel == 9:
                    pygame.draw.rect(screen, (255, 255, 255), (70, 335, 656, 22)) 
                elif sel == 10:
                    pygame.draw.rect(screen, (255, 255, 255), (70, 375, 656, 22))
                # Render the names of the actions
                if sel == 1: # Move Left
                    text_surface = controls_fnt.render("Move Left", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render("Move Left", True, (255, 255, 255))
                screen.blit(text_surface, (85, 175))
                if sel == 2: # Move Right
                    text_surface = controls_fnt.render("Move Right", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render("Move Right", True, (255, 255, 255))
                screen.blit(text_surface, (85, 195))
                if sel == 3: # Pause
                    text_surface = controls_fnt.render("Pause", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render("Pause", True, (255, 255, 255))
                screen.blit(text_surface, (85, 215))
                if sel == 4: # Navigate up in menus
                    text_surface = controls_fnt.render("Navigate Up in Menus", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render("Navigate Up in Menus", True, (255, 255, 255))
                screen.blit(text_surface, (85, 235))
                if sel == 5: # Navigate down in menus
                    text_surface = controls_fnt.render("Navigate Down in Menus", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render("Navigate Down in Menus", True, (255, 255, 255))
                screen.blit(text_surface, (85, 255))
                if sel == 6: # Navigate left in menus
                    text_surface = controls_fnt.render("Navigate Left in Menus", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render("Navigate Left in Menus", True, (255, 255, 255))
                screen.blit(text_surface, (85, 275))
                if sel == 7: # Navigate right in menus
                    text_surface = controls_fnt.render("Navigate Right in Menus", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render("Navigate Right in Menus", True, (255, 255, 255))
                screen.blit(text_surface, (85, 295))
                if sel == 8: # Select in title screen menus
                    text_surface = controls_fnt.render("Select in Title Screen Menus", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render("Select in Title Screen Menus", True, (255, 255, 255))
                screen.blit(text_surface, (85, 315))
                if sel == 9: # Select in pause menu
                    text_surface = controls_fnt.render("Select in Pause Menu", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render("Select in Pause Menu", True, (255, 255, 255))
                screen.blit(text_surface, (85, 335))
                #* Render the actual keybinds
                with open("json/keybinds.json", 'r') as file:
                    keybnds = json.load(file)
                if sel == 1: # Move Left
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['mv_l']}", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['mv_l']}", True, (255, 255, 255))
                screen.blit(text_surface, (675, 175))
                if sel == 2: # Move Right
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['mv_r']}", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['mv_r']}", True, (255, 255, 255))
                screen.blit(text_surface, (675, 195))
                if sel == 3: # Pause
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['pause']}", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['pause']}", True, (255, 255, 255))
                screen.blit(text_surface, (675, 215))
                if sel == 4: # Navigate up in menus
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['nav_up']}", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['nav_up']}", True, (255, 255, 255))
                screen.blit(text_surface, (675, 235))
                if sel == 5: # Navigate down in menus
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['nav_dn']}", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['nav_dn']}", True, (255, 255, 255))
                screen.blit(text_surface, (675, 255))
                if sel == 6: # Navigate left in menus
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['nav_lf']}", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['nav_lf']}", True, (255, 255, 255))
                screen.blit(text_surface, (675, 275))
                if sel == 7: # Navigate right in menus
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['nav_rt']}", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['nav_rt']}", True, (255, 255, 255))
                screen.blit(text_surface, (675, 295))
                if sel == 8: # Select in title screen menus
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['m_sel']}", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['m_sel']}", True, (255, 255, 255))
                screen.blit(text_surface, (675, 315))
                if sel == 9: # Select in pause menu
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['p_sel']}", True, (0, 0, 0))
                else:
                    text_surface = controls_fnt.render(f"{keybnds['keybinds']['p_sel']}", True, (255, 255, 255))
                screen.blit(text_surface, (675, 335))
                #* Display Help Option
                if sel == 10:
                    text_surface = controls_fnt.render("Help", True, (0, 0, 0))
                    if keys[pygame.K_RETURN]:
                        messagebox.showinfo("Lifeline.py", "Not here yet!")
                else:
                    text_surface = controls_fnt.render("Help", True, (255, 255, 255))
                screen.blit(text_surface, (85, 375))
                #* Display info text
                text_surface = controls_fnt.render("Press ENT. (Enter) to change a keybind.", True, (255, 255, 255))
                screen.blit(text_surface, (85, 395))
                text_surface = controls_fnt.render("Press ESC. (Escape) while not modifying a keybind to exit this menu.", True, (255, 255, 255))
                screen.blit(text_surface, (85, 415))
                text_surface = controls_fnt.render("Press Shift+ESC. to cancel a modification.", True, (255, 255, 255))
                screen.blit(text_surface, (85, 435))
                text_surface = controls_fnt.render("SPC. is Spacebar. DWN. is the down arrow.", True, (255, 255, 255))
                screen.blit(text_surface, (85, 455))
                text_surface = controls_fnt.render("<- is the left arrow. -> is the right arrow.", True, (255, 255, 255))
                screen.blit(text_surface, (85, 475))
                #* Take key input
                if keys[pygame.K_ESCAPE]:
                    area = 2
                    assets.sel_sfx.play()

            # *Menu Navigation
            # Scroll up
            if keys[pygame.K_UP] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                if not area == 3:
                    sel -= 1
                    if sel < 1: # Make sure that sel (selected option) doesn't exceed limits
                        sel = 1
                    assets.move_sel_sfx.play()
                    last_key_prestime = current_time
            # Scroll down
            if keys[pygame.K_DOWN] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                if not area == 3:
                    sel += 1
                    if area == 1 and sel >= 5: # Make sure that sel (selected option) doesn't exceed limits
                        sel = 1
                    elif area == 2 and sel > 3: # Make sure that sel (selected option) doesn't exceed limits
                        sel = 3
                    elif area == 4 and sel > 10:
                        sel = 10
                    assets.move_sel_sfx.play()
                    last_key_prestime = current_time
            # Select options
            if keys[pygame.K_RETURN] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                if sel == 1 and area == 1: # Start button
                    ld_imgc("gameplay")
                    ld_audc("gameplay")
                    initGame()
                    unld_img("ttsALL")
                    unld_img("tts1")
                if sel == 2 and area == 1: # Background colour
                    ld_imgc("options")
                    area = 2 # 2 is options
                    sel = 1
                    unld_img("tts1")
                if sel == 3 and area == 1: # Updates button
                    ld_imgc("updates")
                    area = 3 # 3 is updates
                    sel = 1
                    pg = 1
                    unld_img("tts1")
                elif sel == 3 and area == 2: # Back button in options
                    ld_imgc("tts1")
                    area = 1 # 1 is the main page
                    unld_img("options")
                elif sel == 2 and area == 2:
                    ld_imgc("controls")
                    unld_img("tts1")
                    area = 4 # 4 is controls
                    sel = 1
                if area == 4:
                    if sel == 1:
                        sel_kbnd = "mv_l"
                    elif sel == 2:
                        sel_kbnd = "mv_r"
                    elif sel == 3:
                        sel_kbnd = "pause"
                    elif sel == 4:
                        sel_kbnd = "nav_up"
                    elif sel == 5:
                        sel_kbnd = "nav_dn"
                    elif sel == 6:
                        sel_kbnd = "nav_lf"
                    elif sel == 7:
                        sel_kbnd = "nav_rt"
                    elif sel == 8:
                        sel_kbnd = "m_sel"
                    elif sel == 9:
                        sel_kbnd = "p_sel"
                assets.sel_sfx.play()
                last_key_prestime = current_time
            # Navigate other option for option buttons
            if keys[pygame.K_RIGHT] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                if sel == 4 and area == 1: # Difficulty
                    dif += 1
                    if dif == 4: # Make sure that the selected option doesn't exceed limits
                        dif = 3
                    if not dif == 2:
                        messagebox.showinfo("Warning", "The Normal (yellow heart) difficulty has attempted to strike a balance in gameplay. Other difficulties disturb this balance and do not make optimal gameplay. Work will be done in future updates to fix this.")
                    assets.move_sel_sfx.play()
                    last_key_prestime = current_time
                if sel == 1 and area == 2: # Background colour
                    bg += 1
                    if bg == 12:  # Make sure that the selected option doesn't exceed limits
                        bg = 1
                    assets.move_sel_sfx.play()
                    last_key_prestime = current_time
        
            if keys[pygame.K_LEFT] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                if sel == 4 and area == 1: # Difficulty
                    dif -= 1
                    if dif == 0:   # Make sure that the selected option doesn't exceed limits
                        dif = 1
                    if not dif == 2:
                        messagebox.showinfo("Warning", "The Normal (yellow heart) difficulty has attempted to strike a balance in gameplay. Other difficulties disturb this balance and do not make optimal gameplay.")
                    assets.move_sel_sfx.play()
                    last_key_prestime = current_time
                if sel == 1 and area == 2: # Background colour
                    bg -= 1
                    if bg == 0:   # Make sure that the selected option doesn't exceed limits
                        bg = 11
                    assets.move_sel_sfx.play()
                    last_key_prestime = current_time

        # *Game Loop
        if state == "game":
            pygame.display.set_caption("Lifeline.py - Ingame")
            # Bar display script
            img_rect = assets.bar_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.centery = screen.get_height() // 2
            screen.blit(assets.bar_img, (img_rect))
            img_rect = assets.plr_img.get_rect()

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
                        if plrx > 640:
                            plrx = 640
                    elif keys[pygame.K_a]:
                        plrx -= 10
                        if plrx < 148:
                            plrx = 148

            # Player display script
            plr_rect = assets.plr_img.get_rect()
            plr_rect.x = plrx
            plr_rect.centery = screen.get_height() // 2
            screen.blit(assets.plr_img, (plr_rect))

            # Check protection script
            if protection == True:
                if current_time - last_prot >= 500:
                    protection = False

            # Effects display script
            img_rect = assets.plr_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.y = 5
            if protection == True:
                screen.blit(assets.protected_eff, img_rect)

            # Life display script
            if life < 1:
                img_rect = assets.gameover_img.get_rect()
                img_rect.centerx = screen.get_width() // 5
                img_rect.y = screen.get_height() // 2 + 20
                screen.blit(assets.gameover_img, (img_rect))
            else:
                img_rect = assets.L5_img.get_rect()
                img_rect.centerx = screen.get_width() // 5
                img_rect.y = screen.get_height() // 2 + 20
                if life == 5:
                    screen.blit(assets.L5_img, (img_rect))
                elif life == 4:
                    screen.blit(assets.L4_img, (img_rect))
                elif life == 3:
                    screen.blit(assets.L3_img, (img_rect))
                elif life == 2:
                    screen.blit(assets.L2_img, (img_rect))
                elif life == 1:
                    screen.blit(assets.L1_img, (img_rect))

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
                screen.blit(assets.enemy_img, (ex, ey))
                en_rect = pygame.Rect(ex, ey, assets.enemy_img.get_width(), assets.enemy_img.get_height())

                if plr_rect.colliderect(en_rect) and protection == False:
                    enemies.remove(en)
                    life -= 1
                    last_prot = current_time
                    protection = True
                    assets.lostlife_sfx.play()
                    if life < 1:
                        gameover = True
                        totalscore += score

            # Heal script
            for h in heals:
                hx, hy = h
                screen.blit(assets.heal_img, (hx, hy))
                h_rect = pygame.Rect(hx, hy, assets.heal_img.get_width(), assets.heal_img.get_height())

                if plr_rect.colliderect(h_rect):
                    heals.remove(h)
                    life += 1
                    assets.heal_sfx.play()
                    if life > 5:
                        life = 5

            # Activate pause
            if keys[pygame.K_ESCAPE] and paused == False and gameover == False:
                paused = True
                sel = 1
                assets.sel_sfx.play()

            # *Pause script
            if paused == True and gameover == False:
                img_rect.centerx = screen.get_width() // 10
                img_rect.y = 560
                screen.blit(assets.pause_barcontent, (img_rect))
                img_rect.centerx = screen.get_width() // 2.5
                img_rect.centery = screen.get_height() // 2.5
                if sel == 1:
                    screen.blit(assets.pause_1_img, (img_rect))
                elif sel == 2:
                    screen.blit(assets.pause_2_img, (img_rect))
                elif sel == 3:
                    screen.blit(assets.pause_3_img, (img_rect))

                if keys[pygame.K_DOWN] and (current_time - last_key_prestime >= key_delay):
                    sel += 1
                    if sel > 3:
                        sel = 3
                    assets.move_sel_sfx.play()
                    last_key_prestime = current_time

                if keys[pygame.K_UP] and (current_time - last_key_prestime >= key_delay):
                    sel -= 1
                    if sel < 1:
                        sel = 1
                    assets.move_sel_sfx.play()
                    last_key_prestime = current_time

                if keys[pygame.K_RETURN] and (current_time - last_key_prestime >= key_delay):
                    if sel == 1:
                        paused = False
                    elif sel == 2:
                        result = msgbx("Notice", "Are you sure you want to restart the game?", "yn", alerts)
                        if result:
                            initGame()
                    elif sel == 3:
                        state = "title"
                        paused = False
                        sel = 1
                    assets.sel_sfx.play()
                    last_key_prestime = current_time

            # Gameover script
            if gameover == True:
                screen.blit(assets.gameover_barcontent, (20, 560))
                if score > highscore or hsu:
                    text_surface = fpfont.render(f"New Highscore of {score}! Total Score: {totalscore}", True, (255, 255, 255))
                    highscore = score
                    hsu = True
                else:
                    text_surface = fpfont.render(f"Score: {score}, Total Score: {totalscore}", True, (255, 255, 255))
                screen.blit(text_surface, (0, 0))
                if keys[pygame.K_r]:
                    assets.sel_sfx.play()
                    initGame()
            else: # If there isnt a gameover, display the score
                if score > highscore:
                    highscore = score
                    text_surface = fpfont.render(f"Score: {score}, Highscore: {highscore}", True, (255, 255, 255))
                    screen.blit(text_surface, (0, 0))

        # *Autosave animation
        autotick += 1
        if autotick >= 5:
            autosavei += 1 # Increase frame
            if autosavei > 8: # Return to first if past frame count
                autosavei = 1
            autotick = 0
        # Render autosave icon
        if autosaving == True:
            if autosavei == 1:
                screen.blit(assets.autosave1, (5, 5))
            elif autosavei == 2:
                screen.blit(assets.autosave2, (5, 5))
            elif autosavei == 3:
                screen.blit(assets.autosave3, (5, 5))
            elif autosavei == 4:
                screen.blit(assets.autosave4, (5, 5))
            elif autosavei == 5:
                screen.blit(assets.autosave5, (5, 5))
            elif autosavei == 6:
                screen.blit(assets.autosave6, (5, 5))
            elif autosavei == 7:
                screen.blit(assets.autosave7, (5, 5))
            elif autosavei == 8:
                screen.blit(assets.autosave8, (5, 5))

        if mouse_y < 45: # Show X and fullscreen/minimize if mouse is at top
            xhb = assets.xt_img.get_rect() #* Make for X button
            xhb.x = screen.get_width() // 2 - 10 #XHB stands for X HitBox
            xhb.y = 0
            if xhb.collidepoint(mouse_x, mouse_y): # Check if mouse is touching hitbox
                screen.blit(assets.xt_img, (xhb))
                if mb[0]: # Check if mouse is down
                    byebye() # End the program
            else:
                screen.blit(assets.xf_img, (xhb))
            fmhb = assets.mt_img.get_rect() #* Make rect for minimize/fullscreen button
            fmhb.x = screen.get_width() // 2 + 10 #FMHB stands for Fullscreen/Minimize HitBox
            fmhb.y = 0
            if fmhb.collidepoint(mouse_x, mouse_y): # Check if mouse is touching hitbox
                if window == "b": # Check if window is bordered
                    screen.blit(assets.ft_img, (fmhb))
                    if mb[0] and (current_time - last_key_prestime >= key_delay): # Check if mouse is down and avoid repetitive presses
                        window = "f"
                        if not osnm == "Linux":
                            msgbx("Warning", "Notifications like these do not work in fullscreen and will cause bugs if you do anything that makes them.", "ok", alerts)
                        else:
                            msgbx("Warning", "It seems that you're running Linux. Keep in mind that fullscreen mode is incredibly buggy in Linux. Not only that, notifications like this one will not work.", "ok", alerts)
                        makeDisp() # Refresh window
                        last_key_prestime = current_time # Reset last key press
                else: # Else if window is fullscreen
                    screen.blit(assets.mt_img, (fmhb))
                    if mb[0] and (current_time - last_key_prestime >= key_delay): # Check if mouse is down and avoid repetitive presses
                        window = "b"
                        makeDisp() # Refresh window
                        last_key_prestime = current_time # Reset last key press
            else:
                if window == "b": # Check if window is bordered
                    screen.blit(assets.ff_img, (fmhb))
                else: # Else if window is fullscreen
                    screen.blit(assets.mf_img, (fmhb))

        play_music()

        screen.blit(assets.mouse_img, (mouse_x, mouse_y)) # Render mouse
        pygame.display.flip() # Update screen

        # Set the frame rate
        clock.tick(60)
# Quit pygame
pygame.quit()
sys.exit()
