#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys
import openpyxl


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

HEADER = [
	'Relatienummer', 'Volledige naam', 'Adres: Achternaam', 'Adres: Tussenvoegsel', 
	'Adres: Voorletters', 'Adres: Straatnaam', 'Adres: Huisnummer', 
	'Adres: Hnr Toevoeging', 'Adres: Postcode', 'Adres: Woonplaats, Gemeente',
	'Adres: Land', 'Geen lid sinds', 'Geen abonnement sinds', 'Is lid D66', 
	'Stemrecht D66', 'Is lid JD', 'Stemrecht JD', 'E-mail privé', 
	'Telefoon: Mobiel', 'Telefoon: Prive', 'Geslacht', 'Geboortedatum', 
	'Ontbrekende gegevens', 'Vrij tekstveld test', 'Aanhef formeel', 
	'Aanhef informeel', 'Betaalmethodevoorkeur', 'Gewijzigd op', 
	'Contact: Bulk-e-mail niet toestaan', 'Overleden'
]

# Relatienummer, Volledige naam, Adres: Achternaam, Adres: Tussenvoegsel, Adres: Voorletters
# Adres: Straatnaam, Adres: Huisnummer, Adres: Hnr Toevoeging, Adres: Postcode	
# Adres: Woonplaats, Gemeente,	Adres: Land, Geen lid sinds, Geen abonnement sinds,
# Is lid D66, Stemrecht D66, Is lid JD, Stemrecht JD, E-mail privé,
# Telefoon: Mobiel, Telefoon: Prive, Geslacht, Geboortedatum, Ontbrekende gegevens,
# Vrij tekstveld test, Aanhef formeel, Aanhef informeel, Betaalmethodevoorkeur,
# Gewijzigd op, Contact: Bulk-e-mail niet toestaan, Overleden
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
		country = "NEDERLAND"
		notamembersince = '' # TODO: Pick random date
		nosubscriptionsince = '' # TODO: Pick random date
		isd66member = random.choice(['ja', 'nee'])
		canvoted66 = random.choice(['ja', 'nee'])
		isjdmember = random.choice(['ja', 'nee'])
		canvotejd = random.choice(['ja', 'nee'])
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
			city, country, notamembersince, nosubscriptionsince,
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
		print "\t\tfuzzy: (not implemented) messy data"
		print "\tformat: output format"
		print "\t\texcel: MS Excel format"
		print "\tfilaneme: Filename to write output to"
		sys.exit()
count = int(sys.argv[1])
datatype = sys.argv[2]
fileformat = sys.argv[3]
filename = sys.argv[4]

if datatype == "normal":
	data = [row for row in gen_members(count)]
elif datatype == "fuzzy":
	print "Fuzzy data is not yet implemented"
	sys.exit()
if fileformat == "excel":
	wb = openpyxl.Workbook()
	ws = wb.active
	ws.append(HEADER)
	for row in data:
		ws.append(row)
	wb.save(filename)



