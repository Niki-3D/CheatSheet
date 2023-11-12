from flask import Flask, jsonify

app = Flask(__name__)

titles = [
    {"id": 1, "title": "Najważniejsze wydarzenia"},
    {"id": 2, "title": "Najważniejsze osoby"},
    {"id": 3, "title": "Inne istotne informacje"}
]

details = {
    1: {
        "id": 1,
        "title": "Najważniejsze wydarzenia",
        "info": "Złoty Wieki Renesansu (The Golden Age of the Renaissance): W XVI wieku, Polska doświadczyła okresu intensywnego rozwoju nauki, sztuki i kultury. Renesans przyniósł ze sobą rozwój humanizmu, a polscy intelektualiści i artyści zaczęli czerpać inspirację z antycznych wzorców. W tym okresie powstały znaczące dzieła literackie, artystyczne i naukowe, które wpłynęły na kształtowanie się europejskiej myśli renesansowej. Uczestnictwo w układach politycznych: Polska odegrała istotną rolę w europejskich układach politycznych i dyplomatycznych. Przykładem może być udział w traktatach i sojuszach, które miały wpływ na stabilność regionu. Również konflikty i przymierza z innymi państwami kształtowały bieg historii Polski w tym okresie. Ewolucja społeczeństwa: XVI wiek to także czas, gdy polskie społeczeństwo ewoluowało pod wpływem zmian społeczno-politycznych. Zmiany te mogą obejmować rozwój warstw społecznych, zmiany w strukturze społecznej, a także ewolucję życia codziennego."
    },
    2: {
        "id": 2,
        "title": "Najważniejsze osoby",
        "info": "Zygmunt II August: Król, który odegrał kluczową rolę w zjednoczeniu Polski i Litwy w unii personalnej. Jego panowanie było okresem wzmożonej aktywności dyplomatycznej i kulturalnej. Mikołaj Rej: Pisarz i poeta, uznawany za jednego z przedstawicieli polskiego renesansu. Jego twórczość miała istotny wpływ na rozwój polskiej literatury i kultury. Humaniści i intelektualiści: Oprócz wymienionych postaci, XVI wiek w Polsce był bogaty w humanistów, filozofów i uczonych, którzy przyczynili się do rozwoju myśli renesansowej. Ich prace wpłynęły na rozwój nauki, filozofii i sztuki."
    },
    3: {
        "id": 3,
        "title": "Inne istotne informacje",
        "info": "Rozwój sztuki i architektury: XVI wiek to okres intensywnego rozwoju sztuki i architektury. Z tego czasu pochodzą liczne zabytki, które do dziś stanowią ważny element dziedzictwa kulturowego Polski. Architektura renesansowa zdobiła miasta, a artyści tworzyli dzieła inspirowane humanizmem. Kształtowanie się systemu politycznego i społecznego: W XVI wieku Polska doświadczała zmian w systemie politycznym i społecznym. To okres, w którym kształtowały się instytucje, mające wpływ na strukturę państwa i społeczeństwa. Reformy polityczne i społeczne wprowadzone w tym czasie miały długotrwałe konsekwencje dla polskiej historii. Wpływ na dalsze losy kraju: Decyzje podjęte w XVI wieku miały istotny wpływ na późniejsze wydarzenia w historii Polski. Zarówno kultura, jak i polityka tego okresu wpłynęły na kształtowanie się tożsamości narodowej i społecznej."
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
