# Python-ohjelmointi -kurssin koe

Kukin tehtävänanto löytyy erillisestä `.py`-tiedostosta. Tehtävien ratkaisut tulee toteuttaa näihin samoihin tiedostoihin ratkaisuille varattuihin kohtiin. Tehtävät ovat suuntaa-antavasti haastavuuden mukaan kasvavassa järjestyksessä.

1. [Tervehdys](./tervehdys.py)
2. [Viikonpäivä](./viikonpaiva.py)
3. [Puuttuva kirjain](./puuttuva_kirjain.py)
4. [Alkukirjaimet](./alkukirjaimet.py)
5. [Bingo](./bingo.py)

Jokaisen tehtävän painoarvo arvioinnissa on sama.

Voit tallentaa tehtävät itsellesi joko yksitellen, kloonata projektin Gitin avulla tai ladata kaikki tiedostot kerralla yhtenä zip-pakettina.


## Tehtävien testaaminen

Tehtävänannot sisältävät [doctest-testejä](https://docs.python.org/3/library/doctest.html), joiden avulla voit testata ohjelmasi toimintaa. Doctest-testit saat suoritettua oletuksena komennolla `python3 -m doctest --verbose tiedosto.py`. Mikäli Python on asennettuna sinulla eri nimellä, komento voi olla vaihtoehtoisesti esim. `py -m doctest --verbose tiedosto.py` tai `python -m doctest --verbose tiedosto.py`.


## Muutokset, tulosteet ja syötteet

Huomaa, että automaattisen arvioinnin vuoksi:

* et saa muuttaa funktioiden nimiä etkä niiden parametreja
* et saa nimetä tiedostoja uudelleen.

Ratkaisusi eivät saa kysyä käyttäjältä tietoja tai tehdä tulosteita, ellei näin ole ohjeistettu tehtävänannossa. Mikäli toteutat omia testejä ja kokeiluja, toteuta ne kurssin tehtävistä tuttuihin `if __name__ == "__main__":`-lohkoihin.

Kokeen tehtävänannot ja testit on tallennettu UTF-8 -merkistöllä, jota käytetään myös tehtävien automaattisessa tarkastamisessa. [UTF-8 on Pythonin oletusmerkistö](https://peps.python.org/pep-0686/).


## Kokeen arviointi

Kokeen arvioinnissa hyödynnetään automaattisia testejä, jotka ovat samankaltaisia kuin tehtävänannoissa esitetyt doctest-testit. Arvioinneissa käytettäviä testejä on kuitenkin enemmän ja ne testaavat ratkaisujasi eri syötteillä.

Kunkin tehtävän ratkaisu pisteytetään sen mukaan, kuinka suuren osan tehtävälle kirjoitetuista testeistä ratkaisu läpäisee. Automaattisen arvioinnin vuoksi on välttämätöntä, että toteuttamiesi funktioiden nimet ja parametrit vastaavat täysin tehtävänantoja. Ohjelmasi ei saa kysyä syötteitä eikä tehdä tulosteita, ellei niitä ole tehtävänannossa erikseen mainittu.

Kokeen ratkaisuissa on sallittua käyttää ainoastaan [Pythonin standardikirjastoa](https://docs.python.org/3/library/index.html). Erikseen esimerkiksi pip-komennolla asennettavat kirjastot, kuten NumPy tai pandas, eivät ole sallittuja. Suosittelemme että käytät kokeessa ainoastaan [Pythonin ylläpidettyjä versioita](https://devguide.python.org/versions/), joita käytetään myös ratkaisujesi automaattisessa arvioinnissa.

Laskulogiikka kokeen arvosanan laskemiseksi saamiesi pisteiden perusteella löytyy kurssin kotisivulta.


## Tyyppivihjeet

Näissä tehtäväpohjissa on hyödynnetty [tyyppivihjeitä (type hint)](https://docs.python.org/3/library/typing.html), jotka auttavat koodin ymmärtämisessä ja virheiden välttämisessä. Jos tyyppivihjeet sekoittavat sinua tai aiheuttavat ongelmia, voit poistaa ne tehtävistä. Tyyppivihjeiden tarkoituksena on helpottaa tehtävän ratkaisua, mutta niiden käyttö ei ole pakollista.


## Tehtävien tekijänoikeudet

Tehtävien ideoinnissa sekä tehtävänantojen laatimisessa on hyödynnetty ChatGPT-kielimalleja sekä GitHub copilot-työkalua.
