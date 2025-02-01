
#* /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
#* |  Lifeline.py - v1.1 Beta 2.1                         |
#* |  Last updated: 2024-12-28                            |
#* |  Author: jasperredis                                 |
#* |                                                      |
#* |  This module in Lifeline.py manages errors.          |
#* |                                                      |
#* |  License: MIT License                                |
#* |  See the LICENSE file in the project root for more   |
#* |  information.                                        |
#* \______________________________________________________/
thismodule="error.py"

# Initialization
import tkinter
from tkinter import messagebox
import time
import traceback
import sys

# logerr usage:
# try
#   code
# except Exception as e
#   error.logerr(e, "process being done", thismodule)

def logerr(e, proc, callfrom):
    try:
        print("--------------------------------------------------------------")
        # Construct current time
        ctime = time.localtime()
        ltime = f"{ctime.tm_year}-{ctime.tm_mon}-{ctime.tm_mday} @ {ctime.tm_hour}:{ctime.tm_min}:{ctime.tm_sec}"
        
        # Provide feedback
        messagebox.showerror("Lifeline.py - Error", "An error has occurred in Lifeline.py.\nPlease select 'OK' and pay attention to your terminal.")
        print(f"Error while {proc}: {e}")
        print(f"This error was called by {callfrom}.")
        print("Logging error...")
        
        # Log error
        with open("log.txt", "a") as log_file:
            log_file.write(f"\nError on {ltime}\n")  # Time
            log_file.write(f"Error during {proc}: {e}\n")  # Exact error
            log_file.write(f"Error called by {callfrom}\n")
            log_file.write(f"Traceback:\n{traceback.format_exc()}")  # Traceback
        
        # Provide exitting info
        print("Error logged.")
        print("Plese check your log.txt file for more info.")
        print("You should now see a dialogue asking a question.")
        result = messagebox.askyesno("Lifeline.py - Error", "Would you like to attempt to run the game despite this error?\nIt is recommended that you select 'No'.")
        if result:
            result = messagebox.askyesno("Lifeline.py - Error", "Are you sure?")
            if result:
                print("Ok.")
            else:
                msgexit()
        else:
            msgexit()
    except Exception as etwo:
        # Except for error in error handling
        print(f"Somehow, there was an error in having an error. This error is: {etwo}")
        print("The following code will be handled extra carefully to ensure no further errors occur.")
        print("-------------------------------------------------------------------------------------")
        try:
            print("Attempting to provide what module called this error...")
            print(f"This error was called by {callfrom}.")
            print("Attempting to log error...")
            # Log error
            with open("log.txt", "a") as log_file:
                log_file.write(f"\nError on {ltime}\n")  # Time
                log_file.write(f"Error during {proc}: {e}\n")  # Exact error
                log_file.write(f"Error called by {callfrom}\n")
                log_file.write(f"Traceback:\n{traceback.format_exc()}\n")  # Traceback
            print("Error succesfully logged.\nExitting...")
            kill()
        except Exception as ethree:
            print("An error ocurred. No futher actions will be made to prevent further errors.")

def msgexit():
    result = messagebox.askokcancel("Lifeline.py - Error", "The game will exit after you select 'Ok'.")
    if result:
        kill()
    else:
        result = messagebox.askyesno("Lifeline.py - Error", "Are you sure?")
        if not result:
            messagebox.showinfo("Lifeline.py - Error", "The game will exit after you select 'Ok'.")
            kill()

def kill():
    print("Exiting...")
    sys.exit()
