"""カラー表示用モジュール。

入力された予想数字（guess）の各桁に、Hit（緑）/ Blow（黄）の色をつけます。
"""

GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def format_colored_guess(secret: str, guess: str) -> str:
    result = [""] * len(guess)

    # リスト化（使用済み管理のため）
    secret_list = list(secret)
    guess_list = list(guess)

    # まず Hit を判定
    for i in range(len(guess)):
        if guess_list[i] == secret_list[i]:
            result[i] = f"{GREEN}{guess_list[i]}{RESET}"
            secret_list[i] = None
            guess_list[i] = None

    # 次に Blow を判定
    for i in range(len(guess)):
        if guess_list[i] is None:
            continue

        if guess_list[i] in secret_list:
            result[i] = f"{YELLOW}{guess_list[i]}{RESET}"
            secret_list[secret_list.index(guess_list[i])] = None
        else:
            result[i] = guess_list[i]

    return "".join(result)
