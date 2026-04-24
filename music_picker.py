def choose_music_file():
    from tkinter import Tk, filedialog

    root = Tk()
    root.withdraw()  # hide the empty Tk window

    file_path = filedialog.askopenfilename(
        title="Select a music file",
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")]
    )

    return file_path