# Arkkitehtuurikuvaus

## Rakenne
![pakkausrakenne](pakkaus.png)
- Screens sisältää nimensä mukaisesti näytöt ja kutsuu niiden liittyviä logiikoita
- Buttons kansio sisältää nappulat
- event_logic sisältää monimutkaisemmat pelilogiikat eli minipelit yms.
- static alakansiot sisältävät yläkansioon liittyvää grafiikkaa
- texts kansio sisältää ainoastaan ruudulle tulostettavaa tekstiä, koska tämä veisi muuten paljon tilaa riveiltä, josta pylint ei tykkää (voisi toki olla myös draw kansion alakansio)
- entities sisältää tietoa "olennoista" (tällä hetkellä pullosta ja käyttäjästä), jotka on eristetty pygame/käyttöliittymä asioista
- draw kansiossa on komennot jotka piirtävät kaikki kuvat ja tekstit joihon ei liity mitään logiikkaa (esim. niitä ei voi klikata)
## Käyttöliittymä
Käyttöliitymässä on tällä hetkellä kaksi eri ruutua:

- Aloitusvalikko
- Pääpeli (Pääpeli saatetaan jaotella myöhemmin vielä useampaan ruutuun)

Sovellus on hyvin käyttöliittymäkeskeinen, joten tein pakkausrakenteesta erilaisen kuin mallisovelluksessa.
## Sovelluslogiikka
-raha


## Tietojen pysyväistallennus
- Käyttäjän tiedot (nimi ja rahat) tallennetaan entities kansiossa olevaan users.py tiedostoon
### Tiedostot

## Päätoiminnallisuudet
- Käynnistä peli aloitusvalikosta
```mermaid
sequenceDiagram
  actor User
  participant gamemenu
  participant Buttons
  participant firstscreen
  User->>Buttons:Paina nappia "Aloita"
  Buttons->>Buttons: check_click()
  Buttons ->> gamemenu: return True
  gamemenu ->> main.py: start = True
  main.py ->> firstscreen: Screen1().run()
  
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
  participant event_logic
  User ->> event_logic: Paina pulloa
  event_logic ->> entites: Bottle("aluminium").isclicked()
  entites ->> event_logic: 0.15
  event_logic ->> Screens: 0.15
  Screens ->> entities: User().update_money(0.15)
  entites ->> Screens: aiemmat rahat +0.15

  

```


## Ohjelman rakenteeseen jääneet heikkoudet
- Testejä ei ole vielä tarpeeksi
- Käyttöliittymän ulkonäkö kaipaa hienosäätöä
- Ominaisuudet ovat vielä vajavaiset
- (Lisää juttua arkkitehtuuritiedostoon)
