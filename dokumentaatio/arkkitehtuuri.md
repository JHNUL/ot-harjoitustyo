
# Arkkitehtuuri

## Tietomalli

![Kuva](./images/data_model.png)

Kuvassa on sovelluksen persistoima data luokkakuvauksena. Sovelluksessa on pelaajia, joihin liittyy pelituloksia, ja nämä molemmat tallennetaan. Pelaajilla ei ole muuta rajoitetta kuin että nimi on yksilöllinen, eli kahta samaa pelaajanimeä ei voi rekisteröidä.

## Sovelluslogiikkaa

![Kuva](./images/game.png)

Kuvassa sovelluksen logiikan kannalta olennaisin kokonaisuus eli taso ja siinä vaikuttavat entiteetit. Taso tietää sisällään olevat entiteetit ja tason julkista metodia `move_pac` kutsutaan liikuttamaan Pacia. Taso myös tietää senhetkisen pistetilanteen, koska sen täytyy sitä pystyä manipuloimaan pelitapahtumien perusteella.