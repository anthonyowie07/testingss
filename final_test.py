# Function to add songs to the playlist
def add_songs():
    print("It's time to add some sick songs to The Family Playlist!\nPS: no swearing")
    songs = []
    while True:
        song = input("Enter a song (or type 'done' to save songs): ")
        if song.lower() == 'done':
            break
        songs.append(song)

    # Write songs to the playlist file
    with open("playlist.dat", "a") as file:
        for song in songs:
            file.write(song + "\n")
    print("Songs added successfully!")

# Function to display the playlist
def display_playlist():
    print("\n \nHere's The Family Playlist:")
    try:
        with open("playlist.dat", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("The playlist is empty.")

# Main function to interact with the user
def main():
    print("Welcome to The Family Playlist!")
    while True:
        print("\nMain Menu:")
        print("1. Add songs to the playlist")
        print("2. View the playlist")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            add_songs()
        elif choice == '2':
            display_playlist()
        elif choice == '3':
            print("Thank you for using for checking out The Family Playlist. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()