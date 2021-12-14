# Käyttöohje

Lataa projektin lähdekoodi releases-sivulta tai kloonaa repositorio koneellesi.


Jos kloonaat repositoriota uudelleen, poista edellisen kerran generoima `data/database.prod.sqlite` tiedosto. Tauluihin on voinut tulla muutoksia versioiden välillä ja migraatiota ei ole.

## Ohjelman käynnistäminen

Asenna ensin projektin riippuvuudet komennolla:
```sh
poetry install
```

Sen jälkeen käynnistä peli komennolla:
```sh
poetry run invoke start
```

## Kirjautuminen

Pelin alussa pelaajaa pyydetään luomaan pelaajatunnus. Käyttäjätunnukseen tarvitaan 1-10 normaalia aakkosta ja/tai numeroa.

![Kuva](./images/login.png)

## Kirjautumisen jälkeen

Peli alkanee. Tämä on vielä vähän raffi visuaalinen ilme, mutta homma ei ole vielä valmis.

![Kuva](./images/pacman.png)