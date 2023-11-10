#!/usr/bin/env python3
from email.utils import parsedate_tz
import sys

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

PAYMENT_METHODS = {
    "B": "CASH",
    "S": "SCRATCH",
    "C": "CARD"
}

sales = {}
counts = {}

for m in PAYMENT_METHODS.keys():
    sales[m] = {}
    counts[m] = {}

with open("../db/boughts" if len(sys.argv) < 2 else sys.argv[1]) as f:
    for bought in f:
        try:
            (datestr, ip, pricetext, cashorcard, product) = bought.rstrip().split("\t")
        except ValueError:
            print(f"ERROR: -neous line: {bought.strip()}")
            continue
        if cashorcard not in PAYMENT_METHODS:
            print("ERROR: Neither Cash nor Scratchcard nor Card, but '" + cashorcard + "'...")
            continue
        date = parsedate_tz(datestr)
        price = float(pricetext)

        if "Eintritt" in product or "Tagesticket" in product or "Ticket" in product:
            category = "ticket"
        elif "T-Shirt" in product:
            category = "shirt"
        elif "Loet" in product or "Ardui" in product or "ausaetze" in product or "ausatz" in product or "adge" in product or "teile" in product:
            category = "bausatz"
        elif "Scratchc" in product or "etour" in product or "scratch" in product:
            category = "scratch"
        elif "uchen" in product or "UCHEN" in product or "ssen" in product or "Waffel" in product or "kompott" in product or "ortion" in product:
            category = "essen"
        elif "Spende" in product or "Wechselgeld" in product:
            category = "spende"
        elif "Club" in product or "Tea" in product or "Herrmann" in product or "Hermann" in product or "Cola" in product or "Fanta" in product or "Sprite" in product or "Mate" in product or "Tschunk" in product or "SCHUNK" in product or "Matcha" in product or "Spezi" in product or "Wasser" in product or "Rum" in product or "Frohlunder" in product or "sake" in product or "Sake" in product or "tschunk" in product or "medium" in product or "shot" in product or "MioMio" in product or "5cl" in product:
            category = "drink"
        elif "reo" in product or "entos" in product or "ritt" in product or "ilka" in product or "uesse" in product or "curly" in product or "Mr. Tom" in product or "Lion" in product or "Twix" in product or "Nic" in product or "Bounty" in product or "Mars" in product or "Daim" in product or "Chips" in product or "Knoppers" in product or "Kat" in product or "Snickers" in product or "Pick" in product or "Hanuta" in product or "Ei" in product or "Goldb" in product or "M&" in product or "Duplo" in product or "Milky" in product or "Kinder" in product or "E" in product:
            category = "snack"
        else:
            print(f"WARNING: 1 x {product} for EUR {price}({PAYMENT_METHODS[cashorcard]})")
            continue

        if category not in sales[cashorcard]:
            sales[cashorcard][category] = 0
            counts[cashorcard][category] = 0
        
        sales[cashorcard][category] += price
        counts[cashorcard][category] += 1

CATEGORY_NAMES = {
    "ticket": "Tickets",
    "shirt": "T-Shirts",
    "bausatz": "Bausätze",
    "scratch": "Scratchcards",
    "drink": "Getränke",
    "snack": "Snacks",
    "essen": "Essen",
    "spende": "Spenden"
}

for m, long_m in PAYMENT_METHODS.items():
    print(f"==== {long_m} ====")
    for c, long_c in CATEGORY_NAMES.items():
        if c in sales[m]:
            print(f"{long_c}:" + ("\t" if len(long_c) > 6 else "\t\t") + f"{sales[m][c]} ({counts[m][c]})")
    print(f"--------------------------------\nSum:\t\t{sum(sales[m].values())} ({sum(counts[m].values())})\n")

print("==== TOTAL ====")
sum_total_sales = 0
sum_total_counts = 0
for c, long_c in CATEGORY_NAMES.items():
    total_sales = sum(sales[m][c] for m in PAYMENT_METHODS.keys() if c in sales[m])
    total_counts = sum(counts[m][c] for m in PAYMENT_METHODS.keys() if c in sales[m])
    print(f"{long_c}:" + ("\t" if len(long_c) > 6 else "\t\t") + f"{total_sales} ({total_counts})")
    sum_total_sales += total_sales
    sum_total_counts += total_counts
print(f"--------------------------------\nSum:\t\t{sum_total_sales} ({sum_total_counts})\n")