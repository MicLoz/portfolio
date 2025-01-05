import pyautogui as auto
import platform
import time

# Get operating system name
os_name = platform.system()

def scroll_page(page_is_read):
    # Wait for the page to load
    time.sleep(.1)
    if page_is_read == False:
        scroll_to_top()
    elif page_is_read == True:
        scroll_to_bottom()

def scroll_to_top():
    if os_name == "Windows":
        auto.press('home')  # 'Home' key scrolls to top on Windows
    elif os_name == "Darwin":  # 'Darwin' is the system name for macOS
        auto.hotkey('command', 'up')  # 'Cmd + Up Arrow' scrolls to top on macOS
    elif os_name == "Linux":
        auto.press('home')  # Most Linux setups use the Home key
    else:
        # If other operating systems try both methods.
        auto.press('home')
        auto.hotkey('command', 'up')

def scroll_to_bottom():
    if os_name == "Windows":
        auto.press('end')
    elif os_name == "Darwin":
        auto.hotkey('command', 'down')
    elif os_name == "Linux":
        auto.press('end')
    else:
        # If other operating systems try both methods.
        auto.press('end')
        auto.hotkey('command', 'down')


