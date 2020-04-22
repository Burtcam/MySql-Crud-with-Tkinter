# **Tkinter interface for Liveplay Database**

This interface will connect to the liveplay MySql database and provided the database is hosted locally, connect automatically and allow for a variety of business functions in our simulated gameshop. ***Note: If you wish to deploy the database you must manually change the config.Ini file to reflect the connection string attributes***

## Installation Instructions

1. Install Dependencies listed in ```requirements.txt``` (```pip install -r requirements.txt```)
2. Obtain and install MySql DB. (.sql files for the database can be found in directory LivePlayDB)
3. Play with it! 

## Functions Included
### BaseTable Management
This includes the ability to:
- Add new master items
- Add new vendors
- Define new terms codes

### Inventory Management
These functions will allow a user to manage various inventory functions.
- Add a new inventory (putaway)
- View the current inventory
- Update an existing inventory line
- Delete inventory from the record

### Order Management
These functions will allow a user to manage various functions related to orders.
- Add a new order/Add new lines to an existing order
- Update existing lines on a particular order
- Update order headers in relation to their ship date and receive date
- See all orders

###Invoice Management
These functions allow for basic invoice management
- Log new invoices received from vendors
- Query All invoices
- Log payments on invoices

