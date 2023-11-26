import pyautogui
import pyperclip

def mensagem(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

    pyautogui.moveTo(x=1276,y=888,duration=2)
    pyautogui.click()
    mensagem('Olá mundo')