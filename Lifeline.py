# /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
# |  Lifeline.py - Version 1.1                           |
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
import colorama
from colorama import Fore, Back, Style, init
import plyer
from plyer import notification
import platform

def sysnotif(t, d, c):
    try:
        notification.notify(
        title=t,   # Title of the notification
        message=d, # Message content
        timeout=c  # Duration in seconds the notification will stay visible
        )
    except:
        messagebox.showinfo("Error", "Could not make a notification!")
#* Send basic notification
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

def kill_application():
    sysnotif("Lifeline.py", "Goodbye! Thanks for playing Lifeline.py!", 5)
    pygame.quit()
    sys.exit()

# *Load saved data
txtprnt = (Fore.MAGENTA + "OPENING:" + Fore.LIGHTCYAN_EX + " json/saved.json" + Style.RESET_ALL + "...")
print(txtprnt)
try:
    with open("json/saved.json", 'r') as file:
        saved_info = json.load(file)
        txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Fore.LIGHTCYAN_EX + "opened json/saved.json and saved to variable" + Style.RESET_ALL + "!")
        print(txtprnt)
except Exception as e:  # Close the program upon error and provide reason
    messagebox.showinfo("Error", f"Could not load saved.json because of provided reason: {e}")
    kill_application()

# *Set settings to preferences (previous settings)
txtprnt = (Fore.MAGENTA + "LOADING SAVE DATA" + Style.RESET_ALL + "...")
print(txtprnt)
bg = saved_info['bg']  # The background colour, defaulted to 7 (pink)
if bg < 1 or bg > 11:
    bg = 7  # Default to pink if invalid
# A list of all background numbers and their corresponding colours can be found in the main loop where the background is rendered
window = saved_info['window']  # Controls whether the window is windowed borderless or fullscreen, defaulted to windowed borderless
mute = saved_info['mute']  # Controls whether audio is muted or not, defaulted to false
movmod = saved_info['movemode']  # Controls whether the player moves with WASD or their mouse, defaulted to WASD
highscore = saved_info['highscore']  # Highscore, self-explanatory.
totalscore = saved_info['totalscore']  # All scores ever gotten, added together.
gamesplayed = saved_info['gamesplayed']  # How many games the user has played.
alerts = saved_info['allow_alerts']  # Whether alerts are allowed.
seen_upd = saved_info['seen_updates']
txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Style.RESET_ALL + "Loaded save data")
print(txtprnt)

# *Set up the display
txtprnt = (Fore.MAGENTA + "SETTING UP WINDOW" + Style.RESET_ALL + "...")
print(txtprnt)
def makeDisp():
    global window, screen
    if window == "b":  # b stands for borderless
        screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)  # 800x600 window
    else:  # else is to prevent unnecessary use of an elif and a possible fallback (this is fullscreen)
        screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)  # 800x600 window
makeDisp()
pygame.display.set_caption("Lifeline.py - Intro")
txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Style.RESET_ALL + "Set up window")
print(txtprnt)

imaud_ind = 1
each_perc = 1.21951219512  # ! This needs to be manually updated!
perc = each_perc
txtprnt = ""
ttl_assets = 82

def ld_img(path, default, w, h):
    global ldimg_temp, ldimg_w, ldimg_h, ldimg_new_w, ldimg_new_h, imaud_ind, perc, each_perc, txtprnt, ttl_assets
    txtprnt = (Fore.MAGENTA + f"LOADING IMAGE " + Fore.LIGHTGREEN_EX + str(imaud_ind) + Style.RESET_ALL + 
            "/" + Fore.LIGHTGREEN_EX + str(ttl_assets) + Style.RESET_ALL + 
            ": " + Fore.LIGHTCYAN_EX + path + Style.RESET_ALL + 
            "... (" + Fore.LIGHTGREEN_EX + f"{int(perc)}%" + Style.RESET_ALL + ")")
    print(txtprnt)
    ldimg_temp = pygame.image.load(path)
    ldimg_w = ldimg_temp.get_width()
    ldimg_h = ldimg_temp.get_height()
    imaud_ind += 1
    perc += each_perc
    if default:
        ldimg_new_w = ldimg_w * 4
        ldimg_new_h = ldimg_h * 4
        return pygame.transform.scale(ldimg_temp, (ldimg_new_w, ldimg_new_h))
    else:
        return pygame.transform.scale(ldimg_temp, (w, h))

def msgbx(title, description, okyn):
    global alerts
    if alerts:
        if okyn == "yn":
            return messagebox.askyesno(title, description)
        else:
            messagebox.showinfo(title, description)

# *Load Images
try:
    bg_r = ld_img("assets/images/bg/bgs/red.png", False, 800, 512)
    bg_o = ld_img("assets/images/bg/bgs/orange.png", False, 800, 512)
    bg_y = ld_img("assets/images/bg/bgs/yellow.png", False, 800, 512)
    bg_g = ld_img("assets/images/bg/bgs/green.png", False, 800, 512)
    bg_gg = ld_img("assets/images/bg/bgs/greener green.png", False, 800, 512)
    bg_b = ld_img("assets/images/bg/bgs/blue.png", False, 800, 512)
    bg_db = ld_img("assets/images/bg/bgs/dark blue.png", False, 800, 512)
    bg_pi = ld_img("assets/images/bg/bgs/pink.png", False, 800, 512)
    bg_pu = ld_img("assets/images/bg/bgs/purple.png", False, 800, 512)
    bg_mg = ld_img("assets/images/bg/bgs/mint green.png", False, 800, 512)
    bg_gr = ld_img("assets/images/bg/bgs/grey.png", False, 800, 512)
    lll_img = ld_img("assets/images/title/other/lifeline logo.png", True, None, None)
    optt_img = ld_img("assets/images/title/buttons/opts/true.png", True, None, None)
    optf_img = ld_img("assets/images/title/buttons/opts/false.png", True, None, None)
    start_t_img = ld_img("assets/images/title/buttons/start/true.png", True, None, None)
    start_f_img = ld_img("assets/images/title/buttons/start/false.png", True, None, None)
    bar_img = ld_img("assets/images/ingame/bar.png", True, None, None)
    plr_img = ld_img("assets/images/ingame/plr.png", True, None, None)
    L1_img = ld_img("assets/images/ingame/life/1.png", True, None, None)
    L2_img = ld_img("assets/images/ingame/life/2.png", True, None, None)
    L3_img = ld_img("assets/images/ingame/life/3.png", True, None, None)
    L4_img = ld_img("assets/images/ingame/life/4.png", True, None, None)
    L5_img = ld_img("assets/images/ingame/life/5.png", True, None, None)
    enemy_img = ld_img("assets/images/ingame/enemy.png", True, None, None)
    heal_img = ld_img("assets/images/ingame/heal.png", True, None, None)
    stop_img = ld_img("assets/images/ingame/stop.png", True, None, None)
    pause_1_img = ld_img("assets/images/ingame/pause/1.png", True, None, None)
    pause_2_img = ld_img("assets/images/ingame/pause/2.png", True, None, None)
    pause_3_img = ld_img("assets/images/ingame/pause/3.png", True, None, None)
    pause_barcontent = ld_img("assets/images/bars/bottom/ingame/pause.png", True, None, None)
    dif_1_t_img = ld_img("assets/images/title/difficulty/1/true.png", True, None, None)
    dif_1_f_img = ld_img("assets/images/title/difficulty/1/false.png", True, None, None)
    dif_2_t_img = ld_img("assets/images/title/difficulty/2/true.png", True, None, None)
    dif_2_f_img = ld_img("assets/images/title/difficulty/2/false.png", True, None, None)
    dif_3_t_img = ld_img("assets/images/title/difficulty/3/true.png", True, None, None)
    dif_3_f_img = ld_img("assets/images/title/difficulty/3/false.png", True, None, None)
    bg_t_img = ld_img("assets/images/title/buttons/bg/true.png", True, None, None)
    bg_f_img = ld_img("assets/images/title/buttons/bg/false.png", True, None, None)
    gameover_img = ld_img("assets/images/ingame/life/0.png", True, None, None)
    vol_10 = ld_img("assets/images/bars/top/vol/1.png", True, None, None)
    vol_08 = ld_img("assets/images/bars/top/vol/0.8.png", True, None, None)
    vol_06 = ld_img("assets/images/bars/top/vol/0.6.png", True, None, None)
    vol_04 = ld_img("assets/images/bars/top/vol/0.4.png", True, None, None)
    vol_02 = ld_img("assets/images/bars/top/vol/0.2.png", True, None, None)
    vol_00 = ld_img("assets/images/bars/top/vol/0.png", True, None, None)
    protected_eff = ld_img("assets/images/bars/top/effects/protected.png", True, None, None)
    gameover_barcontent = ld_img("assets/images/bars/bottom/ingame/gameover.png", True, None, None)
    autosave1 = ld_img("assets/images/other/autosave/f1.png", True, None, None)
    autosave2 = ld_img("assets/images/other/autosave/f2.png", True, None, None)
    autosave3 = ld_img("assets/images/other/autosave/f3.png", True, None, None)
    autosave4 = ld_img("assets/images/other/autosave/f4.png", True, None, None)
    autosave5 = ld_img("assets/images/other/autosave/f5.png", True, None, None)
    autosave6 = ld_img("assets/images/other/autosave/f6.png", True, None, None)
    autosave7 = ld_img("assets/images/other/autosave/f7.png", True, None, None)
    autosave8 = ld_img("assets/images/other/autosave/f8.png", True, None, None)
    jris_img = ld_img("assets/images/other/intro/jris.png", True, None, None)
    updatet_img = ld_img("assets/images/title/buttons/updates/true.png", True, None, None)
    updatef_img = ld_img("assets/images/title/buttons/updates/false.png", True, None, None)
    updatecontent = ld_img("assets/images/title/updates/contentbox/contentbox.png", True, None, None)
    nointernet_img = ld_img("assets/images/title/updates/contentbox/no internet.png", True, None, None)
    updatebarcontent = ld_img("assets/images/bars/bottom/title/updates.png", True, None, None)
    upd_button = ld_img("assets/images/title/updates/buttons/update.png", True, None, None)
    back_t_img = ld_img("assets/images/title/buttons/back/true.png", True, None, None)
    back_f_img = ld_img("assets/images/title/buttons/back/false.png", True, None, None)
    mouse_img = ld_img("assets/images/other/other/mouse.png", True, None, None)
    windicon = ld_img("windicon.png", True, None, None)
    xt_img = ld_img("assets/images/other/other/xt.png", True, None, None)
    xf_img = ld_img("assets/images/other/other/xf.png", True, None, None)
    ft_img = ld_img("assets/images/other/other/ft.png", True, None, None)
    ff_img = ld_img("assets/images/other/other/ff.png", True, None, None)
    mt_img = ld_img("assets/images/other/other/mt.png", True, None, None)
    mf_img = ld_img("assets/images/other/other/mf.png", True, None, None)
    upd_ping = ld_img("assets/images/title/updates/other/ping.png", True, None, None)
    bacb = ld_img("assets/images/title/updates/buttons/back.png", True, None, None)
    refb = ld_img("assets/images/title/updates/buttons/refresh.png", True, None, None)
    prev_pg = ld_img("assets/images/title/updates/buttons/previous.png", True, None, None)
    next_pg = ld_img("assets/images/title/updates/buttons/next.png", True, None, None)
    updnf = ld_img("assets/images/notifs/updf.png", True, None, None)
    updnt = ld_img("assets/images/notifs/updt.png", True, None, None)
    previews_img = ld_img("assets/images/bg/selecter/previews.png", True, None, None)
    pointer_t = ld_img("assets/images/bg/selecter/pointert.png", True, None, None)
    pointer_t = ld_img("assets/images/bg/selecter/pointerf.png", True, None, None)

    txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED!" + Fore.MAGENTA + " Loaded all images!")
    print(txtprnt)
except Exception as e:
    with open("log.txt", "a") as log_file:
        log_file.write(f"Error loading images: {e}\n")
    msgbx("Error", f"Could not load images because: {e}. Saved to log.", "ok")
    kill_application()

# Set window icon
pygame.display.set_icon(windicon)

def ld_aud(path):
    global imaud_ind, perc, each_perc, txtprnt
    if perc > 99:
        perc = 100
    txtprnt = (Fore.MAGENTA + f"LOADING SOUND " + Fore.LIGHTGREEN_EX + str(imaud_ind) + Style.RESET_ALL + 
            "/" + Fore.LIGHTGREEN_EX + str(ttl_assets) + Style.RESET_ALL + 
            ": " + Fore.LIGHTCYAN_EX + path + Style.RESET_ALL + 
            "... (" + Fore.LIGHTGREEN_EX + f"{int(perc)}%" + Style.RESET_ALL + ")")
    print(txtprnt)
    imaud_ind += 1
    perc += each_perc
    return pygame.mixer.Sound(path)

# Declare Sounds
try:
    move_sel_sfx = ld_aud("assets/audio/sfx/move_sel.ogg")
    sel_sfx = ld_aud("assets/audio/sfx/sel.ogg")
    screenshot_sfx = ld_aud("assets/audio/sfx/screenshot.ogg")
    lostlife_sfx = ld_aud("assets/audio/sfx/lostlife.ogg")
    heal_sfx = ld_aud("assets/audio/sfx/heal.ogg")
    intro1_sfx = ld_aud("assets/audio/sfx/jris1.ogg")
    intro2_sfx = ld_aud("assets/audio/sfx/jris3.ogg")
    main_ost = ld_aud("assets/audio/ost/main.ogg")
    gameplay_ost = ld_aud("assets/audio/ost/gameplay.ogg")
    txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED!" + Fore.MAGENTA + " Loaded all audio!")
    print(txtprnt)
except Exception as e:
    with open("log.txt", "a") as log_file:
        log_file.write(f"Error loading audio: {e}\n")
    messagebox.showinfo("Error", f"Could not load audio because: {e}. Saved to log.")
    kill_application()
txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED!" + Fore.MAGENTA + " Loaded all assets!")
print(txtprnt)

s_jris_img = pygame.transform.scale(jris_img, (150, 150))

debug_start_in_title = True

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
intro2_sfx.play()
lnscan = 0

def modifySave():
    try:
        global bg, window, mute, movmod, highscore, totalscore, gamesplayed, txtprnt
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
                "seen_updates": seen_upd
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

# *Main Loop
while running:
    try:
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

        # *Screenshot script
        if keys[pygame.K_F2] and (current_time - last_key_prestime_f2 >= key_delay_f2):
            ssf = f"screenshots/{int(time.time())}.png"
            pygame.image.save(screen, ssf)
            last_key_prestime_f2 = current_time
            screenshot_sfx.play()
            img_rect = dif_1_f_img.get_rect()
            img_rect.centerx = screen.get_width() // 2.5
            img_rect.centery = screen.get_height() // 3
            ssh = pygame.image.load(ssf)
            ssh = pygame.transform.scale(ssh, (400, 300))
            screen.blit(ssh, (img_rect))
            pygame.display.flip()
            time.sleep(0.2)

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
        bgrect = bg_r.get_rect()
        bgrect.centerx = screen.get_width() // 2
        bgrect.y = 44
        if not state == "intro":  # Allows the black background in the intro
            if bg == 1:
                screen.blit(bg_r, (bgrect))
            elif bg == 2:
                screen.blit(bg_o, (bgrect))
            elif bg == 3:
                screen.blit(bg_y, (bgrect))
            elif bg == 4:
                screen.blit(bg_g, (bgrect))
            elif bg == 5:
                screen.blit(bg_b, (bgrect))
            elif bg == 6:
                screen.blit(bg_pu, (bgrect))
            elif bg == 7:
                screen.blit(bg_pi, (bgrect))
            elif bg == 8:
                screen.blit(bg_gg, (bgrect))
            elif bg == 9:
                screen.blit(bg_db, (bgrect))
            elif bg == 10:
                screen.blit(bg_mg, (bgrect))
            elif bg == 11:
                screen.blit(bg_gr, (bgrect))

        # *Intro loop
        if state == "intro":  #! Possibly not done yet
            introtick += 1
            if intropart == 1:
                if not introtick >= 150:  # Rotate if 150 ticks have not passed
                    jrot += 5
                if not introtick >= 150:
                    rjriimg = pygame.transform.rotate(s_jris_img, jrot)  # Rotate the image
                    # Get a rect centered around a fixed position
                    img_rect = rjriimg.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))  # Make img_rect
                    jx = img_rect.x
                    # Blit the rotated image at this position
                    screen.blit(rjriimg, img_rect)

                if introtick >= 150:  # Begin second part if 150 ticks have passed
                    if played_jris2 == False:
                        intro1_sfx.play()
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
            # *Render buttons
            pygame.display.set_caption("Lifeline.py - Title Screen")
            img_rect = lll_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.y = 70
            screen.blit(lll_img, (img_rect))
            if area == 1:  # 1 is the main menu screen
                # Render start button
                img_rect = start_t_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 270
                if sel == 1:
                    screen.blit(start_t_img, (img_rect))
                else:
                    screen.blit(start_f_img, (img_rect))
                # Render options button
                img_rect = optt_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 300
                if sel == 2:
                    screen.blit(optt_img, (img_rect))
                else:
                    screen.blit(optf_img, (img_rect))
                # Render updates button
                img_rect = updatet_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 330
                if sel == 3:
                    screen.blit(updatet_img, (img_rect))
                else:
                    screen.blit(updatef_img, (img_rect))
                # Render update tick if not on latest version
                if not latestVer:
                    screen.blit(upd_ping, (478, 326))
            elif area == 2: # 2 is options
            # Render background colour button
                img_rect = bg_t_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 270
                if sel == 1:
                    screen.blit(bg_t_img, (img_rect))
                else:
                    screen.blit(bg_f_img, (img_rect))
                # Render back button
                img_rect = back_t_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 300
                if sel == 2:
                    screen.blit(back_t_img, (img_rect))
                else:
                    screen.blit(back_f_img, (img_rect))
            elif area == 3: # *Special, but 3 is updates, which renders a box instead of the regular buttons. This also renders and makes functions of the entirety of area 3.
                if connection: # Display update contents if connected to internet
                    img_rect = updatecontent.get_rect()
                    img_rect.centerx = screen.get_width() // 2
                    img_rect.y = 270
                    screen.blit(updatecontent, (img_rect))
                    text_surface = updt_font.render(upd['title'], True, (255, 255, 255))
                    screen.blit(text_surface, (70, 280))
                    text_surface = updv_font.render(f"{upd['version']} - {upd['date']}", True, (255, 255, 255))
                    screen.blit(text_surface, (70, 520))
                    dispLns()
                else: # Display no internet image
                    img_rect = nointernet_img.get_rect()
                    img_rect.centerx = screen.get_width() // 2
                    img_rect.y = 320
                    screen.blit(nointernet_img, (img_rect))
                if not latestVer: # Display update version if not on the latest version
                    updb_rect = upd_button.get_rect()
                    updb_rect.centerx = screen.get_width() // 2
                    updb_rect.y = 550
                    if updb_rect.collidepoint(mouse_x, mouse_y): # Check if mouse is touching hitbox:
                        updb_rect.y = 545
                        if mb[0] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering:
                            webbrowser.open("https://jasperredis.github.io/lifelinepy.github.io/")
                            sysnotif("Lifeline.py", "Not getting the browser window? Try opening it manually, as it may have not maximised the window.", 5)
                            last_key_prestime = current_time
                    screen.blit(upd_button, (updb_rect))

                #* Add clickable buttons
                bacb_rect = bacb.get_rect() # Display and make back button work
                if latestVer:
                    bacb_rect.centerx = screen.get_width() // 2 - 97
                else:
                    bacb_rect.centerx = screen.get_width() // 2 - 199
                bacb_rect.y = 550
                if bacb_rect.collidepoint(mouse_x, mouse_y): # Check if mouse is touching hitbox:
                    bacb_rect.y = 545
                    if mb[0]:
                        area = 1
                        sel_sfx.play()
                screen.blit(bacb, (bacb_rect))

                refb_rect = refb.get_rect() # Display and make refresh button work
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
                screen.blit(refb, (refb_rect))

                prev_rect = prev_pg.get_rect() # Display and make previous page button work
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
                        move_sel_sfx.play()
                        last_key_prestime = current_time
                screen.blit(prev_pg, (prev_rect))

                next_rect = next_pg.get_rect() # Display and make next page button work
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
                        move_sel_sfx.play()
                        last_key_prestime = current_time
                screen.blit(next_pg, (next_rect))

                if not seen_upd: # Show notification
                    if ingnotif(updnt, updnf, "tl"):
                        seen_upd = True

            # *Menu Navigation
            # Scroll up
            if keys[pygame.K_UP] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                if not area == 3:
                    sel -= 1
                    if sel < 1: # Make sure that sel (selected option) doesn't exceed limits
                        sel = 1
                    move_sel_sfx.play()
                    last_key_prestime = current_time
            # Scroll down
            if keys[pygame.K_DOWN] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                if not area == 3:
                    sel += 1
                    if area == 1 and sel >= 5: # Make sure that sel (selected option) doesn't exceed limits
                        sel = 1
                    elif area == 2 and sel >= 3: # Make sure that sel (selected option) doesn't exceed limits
                        sel = 2
                    move_sel_sfx.play()
                    last_key_prestime = current_time
            # Select options
            if keys[pygame.K_RETURN] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                if sel == 1 and area == 1: # Start button
                    initGame()
                if sel == 2 and area == 1: # Background colour
                    area = 2
                    sel = 1
                if sel == 3 and area == 1: # Updates button
                    area = 3
                    sel = 1
                    pg = 1
                elif sel == 2 and area == 2:
                    area = 1
                sel_sfx.play()
                last_key_prestime = current_time
            # Navigate other option for option buttons
            if keys[pygame.K_RIGHT] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                if sel == 4 and area == 1: # Difficulty
                    dif += 1
                    if dif == 4: # Make sure that the selected option doesn't exceed limits
                        dif = 3
                    if not dif == 2:
                        messagebox.showinfo("Warning", "The Normal (yellow heart) difficulty has attempted to strike a balance in gameplay. Other difficulties disturb this balance and do not make optimal gameplay. Work will be done in future updates to fix this.")
                    move_sel_sfx.play()
                    last_key_prestime = current_time
                if sel == 1 and area == 2: # Background colour
                    bg += 1
                    if bg == 12:  # Make sure that the selected option doesn't exceed limits
                        bg = 1
                    move_sel_sfx.play()
                    last_key_prestime = current_time
        
            if keys[pygame.K_LEFT] and (current_time - last_key_prestime >= key_delay): # Avoid repeatedly triggering
                if sel == 4 and area == 1: # Difficulty
                    dif -= 1
                    if dif == 0:   # Make sure that the selected option doesn't exceed limits
                        dif = 1
                    if not dif == 2:
                        messagebox.showinfo("Warning", "The Normal (yellow heart) difficulty has attempted to strike a balance in gameplay. Other difficulties disturb this balance and do not make optimal gameplay.")
                    move_sel_sfx.play()
                    last_key_prestime = current_time
                if sel == 1 and area == 2: # Background colour
                    bg -= 1
                    if bg == 0:   # Make sure that the selected option doesn't exceed limits
                        bg = 11
                    move_sel_sfx.play()
                    last_key_prestime = current_time

            # Render difficulty
            if area == 1:
                img_rect = dif_1_f_img.get_rect()
                img_rect.centerx = screen.get_width() // 2
                img_rect.y = 360
                if sel == 4:
                    if dif == 1:
                        screen.blit(dif_1_t_img, (img_rect))
                    elif dif == 2:
                        screen.blit(dif_2_t_img, (img_rect))
                    elif dif == 3:
                        screen.blit(dif_3_t_img, (img_rect))
                else:
                    if dif == 1:
                        screen.blit(dif_1_f_img, (img_rect))
                    elif dif == 2:
                        screen.blit(dif_2_f_img, (img_rect))
                    elif dif == 3:
                        screen.blit(dif_3_f_img, (img_rect))

        # *Game Loop
        if state == "game":
            pygame.display.set_caption("Lifeline.py - Ingame")
            # Bar display script
            img_rect = bar_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.centery = screen.get_height() // 2
            screen.blit(bar_img, (img_rect))
            img_rect = plr_img.get_rect()

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
            plr_rect = plr_img.get_rect()
            plr_rect.x = plrx
            plr_rect.centery = screen.get_height() // 2
            screen.blit(plr_img, (plr_rect))

            # Check protection script
            if protection == True:
                if current_time - last_prot >= 500:
                    protection = False

            # Effects display script
            img_rect = plr_img.get_rect()
            img_rect.centerx = screen.get_width() // 2
            img_rect.y = 5
            if protection == True:
                screen.blit(protected_eff, img_rect)

            # Life display script
            if life < 1:
                img_rect = gameover_img.get_rect()
                img_rect.centerx = screen.get_width() // 5
                img_rect.y = screen.get_height() // 2 + 20
                screen.blit(gameover_img, (img_rect))
            else:
                img_rect = L5_img.get_rect()
                img_rect.centerx = screen.get_width() // 5
                img_rect.y = screen.get_height() // 2 + 20
                if life == 5:
                    screen.blit(L5_img, (img_rect))
                elif life == 4:
                    screen.blit(L4_img, (img_rect))
                elif life == 3:
                    screen.blit(L3_img, (img_rect))
                elif life == 2:
                    screen.blit(L2_img, (img_rect))
                elif life == 1:
                    screen.blit(L1_img, (img_rect))

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
                screen.blit(enemy_img, (ex, ey))
                en_rect = pygame.Rect(ex, ey, enemy_img.get_width(), enemy_img.get_height())

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
                screen.blit(heal_img, (hx, hy))
                h_rect = pygame.Rect(hx, hy, heal_img.get_width(), heal_img.get_height())

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
                screen.blit(pause_barcontent, (img_rect))
                img_rect.centerx = screen.get_width() // 2.5
                img_rect.centery = screen.get_height() // 2.5
                if sel == 1:
                    screen.blit(pause_1_img, (img_rect))
                elif sel == 2:
                    screen.blit(pause_2_img, (img_rect))
                elif sel == 3:
                    screen.blit(pause_3_img, (img_rect))

                if keys[pygame.K_DOWN] and (current_time - last_key_prestime >= key_delay):
                    sel += 1
                    if sel > 3:
                        sel = 3
                    move_sel_sfx.play()
                    last_key_prestime = current_time

                if keys[pygame.K_UP] and (current_time - last_key_prestime >= key_delay):
                    sel -= 1
                    if sel < 1:
                        sel = 1
                    move_sel_sfx.play()
                    last_key_prestime = current_time

                if keys[pygame.K_RETURN] and (current_time - last_key_prestime >= key_delay):
                    if sel == 1:
                        paused = False
                    elif sel == 2:
                        result = msgbx("Notice", "Are you sure you want to restart the game?", "yn")
                        if result:
                            initGame()
                    elif sel == 3:
                        state = "title"
                        paused = False
                        sel = 1
                    sel_sfx.play()
                    last_key_prestime = current_time

            # Gameover script
            if gameover == True:
                screen.blit(gameover_barcontent, (20, 560))
                if score > highscore or hsu:
                    text_surface = fpfont.render(f"New Highscore of {score}! Total Score: {totalscore}", True, (255, 255, 255))
                    highscore = score
                    hsu = True
                else:
                    text_surface = fpfont.render(f"Score: {score}, Total Score: {totalscore}", True, (255, 255, 255))
                screen.blit(text_surface, (0, 0))
                if keys[pygame.K_r]:
                    sel_sfx.play()
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
                screen.blit(autosave1, (5, 5))
            elif autosavei == 2:
                screen.blit(autosave2, (5, 5))
            elif autosavei == 3:
                screen.blit(autosave3, (5, 5))
            elif autosavei == 4:
                screen.blit(autosave4, (5, 5))
            elif autosavei == 5:
                screen.blit(autosave5, (5, 5))
            elif autosavei == 6:
                screen.blit(autosave6, (5, 5))
            elif autosavei == 7:
                screen.blit(autosave7, (5, 5))
            elif autosavei == 8:
                screen.blit(autosave8, (5, 5))

        if mouse_y < 45: # Show X and fullscreen/minimize if mouse is at top
            xhb = xt_img.get_rect() #* Make for X button
            xhb.x = screen.get_width() // 2 - 10 #XHB stands for X HitBox
            xhb.y = 0
            if xhb.collidepoint(mouse_x, mouse_y): # Check if mouse is touching hitbox
                screen.blit(xt_img, (xhb))
                if mb[0]: # Check if mouse is down
                    byebye() # End the program
            else:
                screen.blit(xf_img, (xhb))
            fmhb = mt_img.get_rect() #* Make rect for minimize/fullscreen button
            fmhb.x = screen.get_width() // 2 + 10 #FMHB stands for Fullscreen/Minimize HitBox
            fmhb.y = 0
            if fmhb.collidepoint(mouse_x, mouse_y): # Check if mouse is touching hitbox
                if window == "b": # Check if window is bordered
                    screen.blit(ft_img, (fmhb))
                    if mb[0] and (current_time - last_key_prestime >= key_delay): # Check if mouse is down and avoid repetitive presses
                        window = "f"
                        if not osnm == "Linux":
                            msgbx("Warning", "Notifications like these do not work in fullscreen and will cause bugs if you do anything that makes them.", "ok")
                        else:
                            msgbx("Warning", "It seems that you're running Linux. Keep in mind that fullscreen mode is incredibly buggy in Linux. Not only that, notifications like this one will not work.", "ok")
                        makeDisp() # Refresh window
                        last_key_prestime = current_time # Reset last key press
                else: # Else if window is fullscreen
                    screen.blit(mt_img, (fmhb))
                    if mb[0] and (current_time - last_key_prestime >= key_delay): # Check if mouse is down and avoid repetitive presses
                        window = "b"
                        makeDisp() # Refresh window
                        last_key_prestime = current_time # Reset last key press
            else:
                if window == "b": # Check if window is bordered
                    screen.blit(ff_img, (fmhb))
                else: # Else if window is fullscreen
                    screen.blit(mf_img, (fmhb))

        screen.blit(mouse_img, (mouse_x, mouse_y)) # Render mouse
        pygame.display.flip() # Update screen

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
    except Exception as e:
        messagebox.showinfo("Error", f"Unexpected error: {e}")
        kill_application()
# Quit pygame
pygame.quit()
sys.exit()
