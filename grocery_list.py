class GroceryItem:

  def __init__(self, name, price, quantity):
    
    self.name = name
    self.price = price
    self.quantity = quantity

  def __repr__(self):
    return f'item: {self.name}, price: {self.price}, units: {self.quantity} |'

class GroceryList:

  def __init__(self, name):
    
    self.name = name
    self.items = []

  def __repr__(self):
    output_string = ''
    for item in self.items:
      output_string += f'{item.name}: {item.price}, {item.quantity} count \n'
    return output_string + '\n'
  

class ListManager:

  def __init__(self):

    self.groceryListArray = []
    self.selectedListObj = None

    self.groceryListArray.append(GroceryList('walmart'))
    self.groceryListArray.append(GroceryList('randalls'))
    self.groceryListArray.append(GroceryList('HEB'))

  def prompt_user(self):

    if not self.selectedListObj:

      print('no list is selected currently')
      continueOrQuit = input('c: continue, q: quit \n')

      if continueOrQuit == 'q':

        exit()

      self.select_list()

    else:
      
      print(f'{self.selectedListObj.name} is currently selected')
      user_selection = input("c: continue, a: add a new list, s: select another list, q: quit \n")
   
      if user_selection.lower() == 'a':
        self.create_new_list()

      if user_selection.lower() == 's':
        self.select_list()

      if user_selection.lower() == 'q':
        exit()
        
      print(f"what would you like to do with {self.selectedListObj.name}? \n")
      user_selection = input("v: view, a: add items, b: go back \n")

      if user_selection.lower() == 'v':
        self.view_list_items()

      if user_selection.lower() == 'a':
        self.add_items_to_list()

      if user_selection.lower() == 'b':
        self.prompt_user()
    
    self.prompt_user()

  def select_list(self, message=None):

    if(message):
      print(self)
      prompt = message
  
    else:
      print('\n')
      print('select a grocery list\n')
      print(self)
      prompt = "type the number of the list you wish to select \n"

    list_number = int(input(prompt))

    if(list_number <= len(self.groceryListArray)-1):
      selected_list_obj = self.groceryListArray[list_number]
      self.selectedListObj = selected_list_obj
    else:
      self.select_list("list with that number doesn't exist, choose again \n")

  def view_list_items(self):

    print(self.selectedListObj.items)

    print(f'above are the items of {self.selectedListObj.name} \n')

    self.prompt_user()

  def create_new_list(self):

    new_list_name = input("enter the name of the new list: ")

    new_grocery_list = GroceryList(new_list_name)

    self.groceryListArray.append(new_grocery_list)

    self.selectedListObj = new_grocery_list

    self.prompt_user()

  def add_items_to_list(self):

    while True:

      print("enter a grocery item(s) \n ")
        
      grocery_item_name = input("type item name or done: ")

      if grocery_item_name == 'done':
        break
      
      grocery_item_price = input("enter item price like $1.00: ")

      if grocery_item_price == 'done':
        break

      grocery_item_quantity = input("enter item quantity: ")

      if grocery_item_quantity == 'done':
        break

      print('\n')

      newGroceryItem = GroceryItem(grocery_item_name, grocery_item_price, grocery_item_quantity)
      self.selectedListObj.items.append(newGroceryItem)

      print(self.selectedListObj.items)

    print('\n')
    self.prompt_user()


  def view_lists(self):

    print(self)

    self.prompt_user()

  def __repr__(self):

    output_string = ''

    list_number = 0

    for groceryList in self.groceryListArray:
      output_string += f"{str(list_number)}. {groceryList.name} \n"
      list_number += 1

    return  output_string 


list_manager = ListManager()
list_manager.prompt_user()


