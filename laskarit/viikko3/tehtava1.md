# Tehtävä 1

![image](monopoli1.png)

Pelilauta sisältää monta ruutua, yksi ruutu kuuluu yhteen pelilautaan.

Ruutu tietää seuraavan ruudun sijainnin, mutta niiden välillä ei ole pysyvää yhteyttä, joten sitä on kuvattu katkoviivalla luokkaan itseensä.

Ruudussa voi olla monta pelinappulaa, mutta yksi pelinappula voi olla vain yhdessä ruudussa kerrallaan.

Pelaajan ja pelinappulan välillä on 1-1 suhde. Pelaaja lienee tarpeellinen entiteetti kuvattavaksi, koska on epäintuitiivista että pelinappula heittäisi noppaa tai että pelaaja sijaitsisi ruudussa, mutta tässä kokonaisuudessa pelaaja/pelinappula on sama asia.

Pelaajan ja pelinappulan välillä on riippuvuus, koska pelaaja käyttää noppia, mutta ilman pysyvää yhteyttä.