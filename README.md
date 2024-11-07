I want to create a console-based application that allows users to manage a music playlist using a linked list. The application should support adding, removing, displaying and rearranging songs.

Key Features : 
1.	Add a new song to the Playlist:
a.	Users can add a new song to the end or a specific position in the playlist.
b.	The song should have properties like 'title', 'artist' and 'duration'

2.	Removing song from the playlist:
a.	Users can remove a song by its title or position in the playlist

3.	Display Playlist:
a.	Display the entire Playlist showing the song's position, title, artist and duration.
b.	Optionally, display the total duration of all songs

4.	Reorder Songs
a.	Move a song from one position to another within the playlist.
b.	Reverse the entire playlist

5.	Search for a song:
a.	Search for a song by title or an artist and get its position in the playlist.

6.	Save and Load Playlist:
a.	Save the current playlist to a file and load it back into the application

Technical Details:
1.	Data Structure:
a.	Implement the playlist using a Singly-Linked list or a doubly-linked list. Each node in the list will represent a song, containing the song's details and a pointer/reference to the next song in the list.

2.	Classes and Methods:
a.	Song Class: To store details of each song.(Title, artist, duration)
b.	Playlist Class: To manage the linked list of songs with methods like 'addSong', 'removeSong', 'displaySong', 'displayPlaylist', 'reorderSongs' and 'searchSong'.

3.	Operations:
a.	Add Node: Insert a new Song into the linked list
b.	Delete Node: Remove a song from the linked list.
c.	Traverse List: Display the songs by traversing the linked list.
d.	Rearrange Nodes: Change the order of the songs by updating the pointers in the linked list.

Advanced Features:
1.	Shuffle Playlist: Randomly reorder the songs in the playlist
2.	Repeat Mode: Create a loop in the linked list to stimulate a repeat function, where the last song links back to the first song.
3.	Sort Playlist: Sort the songs alphabetically, or by title, or by artist.
4.	Graphical Interface: Build a simple GUI for the playlist manager using a framework like Tkinter(Python).

Language and Tools:
1.	Programming Language: C++, Python
2.	Text Editor: VS Code
