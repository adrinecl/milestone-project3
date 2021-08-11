### Test cases (user story based with screenshots)

**1. As a User, I want to have a smart, inexpensive and efficient solution to manage orders in my dry cleaning business.**
The implemented system is very simple, but does the job well. It is less error prone than manually updating a spreadsheet, and lets the user quickly see what actions are available to them.
![Program start](https://github.com/adrinecl/milestone-project3/blob/master/docs/images/rinse-and-repeat_start.jpg)
 
**2. I want to be able to enter new orders, as clients come into the store with items dropped off for dry cleaning.**
The first action presented to the user is to enter a new order. It is just a couple of key taps away to start entering a new order.
![Create New Order](https://github.com/adrinecl/milestone-project3/blob/master/docs/images/rinse-and-repeat_creating-new-order1.jpg)

**3. I want to be able to enter how many and the type of items that are being dropped off.**
The program lets the user enter the count of each type of item that can be dry cleaned. The total price is automatically calculated based on the added items. The item types are pulled from the spreadsheet so it is easy to add new types if needed, without editing the code.
![Create New Order - add quantities and calculate total price](https://github.com/adrinecl/milestone-project3/blob/master/docs/images/rinse-and-repeat_creating-new-order2.jpg)

**4. I want to be able to consult orders in details, so I know which orders still need to be done and I can mark them as ready to avoid mixing them up.**
From the main menu, the user can list all orders with various statuses, e.g., all orders that are ready to be picked up. They can also list all orders if desired.
![Create New Order - adding all items and entering customer information](https://github.com/adrinecl/milestone-project3/blob/master/docs/images/rinse-and-repeat_creating-new-order3.jpg)
![Create New Order - reviewing new order just created](https://github.com/adrinecl/milestone-project3/blob/master/docs/images/rinse-and-repeat_creating-new-order4.jpg)

**5. I want to identify the orders with unique numbers, so I can quickly find my client's clothes when they are picking up at the store.**
Each order gets an ID number that can be given out to the customer when dropping off the items to clean. This order ID can be used to look up orders to change their status when they are ready to be picked up or are picked up.
![Create New Order - reviewing new order just created](https://github.com/adrinecl/milestone-project3/blob/master/docs/images/rinse-and-repeat_marking-order-ready-for-pickup.jpg)

**6. I want to mark orders as "picked up" when the customer gets their order.**
By finding the order by ID, the user can easily mark the order as ready to be picked up or picked up already.
![Create New Order - reviewing new order just created](https://github.com/adrinecl/milestone-project3/blob/master/docs/images/rinse-and-repeat_marking-order-as-picked-up.jpg)


### Fixed Bugs
**1. "Create Order" issues**
- While creating the program and testing it a bug was found in the order creation option.
If you don't enter any quantities, a order is still created.
![Create Order - test 1](https://github.com/adrinecl/milestone-project3/blob/master/docs/images/rinse-and-repeat_testing1.jpg)

**2. "View customer information" showing submenu options**
![View customer information - bug](https://github.com/adrinecl/milestone-project3/blob/master/docs/images/rinse-and-repeat_viewing-customer-information-bug.jpg)

