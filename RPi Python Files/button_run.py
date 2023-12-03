import os

def on_press():
    # Set time to 6 am
    os.system('sudo timedatectl set-ntp false')
    os.system("sudo timedatectl set-time '2023-09-18 06:00:00'")

    # Run Main Loop