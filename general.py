import plyer
from plyer import notification
import pygame
import sys
import tkinter as tk
from tkinter import messagebox

def sysnotif(t, d, c):
    try:
        notification.notify(
        title=t,   # Title of the notification
        message=d, # Message content
        timeout=c  # Duration in seconds the notification will stay visible
        )
    except:
        messagebox.showinfo("Error", "Could not make a notification!")

def kill_application():
    sysnotif("Lifeline.py", "Goodbye! Thanks for playing Lifeline.py!", 5)
    pygame.quit()
    sys.exit()

def msgbx(title, description, okyn, alerts):
    if alerts:
        if okyn == "yn":
            return messagebox.askyesno(title, description)
        else:
            messagebox.showinfo(title, description)
