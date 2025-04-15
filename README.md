
# Tarinapeli:

Ideana olisi yksinkertainen peli, jossa pelaajan valinnat vaikuttavat tarinan kulkuun (mahdollisesti useampi lopetus). Peliin tulee mahdollisesti myös yksinkertaisia tehtäviä (minipelejä), joista suoriutuminen vaikuttaa tarinan kulkuun. 

Pelin voittaa, jos kerää tarpeeksi rahaa lemmikki parta-agamaan.
## Releaset:
[Tuorein versio](https://github.com/Sampinen/ot-harjoitusty-/releases/tag/viikko5)

[Viikko4](https://github.com/Sampinen/ot-harjoitusty-/releases/tag/viikko4)
## Dokumentaatio:
[Työaikakirjanpito](/TodoApp/dokumentaatio/Tyoaikakirjanpito.md)

[changelog](/TodoApp/dokumentaatio/changelog.md)

[Vaatimusmäärittely](/TodoApp/dokumentaatio/vaatimusmaarittely.md)

[Sovellusarkkitehtuuri](TodoApp/dokumentaatio/arkkitehtuuri.md)

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
poetry run invoke coverage
```
### Pylint

```bash
poetry run invoke lint
```


