
# Tarinapeli:

Ideana olisi yksinkertainen peli, jossa pelaajan valinnat vaikuttavat tarinan kulkuun (mahdollisesti useampi lopetus). Peliin tulee mahdollisesti myös yksinkertaisia tehtäviä (minipelejä), joista suoriutuminen vaikuttaa tarinan kulkuun. 

Pelin voittaa, jos kerää tarpeeksi rahaa lemmikki parta-agamaan.

## Dokumentaatio:
[Työaikakirjanpito](/TodoApp/dokumentaatio/Tyoaikakirjanpito.md)

[changelog](/TodoApp/dokumentaatio/changelog.md)

## Asennus- ja testien ajo-ohje (Aja seuraavat TodoApp kansiossa, älä juurikansiossa!)

Voit ajaa seuraavat komennot myös ajamalla ensin poetry shell (kunhan poetry install on ensin ajettu) ja sen jälkeen jättää poetry run osan kokonaan pois. 

### Riippuvuuksien asentaminen:

```bash
poetry install
```
### Alutustoimenpiteet:

```bash
poetry run invoke build
```

### Sovelluksen käynnistäminen

```bash
poetry run invoke start
```
### Testit
```bash
poetry run invoke test
```
### Testikattavuus

```bash
poetry run invoke coverage-report
```
### Pylint


## Vaatimusmäärittely:

Käyttäjät:

Sovelluksessa tulee olemaan vain yhdenlaisia käyttäjiä

Nykyiset toteutetut toiminnallisuudet:

- Aloitusvalikko
- Ruutu, jossa voit kirjoittaa tekstikenttään
    
Tulevat suunnitellut tominaisuudet:

- useampia ruutuja, joissa voit valita erilaisista vastausvaihtoehdoista, jotka sen mukaan vie toiseen ruutuun
- Raha
- Voittoruutu, jos onnistuit ostamaan parta-agaman
- kartta, jossa voi mennä eri paikkoihin (ainakin koti, eläinkauppa + jotain muita)

Mahdolliset muut ominaisuudet:

- Peliaika ja häviämisruutu, jos et ehtinyt ostaa parta-agamaa ajan loppuun mennessä
- parta-agamalle pitää ostaa myös terraario, sisusteet ja lamppu
- useampi voitto ja häviämisruutuja riippuen, mitä pelaaja valitsee
- Mahdollisuus muokata pelihahmoa
- Taidetta peliin
- tehtävä, jossa pitää itse kirjoittaa oikea vastaus kysymykseen
- tehtävä, jossa pitää klikata mahdollisimman monta ruudulla olevaa asiaa, ennenkuin aika loppuu
- Froggerin tyylinen tienylityspeli, jossa pitää ylittää tie jäämättä auton alle
- Kartalta voi kerätä klikkaamalla ihmisten jättämiä pulloja, joista saa rahaa menemällä kauppaan




[komentorivi.txt](https://github.com/Sampinen/ot-harjoitusty-/blob/main/laskarit/viikko1/komentorivi.txt)

[gitlog,txt][(https://pages.github.com/)](https://github.com/Sampinen/ot-harjoitusty-/blob/main/laskarit/viikko1/gitlog.txt)
