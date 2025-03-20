import requests
import webbrowser

def get_playlists():
    # Здесь нужно реализовать логику для получения ссылок на открытые плейлисты с vkvideo.ru
    # Это может быть парсинг сайта или использование API, если оно существует
    playlists = [
        "https://vkvideo.ru/playlist1",
        "https://vkvideo.ru/playlist2",
        "https://vkvideo.ru/playlist3"
    ]
    return playlists

def main():
    playlists = get_playlists()
    index = 0
    
    while index < len(playlists):
        playlist_url = playlists[index]
        print(f"Открываю плейлист: {playlist_url}")
        
        # Открыть плейлист в браузере
        webbrowser.open(playlist_url)
        
        # Запрос на продолжение
        user_input = input("Продолжить? (y/n): ")
        if user_input.lower() == 'y':
            index += 1
        else:
            print("Завершение работы.")
            break

if __name__ == "__main__":
    main()
