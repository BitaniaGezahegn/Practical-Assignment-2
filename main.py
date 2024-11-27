class Employee:
    def __init__(self, emp_id: str, emp_name: str, emp_salary: float, emp_department: str) -> None:
        self.id: str = emp_id
        self.name: str = emp_name
        self.salary: float = emp_salary
        self.department: str = emp_department
    
    def calculate_emp_salary(self, hours_worked: str) -> float:
        overtime: float = float(hours_worked) - 50
        overtime_amount: float = (overtime * (self.salary / 50))
        return self.salary + overtime_amount
    
    def emp_assign_department(self, new_department: str = None) -> str:
        if new_department != None:
            self.department = new_department
        return self.department
    
    def print_emp_details(self) -> None:
        print(f"""Employee Details
-------------------
Employee ID: {self.id}
Employee Name: {self.name}
Employee Salary: {self.salary}
Employee Department: {self.department}""")
        
# Creating 4 instances of employees
emp1 = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
emp2 = Employee("E7499", "JONES", 45000, "RESEARCH")
emp3 = Employee("E7900", "MARTIN", 50000, "SALES")
emp4 = Employee("E7698", "SMITH", 55000, "OPERATIONS")


class Restaurant:
    def __init__(self) -> None:
        self.menu_items: dict = {}
        self.table_reservations: list = []
        self.customer_orders: list = []

    def add_item_to_menu(self, item_name: str, price: int | float) -> None:
        self.menu_items[item_name] = price

    def book_table(self, name: str, time: str) -> None:
        self.table_reservations.append({'name': name, 'time': time})

    def customer_order(self, name: str, items: list) -> None:
        self.customer_orders.append({'name': name, 'items': items})

    def print_menu(self) -> None:
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_table_reservations(self) -> None:
        print("Table Reservations:")
        for reservation in self.table_reservations:
            print(f"Name: {reservation['name']}, Time: {reservation['time']}")

    def print_customer_orders(self) -> None:
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"Name: {order['name']}, Items: {order['items']}")

# Create a restaurant instance
restaurant = Restaurant()


def main():
    # 1
    
    #  Assign a new department and Output
    print(emp1.emp_assign_department(''))

    # Display Employee Detail
    emp2.print_emp_details()

    # Calculate Salary and Output
    print(emp3.calculate_emp_salary(55))

    
    # 2
    
    # Add items to the menu
    restaurant.add_item_to_menu("Pizza", 10)
    restaurant.add_item_to_menu("Pasta", 8)
    restaurant.add_item_to_menu("Salad", 5)

    # Make table reservations
    restaurant.book_table("Alice", "7:00 PM")
    restaurant.book_table("Bob", "8:30 PM")

    # Take customer orders
    restaurant.customer_order("Alice", ["Pizza", "Salad"])
    restaurant.customer_order("Bob", ["Pasta"])

    # Print the menu
    restaurant.print_menu()

    # Print table reservations
    restaurant.print_table_reservations()

    # Print customer orders
    restaurant.print_customer_orders()

if __name__ == "__main__":
    main()
