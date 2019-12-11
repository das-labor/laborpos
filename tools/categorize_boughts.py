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

ticketsalescratch = 0
shirtsalescratch = 0
bausatzsalescratch = 0
drinksalescratch = 0
snacksalescratch = 0
essensalescratch = 0
spendesalescratch = 0

with open("../db/boughts") as f:
	for bought in f:
		(datestr, ip, pricetext, cashorcard, product) = bought.rstrip().split("\t")
		if cashorcard != "B" and cashorcard != "S":
			print("Neither Cash nor Scratchcard, but '" + cashorcard + "'...")
		cash = (cashorcard == "B")
		date = parsedate_tz(datestr)
		price = float(pricetext)
		if "Eintritt" in product or "Tagesticket" in product or "Ticket" in product:
			if cash:
				ticketsale += price
			else:
				ticketsalescratch += price
			tickets = tickets + 1
		elif "T-Shirt" in product:
			if cash:
				shirtsale += price
			else:
				shirtsalescratch += price
			shirts = shirts + 1
		elif "Loet" in product or "Ardui" in product or "ausaetze" in product or "ausatz" in product:
			if cash:
				bausatzsale += price
			else:
				bausatzsalescratch += price
			bausatz = bausatz + 1
		elif "Scratchc" in product or "etour" in product:
			scratchsale += price
			scratch = scratch + 1
		elif "uchen" in product or "UCHEN" in product or "ssen" in product or "Waffel" in product or "kompott" in product:
			if cash:
				essensale += price
			else:
				essensalescratch += price
			essen = essen + 1
		elif "Spende" in product or "Wechselgeld" in product:
			if cash:
				spendesale += price
			else:
				spendesalescratch += price
			spende = spende + 1
		elif "Club" in product or "Tea" in product or "Herrmann" in product or "Hermann" in product or "Cola" in product or "Fanta" in product or "Sprite" in product or "Mate" in product or "Tschunk" in product or "SCHUNK" in product or "Matcha" in product or "Spezi" in product or "Wasser" in product or "Rum" in product or "Frohlunder" in product or "sake" in product or "Sake" in product or "tschunk" in product or "medium" in product or "shot" in product:
			if cash:
				drinksale += price
			else:
				drinksalescratch += price
			drink = drink + 1
		elif "reo" in product or "entos" in product or "ritt" in product or "ilka" in product or "uesse" in product or "curly" in product or "Mr. Tom" in product or "Lion" in product or "Twix" in product or "Nic" in product or "Bounty" in product or "Mars" in product or "Daim" in product or "Chips" in product or "Knoppers" in product or "Kat" in product or "Snickers" in product or "Pick" in product or "Hanuta" in product or "Ei" in product or "Goldb" in product or "M&" in product or "Duplo" in product or "Milky" in product or "Kinder" in product or "E" is product:
			if cash:
				snacksale += price
			else:
				snacksalescratch += price
			snack = snack + 1
		else:
			print("1 x " + product + " for EUR " + str(price) + "(" + ("cash" if cash else "scratch") + ")")

print("==== CASH ====")
print("Tickets:\t" + str(ticketsale) + " (" + str(tickets) + ")")
print("T-Shirts:\t" + str(shirtsale) + " (" + str(shirts) + ")")
print("Bausätze:\t" + str(bausatzsale) + " (" + str(bausatz) + ")")
print("Scratchcards:\t" + str(scratchsale) + " (" + str(scratch) + ")")
print("Getränke:\t" + str(drinksale) + " (" + str(drink) + ")")
print("Snacks:\t\t" + str(snacksale) + " (" + str(snack) + ")")
print("Essen:\t\t" + str(essensale) + " (" + str(essen) + ")")
print("Spenden:\t" + str(spendesale) + " (" + str(spende) + ")")

print("==== SCRATCH ====")
print("Tickets:\t" + str(ticketsalescratch) + " (" + str(tickets) + ")")
print("T-Shirts:\t" + str(shirtsalescratch) + " (" + str(shirts) + ")")
print("Bausätze:\t" + str(bausatzsalescratch) + " (" + str(bausatz) + ")")
print("Getränke:\t" + str(drinksalescratch) + " (" + str(drink) + ")")
print("Snacks:\t\t" + str(snacksalescratch) + " (" + str(snack) + ")")
print("Essen:\t\t" + str(essensalescratch) + " (" + str(essen) + ")")
print("Spenden:\t" + str(spendesalescratch) + " (" + str(spende) + ")")
