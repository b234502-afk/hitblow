"""カラー表示用モジュール。

入力された予想数字（guess）の各桁に、Hit（緑）/ Blow（黄）の色をつけます。
"""
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def format_colored_guess(secret: str, guess: str) -> str:
    """ユーザーの予想数字(guess)を判定し、色付きの文字列にして返します。
    
    - 位置も数字も合っている桁 (Hit) -> 緑色
    - 位置は違うが数字は含まれる桁 (Blow) -> 黄色
    - どちらでもない桁 -> そのまま
    """
    colored_digits = []
    
    for i, char in enumerate(guess):
        if char == secret[i]:
            # Hit (位置も数字も一致) -> 緑色
            colored_digits.append(f"{GREEN}{char}{RESET}")
        elif char in secret:
            # Blow (数字は含まれるが位置が違う) -> 黄色
            colored_digits.append(f"{YELLOW}{char}{RESET}")
        else:
            # はずれ -> そのまま
            colored_digits.append(char)
            
    return "".join(colored_digits)