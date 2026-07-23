"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""
from .core import judge
from .color import format_colored_guess
from .level import make_secret_with_mode, select_duplicate_mode

def play(digits=3):
    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    

    allow_duplicates = select_duplicate_mode()
    secret = make_secret_with_mode(digits, allow_duplicates)

    mode_str = "重複あり" if allow_duplicates else "重複なし"
    print(f"\nHit & Blow（{digits} 桁・{mode_str}）")
    print("-" * 40)
    print("【ゲーム説明】")
    print(
        f"相手が隠した {digits} 桁の（{mode_str}）数字を当てるゲームです。"
    )
    print("・Hit  : 数字も位置も合っている数")
    print("・Blow : 数字は合っているが、位置が違う数")
    print("ヒントを頼りに、できるだけ少ない回数で正解を見つけてください！")
    print("-" * 40)

    tries = 0
    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く =====

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            print("-" * 40)
            continue

        # 重複なしモードの時に重複入力された場合の簡易バリデーション (お好みで追加)
        if not allow_duplicates and len(set(guess)) != digits:
            print(f"※重複なしモードです！同じ数字を2回使えません。")
            print("-" * 40)
            continue

        tries += 1
        hit, blow = judge(secret, guess)

        # --- カラー機能の追加ここから ---
        colored_guess = format_colored_guess(secret, guess)
        print(f"結果: {colored_guess}  (Hit={hit}  Blow={blow})")
        # --- カラー機能の追加ここまで ---

        print("-" * 40)

        if hit == digits:
            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break