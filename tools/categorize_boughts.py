#!/bin/env python
from email.utils import parsedate_tz

tickets = 0
shirts = 0
bausatz = 0
scratch = 0
essen = 0
spende = 0
drink = 0
snack = 0

ticketsale = 0
shirtsale = 0
bausatzsale = 0
scratchsale = 0
drinksale = 0
snacksale = 0
essensale = 0
spendesale = 0

with open("../db/boughts") as f:
	for bought in f:
		(datestr, ip, pricetext, product) = bought.rstrip().split("\t")
		date = parsedate_tz(datestr)
		price = float(pricetext)
		if "Eintritt" in product or "Tagesticket" in product:
			ticketsale = ticketsale + price
			tickets = tickets + 1
		elif "T-Shirt" in product:
			shirtsale = shirtsale + price
			shirts = shirts + 1
		elif "Loet" in product or "Ardui" in product:
			bausatzsale = bausatzsale + price
			bausatz = bausatz + 1
		elif "Scratchc" in product:
			scratchsale = scratchsale + price
			scratch = scratch + 1
		elif "Essen" in product:
			essensale = essensale + price
			essen = essen + 1
		elif "Spende" in product or "Wechselgeld" in product:
			spendesale = spendesale + price
			spende = spende + 1
		elif "Club" in product or "Herrmann" in product or "Hermann" in product or "Cola" in product or "Fanta" in product or "Sprite" in product or "Mate" in product or "Tschunk" in product or "Matcha" in product or "Spezi" in product or "Wasser" in product or "Rum" in product:
			drinksale = drinksale + price
			drink = drink + 1
		elif "Lion" in product or "Twix" in product or "Nic" in product or "Bounty" in product or "Mars" in product or "Daim" in product or "Chips" in product or "Knoppers" in product or "Kat" in product or "Snickers" in product or "Pick" in product or "Hanuta" in product or "Ei" in product or "Goldb" in product or "M&" in product or "Duplo" in product or "Milky" in product or "Kinder" in product or "E" is product:
			snacksale = snacksale + price
			snack = snack + 1
		else:
			print("1 x " + product + " for EUR " + str(price))

print("Tickets:\t" + str(ticketsale) + " (" + str(tickets) + ")")
print("T-Shirts:\t" + str(shirtsale) + " (" + str(shirts) + ")")
print("Bausätze:\t" + str(bausatzsale) + " (" + str(bausatz) + ")")
print("Scratchcards:\t" + str(scratchsale) + " (" + str(scratch) + ")")
print("Getränke:\t" + str(drinksale) + " (" + str(drink) + ")")
print("Snacks:\t\t" + str(snacksale) + " (" + str(snack) + ")")
print("Essen:\t\t" + str(essensale) + " (" + str(essen) + ")")
print("Spenden:\t" + str(spendesale) + " (" + str(spende) + ")")
