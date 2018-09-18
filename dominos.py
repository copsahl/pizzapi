#!/usr/bin/env python2.7
from pizzapi import *
from os import system

def main():

	# Create Customer object
	customer = Customer('FirstName', 'LastName', 'Email', 'Phone#', 'Street, City, State, Zip')
	address = Address(*customer.address.split(','))
	
	# Get nearest store
	store = address.closest_store()

	# Get menu
	menu = store.get_menu()

	# Start loop to create our order
	itemList = []
	while(True):
		system('clear')
		print("Type 'DONE' at any point to finish!\n")
		search = raw_input('Search: ').title()
		if search == 'Done':
			break
		menu.search(Name=search)
		print("\nType in code of item you want! Ex.(20BDCOKE)")
		print("Leave blank to move onto next search!\n")
		item = raw_input("Item Code: ")
		if item == 'DONE':
			system('clear')
			break
		elif item == '':
			continue
		itemList.append(item)
	
	# Confirm items for order
	order = Order(store, customer, address)
	for i in itemList:
		confirm = raw_input('Add {} to your order?(y/n): '.format(i)).lower()
		if confirm == 'y':
			order.add_item(i)

	card = PaymentObject('Card#', 'CardExpire', 'CVV', address.zip)
	print("[Processing Payment]")
	try:
		# Try to order
		order.place(card)
	except:
		print("Card did not work! Cancelling order!\n")
	

	

if __name__ == '__main__':
	main()
