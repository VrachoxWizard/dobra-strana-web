# Dobra Strana · identitet studija

## Položaj

**Ime:** Dobra Strana. U svim materijalima piše se s razmakom, bez točke. Ime povezuje dobru stranu posla koju klijent želi pokazati i web stranicu na kojoj to može učiniti.

**Glavna poruka:** Web stranica koja pokazuje *dobru stranu* vašeg posla.

**Kratki opis:** Studio iz Zagreba koji za obrte i male tvrtke u Hrvatskoj oblikuje identitet, piše tekst prema njihovim podacima te dizajnira i izrađuje jednostavnu web stranicu.

**Publika:** prioritet su zdravlje i terapije te uslužne djelatnosti i savjetovanje; zatim obrti i ugostiteljstvo; mikro i mala poduzeća. Ne navodimo imena osnivača u marketinškom sadržaju.

**Promet:** većina posjetitelja dolazi iz hladnih poruka e-poštom i ne zna nas. Stranica mora u pola minute reći što radimo, za koga, koliko košta i zašto je sigurno javiti se.

**Ton:** izravan, topao i precizan. Govorimo „mi” i „vi”. Kratke rečenice, obične riječi, bez žargona i bez uskličnika. Naslovi u rečeničnom obliku. Ne obećavamo rezultate prodaje, pozicije na tražilicama ni rok koji nismo potvrdili. Izjave klijenata objavljujemo samo stvarne i uz njihovo dopuštenje, s imenom i inicijalom prezimena; smijemo dotjerati gramatiku, ne i smisao.

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
- dizajn i izrada pregledne responzivne web stranice; opseg se dogovara na prvom razgovoru, osnova je jedna stranica sa svim bitnim;
- osnovne postavke za tražilice i objava;
- dva kruga dorada.

**Uvjeti koje smijemo navoditi:** 500 € je konačan iznos za kupca. Plaćanje u dva dijela: 250 € kad klijent odobri prijedlog izgleda i teksta, 250 € kad odobri gotovu stranicu, prije objave. Razgovor i prijedlog ne naplaćujemo ako prijedlog nije odobren. Domena, datoteke logotipa i pristup stranici glase na klijenta; bez mjesečne pretplate, održavanje samo po dogovoru. Na upit odgovaramo isti ili idući radni dan. Rok izrade ne navodimo javno, potvrđuje se u pisanoj ponudi.

Klijent dostavlja poslovne činjenice i, ako ih ima, vlastite fotografije. Bez fotografija za početak biramo besplatne fotografije iz foto-baza, a za vlastite preporučujemo fotografa. Dodatne stranice ili zahtjevi idu u zasebnu ponudu. Domenu i hosting klijent plaća izravno pružatelju, na svoje ime; mi pomažemo odabrati najpovoljniju opciju i ne navodimo javno iznose. Nakon osnivanja j.d.o.o. potvrditi porezni tretman tako da javnih 500 € ostane ukupan iznos za kupca.

**Zašto 500 €:** paket je jasno ograničen i proces je uvijek isti. Tako to i objašnjavamo, bez popusta i hitnosti.

**Pozivi:** navigacija ima samo logo i gumb **Javite se**. Glavni poziv u heroju: **Pogledajte radove.** Gumb u cjeniku: **Zatražite prijedlog.** Završni poziv: **Recite nam čime se bavite**, s gumbom za e-poštu. Odgovor na pristigli mail ostaje dodatni jednostavan put.

**Naslovi i opis za tražilice:** title „Izrada web stranice i logotipa · Dobra Strana, Zagreb”; naslov sekcije paketa „Jedna cijena. Bez iznenađenja.” (ne „Sve uključeno”, jer domena, hosting i održavanje idu zasebno).

## Dokaz rada

Uz potvrdu da su identitet, dizajn i web naši te da imamo dopuštenje za prikaz:

- [Atasol](https://www.atasol.hr/): somatska psihoterapija u Zagrebu; izjava: Maja V.;
- [Produkt Auto](https://produktauto.com/): prodaja vozila u Oroslavju; izjava: Hasan L.;
- [Dogan Septem Interijeri](https://www.doganseptem-interijeri.hr/): adaptacije i uređenje interijera u Sesvetama; izjava: Mario J.

Snimke u `dist/media/` (računalo i mobitel) zabilježene su s javnih početnih stranica. Opisi navode djelatnost i ono što se vidi na stranici. Izjave su stvarne, objavljene uz dopuštenje klijenata, jezično dotjerane bez promjene smisla. Nema izmišljenih rezultata ni izjava.

## Prije javne objave

1. Potvrditi naziv i slične žigove kroz [baze koje navodi DZIV](https://www.dziv.hr/hr/intelektualno-vlasnistvo/zigovi/podnosenje-prijave/pretrazite/). Preliminarna internetska pretraga nije pravna provjera.
2. Provjeriti i kupiti željenu `.hr` domenu putem [CARNET-ova registra](https://www.domene.hr/portal/home).
3. **Zamijeniti `[email]`** u sekciji Kontakt u `dist/index.html` (poveznica `mailto:` i vidljiva adresa) stvarnom poslovnom adresom. Isto u `outreach/potpis.html`, uz `[domena]`.
4. Nakon kupnje domene zamijeniti probnu adresu u `og:image` (`https://dobra-strana-web-dist.vercel.app/og-image.png`) pravom domenom (npr. `https://dobrastrana.hr/og-image.png`) i **maknuti `<meta name="robots" content="noindex">`** iz `dist/index.html`, inače Google neće indeksirati stranicu.
5. Dovršiti osnivanje j.d.o.o., potvrditi porezni tretman cijene i podatke pružatelja usluge.
6. Povezati domenu, objaviti stranicu i provjeriti je bez prijave.
