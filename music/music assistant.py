import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        self.playlist = []
        self.current_song_index = 0

        pygame.init()

        self.create_widgets()
        self.update_song_label()

    def create_widgets(self):
        self.song_label = tk.Label(self.root, text="Select a folder and play music")
        self.song_label.pack(pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.select_folder_button = tk.Button(self.root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(side=tk.LEFT, padx=10)

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.playlist = [os.path.join(folder_selected, file) for file in os.listdir(folder_selected) if file.endswith(".mp3")]
            self.current_song_index = 0
            self.update_song_label()

    def play_music(self):
        if not pygame.mixer.music.get_busy() and self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_song_index])
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def update_song_label(self):
        if self.playlist:
            current_song = os.path.basename(self.playlist[self.current_song_index])
            self.song_label.config(text=current_song)
        else:
            self.song_label.config(text="No songs in playlist")

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
