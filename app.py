"""
Tkinter Desktop GUI Application Sample
Windows 11環境向け Python標準ライブラリのみで構成されたGUIサンプルアプリ
（PyInstallerによるexe化に対応）
"""

import os
import tkinter as tk
from tkinter import filedialog, ttk

# ==============================================================================
# 設定セクション（カスタマイズ用定数）
# ==============================================================================
APP_TITLE: str = "Tkinterサンプルアプリ"
INITIAL_DIR: str = os.getcwd()  # 初期表示フォルダ（カレントディレクトリ）
FILE_TYPES: list[tuple[str, str]] = [("すべてのファイル", "*.*")]  # 選択可能な拡張子


def print_input(folder_path: str, file_path: str, input_text: str) -> None:
    """入力内容をコマンドプロンプトにprint関数で出力"""
    print("========================================")
    print("[入力内容の確認]")
    print("========================================")
    print(f"フォルダパス : {folder_path or '(未選択)'}")
    print(f"ファイルパス : {file_path or '(未選択)'}")
    print(f"入力文字     : {input_text or '(未入力)'}")
    print("========================================")
    print()


class App(tk.Tk):
    """メインアプリケーションウィンドウ"""

    def __init__(self) -> None:
        super().__init__()

        # ウィンドウの基本設定
        self.title(APP_TITLE)
        self.minsize(520, 200)

        # 入力値を管理する変数（TkinterのStringVar）
        self.folder_path_var = tk.StringVar(value="")
        self.file_path_var = tk.StringVar(value="")
        self.input_text_var = tk.StringVar(value="")

        # UIコンポーネントの構築
        self._create_widgets()

    def _create_widgets(self) -> None:
        """GUIレイアウトの作成・配置"""
        # メインフレーム（余白設定）
        main_frame = ttk.Frame(self, padding=16)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # カラムの伸縮設定（入力欄のある列をウィンドウ幅に合わせて伸縮）
        main_frame.columnconfigure(1, weight=1)

        # ----------------------------------------------------------------------
        # 行1: フォルダ選択
        # ----------------------------------------------------------------------
        lbl_folder = ttk.Label(main_frame, text="フォルダを選択:")
        lbl_folder.grid(row=0, column=0, sticky=tk.W, padx=(0, 8), pady=6)

        entry_folder = ttk.Entry(main_frame, textvariable=self.folder_path_var)
        entry_folder.grid(row=0, column=1, sticky=tk.EW, padx=(0, 8), pady=6)

        btn_folder = ttk.Button(
            main_frame, text="参照...", width=8, command=self._browse_folder
        )
        btn_folder.grid(row=0, column=2, sticky=tk.E, pady=6)

        # ----------------------------------------------------------------------
        # 行2: ファイル選択
        # ----------------------------------------------------------------------
        lbl_file = ttk.Label(main_frame, text="ファイルを選択:")
        lbl_file.grid(row=1, column=0, sticky=tk.W, padx=(0, 8), pady=6)

        entry_file = ttk.Entry(main_frame, textvariable=self.file_path_var)
        entry_file.grid(row=1, column=1, sticky=tk.EW, padx=(0, 8), pady=6)

        btn_file = ttk.Button(
            main_frame, text="参照...", width=8, command=self._browse_file
        )
        btn_file.grid(row=1, column=2, sticky=tk.E, pady=6)

        # ----------------------------------------------------------------------
        # 行3: 文字入力（幅6、左寄せ）
        # ----------------------------------------------------------------------
        lbl_text = ttk.Label(main_frame, text="文字を入力:")
        lbl_text.grid(row=2, column=0, sticky=tk.W, padx=(0, 8), pady=6)

        entry_text = ttk.Entry(
            main_frame, textvariable=self.input_text_var, width=6
        )
        entry_text.grid(row=2, column=1, sticky=tk.W, pady=6)

        # ----------------------------------------------------------------------
        # 行4: ボタン領域（実行 / 終了）
        # ----------------------------------------------------------------------
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=3, column=0, columnspan=3, sticky=tk.E, pady=(16, 0))

        btn_execute = ttk.Button(
            btn_frame, text="実行", width=10, command=self._execute
        )
        btn_execute.pack(side=tk.LEFT, padx=(0, 8))

        btn_close = ttk.Button(
            btn_frame, text="終了", width=10, command=self.destroy
        )
        btn_close.pack(side=tk.LEFT)

    def _browse_folder(self) -> None:
        """フォルダ選択ダイアログを表示し、選択結果を入力欄に反映"""
        selected_dir = filedialog.askdirectory(
            initialdir=self.folder_path_var.get() or INITIAL_DIR,
            title="フォルダを選択してください",
        )
        if selected_dir:
            self.folder_path_var.set(os.path.normpath(selected_dir))

    def _browse_file(self) -> None:
        """ファイル選択ダイアログを表示し、選択結果を入力欄に反映"""
        selected_file = filedialog.askopenfilename(
            initialdir=self.file_path_var.get()
            or self.folder_path_var.get()
            or INITIAL_DIR,
            title="ファイルを選択してください",
            filetypes=FILE_TYPES,
        )
        if selected_file:
            self.file_path_var.set(os.path.normpath(selected_file))

    def _execute(self) -> None:
        """実行ボタン押下時の処理: print_inputを直接呼び出してコンソールに出力"""
        folder_path = self.folder_path_var.get()
        file_path = self.file_path_var.get()
        input_text = self.input_text_var.get()

        print_input(folder_path, file_path, input_text)


def main() -> None:
    """アプリケーションのエントリーポイント"""
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
