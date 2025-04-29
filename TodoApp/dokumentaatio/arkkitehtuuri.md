# Arkkitehtuurikuvaus

## Rakenne
![pakkausrakenne](pakkaus.png)
- Screens sisältää nimensä mukaisesti näytöt ja kutsuu niiden liittyviä logiikoita
- Buttons sisältää nappulat (mahdollisesti liitetään myöhemmin event_logic kansion alakansioksi
- event_logic sisältää monimutkaisemmat pelilogiikat (peliin liittyvät minipelit)
- static kansio sisältää pelin grafiikat
## Käyttöliittymä
Käyttöliitymässä on tällä hetkellä kaksi eri ruutua:

- Aloitusvalikko
- Pääpeli (Pääpeli saatetaan jaotella myöhemmin vielä useampaan ruutuun)

Tällä hetkellä sovelluslogiikasta ainoastaan nappulat ovat erillisessä tiedostossa, tosin paljon siitäkin liittyy käyttöliittymään

Sovellus on hyvin käyttöliittymäkeskeinen, joten sovelluslogiikkaa ei ole ainakaan tällä hetkellä eristetty käyttöliittymästä. Sen sijaan eri toiminnallisuudet on eristetty omiin kansioihin.
## Sovelluslogiikka
Pullojen klikkaaminen nostaa rahamäärää


## Tietojen pysyväistallennus
- Tälläistä ominaisuutta ei vielä ole
### Tiedostot

## Päätoiminnallisuudet
- Käynnistä peli aloitusvalikosta
```mermaid
sequenceDiagram
  actor User
  participant Gamemenu
  participant Buttons
  participant firstscreen
Gamemenu->>Buttons: draw()
  User->>Buttons:Paina nappia "Aloita"
  Buttons->>Buttons: check_click()
  Buttons ->> firstscreen: Käynnistä Screen1() (tarkoitus muuttaa niin, että palauttaa jonkin arvon, jonka perusteella main käynnistää firstscreenin)
```
- Kirjoita nimi tekstikenttään ja palauta nimi ja lisää tekstiä painamalla enteriä
```mermaid
sequenceDiagram
  actor User
  participant firstscreen
  firstscreen->>firstscreen: input_rect()
  User->>firstscreen:Paina tekstikenttää
  firstscreen->>firstscreen: self.active=True
  User->>firstscreen: Paina kirjainta "K"
  firstscreen->>firstscreen: self.name = "K"
  User ->> firstscreen: Paina enteriä
  firstscreen ->> firstscreen: phase_one(0)
```
Kerää pullo (Todo)
```mermaid
sequenceDiagram
  actor User
  participant Screens
  participant even_logic

```


## Ohjelman rakenteeseen jääneet heikkoudet
- Testejä ei ole vielä tarpeeksi
- Käyttöliittymän ulkonäkö kaipaa hienosäätöä
- Ominaisuudet ovat vielä vajavaiset
- (Lisää juttua arkkitehtuuritiedostoon)
