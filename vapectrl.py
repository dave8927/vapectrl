#!/usr/bin/env python
import time
from simple_term_menu import TerminalMenu
import RPi.GPIO as GPIO


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
    print("Starting vapectrol Setup Script")
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
    print("Starting Vape Script /n")

    # requested vape time in seconds
    vape_time = 1
    print("Vape time = ", vape_time, " seconds")
    time.sleep(1)

    GPIO.setmode(GPIO.BCM)  # sets GPIO mode to BCM numbering
    GPIO.setup(26, GPIO.OUT)  # use GPIO pin 26

    GPIO.output(26, False)  # sets GPIO 26 starting state to False

    delay_time = 5  # requested delay time in seconds
    print("Starting ", delay_time, " second delay:")
    print("Start Mass Flow Control...")
    for x in range(delay_time):  # range is no. times the loop will repeat
        print(x + 1)  # range starts at 0, +1 makes it start at 1
        time.sleep(1)

    print("Starting Vape...")

    try:
        for x in range(1):  # sets the number of times to repeat the loop
            GPIO.output(26, True)  # sets GPIO 26 to True, activating the relay
            time.sleep(vape_time)  # time to leave relay on

            GPIO.output(26, False)  # sets GPIO 26 to False, deactivating the relay
            time.sleep(1)  # time leave relay off before before repeating loop
        GPIO.cleanup()  # resets GPIO pins after loop/script is complete
        print("...Vape complete")

    except KeyboardInterrupt:
        GPIO.cleanup()  # resets GPIO pins on exit (Ctrl-C)


def main():
    main_menu_title = "  Vape Control Menu\n"
    main_menu_items = ["Power on", "Setup", "Vape (4s)", "Settings...", "Quit"]
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

    settings_menu_title = "  Settings Menu\n"
    settings_menu_items = ["Change Vape Time", "Update Script", "Back to Main Menu"]
    settings_menu_back = False

    settings_menu = TerminalMenu(
        menu_entries=settings_menu_items,
        title=settings_menu_title,
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
            time.sleep(1)
            vape_power_on()
        elif main_sel == 1:
            print("Setup Selected")
            time.sleep(1)
            vape_setup()
        elif main_sel == 2:
            print("Vape (4s) Selected")
            time.sleep(1)
            vape_vape()
        elif main_sel == 3:
            while not settings_menu_back:
                settings_sel = settings_menu.show()
                if settings_sel == 0:
                    print("Change Vape time...")
                    time.sleep(5)
                elif settings_sel == 1:
                    print("Update Script")
                    time.sleep(5)
                elif settings_sel == 2:
                    settings_menu_back = True
                    print("Back Selected")
            settings_menu_back = False
        elif main_sel == 4:
            main_menu_exit = True
            print("Quit Selected")


if __name__ == "__main__":
    main()
