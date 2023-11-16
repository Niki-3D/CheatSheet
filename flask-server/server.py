from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# titles = [
#     {"id": 1, "title": "Najważniejsze wydarzenia"},
#     {"id": 2, "title": "Najważniejsze osoby"},
#     {"id": 3, "title": "Inne istotne informacje"}
# ]
#
# details = {
#     1: {
#         "id": 1,
#         "title": "Najważniejsze wydarzenia",
#         "info": "Złoty Wieki Renesansu (The Golden Age of the Renaissance): W XVI wieku, Polska doświadczyła okresu intensywnego rozwoju nauki, sztuki i kultury. Renesans przyniósł ze sobą rozwój humanizmu, a polscy intelektualiści i artyści zaczęli czerpać inspirację z antycznych wzorców. W tym okresie powstały znaczące dzieła literackie, artystyczne i naukowe, które wpłynęły na kształtowanie się europejskiej myśli renesansowej. Uczestnictwo w układach politycznych: Polska odegrała istotną rolę w europejskich układach politycznych i dyplomatycznych. Przykładem może być udział w traktatach i sojuszach, które miały wpływ na stabilność regionu. Również konflikty i przymierza z innymi państwami kształtowały bieg historii Polski w tym okresie. Ewolucja społeczeństwa: XVI wiek to także czas, gdy polskie społeczeństwo ewoluowało pod wpływem zmian społeczno-politycznych. Zmiany te mogą obejmować rozwój warstw społecznych, zmiany w strukturze społecznej, a także ewolucję życia codziennego."
#     },
#     2: {
#         "id": 2,
#         "title": "Najważniejsze osoby",
#         "info": "Zygmunt II August: Król, który odegrał kluczową rolę w zjednoczeniu Polski i Litwy w unii personalnej. Jego panowanie było okresem wzmożonej aktywności dyplomatycznej i kulturalnej. Mikołaj Rej: Pisarz i poeta, uznawany za jednego z przedstawicieli polskiego renesansu. Jego twórczość miała istotny wpływ na rozwój polskiej literatury i kultury. Humaniści i intelektualiści: Oprócz wymienionych postaci, XVI wiek w Polsce był bogaty w humanistów, filozofów i uczonych, którzy przyczynili się do rozwoju myśli renesansowej. Ich prace wpłynęły na rozwój nauki, filozofii i sztuki."
#     },
#     3: {
#         "id": 3,
#         "title": "Inne istotne informacje",
#         "info": "Rozwój sztuki i architektury: XVI wiek to okres intensywnego rozwoju sztuki i architektury. Z tego czasu pochodzą liczne zabytki, które do dziś stanowią ważny element dziedzictwa kulturowego Polski. Architektura renesansowa zdobiła miasta, a artyści tworzyli dzieła inspirowane humanizmem. Kształtowanie się systemu politycznego i społecznego: W XVI wieku Polska doświadczała zmian w systemie politycznym i społecznym. To okres, w którym kształtowały się instytucje, mające wpływ na strukturę państwa i społeczeństwa. Reformy polityczne i społeczne wprowadzone w tym czasie miały długotrwałe konsekwencje dla polskiej historii. Wpływ na dalsze losy kraju: Decyzje podjęte w XVI wieku miały istotny wpływ na późniejsze wydarzenia w historii Polski. Zarówno kultura, jak i polityka tego okresu wpłynęły na kształtowanie się tożsamości narodowej i społecznej."
#     }
# }

titles = [
    {"id": 1, "title": "Anatomia układu mięśniowego"},
    {"id": 2, "title": "Kluczowe elementy mięśni"},
    {"id": 3, "title": "Inne istotne informacje"}
]

details = {
    1: {
        "id": 1,
        "title": "Anatomia układu mięśniowego",
        "info": "Tkanka mięśniowa i jej funkcje: Układ mięśniowy składa się z różnych rodzajów tkanek mięśniowych, które odgrywają kluczową rolę w ruchu i stabilności. Zrozumienie anatomii tkanek mięśniowych, w tym mięśni szkieletowych, gładkich i sercowych, jest istotne dla zrozumienia funkcjonowania układu mięśniowego. Interakcja z układem nerwowym: Układ mięśniowy ściśle współpracuje z układem nerwowym, umożliwiając zarówno dobrowolne, jak i nieświadome skurcze mięśni. Ta koordynacja jest istotna dla czynności od prostych ruchów do skomplikowanych aktywności sportowych. Rozwój siły i wytrzymałości mięśniowej: Zbadanie rozwoju siły i wytrzymałości mięśniowej jest kluczowe dla zrozumienia, w jaki sposób układ mięśniowy adaptuje się do różnych aktywności fizycznych i ćwiczeń. Czynniki takie jak odżywianie, aktywność fizyczna i odpoczynek przyczyniają się do ogólnego zdrowia mięśniowego."
    },
    2: {
        "id": 2,
        "title": "Kluczowe elementy mięśni",
        "info": "Główne mięśnie w ludzkim ciele: Podkreślenie kluczowych mięśni, takich jak biceps, triceps, czworogłowy i mięśnie dwugłowe uda, dostarcza informacji na temat ich funkcji i roli w ogólnym ruchu ciała. Znaczenie mięśni rdzenia: Mięśnie rdzenia, w tym mięśnie brzucha i dolnej części pleców, są kluczowe dla utrzymania postawy, równowagi i stabilności. Zrozumienie ich znaczenia pomaga zrozumieć podstawy układu mięśniowego. Układ mięśniowy w działaniu: Przyjrzenie się przykładom życia codziennego, takim jak chodzenie, bieganie czy podnoszenie przedmiotów, umożliwia lepsze zrozumienie dynamicznej natury skurczy i interakcji mięśni."
    },
    3: {
        "id": 3,
        "title": "Inne istotne informacje",
        "info": "Powszechne zaburzenia mięśni: Zbadanie warunków wpływających na układ mięśniowy, takich jak dystrofia mięśniowa czy miastenia, pozwala zrozumieć znaczenie dbania o zdrowie mięśni. Rehabilitacja i regeneracja mięśni: Zrozumienie procesu rehabilitacji mięśniowej i regeneracji po kontuzjach lub intensywnych aktywnościach jest kluczowe dla osób zaangażowanych w trening fizyczny lub powracających do zdrowia po problemach związanych z mięśniami. Wpływ układu mięśniowego na ogólne zdrowie: Oddziaływanie układu mięśniowego na ogólne zdrowie, w tym metabolizm, funkcję immunologiczną i zdrowie sercowo-naczyniowe, podkreśla wzajemne powiązania różnych systemów organizmu."
    }
}


@app.route('/titles')
def get_titles():
    return jsonify({"titles": titles})

@app.route('/titles/<int:title_id>')
def get_title_details(title_id):
    return jsonify(details[title_id])

if __name__ == '__main__':
    app.run(debug=True)
