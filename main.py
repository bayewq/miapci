#   Created By: LocalKebabShackOwner, bayewq


import pytesseract

from PIL import Image, ImageEnhance

import mss

import mss.tools

from ahk import AHK

from time import sleep 



##########################################
#               EDIT THESE               #

max_shares = 50
buy_at     = 300
sell_at    = 800

#change this to the tesseract.exe Location
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#                                        # 
##########################################

ahk = AHK()

item_coordinates = { # Made for 1980 x 1080 Monitor
    "empty"            : {"x": 1000, "y": 40},

    "enter"            : {"x": 620, "y": 340},
    "portfolio"        : {"x": 730, "y": 550},
    "buy_menu"         : {"x": 1200, "y": 550},
    "back"             : {"x": 500, "y": 180},

    "box1_buy_amount"  : {"x": 1200, "y": 450},
    "box1_buy"         : {"x": 1200, "y": 470},
    "box1_sell_amount" : {"x": 1335, "y": 450},
    "box1_sell"        : {"x": 1335, "y": 470},

    "box2_buy_amount"  : {"x": 1200, "y": 500},
    "box2_buy"         : {"x": 1200, "y": 525},
    "box2_sell_amount" : {"x": 1335, "y": 500},
    "box2_sell"        : {"x": 1335, "y": 525}, 

    "box3_buy_amount"  : {"x": 1200, "y": 565},
    "box3_buy"         : {"x": 1200, "y": 580},
    "box3_sell_amount" : {"x": 1335, "y": 565},
    "box3_sell"        : {"x": 1335, "y": 580},     
}

images = ["stats_meinc.png", "stats_sesh.png", "stats_vrt.png"]

def main():
    mode = ["buy", True]

    print_logo()
    confirm = input("press enter to start... ")
    print("Tab Back Into Roblox")

    sleep(3)

    enter_stocks_menu() 
    enter_market()
    
    sleep(1)

    while True:
        mode = logic(mode[0], mode[1])
        
def logic(newmode, whatbought):
    prices = {}
    bought = whatbought
    mode = newmode
    if mode == "buy":


            capture_all()
            sleep(1)

            prices = scan_all(images)

            sleep(1)
            try:
                prices["stats_meinc"][1] = prices["stats_meinc"][1].replace(',', '')
                prices["stats_sesh"][1] = prices["stats_sesh"][1].replace(',', '')
                prices["stats_vrt"][1] = prices["stats_vrt"][1].replace(',', '')
            except:
                print("permutation error")
                remount()
                sleep(2)
                enter_stocks_menu() 
                enter_market()
                sleep(1)
            sleep(1)

            try:
                if (int(prices["stats_meinc"][1]) <= buy_at):
                    #if (int(prices["stats_meinc"][0]) > 0):
                    if True:

                        print("buying meinc")
                        
                        ahk.mouse_move(item_coordinates["box1_buy_amount"]["x"], item_coordinates["box1_buy_amount"]["y"])
                        sleep(0.5)
                        ahk.click()
                        sleep(0.5)
                        ahk.type(f"{max_shares}")

                        sleep(0.5)
                        ahk.mouse_move(item_coordinates["box1_buy"]["x"], item_coordinates["box1_buy"]["y"])
                        sleep(0.1)
                        ahk.click()

                        sleep(1)
                        remount()
                        sleep(2)
                        enter_stocks_menu() 
                        enter_market()

                        return ["sell", "stats_meinc"]
            except:
                print("error while looking at meinc")
                pass


            try:
                if (int(prices["stats_sesh"][1]) <= buy_at):
                    #if (int(prices["stats_sesh"][0]) > 0):
                    if True:

                        print("buying sesh")
                        
                        ahk.mouse_move(item_coordinates["box2_buy_amount"]["x"], item_coordinates["box2_buy_amount"]["y"])
                        sleep(0.1)
                        ahk.click()
                        sleep(0.1)
                        ahk.type(f"{max_shares}")

                        sleep(0.1)
                        ahk.mouse_move(item_coordinates["box2_buy"]["x"], item_coordinates["box2_buy"]["y"])
                        sleep(0.1)
                        ahk.click()

                        sleep(1)
                        remount()
                        sleep(2)
                        enter_stocks_menu() 
                        enter_market()

                        return ["sell", "stats_sesh"]
            except:
                print("error while looking at sesh")
                pass


            try:
                if (int(prices["stats_vrt"][1]) <= buy_at):
                    #if (int(prices["stats_vrt"][0]) > 0):
                    if True:

                        print("buying vrt")

                        ahk.mouse_move(item_coordinates["box3_buy_amount"]["x"], item_coordinates["box3_buy_amount"]["y"])
                        sleep(0.5)
                        ahk.click()
                        sleep(0.5)
                        ahk.type(f"{max_shares}")

                        sleep(0.5)
                        ahk.mouse_move(item_coordinates["box3_buy"]["x"], item_coordinates["box3_buy"]["y"])
                        sleep(0.5)
                        ahk.click()

                        sleep(1)
                        remount()
                        sleep(2)
                        enter_stocks_menu() 
                        enter_market()

                        return ["sell", "stats_vrt"]


            except:
                print("error while looking at vrt")
                pass

            ahk.key_press('b')
            sleep(0.2)
            ahk.key_press('b')
            sleep(18)
            return ["buy", True]
        
        
    if mode == "sell":

        capture_all()
        
        sleep(1)
        prices = scan_all(images)
        sleep(1)

        try:
            prices["stats_meinc"][1] = prices["stats_meinc"][1].replace(',', '')
            prices["stats_sesh"][1] = prices["stats_sesh"][1].replace(',', '')
            prices["stats_vrt"][1] = prices["stats_vrt"][1].replace(',', '')
            
        except:
            print("permutation error")
            remount()
            sleep(2)
            enter_stocks_menu() 
            enter_market()
            sleep(1)
        sleep(1)

        if bought == "stats_meinc":
            try:
                if (int(prices["stats_meinc"][1]) >= sell_at):

                    print("selling meinc")

                    ahk.mouse_move(item_coordinates["box1_sell_amount"]["x"], item_coordinates["box1_sell_amount"]["y"])
                    sleep(0.5)
                    ahk.click()
                    sleep(0.5)
                    ahk.type(f"{max_shares}")

                    sleep(0.5)
                    ahk.mouse_move(item_coordinates["box1_sell"]["x"], item_coordinates["box1_sell"]["y"])
                    sleep(0.5)
                    ahk.click()

                    sleep(1)
                    remount()
                    sleep(2)
                    enter_stocks_menu() 
                    enter_market()

                    return ["buy", True]
                    
            except:
                print("error while looking at price")
                

        if bought == "stats_sesh":
            try:
                if (int(prices["stats_sesh"][1]) >= sell_at):

                    print("selling sesh")

                    ahk.mouse_move(item_coordinates["box2_sell_amount"]["x"], item_coordinates["box2_sell_amount"]["y"])
                    sleep(0.5)
                    ahk.click()
                    sleep(0.5)
                    ahk.type(f"{max_shares}")

                    sleep(0.5)
                    ahk.mouse_move(item_coordinates["box2_sell"]["x"], item_coordinates["box2_sell"]["y"])
                    sleep(0.5)
                    ahk.click()

                    sleep(1)
                    remount()
                    sleep(2)
                    enter_stocks_menu() 
                    enter_market()

                    return ["buy", True]
            
            except:
                print("error while looking at price")


        if bought == "stats_vrt":
            try:
                if (int(prices["stats_vrt"][1]) >= sell_at):

                    print("selling vrt")
                    
                    ahk.mouse_move(item_coordinates["box3_sell_amount"]["x"], item_coordinates["box3_sell_amount"]["y"])
                    sleep(0.5)
                    ahk.click()
                    sleep(0.5)
                    ahk.type(f"{max_shares}")

                    sleep(0.5)
                    ahk.mouse_move(item_coordinates["box3_sell"]["x"], item_coordinates["box3_sell"]["y"])
                    sleep(0.5)
                    ahk.click()

                    sleep(1)
                    remount()
                    sleep(2)
                    enter_stocks_menu() 
                    enter_market()

                    return ["buy", True]
            
            except:
                print("error while looking at price")   

        ahk.key_press('b')
        sleep(0.2)
        ahk.key_press('b')
        sleep(25)
        return [newmode, whatbought]

def print_logo():
    print(f"              $$\                               $$\ ")
    print(f"              \__|                              \__|")
    print(f"$$$$$$\$$$$\  $$\  $$$$$$\   $$$$$$\   $$$$$$$\ $$\ ")
    print(f"$$  _$$  _$$\ $$ | \____$$\ $$  __$$\ $$  _____|$$ |")
    print(f"$$ / $$ / $$ |$$ | $$$$$$$ |$$ /  $$ |$$ /      $$ |")
    print(f"$$ | $$ | $$ |$$ |$$  __$$ |$$ |  $$ |$$ |      $$ |")
    print(f"$$ | $$ | $$ |$$ |\$$$$$$$ |$$$$$$$  |\$$$$$$$\ $$ |")
    print(f"\__| \__| \__|\__| \_______|$$  ____/  \_______|\__|")
    print(f"version BEATA               $$ |                    ")           
    print(f"                            $$ |                    ")         
    print(f"                            \__|                    ")             
    return 0 

def translate(image):
    img = Image.open(image)
    img = img.convert("L")
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)
    output = pytesseract.image_to_string(img, config = "--psm 7 -c tessedit_char_whitelist='0123456789$'")
    price_data = output[0:-2]
    price_data = price_data.split("$")
    return price_data

def scan_all(list):
    allout = {}
    for item in list:
        objname = item[:-4]
        allout[objname] = translate(item)
    print(allout)
    return allout


def capture_price_meinc():
    with mss.mss() as sct:
        monitor = {"top": 475, "left": 758, "width": 326, "height": 35}
        output = "stats_meinc.png"
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        return 0


def capture_price_seesh():
    with mss.mss() as sct:
        monitor = {"top": 530, "left": 758, "width": 326, "height": 35}
        output = "stats_sesh.png"
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        return 0


def capture_price_vrt():
    with mss.mss() as sct:
        monitor = {"top": 590, "left": 758, "width": 326, "height": 35}
        output = "stats_vrt.png"
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        return 0

def capture_all():
    capture_price_vrt()
    capture_price_seesh()
    capture_price_meinc()

def enter_stocks_menu():
    print("Entering Stocks Menu")
    ahk.mouse_move(item_coordinates["enter"]["x"], item_coordinates["enter"]["y"])
    sleep(3)
    ahk.click()
    sleep(3)
    return 0


def enter_market():
    print("Entering Stock Market")
    ahk.mouse_move(item_coordinates["buy_menu"]["x"], item_coordinates["buy_menu"]["y"])
    sleep(3)
    ahk.click()
    sleep(3)
    ahk.mouse_move(item_coordinates["empty"]["x"], item_coordinates["empty"]["y"])
    sleep(1)
    return 0


def back():
    print("Clicking Back Button")
    ahk.mouse_move(item_coordinates["back"]["x"], item_coordinates["back"]["y"])
    sleep(2)
    ahk.click()
    sleep(1)
    return 0 


def remount():
    print("Remounting")
    ahk.key_press('space')
    sleep(3)
    ahk.key_press('e')
    sleep(3)
    return 0 


if __name__ == "__main__":
    main()
