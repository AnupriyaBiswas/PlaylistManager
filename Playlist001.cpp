#include <iostream>
#include <string>
#include <fstream>
using namespace std;

class Song {
public:
    string title;
    string artist;
    double duration;

    Song(string t, string a, double d) : title(t), artist(a), duration(d) {}
};

class Playlist {
private:
    struct Node {
        Song* song;
        Node* next;
        Node(Song* s) : song(s), next(nullptr) {}
    };
    
    Node* head;
    int size;

public:
    Playlist() : head(nullptr), size(0) {}

    // Method to add a song
    void addSong(const string& title, const string& artist, double duration, int position = -1);

    // Method to remove a song by title or position
    void removeSong(const string& title);
    void removeSongByPosition(int position);

    // Method to display the entire playlist
    void displayPlaylist() const;

    // Method to reorder songs
    void moveSong(int fromPos, int toPos);
    void reversePlaylist();

    // Method to search for a song by title or artist
    void searchSong(const string& query) const;

    // Method to save and load the playlist from a file
    void saveToFile(const string& filename) const;
    void loadFromFile(const string& filename);
};

void Playlist::addSong(const string& title, const string& artist, double duration, int position) {
    Song* newSong = new Song(title, artist, duration);
    Node* newNode = new Node(newSong);

    if (position == -1 || position >= size) {
        // Add to the end
        if (head == nullptr) {
            head = newNode;
        } else {
            Node* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
    } else {
        // Add at specific position
        if (position == 0) {
            newNode->next = head;
            head = newNode;
        } else {
            Node* temp = head;
            for (int i = 0; i < position - 1 && temp != nullptr; ++i) {
                temp = temp->next;
            }
            if (temp != nullptr) {
                newNode->next = temp->next;
                temp->next = newNode;
            }
        }
    }
    size++;
}

void Playlist::removeSong(const string& title) {
    Node* temp = head;
    Node* prev = nullptr;

    while (temp != nullptr && temp->song->title != title) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == nullptr) return; // Song not found

    if (prev == nullptr) {
        head = temp->next;
    } else {
        prev->next = temp->next;
    }

    delete temp->song;
    delete temp;
    size--;
}

void Playlist::removeSongByPosition(int position) {
    if (position < 0 || position >= size) return;

    Node* temp = head;
    Node* prev = nullptr;

    for (int i = 0; i < position; ++i) {
        prev = temp;
        temp = temp->next;
    }

    if (prev == nullptr) {
        head = temp->next;
    } else {
        prev->next = temp->next;
    }

    delete temp->song;
    delete temp;
    size--;
}

void Playlist::displayPlaylist() const {
    Node* temp = head;
    int position = 0;
    double totalDuration = 0;

    while (temp != nullptr) {
        cout << position++ << ". " << temp->song->title << " by " << temp->song->artist 
                  << " (" << temp->song->duration << " mins)\n";
        totalDuration += temp->song->duration;
        temp = temp->next;
    }

    cout << "Total Duration: " << totalDuration << " mins\n";
}

void Playlist::moveSong(int fromPos, int toPos) {
    if (fromPos < 0 || fromPos >= size || toPos < 0 || toPos >= size) return;

    if (fromPos == toPos) return;

    // Find the node to move
    Node* temp = head;
    Node* prevFrom = nullptr;
    for (int i = 0; i < fromPos; ++i) {
        prevFrom = temp;
        temp = temp->next;
    }

    // Remove the node from the list
    if (prevFrom == nullptr) {
        head = temp->next;
    } else {
        prevFrom->next = temp->next;
    }

    // Reinsert the node at the new position
    if (toPos == 0) {
        temp->next = head;
        head = temp;
    } else {
        Node* temp2 = head;
        Node* prevTo = nullptr;
        for (int i = 0; i < toPos; ++i) {
            prevTo = temp2;
            temp2 = temp2->next;
        }
        prevTo->next = temp;
        temp->next = temp2;
    }
}

void Playlist::reversePlaylist() {
    Node* prev = nullptr;
    Node* current = head;
    Node* next = nullptr;

    while (current != nullptr) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
}

void Playlist::searchSong(const string& query) const {
    Node* temp = head;
    int position = 0;

    while (temp != nullptr) {
        if (temp->song->title == query || temp->song->artist == query) {
            cout << "Found: " << temp->song->title << " by " << temp->song->artist 
                      << " at position " << position << "\n";
            return;
        }
        position++;
        temp = temp->next;
    }

    cout << "Song not found.\n";
}

void Playlist::saveToFile(const string& filename) const {
    ofstream outFile(filename);
    Node* temp = head;

    while (temp != nullptr) {
        outFile << temp->song->title << "," << temp->song->artist << "," << temp->song->duration << "\n";
        temp = temp->next;
    }
    outFile.close();
}

int main()
{
    Playlist playlist;
    int choice;

    while(true){
        cout << "\n Playlist Manager : \n";
        cout << "1. Add a New Song\n";
        cout << "2. Remove a Song by Title\n";
        cout << "3. Remove a Song by Position\n";
        cout << "4. Display Playlist\n";
        cout << "5. Move Song from One Position to Another.\n";
        cout << "6. Reverse Playlist\n";
        cout << "7. Search for a Song by Title or Artist\n";
        cout << "8. Save Playlist to File\n";
        cout << "9. Exit\n\n";
        
        cout << "Choose an Option (1-9): ";
        cin >> choice;

        if(choice == 1){
            string title, artist;
            double duration;
            int pos;

            cout << "Enter Song Title            : ";
            cin.ignore();
            getline(cin, title);

            cout << "Enter Artist                : ";
            getline(cin, artist);

            cout << "Enter Duration (In Minutes) : ";
            cin >> duration;

            cout << "Enter Position (-1 for End) : ";
            cin >> pos;

            playlist.addSong(title, artist, duration, pos);
        }
        else if (choice == 2){
            string title;
            cout << "Enter Song Title to Remove : ";
            cin.ignore();
            getline(cin, title);

            playlist.removeSong(title);
        }
        else if (choice == 3){
            int pos;
            cout << "Enter Position of the Song to Remove : ";
            cin >>pos;

            playlist.removeSongByPosition(pos);
        }
        else if (choice == 4){
            playlist.displayPlaylist();
        }
        else if (choice == 5){
            int toPos, fromPos;
            cout << "Enter the Current Position of the Song : ";
            cin >> fromPos;

            cout << "Enter the New     Position of the Song : ";
            cin >> toPos;

            playlist.moveSong(fromPos, toPos);
        }
        else if (choice == 6){
            playlist.reversePlaylist();
            cout << "playlist Reversed.";
        }
        else if (choice == 7){
            string query;
            cout << "Enter Song Title or Artist to Search : ";
            cin.ignore();
            getline(cin, query);

            playlist.searchSong(query);
        }
        else if (choice == 8) {
            string filename;
            cout << "Enter File Name to Save the Playlist : ";
            cin.ignore();
            getline(cin, filename);

            playlist.saveToFile(filename);
            cout << "Playlist saved to " << filename << ".\n";
        }
        else if (choice == 9) {
            cout << "Exiting Playlist Manager.\n";
        }
        else{
            cout << "Invalid Choice. Please Try Again.\n";
        }
    }
    return 0;
}