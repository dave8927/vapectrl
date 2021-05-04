#!/usr/bin/env python
import time
from datetime import datetime
from simple_term_menu import TerminalMenu
import RPi.GPIO as GPIO

# update


def vape_power_on():
    print("Starting vapectrl Power-on Script")
    time.sleep(1)

    GPIO.setmode(GPIO.BCM)  # sets GPIO mode to BCM numbering
    GPIO.setup(26, GPIO.OUT)  # use GPIO pin 26
    GPIO.output(26, False)  # sets GPIO 26 starting state to False

    try:
        for x in range(5):  # sets the number of times to repeat the loop
            GPIO.output(26, True)  # sets GPIO 26 to True, activating the relay
            time.sleep(0.1)  # time to leave relay on
            GPIO.output(26, False)  # sets GPIO 26 to False, deactivating the relay
            time.sleep(0.1)  # time leave relay off before before looping
        GPIO.cleanup()
        print("Power on complete")
        time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()  # resets GPIO pins on exit (Ctrl-C)


def vape_setup():
    print("Starting vapectrl Setup Script")
    time.sleep(1)

    GPIO.setmode(GPIO.BCM)  # sets GPIO mode to BCM numbering
    GPIO.setup(26, GPIO.OUT)  # use GPIO pin 26

    GPIO.output(26, False)  # sets GPIO 26 starting state to False

    try:
        for x in range(1):  # sets the number of times to repeat the loop
            GPIO.output(26, True)  # sets GPIO 26 to True, activating the relay
            time.sleep(0.2)  # time to leave relay on
            GPIO.output(26, False)  # sets GPIO 26 to False, deactivating the relay
            time.sleep(1)
            GPIO.output(26, True)  # sets GPIO 26 to True, activating the relay
            time.sleep(2)  # time to leave relay on
            GPIO.output(26, False)  # sets GPIO 26 to False, deactivating the relay
            time.sleep(1)
        GPIO.cleanup()  # resets GPIO pins after loop/script is complete

    except KeyboardInterrupt:
        GPIO.cleanup()  # resets GPIO pins on exit (Ctrl-C)


def vape_vape():
    print("Starting Vape Script: \n")
    vape_time = 4  # requested vape time in seconds
    print("Vape time setting = ", vape_time, " seconds")
    print("Get ready to start Mass Flow Controller \n")
    input("Press Enter to start automatic vape after 5s countdown..")
    print("Start Mass Flow Controller!\n")

    GPIO.setmode(GPIO.BCM)  # sets GPIO mode to BCM numbering
    GPIO.setup(26, GPIO.OUT)  # use GPIO pin 26
    GPIO.output(26, False)  # sets GPIO 26 starting state to False

    countdown_time = 5  # requested delay time in seconds
    for x in range(countdown_time):  # range is no. times the loop will repeat
        print("Vape starting in:", 5 - x, "s...\r", end="")
        time.sleep(1)

    try:
        print("\nVape started...")
        t1 = datetime.utcnow()
        for x in range(1):  # sets the number of times to repeat the loop
            GPIO.output(26, True)  # sets GPIO 26 to True, activating the relay
            time.sleep(vape_time)  # time to leave relay on

            GPIO.output(26, False)  # sets GPIO 26 to False, deactivating the relay
            # time.sleep(1)  # time leave relay off before before repeating loop
        GPIO.cleanup()  # resets GPIO pins after loop/script is complete
        t2 = datetime.utcnow()
        t = (t2-t1)*1000  # timedelta in ms
        print("...Vape complete!")
        print("Time = ", t.total_seconds(), "ms\n")
        input("Press Enter to return to Menu...")

    except KeyboardInterrupt:
        GPIO.cleanup()  # resets GPIO pins on exit (Ctrl-C)


def config_vape_time():
    print("Config Script:\n")
    print("This has not yet been implimented...")
    print((
        '......\n'
    ))
    input("Press Enter to go back...")


def config_update():
    print("Update Script:\n")
    print("This has not yet been implimented...")
    print((
        'To update manually, exit this script and run "./update.sh"'
        'to download the latest version from GitHub\n'
    ))
    input("Press Enter to go back...")


def main():
    main_menu_title = "  Vape Control Menu\n"
    main_menu_items = ["Power on", "Setup", "Vape", "Config...", "Quit"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    config_menu_title = "  Config Menu\n"
    config_menu_items = ["Change Vape Time", "Update Script", "Back to Main Menu"]
    config_menu_back = False

    config_menu = TerminalMenu(
        menu_entries=config_menu_items,
        title=config_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            print("Power on Selected")
            time.sleep(0.3)
            vape_power_on()
        elif main_sel == 1:
            print("Setup Selected")
            time.sleep(0.3)
            vape_setup()
        elif main_sel == 2:
            print("Vape Selected")
            time.sleep(0.3)
            vape_vape()
        elif main_sel == 3:
            while not config_menu_back:
                config_sel = config_menu.show()
                if config_sel == 0:
                    print("Config: Vape Time Selected")
                    time.sleep(0.3)
                    config_vape_time()
                elif config_sel == 1:
                    print("Config: Update Selected")
                    time.sleep(0.3)
                    config_update()
                elif config_sel == 2:
                    config_menu_back = True
                    print("Config: Back Selected")
            config_menu_back = False
        elif main_sel == 4:
            main_menu_exit = True
            print("Quit Selected")


if __name__ == "__main__":
    main()
