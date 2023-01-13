import sys
print(sys.executable)
print(sys.version)
print(sys.platform)

print("Бібліотека Colorama. "
      "Один із вбудованих модулів Python для відображення тексту різними кольорами, а також "
      "для поліпшеної читабельності виводу."
      "\n   Version: 0.4.6 "
      "\n   Summary: Cross-platform colored terminal text."
      "\n   Author-email: Jonathan Hartley <tartley@tartley.com>")

from colorama import Fore, Back, Style
print(Fore.MAGENTA + 'some magenta text')
print(Back.LIGHTCYAN_EX + 'and with a cyan background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

print("Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET."
      "\nBack: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET."
      "\nStyle: DIM, NORMAL, BRIGHT, RESET_ALL")




