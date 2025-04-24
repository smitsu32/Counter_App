import tkinter as tk
from tkinter import ttk
import os

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.counter_value = 0
        
        # ウィンドウの設定
        self.root.title("シンプルカウンター")
        self.root.geometry("480x360")
        self.root.configure(bg="#f0f0f0")
        
        # スタイルの設定
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 14), padding=10)
        self.style.configure("TLabel", font=("Helvetica", 16), background="#f0f0f0")
        
        # メインフレーム
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")
        
        # タイトルラベル
        self.title_label = ttk.Label(self.main_frame, text="カウンターアプリ", font=("Helvetica", 22, "bold"))
        self.title_label.pack(pady=10)
        
        # カウンター表示
        self.counter_frame = tk.Frame(self.main_frame, bg="#e0e0e0", padx=15, pady=15, bd=2, relief=tk.RAISED)
        self.counter_frame.pack(pady=15)
        
        self.counter_label = ttk.Label(self.counter_frame, text=str(self.counter_value), font=("Helvetica", 36))
        self.counter_label.pack(pady=5)
        
        # ボタンフレーム - 基本操作
        self.button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.button_frame.pack(pady=10)
        
        # 減少ボタン (-1)
        self.decrement_button = ttk.Button(self.button_frame, text="-", command=self.decrement, width=5)
        self.decrement_button.pack(side=tk.LEFT, padx=10)
        
        # リセットボタン
        self.reset_button = ttk.Button(self.button_frame, text="リセット", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # 増加ボタン (+1)
        self.increment_button = ttk.Button(self.button_frame, text="+", command=self.increment, width=5)
        self.increment_button.pack(side=tk.LEFT, padx=10)
        
        # ボタンフレーム - 10ずつ操作
        self.button_frame_10 = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.button_frame_10.pack(pady=10)
        
        # 10ずつ減少ボタン (-10)
        self.decrement_10_button = ttk.Button(self.button_frame_10, text="-10", command=self.decrement_10, width=5)
        self.decrement_10_button.pack(side=tk.LEFT, padx=10)
        
        # 10ずつ増加ボタン (+10)
        self.increment_10_button = ttk.Button(self.button_frame_10, text="+10", command=self.increment_10, width=5)
        self.increment_10_button.pack(side=tk.LEFT, padx=10)
        
        # 保存・読み込みフレーム
        self.save_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.save_frame.pack(pady=15)
        
        self.save_button = ttk.Button(self.save_frame, text="保存", command=self.save_counter)
        self.save_button.pack(side=tk.LEFT, padx=10)
        
        self.load_button = ttk.Button(self.save_frame, text="読み込み", command=self.load_counter)
        self.load_button.pack(side=tk.LEFT, padx=10)
        
        # ステータス表示用ラベル
        self.status_label = ttk.Label(self.main_frame, text="", foreground="green")
        self.status_label.pack(pady=5)
        
        # 保存済みデータがあれば読み込む
        self.load_counter()
    
    def increment(self):
        self.counter_value += 1
        self.update_display()
    
    def decrement(self):
        self.counter_value -= 1
        self.update_display()
    
    def increment_10(self):
        self.counter_value += 10
        self.update_display()
        self.show_status(f"+10: {self.counter_value}になりました")
    
    def decrement_10(self):
        self.counter_value -= 10
        self.update_display()
        self.show_status(f"-10: {self.counter_value}になりました")
    
    def reset(self):
        self.counter_value = 0
        self.update_display()
        self.show_status("カウンターをリセットしました")
    
    def update_display(self):
        self.counter_label.config(text=str(self.counter_value))
    
    def show_status(self, message, is_error=False):
        # 既存のステータスメッセージをクリア
        self.status_label.config(text=message, foreground="red" if is_error else "green")
        # 2秒後にメッセージを消す
        self.root.after(2000, lambda: self.status_label.config(text=""))
    
    def save_counter(self):
        try:
            with open("counter.txt", "w") as file:
                file.write(str(self.counter_value))
            self.show_status("カウンター値が保存されました")
        except Exception as e:
            self.show_status(f"保存エラー: {str(e)}", True)
    
    def load_counter(self):
        try:
            if os.path.exists("counter.txt"):
                with open("counter.txt", "r") as file:
                    self.counter_value = int(file.read().strip())
                    self.update_display()
                    self.show_status("前回の値を読み込みました")
        except Exception as e:
            self.show_status(f"読み込みエラー: {str(e)}", True)

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()