# Dobra Strana · identitet studija

## Položaj

**Ime:** Dobra Strana. U svim materijalima piše se s razmakom, bez točke. Ime povezuje dobru stranu posla koju klijent želi pokazati i web stranicu na kojoj to može učiniti.

**Glavna poruka:** Web stranica koja pokazuje *dobru stranu* vašeg posla.

**Kratki opis:** Studio iz Zagreba koji za obrte i male tvrtke u Hrvatskoj oblikuje identitet, piše tekst prema njihovim podacima te dizajnira i izrađuje jednostavnu web stranicu.

**Publika:** obrti, zdravlje, usluge i ugostiteljstvo; mikro i mala poduzeća. Ne navodimo imena osnivača u marketinškom sadržaju.

**Ton:** izravan, topao i precizan. Govorimo „mi” i „vi”. Kratke rečenice, obične riječi, bez žargona. Naslovi u rečeničnom obliku. Ne obećavamo rezultate prodaje, pozicije na tražilicama, izjave klijenata ni rok koji nismo potvrdili.

**Interpunkcija:** crtice (—, –) ne koristimo kao interpunkciju. Umjesto njih točka, zarez ili razdjelnik „·”.

## Znak i logotip

Znak čine dva suprotna kuta koji zajedno tvore **okvir tražila**. Unutar okvira je klijentov posao, prikazan s najbolje strane. Kutovi su osnovni element sustava: okviri oko radova, oznake sekcija, fokus i pokret na stranici.

Natpis „Dobra *Strana*” vektoriziran je iz Fraunces (Dobra uspravno, Strana kurzivom u boji naglaska) i uvijek stoji s razmakom između riječi. Logotipe gradi `assets/build-logo.py` iz Fraunces TTF datoteka (repozitorij `google/fonts`, mapa `ofl/fraunces`).

| Primjena | Zaključani logotip | Samostalan znak |
|---|---|---|
| Svijetla podloga | `assets/logo.svg` | `assets/mark.svg` |
| Tamna podloga | `assets/logo-dark.svg` | `assets/mark-dark.svg` |
| Jedna boja | `assets/logo-mono.svg` | `assets/mark-mono.svg` |

Na webu su kopije logotipa u `dist/`, favicon je `dist/favicon.svg`, a PNG znak za potpis e-pošte `dist/mark-email.png`. Oko znaka ostaviti slobodan prostor barem širine jednog kraka. Logotip ne rastezati, ne rotirati i ne dodavati sjene.

## Vizualni sustav

| Uloga | Naziv | HEX |
|---|---|---|
| Glavna podloga | Papir | `#F4F0E8` |
| Sekundarna podloga | Kamen | `#EAE5DA` |
| Hover svijetlog gumba | Glina | `#F3DED3` |
| Tekst i tamna podloga | Tinta | `#1F2421` |
| Naglasak na svijetlom | Cigla | `#B8432A` |
| Naglasak na tamnom | Žar | `#EE7A52` |
| Sekundarni tekst na svijetlom | Siva tinta | `#5E635C` |
| Sekundarni tekst na tamnom | Svijetla tinta | `#C9CCC2` |

**Slova:** naslovi **Fraunces** (lagana težina, uspravno), tekst i sučelje **Geist**, **Geist Mono** samo na dva mjesta: oznaka cijene i podaci o radu. Zamjenski fontovi: Georgia, Arial.

**Kurziv:** potpis branda, zato štedljivo. Dopušten samo u glavnom naslovu (*dobru stranu*), u logotipu i u završnom naslovu kontakta. Ostali naslovi su uspravni, a naglasak nose bojom naglaska. Bez malih oznaka iznad naslova sekcija.

**Ikone:** vlastiti linijski set u `dist/index.html` (24px mreža, linija 1.5, zaobljeni krajevi). Stoje u retku uz tekst, bez pločica. Cigla na svijetlom, Žar na tamnom.

**Površine:** suptilna zrnata tekstura preko cijele stranice, sjene tonirane tintom, zaobljeni rubovi (4, 10 i 18px), gumbi u obliku kapsule. Jedan naglasak po ekranu. Bez gradijenata i obojenih sjaja. Snimke radova prikazujemo bez nacrtanih okvira preglednika ili mobitela, samo s tankim rubom.

**Pokret:** jedan orkestrirani ulaz u heroju (riječi naslova, snimke, kutovi). Ostatak stranice je odmah vidljiv. Pri prelasku mišem jedan signal po elementu: gumb mijenja pozadinu, poveznica povlači podcrtu, oko rada se zatvore kutovi. Sve animacije poštuju postavku smanjenog pokreta.

**Boje u kodu:** svaka boja i font dolaze iz `tokens.css`. Nova vrijednost prvo dobiva imenovani token.

Boje, fontovi i razmaci definirani su u `tokens.css` i kopirani u `dist/tokens.css`. Brand board: `assets/brand-board.png` (izvor `assets/brand-board.html`). Slika za dijeljenje poveznice: `dist/og-image.png` (izvor `assets/og-image.html`).

## Ponuda i jezik stranice

**500 € ukupno, jednokratno** za jedan definirani početni paket:

- razgovor i jedan smjer identiteta;
- logo i osnovne verzije, boje i tipografija;
- tekst prema točnim podacima koje klijent dostavi;
- dizajn i izrada jedne responzivne web stranice;
- osnovne postavke za tražilice i objava;
- dva kruga dorada.

**Uvjeti koje smijemo navoditi:** plaćanje u dva dijela (50 % na početku, 50 % nakon odobrenja, prije objave); domena, datoteke logotipa i pristup stranici glase na klijenta; bez mjesečne pretplate, održavanje samo po dogovoru. Rok izrade ne navodimo javno, potvrđuje se u pisanoj ponudi.

Klijent dostavlja poslovne činjenice i vlastite fotografije. Dodatne stranice ili zahtjevi idu u zasebnu ponudu. Domena i održavanje nisu uključeni u cijenu. Trošak hostinga potvrđuje se pisanom ponudom prije početka. Porezni tretman treba potvrditi nakon osnivanja j.d.o.o. tako da javnih 500 € ostane ukupan iznos za kupca.

Navigacija ima samo logo i gumb **Javite se**. Glavni poziv: **Pogledajte radove.** Završni poziv: **Recite nam čime se bavite**, s gumbom za e-poštu. Odgovor na pristigli mail ostaje dodatni jednostavan put.

## Dokaz rada

Uz potvrdu da su identitet, dizajn i web naši te da imamo dopuštenje za prikaz:

- [Atasol](https://www.atasol.hr/): somatska psihoterapija u Zagrebu;
- [Produkt Auto](https://produktauto.com/): prodaja vozila u Oroslavju;
- [Dogan Septem Interijeri](https://www.doganseptem-interijeri.hr/): adaptacije i uređenje interijera.

Snimke u `dist/media/` (računalo i mobitel) zabilježene su s javnih početnih stranica. Opisi navode djelatnost i ono što se vidi na stranici. Nema izmišljenih rezultata ni izjava.

## Prije javne objave

1. Potvrditi naziv i slične žigove kroz [baze koje navodi DZIV](https://www.dziv.hr/hr/intelektualno-vlasnistvo/zigovi/podnosenje-prijave/pretrazite/). Preliminarna internetska pretraga nije pravna provjera.
2. Provjeriti i kupiti željenu `.hr` domenu putem [CARNET-ova registra](https://www.domene.hr/portal/home).
3. **Zamijeniti `[email]`** u sekciji Kontakt u `dist/index.html` (poveznica `mailto:` i vidljiva adresa) stvarnom poslovnom adresom. Isto u `outreach/potpis.html`, uz `[domena]`.
4. Nakon kupnje domene postaviti apsolutnu adresu u `og:image` (npr. `https://dobrastrana.hr/og-image.png`) kako bi se slika prikazala u pregledu poveznice.
5. Dovršiti osnivanje j.d.o.o., potvrditi porezni tretman cijene i podatke pružatelja usluge.
6. Povezati domenu, objaviti stranicu i provjeriti je bez prijave.
