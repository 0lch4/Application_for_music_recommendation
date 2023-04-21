# Aplikacja-do-polecania-muzyki

Interface in Polish lang

Opis:
Znajduje piosenkę o podobnym brzmieniu na podstawie takich danych jak tempo nastrój energia itd
polecenie_muzyki to główna aplikacja która uruchamia trzy mniejsze

Aplikacja pobranie_piosneki pobiera od użytkownika nazwę oraz autora piosenki i zapisuje informacje o piosence do pliku wynik2.json

Aplikacja AI to prosta sieć neuronowa która pobiera parametry z wynik2.json, przetwarza dane i zapisuje do pliku wynik3.json dane piosenki która według niej jest podobna do pobranej

Aplikacja zwrócenie_piosenki pobiera dane z pliku wynik3.json, prosi użytkownika o wybranie gatunku piosenki z tych które znajdują się na liście, wysyła dane do spotify o wymaganiach utworu i następnie sciąga nam odpowiednią piosenkę

Podany gatunek nie musi się równać gatunkowi piosenki którą podaliśmy wcześniej! Jeśli podamy inny gatunek to dostaniemy piosenkę brzmiącą podobnie do orginału w tym gatunku który podaliśmy na koniec.


wymagane biblioteki:

pip install requests

pip inatall numpy

pip install tensorflow

pip install pybase64

Na początku plików pobrane_piosenki oraz zwrócenie_piosenki należy w poniższych liniach podać swoje id i secret do api spotify w tych liniach:

client_id = os.environ.get('Spotify_client_id')
client_secret = os.environ.get('Spotify_client_secret')

w moim przypadku są to zmienne środowiskowe, można podać po = sam klucz.
