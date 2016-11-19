#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys
import openpyxl
import base64


# Source: http://www.svb.nl/int/nl/kindernamen/
FIRSTNAMES = [
	'Lars', 'Lotte', 'Lynn', 'Fenna', 'Sara', 'Saar', 'Fleur', 'Tim', 
	'Daan', 'Sophie', 'Anna', 'Tess', 'Max', 'Ruben', 'Noa', 'Levi', 'Mees', 
	'Sarah', 'Thijs', 'Jayden', 'Evi', 'Emma', 'Lucas', 'Eva', 'Finn', 
	'Adam', 'Zoë', 'Maud', 'Lisa', 'Isa', 'Bram', 'Thomas', 'Sam', 'Noah', 
	'Lieke', 'Julian', 'Stijn', 'Julia', 'Milan', 'Sanne', 'Mila', 'Sem', 
	'Liam', 'Luuk', 'Jesse'
]

# Source: http://www.vernoeming.nl/meest-voorkomende-achternamen-van-nederland
LASTNAMES = [
	'de Jong', 'Jansen', 'de Vries', 'van de Berg', 'van den Berg', 
	'van der Berg', 'van Dijk', 'Bakker', 'Janssen', 'Visser', 'Smit', 
	'Meijer', 'Meyer', 'de Boer', 'Mulder', 'de Groot', 'Bos', 'Vos', 
	'Peters', 'Hendriks', 'van Leeuwen', 'Dekker', 'Brouwer', 'de Wit', 
	'Dijkstra', 'Smits', 'de Graaf', 'van der Meer', 'van der Linden', 
	'Kok', 'Jacobs', 'de Haan', 'Vermeulen', 'van den Heuvel', 
	'van de Veen', 'van der Veen', 'van den Broek', 'de Bruijn', 'de Bruyn',
	'de Bruin', 'van der Heijden', 'van der Heyden', 'Schouten', 'van Beek', 
	'Willems', 'van Vliet', 'van de Ven', 'van der Ven', 'Hoekstra', 'Maas', 
	'Verhoeven', 'Koster', 'van Dam', 'van de Wal', 'van der Wal', 'Prins', 
	'Blom', 'Huisman', 'Peeters', 'de Jonge', 'Kuipers', 'van Veen', 'Post', 
	'Kuiper', 'Veenstra', 'Kramer', 'van de Brink', 'van den Brink', 
	'Scholten', 'van Wijk', 'Postma', 'Martens', 'Vink', 'de Ruiter', 
	'Timmermans', 'Groen', 'Gerritsen', 'Jonker', 'van Loon', 'Boer', 
	'van de Velde', 'van den Velde', 'van der Velde', 'Willemsen', 'Smeets', 
	'de Lange', 'de Vos', 'Bosch', 'van Dongen', 'Schipper', 'de Koning', 
	'van der Laan', 'Koning', 'van de Velden', 'van den Velden', 
	'van der Velden', 'Driessen', 'van Doorn', 'Hermans', 'Evers', 
	'van den Bosch', 'van der Meulen', 'Hofman', 'Bosman', 'Wolters', 
	'Sanders', 'van der Horst', 'Mol', 'Kuijpers', 'Molenaar', 'van de Pol',
	'van den Pol', 'van der Pol', 'de Leeuw', 'Verbeek'
]

# No source
DOMAINS = ['gmail.com', 'live.com', 'yahoo.com']

# Source: https://nl.wikipedia.org/wiki/Lijst_van_straten_in_Amsterdam
STREETNAMES = [
	'1e Wetering-dwarsstraat', '2e Wetering-dwarsstraat', 
	'3e Wetering-dwarsstraat',  '1e Wetering-plantsoen', 
	'2e Wetering-plantsoen',  'Achter Oosteinde',  
	'Achtergracht', 'Amstel',  'Amstel-straat en -veld',  'Bakkers-straat',  
	'Balk in \'t Oog-steeg',  'Bloemenmarkt',  'Den Tex-straat',  
	'Falck-straat',  'Fokke Simonsz-straat',  'Frederiksplein',  
	'Geelvincksteeg',  'H.M. van Randwijk-plantsoen',  'Halvemaan-steeg',  
	'Herengracht',  'Hirsch Passage',  'Huidekoper-straat',  'Keizersgracht',  
	'Kerk-straat',  'Kleine-Gartman-plantsoen',  'Konings-plein',  
	'Korte Leidse-dwarsstraat',  'Korte Reguliers-dwarsstraat',  
	'Lange Leidse-dwarsstraat',  'Leidsegracht',  
	'Leidse-kade en -straat en -kruisstraat',  'Leidseplein',  
	'Lijnbaansgracht',  'Maarten Janzoon Koster-straat',  'Marnix-straat',  
	'Max Euwe-plein',  'Muntplein',  'Nicolaas Witsen-kade en -straat',  
	'Nieuwe Looiers-dwarsstraat en -straat',  'Nieuwe Spiegel-straat',  
	'Nieuwe Vijzel-gracht en -straat',  'Nieuwe Wetering-straat',  
	'Noorder-dwarsstraat en -straat',  'Oosteinde',  'Openhart-steeg',  
	'Paarden straat',  'Pieter Pauw-straat',  'Prinsen-gracht',  
	'Raamdwarsstraat',  'Reguliers-breestraat',  'Reguliers-dwarsstraat',  
	'Reguliers-gracht en -steeg',  'Rembrandtplein',  'Rokin',  
	'Sarphati-kade en -straat',  'Schapen-steeg',  'Singel',  
	'Sint Joris-straat',  'Spiegel-gracht',  'Thorbeckeplein',  
	'Utrechtse-dwarsstraat',  'Utrechtse-straat',  
	'Vijzel-gracht en -straat',  'Wagen-straat',  'Westeinde',  
	'Wetering-laan en -straat',  'Wetering-plantsoen en -schans',  
	'Ziesenis-kade'
]

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Source: http://allenamen.nl/plaatsnamen/plaatsnamen.html?letter=a
CITIES = [
	'Aadorp',  'Aagtekerke',  'Aalden',  'Aalsmeer',  'Aalsmeerderbrug',  
	'Aalst gld',  'Aalten',  'Aalzum',  'Aardenburg',  'Aarlanderveen',  
	'Aarle-Rixtel',  'Aartswoud',  'Abbega',  'Abbekerk',  'Abbenbroek',  
	'Abbenes',  'Abcoude',  'Achlum',  'Achterveld',  'Achthuizen',  
	'Achtmaal',  'Acquoy',  'Adorp',  'Aduard',  'Aerdenhout',  'Aerdt',  
	'Afferden gld',  'Afferden lb',  'Agelo',  'Akersloot',  'Akkrum',  
	'Akmarijp',  'Albergen',  'Alblasserdam',  'Aldeboarn',  'Aldtsjerk',  
	'Alem',  'Alkmaar',  'Allingawier',  'Almelo',  'Almen',  'Almere',  
	'Almkerk',  'Alphen aan den Rijn',  'Alphen gld',  'Alphen nb',  
	'Alteveer gem de Wolden',  'Alteveer gem Hoogeveen',  
	'Alteveer gem Noordenveld',  'Alteveer gn',  'Altforst',  'Ambt Delden',  
	'Ameide',  'Amen',  'America',  'Amerongen',  'Amersfoort',  'Ammerstol',  
	'Ammerzoden',  'Amstelhoek',  'Amstelveen',  'Amstenrade',  'Amsterdam',  
	'Amsterdam Zuidoost',  'Andel',  'Andelst',  'Anderen',  'Andijk',  'Ane',  
	'Anerveen',  'Anevelde',  'Angeren',  'Angerlo',  'Anjum',  'Ankeveen',  
	'Anloo',  'Anna Paulowna',  'Annen',  'Annerveensche Kanaal',  'Ansen',  
	'Apeldoorn',  'Appelscha',  'Appeltern',  'Appingedam',  'Arcen',  
	'Arkel',  'Arnemuiden',  'Arnhem',  'Arriën',  'Arum',  'Asch',  
	'Asperen',  'Assen',  'Assendelft',  'Asten',  'Augsbuurt',  
	'Augustinusga',  'Austerlitz',  'Avenhorn',  'Axel',  'Azewijn'
]

MUNICIPALITIES = [
    'Utrecht', 'Amsterdam', '\'s-Gravenhage', 'Den Haag', 'Rotterdam'
]

# Source: https://github.com/minimaxir/big-list-of-naughty-strings
NAUGTY_STRINGS = [
     "",
     "dW5kZWZpbmVkCg==",
     "dW5kZWYK",
     "bnVsbAo=",
     "TlVMTAo=",
     "KG51bGwpCg==",
     "bmlsCg==",
     "TklMCg==",
     "dHJ1ZQo=",
     "ZmFsc2UK",
     "VHJ1ZQo=",
     "RmFsc2UK",
     "Tm9uZQo=",
     "XFw=",
     "MAo=",
     "XFxcXAo=",
     "MQo=",
     "MS4wMAo=",
     "JDEuMDAK",
     "MS8yCg==",
     "MUUyCg==",
     "MUUwMgo=",
     "MUUrMDIK",
     "LTEK",
     "LTEuMDAK",
     "LSQxLjAwCg==",
     "LTEvMgo=",
     "LTFFMgo=",
     "LTFFMDIK",
     "LTFFKzAyCg==",
     "MS8wCg==",
     "MC8wCg==",
     "LTIxNDc0ODM2NDgvLTEK",
     "LTkyMjMzNzIwMzY4NTQ3NzU4MDgvLTEK",
     "MC4wMAo=",
     "MC4uMAo=",
     "Lgo=",
     "MC4wLjAK",
     "MCwwMAo=",
     "MCwsMAo=",
     "LAo=",
     "MCwwLDAK",
     "MC4wLzAK",
     "MS4wLzAuMAo=",
     "MC4wLzAuMAo=",
     "MSwwLzAsMAo=",
     "MCwwLzAsMAo=",
     "LS0xCg==",
     "LQo=",
     "LS4K",
     "LSwK",
     "OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5Cg==",
     "TmFOCg==",
     "SW5maW5pdHkK",
     "LUluZmluaXR5Cg==",
     "MHgwCg==",
     "MHhmZmZmZmZmZgo=",
     "MHhmZmZmZmZmZmZmZmZmZmZmCg==",
     "MHhhYmFkMWRlYQo=",
     "MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5Cg==",
     "MSwwMDAuMDAK",
     "MSAwMDAuMDAK",
     "MScwMDAuMDAK",
     "MSwwMDAsMDAwLjAwCg==",
     "MSAwMDAgMDAwLjAwCg==",
     "MScwMDAnMDAwLjAwCg==",
     "MS4wMDAsMDAK",
     "MSAwMDAsMDAK",
     "MScwMDAsMDAK",
     "MS4wMDAuMDAwLDAwCg==",
     "MSAwMDAgMDAwLDAwCg==",
     "MScwMDAnMDAwLDAwCg==",
     "MDEwMDAK",
     "MDgK",
     "MDkK",
     "Mi4yMjUwNzM4NTg1MDcyMDExZS0zMDgK",
     "LC4vOydbXS09Cg==",
     "PD4/OiJ7fXxfKwo=",
     "IUAjJCVeJiooKWB+Cg==",
     "zqniiYjDp+KImuKIq8ucwrXiiaTiiaXDtwo=",
     "w6XDn+KIgsaSwqnLmeKIhsuawqzigKbDpgo=",
     "xZPiiJHCtMKu4oCgwqXCqMuGw7jPgOKAnOKAmAo=",
     "wqHihKLCo8Ki4oiewqfCtuKAosKqwrrigJPiiaAK",
     "wrjLm8OH4peKxLHLnMOCwq/LmMK/Cg==",
     "w4XDjcOOw4/LncOTw5Tvo7/DksOaw4bimIMK",
     "xZLigJ7CtOKAsMuHw4HCqMuGw5jiiI/igJ3igJkK",
     "YOKBhOKCrOKAueKAuu+sge+sguKAocKwwrfigJrigJTCsQo=",
     "4oWb4oWc4oWd4oWeCg==",
     "0IHQgtCD0ITQhdCG0IfQiNCJ0IrQi9CM0I3QjtCP0JDQkdCS0JPQlNCV0JbQl9CY0JnQmtCb0JzQndCe0J/QoNCh0KLQo9Ck0KXQptCn0KjQqdCq0KvQrNCt0K7Qr9Cw0LHQstCz0LTQtdC20LfQuNC50LrQu9C80L3QvtC/0YDRgdGC0YPRhNGF0YbRh9GI0YnRitGL0YzRjdGO0Y8K",
     "2aDZodmi2aPZpNml2abZp9mo2akK",
     "4oGw4oG04oG1Cg==",
     "4oKA4oKB4oKCCg==",
     "4oGw4oG04oG14oKA4oKB4oKCCg==",
     "Jwo=",
     "Igo=",
     "JycK",
     "IiIK",
     "JyInCg==",
     "IicnJyciJyIK",
     "IiciJyInJycnIgo=",
     "55Sw5Lit44GV44KT44Gr44GC44GS44Gm5LiL44GV44GECg==",
     "44OR44O844OG44Kj44O844G46KGM44GL44Gq44GE44GLCg==",
     "5ZKM6KO95ryi6KqeCg==",
     "6YOo6JC95qC8Cg==",
     "7IKs7ZqM6rO87ZWZ7JuQIOyWtO2VmeyXsOq1rOyGjAo=",
     "7LCm7LCo66W8IO2DgOqzoCDsmKgg7Y6y7Iuc66eo6rO8IOyRm+uLpOumrCDrmKDrsKnqsIHtlZgK",
     "56S+5pyD56eR5a246Zmi6Kqe5a2456CU56m25omACg==",
     "7Jq4656A67CU7Yag66W0Cg==",
     "8KCcjvCgnLHwoJ258KCxk/CgsbjwoLKW8KCzjwo=",
     "44O94Ly84LqI2YTNnOC6iOC8ve++iSDjg73gvLzguojZhM2c4LqI4Ly9776JCg==",
     "KO+9oeKXlSDiiIAg4peV772hKQo=",
     "772A772oKMK04oiA772A4oipCg==",
     "X1/vvpsoLF8sKikK",
     "44O7KO+/o+KIgO+/oynjg7s6KjoK",
     "776f772l4py/44O+4pWyKO+9oeKXleKAv+KXle+9oSnilbHinL/vvaXvvp8K",
     "LOOAguODuzoqOuODu+OCnOKAmSgg4pi7IM+JIOKYuyAp44CC44O7Oio644O744Kc4oCZCg==",
     "KOKVr8Kw4pahwrDvvInila/vuLUg4pS74pSB4pS7KQo=",
     "KO++ieCypeebiuCype+8ie++ie+7vyDilLvilIHilLsK",
     "KCDNocKwIM2cypYgzaHCsCkK",
     "8J+YjQo=",
     "8J+RqfCfj70K",
     "8J+RviDwn5mHIPCfkoEg8J+ZhSDwn5mGIPCfmYsg8J+ZjiDwn5mNCg==",
     "8J+QtSDwn5mIIPCfmYkg8J+Zigo=",
     "4p2k77iPIPCfkpQg8J+SjCDwn5KVIPCfkp4g8J+SkyDwn5KXIPCfkpYg8J+SmCDwn5KdIPCfkp8g8J+SnCDwn5KbIPCfkpog8J+SmQo=",
     "4pyL8J+PvyDwn5Kq8J+PvyDwn5GQ8J+PvyDwn5mM8J+PvyDwn5GP8J+PvyDwn5mP8J+Pvwo=",
     "8J+aviDwn4aSIPCfhpMg8J+GlSDwn4aWIPCfhpcg8J+GmSDwn4+nCg==",
     "MO+4j+KDoyAx77iP4oOjIDLvuI/ig6MgM++4j+KDoyA077iP4oOjIDXvuI/ig6MgNu+4j+KDoyA377iP4oOjIDjvuI/ig6MgOe+4j+KDoyDwn5SfCg==",
     "77yR77yS77yTCg==",
     "2aHZotmjCg==",
     "2KvZhSDZhtmB2LMg2LPZgti32Kog2YjYqNin2YTYqtit2K/Zitiv2IwsINis2LLZitix2KrZiiDYqNin2LPYqtiu2K/Yp9mFINij2YYg2K/ZhtmILiDYpdiwINmH2YbYp9ifINin2YTYs9iq2KfYsSDZiNiq2YbYtdmK2Kgg2YPYp9mGLiDYo9mH2ZHZhCDYp9mK2LfYp9mE2YrYp9iMINio2LHZiti32KfZhtmK2Kct2YHYsdmG2LPYpyDZgtivINij2K7YsC4g2LPZhNmK2YXYp9mG2Iwg2KXYqtmB2KfZgtmK2Kkg2KjZitmGINmF2KcsINmK2LDZg9ixINin2YTYrdiv2YjYryDYo9mKINio2LnYrywg2YXYudin2YXZhNipINio2YjZhNmG2K/Yp9iMINin2YTYpdi32YTYp9mCINi52YQg2KXZitmILgo=",
     "15HWsNa816jWtdeQ16nWtNeB15nXqiwg15HWuNa816jWuNeQINeQ1rHXnNa515TWtNeZ150sINeQ1rXXqiDXlNa316nWuNa814HXnta315nWtNedLCDXldaw15DWtdeqINeU1rjXkNa416jWttelCg==",
     "15TWuNeZ1rDXqta415R0ZXN02KfZhNi12YHYrdin2Kog2KfZhNiq2ZHYrdmI2YQK",
     "77e9Cg==",
     "77e6Cg==",
     "4oCLCg==",
     "4ZqACg==",
     "4aCOCg==",
     "44CACg==",
     "77u/Cg==",
     "4pCjCg==",
     "4pCiCg==",
     "4pChCg==",
     "4oCq4oCqdGVzdOKAqgo=",
     "4oCrdGVzdOKAqwo=",
     "4oCpdGVzdOKAqQo=",
     "dGVzdOKBoHRlc3TigKsK",
     "4oGmdGVzdOKBpwo=",
     "4bmwzLrMusyVb82eIMy3acyyzKzNh8yqzZluzJ3Ml82VdsyfzJzMmMymzZ9vzLbMmcywzKBrw6jNmsyuzLrMqsy5zLHMpCDMlnTMnc2VzLPMo8y7zKrNnmjMvM2TzLLMpsyzzJjMsmXNh8yjzLDMpsyszY4gzKLMvMy7zLHMmGjNms2OzZnMnMyjzLLNhWnMpsyyzKPMsMykdsy7zY1lzLrMrcyzzKrMsC1tzKJpzYVuzJbMusyezLLMr8ywZMy1zLzMn82ZzKnMvMyYzLMgzJ7MpcyxzLPMrXLMm8yXzJhlzZlwzaByzLzMnsy7zK3Ml2XMusygzKPNn3PMmM2HzLPNjcydzYllzYnMpcyvzJ7Mss2azKzNnMe5zKzNjs2OzJ/Mls2HzKR0zY3MrMykzZPMvMytzZjNhWnMqsyxbs2gZ8y0zYkgzY/Nic2FY8yszJ9ozaFhzKvMu8yvzZhvzKvMn8yWzY3MmcydzYlzzJfMpsyyLsyozLnNiMyjCg==",
     "zKHNk8yezYVJzJfMmMymzZ1uzYfNh82ZdsyuzKtva8yyzKvMmc2IacyWzZnMrcy5zKDMnm7Mocy7zK7Mo8y6Z8yyzYjNmcytzZnMrM2OIMywdM2UzKZozJ7MsmXMosykIM2NzKzMss2WZsy0zJjNlcyjw6jNluG6ucylzKlszZbNlM2aac2TzZrMps2gbs2WzY3Ml82TzLPMrmfNjSDMqG/NmsyqzaFmzJjMo8ysIMyWzJjNlsyfzZnMrmPSic2UzKvNls2TzYfNls2FaMy1zKTMo82azZTDocyXzLzNlc2Fb8y8zKPMpXPMsc2IzLrMlsymzLvNoi7Mm8yWzJ7MoMyrzLAK",
     "zJfMus2WzLnMr82T4bmuzKTNjcylzYfNiGjMssyBZc2PzZPMvMyXzJnMvMyjzZQgzYfMnMyxzKDNk82NzYVOzZXNoGXMl8yxesyYzJ3MnMy6zZlwzKTMusy5zY3Mr82aZcygzLvMoM2ccsyozKTNjcy6zJbNlMyWzJZkzKDMn8ytzKzMnc2facymzZbMqc2TzZTMpGHMoMyXzKzNicyZbs2azZwgzLvMnsywzZrNhWjMtc2JacyzzJ52zKLNh+G4mc2OzZ8t0onMrcypzLzNlG3MpMytzKtpzZXNh8ydzKZuzJfNmeG4jcyfIMyvzLLNlc2ex6vMn8yvzLDMss2ZzLvMnWYgzKrMsMywzJfMlsytzJjNmGPMps2NzLLMns2NzKnMmeG4pc2aYcyuzY7Mn8yZzZzGocypzLnNjnPMpC7MncydINKJWsyhzJbMnM2WzLDMo82JzJxhzZbMsM2ZzKzNoWzMssyrzLPNjcypZ8yhzJ/MvMyxzZrMnsyszYVvzJfNnC7Mnwo=",
     "zKZIzKzMpMyXzKTNnWXNnCDMnMylzJ3Mu82NzJ/MgXfMlWjMlsyvzZNvzJ3NmcyWzY7MscyuINKJzLrMmcyezJ/NiFfMt8y8zK1hzLrMqs2NxK/NiM2VzK3NmcyvzJx0zLbMvMyuc8yYzZnNlsyVIMygzKvMoELMu82NzZnNicyzzYVlzLVozLXMrM2HzKvNmWnMuc2TzLPMs8yuzY7Mq8yVbs2fZMy0zKrMnMyWIMywzYnMqc2HzZnMss2ezYVUzZbMvM2TzKrNomjNj82TzK7Mu2XMrMydzJ/NhSDMpMy5zJ1XzZnMnsydzZTNh82dzYVhzY/Nk82UzLnMvMyjbMy0zZTMsMykzJ/NlOG4vcyrLs2VCg==",
     "WsyuzJ7MoM2ZzZTNheG4gMyXzJ7NiMy7zJfhuLbNmc2OzK/MucyezZNHzLtPzK3Ml8yuCg==",
     "y5nJkG5i4bSJbMmQIMmQdcaDyZDJryDHncm5b2xvcCDKh8edIMedyblvccmQbCDKh24gyod1bnDhtIlw4bSJyZR14bSJIMm5b2TJr8edyocgcG/Jr3Nu4bSJx50gb3AgcMedcyAnyofhtIlsx50gxoN14bSJyZRz4bSJZOG0iXDJkCDJuW7Kh8edyofJlMedc3VvyZQgJ8qHx53Jr8mQIMqH4bSJcyDJuW9sb3Agya9uc2ThtIkgya/Hncm5b8ulCg==",
     "MDDLmcaWJC0K",
     "77y0772I772FIO+9ke+9le+9ie+9g++9iyDvvYLvvZLvvY/vvZfvvY4g772G772P772YIO+9iu+9le+9je+9kO+9kyDvvY/vvZbvvYXvvZIg772U772I772FIO+9jO+9ge+9mu+9mSDvvYTvvY/vvYcK",
     "8J2Qk/CdkKHwnZCeIPCdkKrwnZCu8J2QovCdkJzwnZCkIPCdkJvwnZCr8J2QqPCdkLDwnZCnIPCdkJ/wnZCo8J2QsSDwnZCj8J2QrvCdkKbwnZCp8J2QrCDwnZCo8J2Qr/CdkJ7wnZCrIPCdkK3wnZCh8J2QniDwnZCl8J2QmvCdkLPwnZCyIPCdkJ3wnZCo8J2QoAo=",
     "8J2Vv/Cdlo3wnZaKIPCdlpbwnZaa8J2WjvCdlojwnZaQIPCdlofwnZaX8J2WlPCdlpzwnZaTIPCdlovwnZaU8J2WnSDwnZaP8J2WmvCdlpLwnZaV8J2WmCDwnZaU8J2Wm/CdlorwnZaXIPCdlpnwnZaN8J2WiiDwnZaR8J2WhvCdlp/wnZaeIPCdlonwnZaU8J2WjAo=",
     "8J2Ru/CdkonwnZKGIPCdkpLwnZKW8J2SivCdkoTwnZKMIPCdkoPwnZKT8J2SkPCdkpjwnZKPIPCdkofwnZKQ8J2SmSDwnZKL8J2SlvCdko7wnZKR8J2SlCDwnZKQ8J2Sl/CdkobwnZKTIPCdkpXwnZKJ8J2ShiDwnZKN8J2SgvCdkpvwnZKaIPCdkoXwnZKQ8J2SiAo=",
     "8J2To/Cdk7HwnZOuIPCdk7rwnZO+8J2TsvCdk6zwnZO0IPCdk6vwnZO78J2TuPCdlIDwnZO3IPCdk6/wnZO48J2UgSDwnZOz8J2TvvCdk7bwnZO58J2TvCDwnZO48J2Tv/Cdk67wnZO7IPCdk73wnZOx8J2TriDwnZO18J2TqvCdlIPwnZSCIPCdk63wnZO48J2TsAo=",
     "8J2Vi/CdlZnwnZWWIPCdlaLwnZWm8J2VmvCdlZTwnZWcIPCdlZPwnZWj8J2VoPCdlajwnZWfIPCdlZfwnZWg8J2VqSDwnZWb8J2VpvCdlZ7wnZWh8J2VpCDwnZWg8J2Vp/CdlZbwnZWjIPCdlaXwnZWZ8J2VliDwnZWd8J2VkvCdlavwnZWqIPCdlZXwnZWg8J2VmAo=",
     "8J2ag/CdmpHwnZqOIPCdmprwnZqe8J2akvCdmozwnZqUIPCdmovwnZqb8J2amPCdmqDwnZqXIPCdmo/wnZqY8J2aoSDwnZqT8J2anvCdmpbwnZqZ8J2anCDwnZqY8J2an/Cdmo7wnZqbIPCdmp3wnZqR8J2ajiDwnZqV8J2aivCdmqPwnZqiIPCdmo3wnZqY8J2akAo=",
     "4pKv4pKj4pKgIOKSrOKSsOKSpOKSnuKSpiDikp3ikq3ikqrikrLikqkg4pKh4pKq4pKzIOKSpeKSsOKSqOKSq+KSriDikqrikrHikqDikq0g4pKv4pKj4pKgIOKSp+KSnOKSteKStCDikp/ikqrikqIK",
     "PHNjcmlwdD5hbGVydCgxMjMpPC9zY3JpcHQ+Cg==",
     "Jmx0O3NjcmlwdCZndDthbGVydCgmIzM5OzEyMyYjMzk7KTsmbHQ7L3NjcmlwdCZndDsK",
     "PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEyMykgLz4K",
     "PHN2Zz48c2NyaXB0PjEyMzwxPmFsZXJ0KDEyMyk8L3NjcmlwdD4K",
     "Ij48c2NyaXB0PmFsZXJ0KDEyMyk8L3NjcmlwdD4K",
     "Jz48c2NyaXB0PmFsZXJ0KDEyMyk8L3NjcmlwdD4K",
     "PjxzY3JpcHQ+YWxlcnQoMTIzKTwvc2NyaXB0Pgo=",
     "PC9zY3JpcHQ+PHNjcmlwdD5hbGVydCgxMjMpPC9zY3JpcHQ+Cg==",
     "PCAvIHNjcmlwdCA+PCBzY3JpcHQgPmFsZXJ0KDEyMyk8IC8gc2NyaXB0ID4K",
     "b25mb2N1cz1KYVZhU0NyaXB0OmFsZXJ0KDEyMykgYXV0b2ZvY3VzCg==",
     "IiBvbmZvY3VzPUphVmFTQ3JpcHQ6YWxlcnQoMTIzKSBhdXRvZm9jdXMK",
     "JyBvbmZvY3VzPUphVmFTQ3JpcHQ6YWxlcnQoMTIzKSBhdXRvZm9jdXMK",
     "77ycc2NyaXB077yeYWxlcnQoMTIzKe+8nC9zY3JpcHTvvJ4K",
     "PHNjPHNjcmlwdD5yaXB0PmFsZXJ0KDEyMyk8L3NjPC9zY3JpcHQ+cmlwdD4K",
     "LS0+PHNjcmlwdD5hbGVydCgxMjMpPC9zY3JpcHQ+Cg==",
     "IjthbGVydCgxMjMpO3Q9Igo=",
     "JzthbGVydCgxMjMpO3Q9Jwo=",
     "SmF2YVNDcmlwdDphbGVydCgxMjMpCg==",
     "O2FsZXJ0KDEyMyk7Cg==",
     "c3JjPUphVmFTQ3JpcHQ6cHJvbXB0KDEzMikK",
     "Ij48c2NyaXB0PmFsZXJ0KDEyMyk7PC9zY3JpcHQgeD0iCg==",
     "Jz48c2NyaXB0PmFsZXJ0KDEyMyk7PC9zY3JpcHQgeD0nCg==",
     "PjxzY3JpcHQ+YWxlcnQoMTIzKTs8L3NjcmlwdCB4PQo=",
     "IiBhdXRvZm9jdXMgb25rZXl1cD0iamF2YXNjcmlwdDphbGVydCgxMjMpCg==",
     "JyBhdXRvZm9jdXMgb25rZXl1cD0namF2YXNjcmlwdDphbGVydCgxMjMpCg==",
     "PHNjcmlwdHgyMHR5cGU9InRleHQvamF2YXNjcmlwdCI+amF2YXNjcmlwdDphbGVydCgxKTs8L3NjcmlwdD4K",
     "PHNjcmlwdHgzRXR5cGU9InRleHQvamF2YXNjcmlwdCI+amF2YXNjcmlwdDphbGVydCgxKTs8L3NjcmlwdD4K",
     "PHNjcmlwdHgwRHR5cGU9InRleHQvamF2YXNjcmlwdCI+amF2YXNjcmlwdDphbGVydCgxKTs8L3NjcmlwdD4K",
     "PHNjcmlwdHgwOXR5cGU9InRleHQvamF2YXNjcmlwdCI+amF2YXNjcmlwdDphbGVydCgxKTs8L3NjcmlwdD4K",
     "PHNjcmlwdHgwQ3R5cGU9InRleHQvamF2YXNjcmlwdCI+amF2YXNjcmlwdDphbGVydCgxKTs8L3NjcmlwdD4K",
     "PHNjcmlwdHgyRnR5cGU9InRleHQvamF2YXNjcmlwdCI+amF2YXNjcmlwdDphbGVydCgxKTs8L3NjcmlwdD4K",
     "PHNjcmlwdHgwQXR5cGU9InRleHQvamF2YXNjcmlwdCI+amF2YXNjcmlwdDphbGVydCgxKTs8L3NjcmlwdD4K",
     "J2AiPjx4M0NzY3JpcHQ+amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "J2AiPjx4MDBzY3JpcHQ+amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "QUJDPGRpdiBzdHlsZT0ieHgzQWV4cHJlc3Npb24oamF2YXNjcmlwdDphbGVydCgxKSI+REVGCg==",
     "QUJDPGRpdiBzdHlsZT0ieDpleHByZXNzaW9ueDVDKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDpleHByZXNzaW9ueDAwKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDpleHB4MDByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDpleHB4NUNyZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4MEFleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4MDlleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTN4ODB4ODBleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4ODRleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4QzJ4QTBleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4ODBleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4OEFleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4MERleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4MENleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4ODdleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RUZ4QkJ4QkZleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4MjBleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4ODhleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4MDBleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4OEJleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4ODZleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4ODVleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4ODJleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4MEJleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4ODFleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4ODNleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "QUJDPGRpdiBzdHlsZT0ieDp4RTJ4ODB4ODlleHByZXNzaW9uKGphdmFzY3JpcHQ6YWxlcnQoMSkiPkRFRgo=",
     "PGEgaHJlZj0ieDBCamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDBGamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEMyeEEwamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDA1amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUxeEEweDhFamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDE4amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDExamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweDg4amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweDg5amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweDgwamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDE3amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDAzamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDBFamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDFBamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDAwamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDEwamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweDgyamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDIwamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDEzamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDA5amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweDhBamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDE0amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDE5amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweEFGamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDFGamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweDgxamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDFEamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweDg3amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDA3amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUxeDlBeDgwamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweDgzamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDA0amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDAxamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDA4amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweDg0amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweDg2amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUzeDgweDgwamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDEyamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDBEamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDBBamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDBDamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDE1amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweEE4amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDE2amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDAyamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDFCamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDA2amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweEE5amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgweDg1amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDFFamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieEUyeDgxeDlGamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0ieDFDamF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0iamF2YXNjcmlwdHgwMDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0iamF2YXNjcmlwdHgzQTpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0iamF2YXNjcmlwdHgwOTpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0iamF2YXNjcmlwdHgwRDpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "PGEgaHJlZj0iamF2YXNjcmlwdHgwQTpqYXZhc2NyaXB0OmFsZXJ0KDEpIiBpZD0iZnV6emVsZW1lbnQxIj50ZXN0PC9hPgo=",
     "YCInPjxpbWcgc3JjPXh4eDp4IHgwQW9uZXJyb3I9amF2YXNjcmlwdDphbGVydCgxKT4K",
     "YCInPjxpbWcgc3JjPXh4eDp4IHgyMm9uZXJyb3I9amF2YXNjcmlwdDphbGVydCgxKT4K",
     "YCInPjxpbWcgc3JjPXh4eDp4IHgwQm9uZXJyb3I9amF2YXNjcmlwdDphbGVydCgxKT4K",
     "YCInPjxpbWcgc3JjPXh4eDp4IHgwRG9uZXJyb3I9amF2YXNjcmlwdDphbGVydCgxKT4K",
     "YCInPjxpbWcgc3JjPXh4eDp4IHgyRm9uZXJyb3I9amF2YXNjcmlwdDphbGVydCgxKT4K",
     "YCInPjxpbWcgc3JjPXh4eDp4IHgwOW9uZXJyb3I9amF2YXNjcmlwdDphbGVydCgxKT4K",
     "YCInPjxpbWcgc3JjPXh4eDp4IHgwQ29uZXJyb3I9amF2YXNjcmlwdDphbGVydCgxKT4K",
     "YCInPjxpbWcgc3JjPXh4eDp4IHgwMG9uZXJyb3I9amF2YXNjcmlwdDphbGVydCgxKT4K",
     "YCInPjxpbWcgc3JjPXh4eDp4IHgyN29uZXJyb3I9amF2YXNjcmlwdDphbGVydCgxKT4K",
     "YCInPjxpbWcgc3JjPXh4eDp4IHgyMG9uZXJyb3I9amF2YXNjcmlwdDphbGVydCgxKT4K",
     "ImAnPjxzY3JpcHQ+eDNCamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eDBEamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEVGeEJCeEJGamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDgxamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDg0amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUzeDgweDgwamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eDA5amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDg5amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDg1amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDg4amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eDAwamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweEE4amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDhBamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUxeDlBeDgwamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eDBDamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eDJCamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEYweDkweDk2eDlBamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+LWphdmFzY3JpcHQ6YWxlcnQoMSk8L3NjcmlwdD4K",
     "ImAnPjxzY3JpcHQ+eDBBamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweEFGamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eDdFamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDg3amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgxeDlGamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweEE5amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEMyeDg1amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEVGeEJGeEFFamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDgzamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDhCamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEVGeEJGeEJFamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDgwamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eDIxamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDgyamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUyeDgweDg2amF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEUxeEEweDhFamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eDBCamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eDIwamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "ImAnPjxzY3JpcHQ+eEMyeEEwamF2YXNjcmlwdDphbGVydCgxKTwvc2NyaXB0Pgo=",
     "PGltZyB4MDBzcmM9eCBvbmVycm9yPSJhbGVydCgxKSI+Cg==",
     "PGltZyB4NDdzcmM9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyB4MTFzcmM9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyB4MTJzcmM9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZ3g0N3NyYz14IG9uZXJyb3I9ImphdmFzY3JpcHQ6YWxlcnQoMSkiPgo=",
     "PGltZ3gxMHNyYz14IG9uZXJyb3I9ImphdmFzY3JpcHQ6YWxlcnQoMSkiPgo=",
     "PGltZ3gxM3NyYz14IG9uZXJyb3I9ImphdmFzY3JpcHQ6YWxlcnQoMSkiPgo=",
     "PGltZ3gzMnNyYz14IG9uZXJyb3I9ImphdmFzY3JpcHQ6YWxlcnQoMSkiPgo=",
     "PGltZ3g0N3NyYz14IG9uZXJyb3I9ImphdmFzY3JpcHQ6YWxlcnQoMSkiPgo=",
     "PGltZ3gxMXNyYz14IG9uZXJyb3I9ImphdmFzY3JpcHQ6YWxlcnQoMSkiPgo=",
     "PGltZyB4NDdzcmM9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyB4MzRzcmM9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyB4MzlzcmM9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyB4MDBzcmM9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmN4MDk9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmN4MTA9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmN4MTM9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmN4MzI9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmN4MTI9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmN4MTE9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmN4MDA9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmN4NDc9eCBvbmVycm9yPSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmM9eHgwOW9uZXJyb3I9ImphdmFzY3JpcHQ6YWxlcnQoMSkiPgo=",
     "PGltZyBzcmM9eHgxMG9uZXJyb3I9ImphdmFzY3JpcHQ6YWxlcnQoMSkiPgo=",
     "PGltZyBzcmM9eHgxMW9uZXJyb3I9ImphdmFzY3JpcHQ6YWxlcnQoMSkiPgo=",
     "PGltZyBzcmM9eHgxMm9uZXJyb3I9ImphdmFzY3JpcHQ6YWxlcnQoMSkiPgo=",
     "PGltZyBzcmM9eHgxM29uZXJyb3I9ImphdmFzY3JpcHQ6YWxlcnQoMSkiPgo=",
     "PGltZ1thXVtiXVtjXXNyY1tkXT14W2Vdb25lcnJvcj1bZl0iYWxlcnQoMSkiPgo=",
     "PGltZyBzcmM9eCBvbmVycm9yPXgwOSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmM9eCBvbmVycm9yPXgxMCJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmM9eCBvbmVycm9yPXgxMSJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmM9eCBvbmVycm9yPXgxMiJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmM9eCBvbmVycm9yPXgzMiJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGltZyBzcmM9eCBvbmVycm9yPXgwMCJqYXZhc2NyaXB0OmFsZXJ0KDEpIj4K",
     "PGEgaHJlZj1qYXZhJiMxJiMyJiMzJiM0JiM1JiM2JiM3JiM4JiMxMSYjMTJzY3JpcHQ6amF2YXNjcmlwdDphbGVydCgxKT5YWFg8L2E+Cg==",
     "PGltZyBzcmM9InhgIGA8c2NyaXB0PmphdmFzY3JpcHQ6YWxlcnQoMSk8L3NjcmlwdD4iYCBgPgo=",
     "PGltZyBzcmMgb25lcnJvciAvIiAnIj0gYWx0PWphdmFzY3JpcHQ6YWxlcnQoMSkvLyI+Cg==",
     "PHRpdGxlIG9ucHJvcGVydHljaGFuZ2U9amF2YXNjcmlwdDphbGVydCgxKT48L3RpdGxlPjx0aXRsZSB0aXRsZT0+Cg==",
     "PGEgaHJlZj1odHRwOi8vZm9vLmJhci8jeD1geT48L2E+PGltZyBhbHQ9ImA+PGltZyBzcmM9eDp4IG9uZXJyb3I9amF2YXNjcmlwdDphbGVydCgxKT48L2E+Ij4K",
     "PCEtLVtpZl0+PHNjcmlwdD5qYXZhc2NyaXB0OmFsZXJ0KDEpPC9zY3JpcHQgLS0+Cg==",
     "PCEtLVtpZjxpbWcgc3JjPXggb25lcnJvcj1qYXZhc2NyaXB0OmFsZXJ0KDEpLy9dPiAtLT4K",
     "PHNjcmlwdCBzcmM9Ii8lKGpzY3JpcHQpcyI+PC9zY3JpcHQ+Cg==",
     "PHNjcmlwdCBzcmM9IlwlKGpzY3JpcHQpcyI+PC9zY3JpcHQ+Cg==",
     "PElNRyAiIiI+PFNDUklQVD5hbGVydCgiWFNTIik8L1NDUklQVD4iPgo=",
     "PElNRyBTUkM9amF2YXNjcmlwdDphbGVydChTdHJpbmcuZnJvbUNoYXJDb2RlKDg4LDgzLDgzKSk+Cg==",
     "PElNRyBTUkM9IyBvbm1vdXNlb3Zlcj0iYWxlcnQoJ3h4cycpIj4K",
     "PElNRyBTUkM9IG9ubW91c2VvdmVyPSJhbGVydCgneHhzJykiPgo=",
     "PElNRyBvbm1vdXNlb3Zlcj0iYWxlcnQoJ3h4cycpIj4K",
     "PElNRyBTUkM9JiMxMDY7JiM5NzsmIzExODsmIzk3OyYjMTE1OyYjOTk7JiMxMTQ7JiMxMDU7JiMxMTI7JiMxMTY7JiM1ODsmIzk3OyYjMTA4OyYjMTAxOyYjMTE0OyYjMTE2OyYjNDA7JiMzOTsmIzg4OyYjODM7JiM4MzsmIzM5OyYjNDE7Pgo=",
     "PElNRyBTUkM9JiMwMDAwMTA2JiMwMDAwMDk3JiMwMDAwMTE4JiMwMDAwMDk3JiMwMDAwMTE1JiMwMDAwMDk5JiMwMDAwMTE0JiMwMDAwMTA1JiMwMDAwMTEyJiMwMDAwMTE2JiMwMDAwMDU4JiMwMDAwMDk3JiMwMDAwMTA4JiMwMDAwMTAxJiMwMDAwMTE0JiMwMDAwMTE2JiMwMDAwMDQwJiMwMDAwMDM5JiMwMDAwMDg4JiMwMDAwMDgzJiMwMDAwMDgzJiMwMDAwMDM5JiMwMDAwMDQxPgo=",
     "PElNRyBTUkM9JiN4NkEmI3g2MSYjeDc2JiN4NjEmI3g3MyYjeDYzJiN4NzImI3g2OSYjeDcwJiN4NzQmI3gzQSYjeDYxJiN4NkMmI3g2NSYjeDcyJiN4NzQmI3gyOCYjeDI3JiN4NTgmI3g1MyYjeDUzJiN4MjcmI3gyOT4K",
     "PElNRyBTUkM9ImphdiBhc2NyaXB0OmFsZXJ0KCdYU1MnKTsiPgo=",
     "PElNRyBTUkM9ImphdiYjeDA5O2FzY3JpcHQ6YWxlcnQoJ1hTUycpOyI+Cg==",
     "PElNRyBTUkM9ImphdiYjeDBBO2FzY3JpcHQ6YWxlcnQoJ1hTUycpOyI+Cg==",
     "PElNRyBTUkM9ImphdiYjeDBEO2FzY3JpcHQ6YWxlcnQoJ1hTUycpOyI+Cg==",
     "cGVybCAtZSAncHJpbnQgIjxJTUcgU1JDPWphdmEwc2NyaXB0OmFsZXJ0KCJYU1MiKT4iOycgPiBvdXQK",
     "PElNRyBTUkM9IiAmIzE0OyBqYXZhc2NyaXB0OmFsZXJ0KCdYU1MnKTsiPgo=",
     "PFNDUklQVC9YU1MgU1JDPSJodHRwOi8vaGEuY2tlcnMub3JnL3hzcy5qcyI+PC9TQ1JJUFQ+Cg==",
     "PEJPRFkgb25sb2FkISMkJSYoKSp+Ky1fLiw6Oz9AWy98XV5gPWFsZXJ0KCJYU1MiKT4K",
     "PFNDUklQVC9TUkM9Imh0dHA6Ly9oYS5ja2Vycy5vcmcveHNzLmpzIj48L1NDUklQVD4K",
     "PDxTQ1JJUFQ+YWxlcnQoIlhTUyIpOy8vPDwvU0NSSVBUPgo=",
     "PFNDUklQVCBTUkM9aHR0cDovL2hhLmNrZXJzLm9yZy94c3MuanM/PCBCID4K",
     "PFNDUklQVCBTUkM9Ly9oYS5ja2Vycy5vcmcvLmo+Cg==",
     "PElNRyBTUkM9ImphdmFzY3JpcHQ6YWxlcnQoJ1hTUycpIgo=",
     "PGlmcmFtZSBzcmM9aHR0cDovL2hhLmNrZXJzLm9yZy9zY3JpcHRsZXQuaHRtbCA8Cg==",
     "IjthbGVydCgnWFNTJyk7Ly8K",
     "PHBsYWludGV4dD4K",
     "MTtEUk9QIFRBQkxFIHVzZXJzCg==",
     "MSc7IERST1AgVEFCTEUgdXNlcnMtLSAxCg==",
     "JyBPUiAxPTEgLS0gMQo=",
     "JyBPUiAnMSc9JzEK",
     "LQo=",
     "LS0K",
     "LS12ZXJzaW9uCg==",
     "LS1oZWxwCg==",
     "JFVTRVIK",
     "L2Rldi9udWxsOyB0b3VjaCAvdG1wL2JsbnMuZmFpbCA7IGVjaG8K",
     "YHRvdWNoIC90bXAvYmxucy5mYWlsYAo=",
     "JCh0b3VjaCAvdG1wL2JsbnMuZmFpbCkK",
     "QHtbc3lzdGVtICJ0b3VjaCAvdG1wL2JsbnMuZmFpbCJdfQo=",
     "ZXZhbCgicHV0cyAnaGVsbG8gd29ybGQnIikK",
     "U3lzdGVtKCJscyAtYWwgLyIpCg==",
     "YGxzIC1hbCAvYAo=",
     "S2VybmVsLmV4ZWMoImxzIC1hbCAvIikK",
     "S2VybmVsLmV4aXQoMSkK",
     "JXgoJ2xzIC1hbCAvJykK",
     "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iSVNPLTg4NTktMSI/PjwhRE9DVFlQRSBmb28gWyA8IUVMRU1FTlQgZm9vIEFOWSA+PCFFTlRJVFkgeHhlIFNZU1RFTSAiZmlsZTovLy9ldGMvcGFzc3dkIiA+XT48Zm9vPiZ4eGU7PC9mb28+Cg==",
     "JEhPTUUK",
     "JEVOVnsnSE9NRSd9Cg==",
     "JWQK",
     "JXMK",
     "ezB9",
     "JSouKnMK",
     "Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMAo=",
     "Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL2hvc3RzCg==",
     "KCkgeyAwOyB9OyB0b3VjaCAvdG1wL2JsbnMuc2hlbGxzaG9jazEuZmFpbDsK",
     "KCkgeyBfOyB9ID5fWyQoJCgpKV0geyB0b3VjaCAvdG1wL2JsbnMuc2hlbGxzaG9jazIuZmFpbDsgfQo=",
     "Q09OCg==",
     "UFJOCg==",
     "QVVYCg==",
     "Q0xPQ0skCg==",
     "TlVMCg==",
     "QToK",
     "Wlo6Cg==",
     "Q09NMQo=",
     "TFBUMQo=",
     "TFBUMgo=",
     "TFBUMwo=",
     "Q09NMgo=",
     "Q09NMwo=",
     "Q09NNAo=",
     "U2N1bnRob3JwZSBHZW5lcmFsIEhvc3BpdGFsCg==",
     "UGVuaXN0b25lIENvbW11bml0eSBDaHVyY2gK",
     "TGlnaHR3YXRlciBDb3VudHJ5IFBhcmsK",
     "SmltbXkgQ2xpdGhlcm9lCg==",
     "SG9ybmltYW4gTXVzZXVtCg==",
     "c2hpdGFrZSBtdXNocm9vbXMK",
     "Um9tYW5zSW5TdXNzZXguY28udWsK",
     "aHR0cDovL3d3dy5jdW0ucWMuY2EvCg==",
     "Q3JhaWcgQ29ja2J1cm4sIFNvZnR3YXJlIFNwZWNpYWxpc3QK",
     "TGluZGEgQ2FsbGFoYW4K",
     "RHIuIEhlcm1hbiBJLiBMaWJzaGl0ego=",
     "bWFnbmEgY3VtIGxhdWRlCg==",
     "U3VwZXIgQm93bCBYWFgK",
     "bWVkaWV2YWwgZXJlY3Rpb24gb2YgcGFyYXBldHMK",
     "ZXZhbHVhdGUK",
     "bW9jaGEK",
     "ZXhwcmVzc2lvbgo=",
     "QXJzZW5hbCBjYW5hbAo=",
     "Y2xhc3NpYwo=",
     "VHlzb24gR2F5Cg==",
     "SWYgeW91J3JlIHJlYWRpbmcgdGhpcywgeW91J3ZlIGJlZW4gaW4gYSBjb21hIGZvciBhbG1vc3QgMjAgeWVhcnMgbm93LiBXZSdyZSB0cnlpbmcgYSBuZXcgdGVjaG5pcXVlLiBXZSBkb24ndCBrbm93IHdoZXJlIHRoaXMgbWVzc2FnZSB3aWxsIGVuZCB1cCBpbiB5b3VyIGRyZWFtLCBidXQgd2UgaG9wZSBpdCB3b3Jrcy4gUGxlYXNlIHdha2UgdXAsIHdlIG1pc3MgeW91Lgo=",
     "Um9zZXMgYXJlIBtbMDszMW1yZWQbWzBtLCB2aW9sZXRzIGFyZSAbWzA7MzRtYmx1ZS4gSG9wZSB5b3UgZW5qb3kgdGVybWluYWwgaHVlCg==",
     "QnV0IG5vdy4uLhtbMjBDZm9yIG15IGdyZWF0ZXN0IHRyaWNrLi4uG1s4bQo=",
     "VGhlIHF1aWMICAgICAhrIGJyb3duIGZvBwcHBwcHBwcHBwd4Li4uIFtCZWVlZXBdCg==",
     "UG93ZXLZhNmP2YTZj9i12ZHYqNmP2YTZj9mE2LXZkdio2Y/Ysdix2Ysg4KWjIOClo2gg4KWjIOClo+WGlwo="
]

HEADER = [
	'Relatienummer', 'Volledige naam', 'Adres: Achternaam', 'Adres: Tussenvoegsel', 
	'Adres: Voorletters', 'Adres: Straatnaam', 'Adres: Huisnummer', 
	'Adres: Hnr Toevoeging', 'Adres: Postcode', 'Adres: Woonplaats', 'Gemeente',
	'Adres: Land', 'Geen lid sinds', 'Geen abonnement sinds', 'Is lid D66', 
	'Stemrecht D66', 'Is lid JD', 'Stemrecht JD', 'E-mail privé', 
	'Telefoon: Mobiel', 'Telefoon: Prive', 'Geslacht', 'Geboortedatum', 
	'Ontbrekende gegevens', 'Vrij tekstveld test', 'Aanhef formeel', 
	'Aanhef informeel', 'Betaalmethodevoorkeur', 'Gewijzigd op', 
	'Contact: Bulk-e-mail niet toestaan', 'Overleden'
]

def gen_members(n):
	"""Generate n unique members.
	"""
	names = set()
	memberid = 58763
	while len(names) < n:
		first = random.choice(FIRSTNAMES)
		last = random.choice(LASTNAMES)
		fullname = ' '.join([first, last])
		if fullname in names: continue
		memberid += random.randrange(1, 50)
		nameinsertion = ' '.join(last.split()[:-1])
		streetname = random.choice(STREETNAMES)
		streetnumber = random.randrange(1, 256)
		streetnumberaddition = random.choice(['', '' 'a', 'b'])
		postcode = str(random.randrange(1000, 9999))+random.choice(LETTERS)+random.choice(LETTERS)
		city = random.choice(CITIES)
		municipality = random.choice(MUNICIPALITIES)
		country = "NEDERLAND"
		notamembersince = '' # TODO: Pick random date
		nosubscriptionsince = '' # TODO: Pick random date
		isd66member = random.choice(['Ja', 'Nee'])
		canvoted66 = random.choice(['Ja', 'Nee'])
		isjdmember = random.choice(['Ja', 'Nee'])
		canvotejd = random.choice(['Ja', 'Nee'])
		email = gen_email(fullname)
		telmob = '06%08d' % (random.randrange(0,99999999),)
		telpriv = ''
		sex = random.choice(['Man', 'Vrouw', 'Anders'])
		birthdate = '%d/%d/%d' % (random.randrange(1,28), 
			random.randrange(1,12), random.randrange(1985,2005))
		missingdata = ''
		freetexttest = ''
		salutationformal = 'Geachte heer '+last+','
		salutationinformal = 'Beste '+first+','
		preferedpaymentmethod = ''
		lastchange = '%d/%d/%d' % (random.randrange(1,28), 
			random.randrange(1,12), random.randrange(2005,2016))
		allowbulkemail = random.choice(['Toestaan', 'Niet toestaan'])
		deceased = random.choice(['', 'Ja']) 
		names.add(fullname)
		yield (
			str(memberid), fullname, last.split()[-1], nameinsertion, first,
			streetname, streetnumber, streetnumberaddition, postcode,
			city, municipality, country, notamembersince, nosubscriptionsince,
			isd66member, canvoted66, isjdmember, canvotejd, email,
			telmob, telpriv, sex, birthdate, missingdata,
			freetexttest, salutationformal, salutationinformal, preferedpaymentmethod,
			lastchange, allowbulkemail, deceased
		)


def gen_email(name):
	return '.'.join(name.split())+'@'+random.choice(DOMAINS)


if __name__ == "__main__":
	if len(sys.argv) != 5:
		print "Usage:"
		print "%s [count] [type] [format] [filename]" % (sys.argv[0],)
		print ""
		print "\tcount: Number of fake members."
		print "\ttype: Type of member data"
		print "\t\tnormal: plain member data"
		print "\t\tfuzzy: messy data intended to test tools"
		print "\tformat: output format"
		print "\t\texcel: MS Excel format"
		print "\tfilaneme: Filename to write output to"
		sys.exit()

	# Parse arguments
	count = int(sys.argv[1])
	datatype = sys.argv[2]
	fileformat = sys.argv[3]
	filename = sys.argv[4]

	if datatype == "normal":
		data = [row for row in gen_members(count)]
	elif datatype == "fuzzy":
		data = [row for row in gen_members(count)]
		numfuzzyrows = int(len(data)*0.5) # 50% of rows wil contain fuzzy data
		fuzzyrows = random.sample(range(len(data)), numfuzzyrows)
		for rownum in fuzzyrows:
			row = list(data[rownum])
			row[random.choice([1,2,3,4,5,6,7,8,9,10])] = base64.b64decode(random.choice(NAUGTY_STRINGS))
			data[rownum] = tuple(row)
	else:
		print "Unknown type %s. Should be normal or fuzzy" % (datatype,)
		sys.exit()
	if fileformat == "excel":
		wb = openpyxl.Workbook()
		ws = wb.active
		ws.append(HEADER)
		for row in data:
			ws.append(row)
		wb.save(filename)
	else:
		print "Unknown format %s. Should be excel" % (fileformat,)
		sys.exit()



