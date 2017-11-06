import time

from selenium import webdriver

mod = 1

def arr(bin,c) :
    global inputtext
    inputtext = bin[c]
    del bin[c]
    bin.append(inputtext)


longtextf = open("kill","r", encoding='utf8')
textlong = longtextf.readlines()
killtextf = open("long","r", encoding='utf8')
textkill = killtextf.readlines()
normal = open("normal","r", encoding="utf8")
normaltext = normal.readlines()

no = False

def longtest(str1):
    global inputtext
    global textlong
    for line in textlong:
        if line[0:1] == str1:
            inputtext = line
            arr(textlong,textlong.index(inputtext))
            return
    killtest(str1)

killcheck = True

def killtest(str1):
    global inputtext
    global textkill
    global killcheck
    for line in textkill:
        if line[0:1] == str1:
            inputtext = line
            arr(textkill, textkill.index(inputtext))
            return
    normaltest(str1)
    killcheck = False

def normaltest(str1):
    global no
    global inputtext
    global normaltext
    for line in normaltext:
        if line[0:1] == str1:
            inputtext = line
            arr(normaltext, normaltext.index(inputtext))
            return
    no = True


c = False
fast = 1.0
def one() :
    global no
    global c
    global fast
    global current
    global chattext
    global chatbtn
    global text1
    while 1:
        if text1.text == "게임 끝!":
            raise NotImplementedError
        if text1.text[0:5] == "이미 쓰인" or text1.text[0:2] == "한방":
            killtest(text1.text[0:1])
            time.sleep(2)
            c = True
        if (current.get_attribute("style")=="display: block;"):
                if not c:
                    duom()
                    if not no :
                        longtest(inp)
                        chattext.send_keys(inputtext)
                        chatbtn.click()
                        print(inputtext)
        else:
            no = False
            break

nexttext = ""
inp = ""

def duom():
    global inp
    global text1
    if text1.text[0:1] == "롭":
        inp = "놉"
    elif text1.text[0:1] == "뉵":
        inp = "육"
    elif text1.text[0:1] == "릭":
        inp = "익"
    elif text1.text[0:1] == "력":
        inp = "역"
    elif text1.text[0:1] == "랄":
        inp = "날"
    elif text1.text[0:1] == "랏":
        inp = "낫"
    elif text1.text[0:1] == "림":
        inp = "임"
    elif text1.text[0:1] == "률":
        inp = "율"
    elif text1.text[0:1] == "랴":
        inp = "야"
    elif text1.text[0:1] == "녁":
        inp = "역"
    elif text1.text[0:1] == "릿":
        inp = "잇"
    elif text1.text[0:1] == "룰":
        inp = "눌"
    elif text1.text[0:1] == "례":
        inp = "예"
    elif text1.text[0:1] == "릇":
        inp = "늣"
    elif text1.text[0:1] == "렁":
        inp = "넝"
    elif text1.text[0:1] == "뢰":
        inp = "뇌"
    elif text1.text[0:1] == "롄":
        inp = "옌"
    elif text1.text[0:1] == "뇽":
        inp = "용"
    elif text1.text[0:1] == "륵":
        inp = "늑"
    else:
        inp = text1.text[0:1]
def one1() :
    global inp
    global no
    global c
    global fast
    global current
    global chattext
    global chatbtn
    global text1
    while 1:
        if text1.text == "게임 끝!":
            raise NotImplementedError
        if text1.text[0:5] == "이미 쓰인" or text1.text[0:2] == "한방":
            c = True
            no = False
        if (current.get_attribute("style")=="display: block;"):
                if not c:
                    duom();
                if not no :
                    longtest(inp)
                    chattext.send_keys(inputtext)
                    chatbtn.click()
                    print(inputtext)



        else:
            no = False
            c = False

def taza():
    global text1
    global chattext
    global chatbtn
    global current
    global inputtext
    global timebar
    global nexttext
    while 1:
        if (current.get_attribute("style") == "display: block;"):
            if (nexttext != timebar.text):
                inputtext = text1.text
                time.sleep(fast)
                chattext.send_keys(inputtext)
                chatbtn.click()
                print(inputtext)
                nexttext = timebar.text
            elif (nexttext == timebar.text):
                continue


driver= webdriver.Chrome()

driver.get("http://kkutu.io/")


inputtext = "기본값"

def f():
    global mod
    global text1
    global chattext
    global chatbtn
    global current
    global timebar
    global longtextf
    global killtextf
    global normal
    global textlong
    global textkill
    global normaltext
    global fast
    while 1 :
        print("모드 변경: 1 / 단일 실행 : 2 / 반복 긴단어 : 3 / 반복 죽이기 : 4 / 초기화 : 5  ")
        a1 = input()
        if (a1 == "1"):
            if (mod == 1):
                print("죽이기 모드로 변경되었습니다.")
                mod = 2
            elif (mod == 2):
                print("긴단어 모드로 변경되었습니다.")
                mod = 1
            temp = textlong
            textlong = textkillf
            textkillf = temp

        if (a1 == "3"):
            text1 = driver.find_element_by_class_name("jjo-display")
            chattext = driver.find_element_by_id("Talk")
            chatbtn = driver.find_element_by_id("ChatBtn")
            current = driver.find_element_by_class_name("game-input")
            timebar = driver.find_element_by_class_name("graph-bar")
            one1()
        if (a1 == "4"):
            text1 = driver.find_element_by_class_name("jjo-display")
            chattext = driver.find_element_by_id("Talk")
            chatbtn = driver.find_element_by_id("ChatBtn")
            current = driver.find_element_by_class_name("game-input")
            timebar = driver.find_element_by_class_name("graph-bar")
            one1()
        if (a1 == "5"):
            longtextf = open("long", "r", encoding='utf8')
            textlong = longtextf.readlines()
            textlong.sort(key=lambda item: (-len(item), item))
            killtextf = open("subkill", "r", encoding='utf8')
            textkill = killtextf.readlines()
            textkill.sort(key=lambda item: (-len(item), item))
            normal = open("normal", "r", encoding="utf8")
            normaltext = normal.readlines()
            mod = 1
        if (a1 == "2"):
            text1 = driver.find_element_by_class_name("jjo-display")
            chattext = driver.find_element_by_id("Talk")
            chatbtn = driver.find_element_by_id("ChatBtn")
            current = driver.find_element_by_class_name("game-input")
            timebar = driver.find_element_by_class_name("graph-bar")
            one()


def g1():
    try:
        f()
    except:
        g1()

g1()



