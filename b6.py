class Product:
    def __init__(self, id, name, price, source):
        self.id, self.name, self.price, self.source = id, name, price, source
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Source: {self.source}"
    
class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self):
        try:
            self.products.append(Product(
                input("Enter product ID: "),
                input("Enter product name: "),
                float(input("Enter product price: ")),
                input("Enter product source: ")
            ))
            print("Product added successfully!")
        except ValueError:
            print("Price must be a number. Failed to add product!")
    
    def display_product(self):
        print("\nProduct List:" if self.products else "Product list is empty!")
        for product in self.products:
            print(product)

    def filter_products(self):
        try:
            max_price = float(input("Enter maximum price to filter: "))
            filtered = [p for p in self.products if p.price < max_price]
            print(f"\nProducts with price less than {max_price}:" if filtered else "No product match found")
            for product in filtered:
                print(product)
        except ValueError:
            print("Price must be a number!")
        
    def update_product(self):
        id = input("Enter product ID to update: ")
        for product in self.products:
            if product.id == id:
                try:
                    product.name, product.price, product.source = (
                        input("Enter new name: "),
                        float(input("Enter new price: ")),
                        input("Enter new source: ")
                    )
                    return print("Product updated successfully!")
                except ValueError:
                    return print("Price must be a number. Update failed!")
        print(f"Product with ID {id} not found!")

    def delete_product(self):
        id = input("Enter product ID to delete: ")
        for i, product in enumerate(self.products):
            if product.id == id:
                self.products.pop(i)
                return print("Product deleted successfully")
        print(f"Product with ID {id} not found!")
    
    def run(self):
        while True:
            print("""
                        ===PRODUCT MANAGEMENT MENU===
                        1. Add product
                        2. Display product list
                        3. Filter products by price
                        4. Update product
                        5. Delete product
                        6. Exit
                  """)

            actions = {
                "1": self.add_product,
                "2": self.display_product,
                "3": self.filter_products,
                "4": self.update_product,
                "5": self.delete_product,
                "6": lambda: (print("Exit!!!!"), exit())
            }

            if (choice := input("Enter choice (1-6): ")) in actions:
                actions[choice]()
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    ProductManager().run()