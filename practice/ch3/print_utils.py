from time import sleep
import sys

def p(message, delay=0):
    sleep(delay)
    print(message)
    sleep(delay)

def printDivider():
    p("--------------------------------------------------")

def printServerCall(message):
    printDivider()
    p(f"Fetching Scalar Simulation", 1)
    printDivider()

def printTransfer():
    p("..", 0)
    p("....", 0)
    p("...", 0)

def ai_typing(message, typing_speed=0.05):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(typing_speed)
    print()  # for newline

def p_with_typing(message, delay=0, typing_speed=0.05):
    sleep(delay)
    ai_typing(message, typing_speed)
    sleep(delay)

def loading_bar(total=30, delay=0.1):
    for i in range(total):
        sys.stdout.write('\r')
        sys.stdout.write(f"[{'=' * i}{' ' * (total - i - 1)}] {int((i + 1) / total * 100)}%")
        sys.stdout.flush()
        sleep(delay)
    print()  # for newline
