import pyautogui
import time
from PIL import ImageGrab
import pytesseract
from queue import Queue




def get_live():
    live_width = 90
    live_height = 35
    live_left = 170
    live_right = live_left + live_width
    live_lower = 1110
    live_upper = live_lower - live_height
    
    mana_width = 90
    mana_height = 35
    mana_left = 2390
    mana_right = mana_left + mana_width
    mana_lower = 1140
    mana_upper = mana_lower - mana_height
    
    
    
    custom_config = r'--psm 10 -c tessedit_char_whitelist=/0123456789'
    
    vilaliti = Queue()
    vilaliti.put('1')
    vilaliti.put('2')
    vilaliti.put('3')
    vilaliti.put('4')
    
    # mana_queue = Queue()
    # mana_queue.put('4')
    # mana_queue.put('5')
    
    count = 0
    print(f'{count:04d}', end='\r')
    while True:
        time.sleep(0.5)
        image_live = ImageGrab.grab(bbox=(live_left, live_upper, live_right, live_lower))
        # image_live = ImageGrab.grab()
        # image_mana = ImageGrab.grab(bbox=(mana_left, mana_upper, mana_right, mana_lower))
        
        # image_live.save('a:\\live_image.png')
        # time.sleep(10000)
        live = pytesseract.image_to_string(image=image_live, config=custom_config)
        # mana = pytesseract.image_to_string(image=image_mana, config=custom_config)
        try:
            curr_live, maximum_live = list(map(int, live.split('/')))
        except ValueError:
            pass
        else:
            tetta_live = curr_live/maximum_live
            if tetta_live <= 0.9:
                item = vilaliti.get()
                # pyautogui.press(item)
                pyautogui.hotkey(item)
                count += 1
                print(f'{curr_live:05d}__{count:04d}', end='\r')
                
                vilaliti.put(item)
                time.sleep(1)
        
        # try:
        #     curr_mana, maximum_mana = list(map(int, mana.split('/')))
        # except ValueError:
        #     pass
        # else:
        #     tetta_mana = curr_mana/maximum_mana
        #     if tetta_mana <= 0.64:
        #         item = mana_queue.get()
        #         pyautogui.press(item)
        #         mana_queue.put(item)
        #         time.sleep(0.2)
        
        
        
if __name__ == '__main__':
    get_live()