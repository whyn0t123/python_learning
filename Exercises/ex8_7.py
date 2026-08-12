def make_album(singer_name, album_name, number=None):
    album = {'singer': singer_name.title(), "album's name": album_name.title()}
    if number:
        album['number'] = number
    return album

active = True

while active:
    print("enter 'q' at any time to quit this program.")
    
    singer = input("enter a singer's name: ")
    if singer == 'q':
        active = False 
        continue   

    albums = input("\nenter a album's name: ")
    if albums == 'q':
        active = False
        continue
    album_0 = make_album(singer, albums)

    print(album_0)