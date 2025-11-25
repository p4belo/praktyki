# Chatbot-api-key
Chatbot based on OpenRouter free API key

## Pobranie bibliotek
Aby uruchomić aplikację trzeba pobrać wszystkie biblioteki, aby to zrobic uruchom terminal
1. Tkinter nie trzeba instalować przez pip, ponieważ jest częścią standardowej biblioteki Pythona, ale na Linuxie czasami trzeba doinstalować pakiet:

`sudo apt install  python3-tk`

2. Requests aby wysyłać zapytania HTTP do API

`pip install requests`

## Ustawienie i wygenerowanie klucza API
Jak już biblioteki zostały pobrane to następnym krokiem będzie pobranie klucza API ze strony openrouter oraz ustawienie zmiennej środowiskowej
1. Wchodzimy na stronę openrouter.ai
2. Rejestrujemy się bądź logujemy
3. W zakładce keys generujemy własny klucz api (Create API key) i skopiuj go i zapisz gdzieś ***NIGDY NIE UDOSTĘPNIAJ KLUCZA API OBCYM***
4. Ustawienie zmiennej środowiskowej
- LINUX/MacOS - w terminalu wchodzisz do swojej powłoki 

`nano ~/.bashrc` lub  `nano ~/.zshrc`

w tych powłokach wpisujesz 

`export klucz_api="<wklejasz tutaj swój klucz>"`

następnie wpisujesz już w terminalu

``source ~/.bashrc`` (odpoowiednio zshrc tez może być)

- WINDOWS - w cmd wpisujesz komendę 

`setx klucz_api "<wklejasz tutaj swój klucz>"`

i restartujesz CMD

## Odpalenie
Odpalenie pliku wpisujesz w terminalu bądź CMD w folderze gdzie jest ten plik

`python chat.py`
    