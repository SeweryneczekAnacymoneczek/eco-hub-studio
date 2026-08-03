#  Eco-Hub Studio

Platforma Edukacyjno-Narzędziowa stworzona w ramach hackathonu. Naszym głównym celem jest budowanie świadomości ekologicznej w środowisku graczy, programistów i twórców serwerów oraz realne zahamowanie zmian klimatycznych poprzez optymalizację zużycia zasobów.

##  Problem, który rozwiązujemy
Sektor IT i gaming generują potężny ślad węglowy. Zamiast tworzyć kolejny nudny, suchy kalkulator, zbudowaliśmy interaktywną platformę z elementami gamifikacji, która zachęca do redukcji emisji CO2 i nagradza użytkowników za proekologiczne wybory.

##  Główne Funkcjonalności
- **Kalkulator Emisji:** Dynamiczne wyliczanie śladu węglowego na podstawie sprzętu (PC, serwery, konsole) i czasu pracy.
- **Eco-Towarzysz (System Maskotek):** Twój wirtualny zwierzak reaguje na Twój miesięczny wynik. Utrzymuj emisję na niskim poziomie, aby Twoja maskotka była szczęśliwa!
- **Gamifikacja i Ankiety:** Użytkownicy zdobywają Eco-Punkty (XP) za udział w głosowaniach dotyczących rozwoju platformy.
- **Eco-Hub Studio:** Zaawansowane narzędzia dla twórców, w tym transkrypcja mowy (Web Speech API), optymalizator wagi tekstu oraz generator gradientów.
- **Wielojęzyczność:** Pełne wsparcie dla 6 języków (PL, EN, ES, DE, RU, UK) tłumaczone w locie.

##  Stack Technologiczny
- **Backend:** Python 3, Flask
- **Baza danych:** SQLite3 (szyfrowanie haseł za pomocą Werkzeug)
- **Frontend:** HTML5, CSS3 (Glassmorphism UI, Custom CSS), JavaScript (ES6)
- **API:** Web Speech API, Google Translate API

##  Jak uruchomić projekt lokalnie?
1. Sklonuj repozytorium:
   `git clone https://github.com/SeweryneczekAnacymoneczek/eco-hub-studio.git`
2. Przejdź do folderu z projektem:
   `cd eco-hub-studio`
3. Zainstaluj wymagane biblioteki:
   `pip install flask werkzeug`
4. Uruchom aplikację:
   `python app.py`
5. Otwórz przeglądarkę i wejdź pod adres: `http://127.0.0.1:5000`