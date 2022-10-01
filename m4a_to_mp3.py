import os
import ffmpeg
from tkinter import filedialog, messagebox

messagebox.showinfo("message", "mp3形式に変換するm4aファイルを選択してください。")
input_file_path = filedialog.askopenfilename()
input_file_name, input_file_ext = os.path.splitext(os.path.basename(input_file_path))

convert_target = ffmpeg.input(input_file_path)
result = ffmpeg.output(convert_target, input_file_path.replace("m4a", "mp3"))
ffmpeg.run(result)