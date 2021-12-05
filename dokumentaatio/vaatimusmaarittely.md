# PACMAN

## Kuvaus
Sovellus on PACMAN-peli, jossa käyttäjä voi siis ohjata pac-ötökkää tavoitteenaan syödä nappuloita ja väistellä vihollisia. Kun pac syö supernappulan, se pystyy myös tuhoamaan vihollisia tietyn ajan kunnes tämä supervoima kuluu loppuun. Yksi taso koostuu labyrinttimaisesta pelikentästä, jonka läpäisemiseksi pacin täytyy onnistua syömään kaikki nappulat. Pelin alkaessa pelaajalle annetaan tietty määrä elämiä, joista poistuu yksi aina kun pac törmää viholliseen. Kun elämät ovat loppu, peli loppuu. Jos pelaaja onnistuu keräämään kaikki nappulat menettämättä kaikkia elämiä, on peli läpäisty.

### Sovelluksen käyttäjäroolit
Pelaaja

### Toiminnallisuuden kuvaus (MVP)
Tunnuksien luominen:
- pelaajan täytyy luoda käyttäjätunnus ***tehty***

Kirjautuminen:
- Kirjautuminen tapahtuu syöttämällä käyttäjätunnus, mitään salasanoja ei ole. Jos käyttäjätunnusta ei ole olemassa, se tallennetaan kirjautumisen yhteydessä.

Kirjautumisen jälkeen:
- pelaaja näkee *tuotantotasoisen* pelialustan ja leaderboardin, jossa listattu max 5 kappaletta parhaita tuloksia käyttäjätunnuksineen
- pelikentällä on vihollisia, jotka liikkuvat näennäisen satunnaisesti ***tehty***
- viholliseen törmäämisestä pelaaja menettää yhden elämän ***tehty***
- viholliseen törmäämisen jälkeen Pac on hetken aikaa turvassa mutta ei voi kerätä nappuloita ***tehty***
- pelaaja voi käynnistää pelin ja kontrolloida pac-ötökkää nuolinäppäimillä ***tehty***
- pelaaja voi kerätä nappuloita ***tehty***
- kerättyään supernappulan pelaaja voi syödä vihollisia tietyn ajan
- pelaaja näkee reaaliaikaisen pistesaldonsa ***tehty***
- pelaaja näkee jäljellä olevat elämänsä ***tehty***
- pelin läpäistyä pelaajan pistesaldo näkyy leaderboardissa, jos se riittää sinne pääsyyn
- peli loppuu jos pelaajan elämät loppuvat ***tehty***


## Toimintaympäristö
Sovelluksen tulee toimia Linux ja macOS-käyttöjärjestelmillä. Tuettu Python-versio on >= 3.8. Pelaajien käyttäjätunnukset ja pelikertojen tulokset tallentuvat sqlite-tietokantaan.

## Jatkokehitysideat
- pelaaja voi kirjautua ulos jolloin sovellus palaa kirjautumisnäkymään
- pelissä on useampia tasoja
- peliin voi "importata" itse luodun tason
- pelissä on vaikeusaste, joka vaikuttaa esimerkiksi vihollisten määrään, nopeuteen ja uudelleenilmestymisen tiheyteen
- vaikeusaste kasvaa joka tasolla
- pelaaja voi konfiguroida vaikeusasteen alkutason
- pelissä on replay-toiminnallisuus, jossa juuri pelatun tason voi katsoa uudelleen