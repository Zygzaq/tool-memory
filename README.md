# Tool Memory & Color Memory GIMP Plugins
Choose your language:
* [English](#english) 🇬🇧
* [Polski](#polski) 🇵🇱

---

<a name="english"></a>
## English 🇬🇧

## Description

The scripts add two additional items to the Tools menu - "Tool Memory" and "Color Memory".
Once activated, the scripts change the functionality of drawing tools.

## Features

- Tool Memory - Remembers the brush parameters for each tool separately (size, shape and behavior).
- Color Memory - Remembers the color for each tool separately.
- Once launched, the script runs in the background until the program is closed.

## Motivation - Why?

Before actually starting creative work, you usually prepare tools with specific properties suitable for the task at hand.
During expressive creative work, only the prepared tools are changed, not their characteristics/properties.
When manipulating a tool, one utilizes its individual characteristics to achieve a specific result, gaining skill in manipulating that characteristic, which often translates into a specific final effect dependent on the tool's constant characteristics.

Thanks to the individual settings of each tool's tip, as well as the ability to assign a separate color to each tool, one can use hand painting tools similarly to how one alternates between different types of brushes with different colors when creating a painting on canvas, or similarly to how an artist uses different types of pencils during professional drawing.
With this approach, each tool MUST have its own individual parameters, set by the artist, which should not be transferred to another tool when quickly changing them during painting.

ps. Personally, when painting/drawing, I change tools every few seconds/minutes, depending on the detail/fragment of the work being done.

## Installation

### GIMP 2.10

1. Copy files from the `v2.10/` folder to:

    - **Windows:** `%AppData%\GIMP\2.10\plug-ins\`
      ...if you don't know where the directory is on your hard drive, check the GIMP settings (Edit/Preferences|Folders/Plugins)
    - **Linux:** `~/.config/GIMP/2.10\plug-ins/`
    - **macOS:** `~/.config/GIMP/2.10/plug-ins/`

2. Grant execution permissions to script files (Linux/macOS only): 

    - `chmod +x ~/.config/GIMP/3.0/plug-ins/tool_memory.py`
    - `chmod +x ~/.config/GIMP/3.0/plug-ins/color_memory.py`

3. Restart GIMP

### GIMP 3.0

1. Copy folders from `v3.0/` to:

    - **Windows:** `%AppData%\GIMP\3.0\plug-ins\`
      ...if you don't know where the directory is on your hard drive, check the GIMP settings (Edit/Preferences|Folders/Plugins)
    - **Linux:** `~/.config/GIMP/3.0/plug-ins/`
    - **macOS:** `~/.config/GIMP/3.0/plug-ins/`

2. Grant execution permissions to script files (Linux/macOS only): 

    - `chmod +x ~/.config/GIMP/3.0/plug-ins/tool-memory/tool-memory.py`
    - `chmod +x ~/.config/GIMP/3.0/plug-ins/color-memory/color-memory.py`

3. Restart GIMP

## License

GPLv3

## Author

Zygzaq


***


<a name="polski"></a>
## Polski 🇵🇱

## Opis

Skrypty dodają do menu Narzędzia dwie dodatkowe pozycje - "Pamięć narzędzia" i "Pamięć koloru",
Po aktywacji skrypty zmieniają funkcjonalność narzędzi rysujących.

## Możliwości

- Pamięć narzędzia - Zapamiętuje parametry końcówki każdego narzędzia oddzielnie (rozmiar, kształt i zachowanie).
- Pamięć koloru - Zapamiętuje kolor każdego narzędzia oddzielnie.
- Po uruchomieniu skrypt działa w tle do czasu zamknięcia programu.

## Motywacja - Dlaczego tak?

Przed rzeczywistym przystąpieniem do pracy twórczej, zwykle przygotowuje się odpowiednie do podejmowanego zadania narzędzia o określonych właściwościach. 
W trakcie ekspresyjnej pracy twórczej zmienia się jedynie przygotowane narzędzia, a nie ich cechy/właściwości. 
Podczas operowania narzędziem wykorzystuje się jego indywidualną cechę do osiągnięcia określonego rezultatu, nabierając wprawy w operowaniu cechą, co przekłada się często na specyficzny, zależny od stałej cechy narzędzia efekt końcowy.
Dzięki indywidualnym ustawieniom końcówki każdego narzędzia oddzielnie, a także możliwości przydzielenia każdemu narzędziu osobnego koloru, można używać narzędzi do malowania ręcznego podobnie, jak używa się różnych rodzajów pędzli z różnymi kolorami na zmianę w trakcie tworzenia obrazu na płótnie, lub też podobnie, jak artysta operuje różnego rodzaju ołówkami podczas profesjonalnego rysownia. 
Przy takim podejściu każde narzędzie MUSI mieć swoje indywidualne, ustawione przez artystę parametry, które nie powinny być przenoszone na inne narzędzie podczas ich szybkiej zmiany w trakcie malowania. 

ps. Osobiście podczas malowania/rysowania zmieniam narzędzia co kilka sekund/minut w zależości od aktualnie realizowanego detalu/fragmentu rękodzieła.

## Instalacja

### GIMP 2.10

1. Skopiuj pliki z folderu `v2.10/` do folderu:

    - **Windows:** `%AppData%\GIMP\2.10\plug-ins\`
      ...jeśli nie wiesz gdzie znajduje się katalog na Twoim dysku, sprawdź w ustawieniach GIMP'a (Edycja/Preferencje|Katalogi/Wtyczki)
    - **Linux:** `~/.config/GIMP/2.10/plug-ins/`
    - **macOS:** `~/.config/GIMP/2.10/plug-ins/`

2. Nadaj plikom skryptów uprawnienia wykonywania (Linux/macOS):

    - `chmod +x ~/.config/GIMP/3.0/plug-ins/tool_memory.py`
    - `chmod +x ~/.config/GIMP/3.0/plug-ins/color_memory.py`

3. Zrestartuj program GIMP


### GIMP 3.0

1. Skopiuj foldery z `v3.0/` do folderu:

    - **Windows:** `%AppData%\GIMP\3.0\plug-ins\`
      ...jeśli nie wiesz gdzie znajduje się katalog na Twoim dysku, sprawdź w ustawieniach GIMP'a (Edycja/Preferencje|Katalogi/Wtyczki)
    - **Linux:** `~/.config/GIMP/3.0/plug-ins/`
    - **macOS:** `~/.config/GIMP/3.0/plug-ins/`

2. Nadaj plikom skryptów uprawnienia wykonywania (Linux/macOS):

    - `chmod +x ~/.config/GIMP/3.0/plug-ins/tool-memory/tool-memory.py`
    - `chmod +x ~/.config/GIMP/3.0/plug-ins/color-memory/color-memory.py`

3. Zrestartuj program GIMP


## Licencja

GPLv3

## Autor

Zygzaq
