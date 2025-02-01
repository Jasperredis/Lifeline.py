
#* /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
#* |  Lifeline.py - v1.1 Beta 2.1                         |
#* |  Last updated: 2024-12-28                            |
#* |  Author: jasperredis                                 |
#* |                                                      |
#* |  This is the assets manager file for Lifeline.py.    |
#* |                                                      |
#* |  License: MIT License                                |
#* |  See the LICENSE file in the project root for more   |
#* |  information.                                        |
#* \______________________________________________________/
thismodule = "assets.py"

# Import libraries
import pygame
import colorama
from colorama import Fore, Back, Style, init
# Import modules
from error import logerr

#* Function to load an audio file
def ld_aud(path):
    global imaud_ind, ttl_assets, each_perc, perc
    try:
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
    except Exception as e:
        error.logerr(e, f"loading audio at {path}", thismodule)

#* Function to load an image
def ld_img(path, default, w, h):
    global imaud_ind, ttl_assets, each_perc, perc
    try:
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
            return pygame.transform.scale(ldimg_temp, (ldimg_w, ldimg_h))
        else:
            return pygame.transform.scale(ldimg_temp, (w, h))
    except Exception as e:
        error.logerr(e, f"loading image at {path}", thismodule)

#* Function to load all images in a category
def ld_imgc(categ):
    global imaud_ind, ttl_assets, each_perc, perc
    txtprnt = Fore.MAGENTA + f"LOADING IMAGE CATEGORY " + Style.RESET_ALL + categ + "..."
    try:
        global imaud_ind, ttl_assets
        imaud_ind = 1
        if categ == "ttsALL":
            # Set variables
            imaud_ind = 1
            ttl_assets = 1
            each_perc = 100 / ttl_assets
            perc = each_perc
            txtprnt = ""
            # Make asset global
            global lll_img
            # Load image
            lll_img = ld_img("assets/images/title/other/lifeline logo.png", True, None, None) # Lifeline.py logo
        elif categ == "tts1":
            # Set variables
            imaud_ind = 1
            ttl_assets = 13     
            each_perc = 100 / ttl_assets
            perc = each_perc
            txtprnt = ""
            # Make assets global
            global optt_img, optf_img, start_t_img, start_f_img, dif_1_t_img, dif_1_f_img, dif_2_t_img, dif_2_f_img, dif_3_t_img, dif_3_f_img, updatet_img, updatef_img, upd_ping  
            # Load images
            optt_img = ld_img("assets/images/title/buttons/opts/true.png", True, None, None) # Options button when selected
            optf_img = ld_img("assets/images/title/buttons/opts/false.png", True, None, None) # Options button when not selected
            start_t_img = ld_img("assets/images/title/buttons/start/true.png", True, None, None) # Start button when selected
            start_f_img = ld_img("assets/images/title/buttons/start/false.png", True, None, None) # Start button when not selected
            dif_1_t_img = ld_img("assets/images/title/difficulty/1/true.png", True, None, None) # Difficulty button when selected and on green
            dif_1_f_img = ld_img("assets/images/title/difficulty/1/false.png", True, None, None) # Difficulty button when not selected and on green
            dif_2_t_img = ld_img("assets/images/title/difficulty/2/true.png", True, None, None) # Difficulty button when selected and on yellow
            dif_2_f_img = ld_img("assets/images/title/difficulty/2/false.png", True, None, None) # Difficulty button when not selected and on yellow
            dif_3_t_img = ld_img("assets/images/title/difficulty/3/true.png", True, None, None) # Difficulty button when selected and on red
            dif_3_f_img = ld_img("assets/images/title/difficulty/3/false.png", True, None, None) # Difficulty button when not selected and on red
            updatet_img = ld_img("assets/images/title/buttons/updates/true.png", True, None, None) # Updates button when selected 
            updatef_img = ld_img("assets/images/title/buttons/updates/false.png", True, None, None) # Updates button when not selected
            upd_ping = ld_img("assets/images/title/updates/other/ping.png", True, None, None)
        elif categ == "gameplay":
            # Set variables
            imaud_ind = 1
            ttl_assets = 16     
            each_perc = 100 / ttl_assets
            perc = each_perc
            txtprnt = ""
            # Make assets global
            global bar_img, plr_img, L1_img, L2_img, L3_img, L4_img, L5_img, enemy_img, heal_img, stop_img, pause_1_img, pause_2_img, pause_3_img, pause_barcontent, gameover_img, gameover_barcontent, protected_eff
            # Load images
            bar_img = ld_img("assets/images/ingame/bar.png", True, None, None)
            plr_img = ld_img("assets/images/ingame/plr.png", True, None, None)
            L1_img = ld_img("assets/images/ingame/life/1.png", True, None, None) # Life at 1
            L2_img = ld_img("assets/images/ingame/life/2.png", True, None, None) # Life at 2
            L3_img = ld_img("assets/images/ingame/life/3.png", True, None, None) # Life at 3
            L4_img = ld_img("assets/images/ingame/life/4.png", True, None, None) # Life at 4
            L5_img = ld_img("assets/images/ingame/life/5.png", True, None, None) # Life at 5
            enemy_img = ld_img("assets/images/ingame/enemy.png", True, None, None)
            heal_img = ld_img("assets/images/ingame/heal.png", True, None, None)
            pause_1_img = ld_img("assets/images/ingame/pause/1.png", True, None, None)
            pause_2_img = ld_img("assets/images/ingame/pause/2.png", True, None, None)
            pause_3_img = ld_img("assets/images/ingame/pause/3.png", True, None, None)
            pause_barcontent = ld_img("assets/images/bars/bottom/ingame/pause.png", True, None, None)
            gameover_img = ld_img("assets/images/ingame/life/0.png", True, None, None)
            gameover_barcontent = ld_img("assets/images/bars/bottom/ingame/gameover.png", True, None, None)
            protected_eff = ld_img("assets/images/bars/top/effects/protected.png", True, None, None)
        elif categ == "autosave":
            # Set variables
            imaud_ind = 1
            ttl_assets = 8     
            each_perc = 100 / ttl_assets  
            perc = each_perc
            txtprnt = ""
            # Make assets global
            global autosave1, autosave2, autosave3, autosave4, autosave5, autosave6, autosave7, autosave8 
            # Load images
            autosave1 = ld_img("assets/images/other/autosave/f1.png", True, None, None)
            autosave2 = ld_img("assets/images/other/autosave/f2.png", True, None, None)
            autosave3 = ld_img("assets/images/other/autosave/f3.png", True, None, None)
            autosave4 = ld_img("assets/images/other/autosave/f4.png", True, None, None)
            autosave5 = ld_img("assets/images/other/autosave/f5.png", True, None, None)
            autosave6 = ld_img("assets/images/other/autosave/f6.png", True, None, None)
            autosave7 = ld_img("assets/images/other/autosave/f7.png", True, None, None)
            autosave8 = ld_img("assets/images/other/autosave/f8.png", True, None, None)
        elif categ == "updates":
            # Set variables
            imaud_ind = 1
            ttl_assets = 10    
            each_perc = 100 / ttl_assets  
            perc = each_perc
            txtprnt = ""
            # Make assets global
            global updatecontent, nointernet_img, updatebarcontent, bacb, refb, prev_pg, next_pg, updnf, updnt, upd_button
            # Load images
            updatecontent = ld_img("assets/images/title/updates/contentbox/contentbox.png", True, None, None) # The box containing the content
            nointernet_img = ld_img("assets/images/title/updates/contentbox/no internet.png", True, None, None)
            updatebarcontent = ld_img("assets/images/bars/bottom/title/updates.png", True, None, None)
            bacb = ld_img("assets/images/title/updates/buttons/back.png", True, None, None)
            refb = ld_img("assets/images/title/updates/buttons/refresh.png", True, None, None)
            prev_pg = ld_img("assets/images/title/updates/buttons/previous.png", True, None, None)
            next_pg = ld_img("assets/images/title/updates/buttons/next.png", True, None, None)
            upd_button = ld_img("assets/images/title/updates/buttons/update.png", True, None, None)
            updnf = ld_img("assets/images/notifs/updf.png", True, None, None)
            updnt = ld_img("assets/images/notifs/updt.png", True, None, None)
        elif categ == "options":
            # Set variables
            imaud_ind = 1
            ttl_assets = 6
            each_perc = 100 / ttl_assets  
            perc = each_perc
            txtprnt = ""
            # Make assets global
            global back_t_img, back_f_img, bg_t_img, bg_f_img, controls_t, controls_f, bg_opts
            # Load images
            back_t_img = ld_img("assets/images/title/buttons/back/true.png", True, None, None) # Back button when selected
            back_f_img = ld_img("assets/images/title/buttons/back/false.png", True, None, None) # Back button when not selected
            bg_t_img = ld_img("assets/images/title/buttons/bg/true.png", True, None, None) # Background button when selected
            bg_f_img = ld_img("assets/images/title/buttons/bg/false.png", True, None, None) # Background button when not selected
            controls_t = ld_img("assets/images/title/buttons/controls/true.png", True, None, None) # Controls button when selected
            controls_f = ld_img("assets/images/title/buttons/controls/false.png", True, None, None) # Controls button when not selected
            bg_opts = ld_img("assets/images/bg/secondary/optsr.png", True, None, None)
        elif categ == "controls":
            # Set variables
            imaud_ind = 1
            ttl_assets = 1    
            each_perc = 100 / ttl_assets  
            perc = each_perc
            txtprnt = ""
            # Make asset global
            global controls_m
            # Load image
            controls_m = ld_img("assets/images/title/controls/menu.png", True, None, None)
        elif categ == "init":
            # Set variables
            imaud_ind = 1
            ttl_assets = 20
            each_perc = 100 / ttl_assets  
            perc = each_perc
            txtprnt = ""
            # Make assets global
            global bg_r, bg_o, bg_y, bg_g, bg_gg, bg_b, bg_db, bg_pi, bg_pu, bg_mg, bg_gr, mouse_img, windicon, xt_img, xf_img, ft_img, ff_img, mt_img, mf_img, jris_img
            bg_r = ld_img("assets/images/bg/bgs/red.png", True, None, None)
            bg_o = ld_img("assets/images/bg/bgs/orange.png", True, None, None)
            bg_y = ld_img("assets/images/bg/bgs/yellow.png", True, None, None)
            bg_g = ld_img("assets/images/bg/bgs/green.png", True, None, None)
            bg_gg = ld_img("assets/images/bg/bgs/greener green.png", True, None, None)
            bg_b = ld_img("assets/images/bg/bgs/blue.png", True, None, None)
            bg_db = ld_img("assets/images/bg/bgs/dark blue.png", True, None, None)
            bg_pi = ld_img("assets/images/bg/bgs/pink.png", True, None, None)
            bg_pu = ld_img("assets/images/bg/bgs/purple.png", True, None, None)
            bg_mg = ld_img("assets/images/bg/bgs/mint green.png", True, None, None)
            bg_gr = ld_img("assets/images/bg/bgs/grey.png", True, None, None)
            mouse_img = ld_img("assets/images/other/other/mouse.png", True, None, None)
            windicon = ld_img("assets/images/other/other/windicon.png", True, None, None)
            xt_img = ld_img("assets/images/other/other/xt.png", True, None, None)
            xf_img = ld_img("assets/images/other/other/xf.png", True, None, None)
            ft_img = ld_img("assets/images/other/other/ft.png", True, None, None)
            ff_img = ld_img("assets/images/other/other/ff.png", True, None, None)
            mt_img = ld_img("assets/images/other/other/mt.png", True, None, None)
            mf_img = ld_img("assets/images/other/other/mf.png", True, None, None)
            jris_img = ld_img("assets/images/other/intro/jris.png", True, None, None) # This will be unloaded later
            jris_img = pygame.transform.scale(jris_img, (48, 48))
        elif categ == "dbg":
            # Set variables
            imaud_ind = 1
            ttl_assets = 1
            each_perc = 100 / ttl_assets  
            perc = each_perc
            txtprnt = ""
            # Make assets global
            global enter_dbg
            # Load images
            enter_dbg = ld_img("assets/debug/images/enter-dbg.png", True, None, None)

        txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Style.RESET_ALL + f"Loaded '{categ}'-based images!")
        print(txtprnt)
    except Exception as e:
        error.logerr(e, f"loading image category {categ}", thismodule)

#* Function to unload all images in a category
def unld_img(categ):
    try:
        global imaud_ind, ttl_assets
        imaud_ind = 1
        if categ == "ttsALL":
            global lll_img
            del lll_img
        elif categ == "tts1":
            global optt_img, optf_img, start_t_img, start_f_img, dif_1_t_img, dif_1_f_img, dif_2_t_img, dif_2_f_img, dif_3_t_img, dif_3_f_img, updatet_img, updatef_img
            del optt_img
            del optf_img
            del start_t_img 
            del start_f_img
            del dif_1_t_img
            del dif_1_f_img
            del dif_2_t_img
            del dif_2_f_img
            del dif_3_t_img
            del dif_3_f_img
            del updatet_img 
            del updatef_img
        elif categ == "gameplay":
            global bar_img, plr_img, L1_img, L2_img, L3_img, L4_img, L5_img, enemy_img, heal_img, stop_img, pause_1_img, pause_2_img, pause_3_img, pause_barcontent, gameover_img, gameover_barcontent, protected_eff
            del bar_img
            del plr_img 
            del L1_img
            del L2_img
            del L3_img
            del L4_img 
            del L5_img
            del enemy_img
            del heal_img 
            del pause_1_img
            del pause_2_img
            del pause_3_img
            del pause_barcontent 
            del gameover_img
        elif categ == "autosave":
            del autosave1
            del autosave2
            del autosave3
            del autosave4
            del autosave5 
            del autosave6
            del autosave7 
            del autosave8
        elif categ == "updates":
            global updatecontent, nointernet_img, updatebarcontent, bacb, refb, prev_pg, next_pg, updnf, updnt
            del updatecontent
            del nointernet_img 
            del updatebarcontent 
            del bacb 
            del refb
            del prev_pg
            del next_pg 
            del updnf 
            del updnt 
        elif categ == "options":
            global back_t_img, back_f_img, bg_t_img, bg_f_img, controls_t, controls_f
            del back_t_img 
            del back_f_img 
            del bg_t_img 
            del bg_f_img
            del controls_t 
            del controls_f 
        elif categ == "controls":
            global controls_m
            del controls_m
        txtprnt = (Fore.LIGHTGREEN_EX + "COMPLETED! " + Style.RESET_ALL + f"Unloaded '{categ}'-based images!")
        print(txtprnt)
    except Exception as e:
        error.logerr(e, f"unloading image category {categ}", thismodule)

def ld_audc(categ):
    global imaud_ind, ttl_assets, each_perc, perc
    try:
        if categ == "tts":
            global move_sel_sfx, sel_sfx
            move_sel_sfx = ld_aud("assets/audio/sfx/move_sel.ogg")
            sel_sfx = ld_aud("assets/audio/sfx/sel.ogg")
        elif categ == "init":
            global screenshot_sfx, intro1_sfx, intro2_sfx, main_ost, gameplay_ost
            screenshot_sfx = ld_aud("assets/audio/sfx/screenshot.ogg")
            intro1_sfx = ld_aud("assets/audio/sfx/jris1.ogg")
            intro2_sfx = ld_aud("assets/audio/sfx/jris3.ogg")
            main_ost = ld_aud("assets/audio/ost/main.ogg")
            gameplay_ost = ld_aud("assets/audio/ost/gameplay.ogg")
        elif categ == "gameplay":
            global lostlife_sfx, heal_sfx
            lostlife_sfx = ld_aud("assets/audio/sfx/lostlife.ogg")
            heal_sfx = ld_aud("assets/audio/sfx/heal.ogg")
    except Exception as e:
        error.logerr(e, f"loading audio category {categ}", thismodule)

def unld_aud(categ):
    try:
        if categ == "tts":
            del move_sel_sfx
            del sel_sfx
        elif categ == "init":
            del screenshot_sfx 
            del main_ost
            del gameplay_ost 
        elif categ == "gameplay":
            del lostlife_sfx
            del heal_sfx
        elif categ == "intro":
            del intro1_sfx
            del intro2_sfx
    except Exception as e:
        error.logerr(e, f"unloading image category {categ}", thismodule)
