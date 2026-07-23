"""難易度・レベル選択機能。"""

import random


def select_duplicate_mode() -> bool:
    """プレイヤーに重複あり/なしを選択させる。

    Returns:
        bool: True なら重複あり、False なら重複なし
    """
    print("【重複モード選択】")
    print(" 1: 重複あり")
    print(" 2: 重複なし")

    while True:
        choice = input("選択してください (1/2) > ").strip()
        if choice == "1":
            return True
        if choice == "2":
            return False
        print("1 か 2 を入力してください。")


def select_digits(allow_duplicates: bool, default_digits: int = 3) -> int:
    """プレイヤーに桁数（1〜10、重複なしの場合は最大10）を入力させる。

    Args:
        allow_duplicates (bool): 重複ありのモードかどうか
        default_digits (int): Enterを直接押した場合のデフォルト桁数

    Returns:
        int: プレイヤーが指定した桁数
    """
    max_digits = 10 if not allow_duplicates else 10  # 実質上限はどちらも10以下が現実的
    prompt = f"桁数を入力してください (1〜{max_digits}桁、デフォルト: {default_digits}) > "

    while True:
        user_input = input(prompt).strip()

        # 入力が空（Enterキーのみ）の場合はデフォルト値を使う
        if not user_input:
            return default_digits

        if user_input.isdigit():
            digits = int(user_input)

            if digits < 1:
                print("1桁以上を指定してください。")
            elif not allow_duplicates and digits > 10:
                print("※重複なしモードでは10桁以下である必要があります（数字0〜9が10個のため）。")
            elif digits > 10:
                print("10桁以下で指定してください。")
            else:
                return digits
        else:
            print("数字を入力してください。")


def make_secret_with_mode(digits: int = 3, allow_duplicates: bool = True) -> str:
    """指定されたモードと桁数に応じて secret を生成する。"""
    if allow_duplicates:
        return "".join(random.choices("0123456789", k=digits))
    else:
        # 重複なし（0~9 から digits 個抽出）
        return "".join(random.sample("0123456789", k=digits))