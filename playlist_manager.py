import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, ttk
import random
import csv

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class Playlist:
    def __init__(self):
        self.songs = []
        self.repeat_mode = False

    def add_song(self, title, artist, duration, position=-1):
        song = Song(title, artist, duration)
        if position == -1 or position >= len(self.songs):
            self.songs.append(song)
        else:
            self.songs.insert(position, song)

    def remove_song_by_title(self, title):
        self.songs = [song for song in self.songs if song.title != title]

    def remove_song_by_position(self, position):
        if 0 <= position < len(self.songs):
            del self.songs[position]

    def display_playlist(self):
        return [f"{i}. {song.title} by {song.artist} ({song.duration} mins)" for i, song in enumerate(self.songs)]

    def move_song(self, from_pos, to_pos):
        if 0 <= from_pos < len(self.songs) and 0 <= to_pos < len(self.songs):
            song = self.songs.pop(from_pos)
            self.songs.insert(to_pos, song)

    def reverse_playlist(self):
        self.songs.reverse()

    def shuffle_playlist(self):
        random.shuffle(self.songs)

    def enable_repeat_mode(self):
        self.repeat_mode = True

    def disable_repeat_mode(self):
        self.repeat_mode = False

    def search_song(self, query):
        return [song for song in self.songs if song.title == query or song.artist == query]

    def save_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for song in self.songs:
                writer.writerow([song.title, song.artist, song.duration])

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    self.add_song(row[0], row[1], float(row[2]))

    def sort_by_title(self):
        self.songs.sort(key=lambda song: song.title)

    def sort_by_artist(self):
        self.songs.sort(key=lambda song: song.artist)
    
class PlaylistManager:
    def __init__(self, root):
        self.playlist = Playlist()
        self.root = root
        self.root.title("Playlist Manager")

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12, "bold"), foreground="#4CAF50")


        self.text_display = tk.Text(root, width=175, height=30, border=10)
        self.text_display.pack()

        self.frame = tk.Frame(root, width=175, height=15)
        self.frame.pack()

        self.add_button = ttk.Button(self.frame, text="Add Song", command=self.add_song, width = 40)
        self.add_button.grid(row=0, column=0)

        self.remove_button = ttk.Button(self.frame, text="Remove Song by Title", command=self.remove_song_by_title, width = 40)
        self.remove_button.grid(row=0, column=1)

        self.remove_position_button = ttk.Button(self.frame, text="Remove Song by Position", command=self.remove_song_by_position, width = 40)
        self.remove_position_button.grid(row=0, column=2)

        self.display_button = ttk.Button(self.frame, text="Display Playlist", command=self.display_playlist, width = 40)
        self.display_button.grid(row=1, column=0)

        self.move_button = ttk.Button(self.frame, text="Move Song", command=self.move_song, width = 40)
        self.move_button.grid(row=1, column=1)

        self.reverse_button = ttk.Button(self.frame, text="Reverse Playlist", command=self.reverse_playlist, width = 40)
        self.reverse_button.grid(row=1, column=2)

        self.shuffle_button = ttk.Button(self.frame, text="Shuffle Playlist", command=self.shuffle_playlist, width = 40)
        self.shuffle_button.grid(row=2, column=0)

        self.repeat_button = ttk.Button(self.frame, text="Enable Repeat Mode", command=self.toggle_repeat_mode, width = 40)
        self.repeat_button.grid(row=2, column=1)

        self.search_button = ttk.Button(self.frame, text="Search Song", command=self.search_song, width = 40)
        self.search_button.grid(row=2, column=2)

        self.sort_title_button = ttk.Button(self.frame, text="Sort by Title", command=self.sort_by_title, width = 40)
        self.sort_title_button.grid(row=3, column=0)

        self.sort_artist_button = ttk.Button(self.frame, text="Sort by Artist", command=self.sort_by_artist, width = 40)
        self.sort_artist_button.grid(row=3, column=1)

        self.save_button = ttk.Button(self.frame, text="Save Playlist", command=self.save_playlist, width = 40)
        self.save_button.grid(row=4, column=0)

        self.load_button = ttk.Button(self.frame, text="Load Playlist", command=self.load_playlist, width = 40)
        self.load_button.grid(row=4, column=1)
        
        self.new_playlist_button = ttk.Button(self.frame, text="New Playlist", command=self.new_playlist, width = 40)
        self.new_playlist_button.grid(row=3, column=2)

    def add_song(self):
        title = simpledialog.askstring("Input", "Enter Song Title:")
        artist = simpledialog.askstring("Input", "Enter Artist:")
        duration = simpledialog.askfloat("Input", "Enter Duration (in minutes):")
        position = simpledialog.askinteger("Input", "Enter Position (-1 for end):", minvalue=-1)
        
        if title and artist and duration is not None:
            self.playlist.add_song(title, artist, duration, position)
            messagebox.showinfo("Success", "Song added successfully!")
        self.display_playlist()

    def remove_song_by_title(self):
        title = simpledialog.askstring("Input", "Enter Song Title to Remove:")
        if title:
            self.playlist.remove_song_by_title(title)
            messagebox.showinfo("Success", "Song removed successfully!")
        self.display_playlist()

    def remove_song_by_position(self):
        position = simpledialog.askinteger("Input", "Enter Position of the Song to Remove:")
        if position is not None:
            self.playlist.remove_song_by_position(position)
            messagebox.showinfo("Success", "Song removed successfully!")
        self.display_playlist()

    def display_playlist(self):
        self.text_display.delete(1.0, tk.END)
        playlist_display = self.playlist.display_playlist()
        if playlist_display:
            self.text_display.insert(tk.END, "\n".join(playlist_display))
        else:
            self.text_display.insert(tk.END, "Playlist is empty.")

    def move_song(self):
        from_pos = simpledialog.askinteger("Input", "Enter Current Position of the Song:")
        to_pos = simpledialog.askinteger("Input", "Enter New Position of the Song:")
        if from_pos is not None and to_pos is not None:
            self.playlist.move_song(from_pos, to_pos)
            messagebox.showinfo("Success", "Song moved successfully!")
        self.display_playlist()

    def reverse_playlist(self):
        self.playlist.reverse_playlist()
        self.display_playlist()
        messagebox.showinfo("Success", "Playlist reversed successfully!")

    def shuffle_playlist(self):
        self.playlist.shuffle_playlist()
        self.display_playlist()
        messagebox.showinfo("Success", "Playlist shuffled successfully!")

    def toggle_repeat_mode(self):
        if self.playlist.repeat_mode:
            self.playlist.disable_repeat_mode()
            messagebox.showinfo("Repeat Mode", "Repeat mode disabled.")
        else:
            self.playlist.enable_repeat_mode()
            messagebox.showinfo("Repeat Mode", "Repeat mode enabled.")

    def search_song(self):
        query = simpledialog.askstring("Input", "Enter Song Title or Artist to Search:")
        if query:
            results = self.playlist.search_song(query)
            if results:
                result_text = "\n".join([f"{song.title} by {song.artist}" for song in results])
                messagebox.showinfo("Search Results", result_text)
            else:
                messagebox.showinfo("Search Results", "Song not found.")

    def sort_by_title(self):
        self.playlist.sort_by_title()
        self.display_playlist()
        messagebox.showinfo("Success", "Playlist sorted by title.")

    def sort_by_artist(self):
        self.playlist.sort_by_artist()
        self.display_playlist()
        messagebox.showinfo("Success", "Playlist sorted by artist.")

    def save_playlist(self):
        filename = simpledialog.askstring("Input", "Enter File Name to Save the Playlist:")
        if filename:
            self.playlist.save_to_file(filename)
            messagebox.showinfo("Success", f"Playlist saved to {filename}.")

    def load_playlist(self):    
        filename = filedialog.askopenfilename(
            title="Select Playlist File",
            filetypes=[("CSV Files", "*.csv")]
        )
    
        if filename:
            self.playlist.load_from_file(filename)  # Load the selected file
            messagebox.showinfo("Success", f"Playlist loaded from {filename}.")
            self.display_playlist()
        else:
            messagebox.showinfo("Error", "No file selected.")

    def new_playlist(self):
        save_first = messagebox.askyesnocancel("New Playlist", "Do you want to save the current playlist before creating a new one?")

        if save_first is None:
            return
        elif save_first:
            self.save_playlist()

        self.playlist.songs.clear()
        self.display_playlist()
        messagebox.showinfo("New Playlist", "New playlist created successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    app = PlaylistManager(root)
    root.mainloop()
