"""難易度・レベル選択機能。"""

import random


def select_duplicate_mode() -> bool:
    """プレイヤーに重複あり/なしを選択させる。

    Returns:
        bool: True なら重複あり、False なら重複なし
    """
    print("【モード選択】")
    print(" 1: 重複あり (例: 112, 055)")
    print(" 2: 重複なし (例: 123, 456)")

    while True:
        choice = input("選択してください (1/2) > ").strip()
        if choice == "1":
            return True
        if choice == "2":
            return False
        print("1 か 2 を入力してください。")


def make_secret_with_mode(digits=3, allow_duplicates=True) -> str:
    """指定されたモードに応じて secret を生成する。"""
    if allow_duplicates:
        return "".join(random.choices("0123456789", k=digits))
    else:
        # 重複なし（0~9 から digits 個抽出）
        return "".join(random.sample("0123456789", k=digits))