# PACMAN

Sovellus on klassinen Pacman-peli, jossa pelaaja ohjaa Pacman-ötökkää labyrintin läpi tavoitteena syödä nappuloita ja väistellä vihollisia. Pelaajan tulee luoda käyttäjätunnus, jonka avulla pelaajan pelitulokset tallennetaan.

## Dokumentaatio

- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

## Asennus

Järjestelmässä on oltava seuraavat ohjelmistot asennettuna:

 - [Python](https://www.python.org/downloads/) v3.8+
 - [Poetry](https://python-poetry.org/)

Projektin riippuvuudet asennetaan komennolla:
```sh
poetry install
```

## Komentorivitoiminnot

Komennot ajetaan projektin juurihakemistossa.

1. Käynnistäminen
```sh
poetry run invoke start
```

2. Yksikkötestien ajo
```sh
poetry run invoke test
```

3. Yksikkötestiraportin muodostaminen
```sh
poetry run invoke coverage-report
```
Raportti muodostuu hakemistoon htmlcov.

4. Linttaus
```sh
poetry run invoke lint
```
