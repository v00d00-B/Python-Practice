stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for a, b in inventory.items():
        print(str(b) + ' ' + a)
        item_total += b
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
