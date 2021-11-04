# PACMAN

## Kuvaus
Sovellus on PACMAN-peli, jossa käyttäjä voi siis ohjata pac-ötökkää tavoitteenaan syödä nappuloita ja väistellä vihollisia. Kun pac syö supernappulan, se pystyy myös tuhoamaan vihollisia tietyn ajan kunnes tämä supervoima kuluu loppuun. Yksi taso koostuu labyrinttimaisesta pelikentästä, jonka läpäisemiseksi pacin täytyy onnistua syömään kaikki nappulat. Pelin alkaessa pelaajalle annetaan tietty määrä elämiä, joista poistuu yksi aina kun pac törmää viholliseen. Kun elämät ovat loppu, peli loppuu. Jos pelaaja onnistuu keräämään kaikkien tasojen nappulat menettämättä kaikkia elämiä, on peli läpäisty.

### Sovelluksen käyttäjäroolit
Pelaaja

### Toiminnallisuuden kuvaus (MVP)
Tunnuksien luominen:
- pelaajan täytyy luoda käyttäjätunnus ja nimimerkki
- sekä käyttäjätunnus että nimimerkki on oltava uniikkeja, järjestelmä ilmoittaa duplikaateista

Kirjautuminen:
- olemattomalla käyttäjätunnuksella kirjautumisesta ilmoitetaan

Kirjautumisen jälkeen:
- pelaaja näkee pelialustan ja leaderboardin, jossa listattu max 5 kappaletta parhaita tuloksia nimimerkkeineen
- pelaaja voi käynnistää pelin ja kontrolloida pac-ötökkää nuolinäppäimillä
- pelaaja näkee reaaliaikaisen pistesaldonsa
- pelaaja näkee, mitä tasoa parhaillaan pelaa
- pelin päätyttyä pelaajan pistesaldo näkyy leaderboardissa, jos se riittää sinne pääsyyn


## Toimintaympäristö
Sovelluksen tulee toimia Linux ja macOS-käyttöjärjestelmillä. Tuettu Python-versio on >= 3.8. Pelaajien käyttäjätunnukset ja pelikertojen tulokset tallentuvat sqlite-tietokantaan (tai tiedostoon).