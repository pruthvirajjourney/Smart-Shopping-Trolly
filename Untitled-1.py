import qrcode
import tkinter as tk
from tkinter import ttk
import pygame  # For playing alarm sound
import os
import winsound  # Import winsound for playing alarm sound


# Initialize pygame mixer for playing alarm and thanks sound
pygame.mixer.init()

# Owner's Bank Account Details
account_number = "7058141648"
ifsc_code = "ybl"
owner_name = "John Doe"

# Global total amount (based on cart)
total_amount = 0

# Mock Product Database
product_db = {
    '1': {'name': 'Apple', 'quantity': '1 kg', 'price': 10},
    '2': {'name': 'Banana', 'quantity': '1 bunch', 'price': 5},
    '3': {'name': 'Orange', 'quantity': '1 kg', 'price': 8},
    '4': {'name': 'Tomato', 'quantity': '1 kg', 'price': 12},
    '5': {'name': 'Potato', 'quantity': '1 kg', 'price': 6},
    '6': {'name': 'Onion', 'quantity': '1 kg', 'price': 7},
    '7': {'name': 'Carrot', 'quantity': '1 kg', 'price': 15},
    '8': {'name': 'Spinach', 'quantity': '1 bunch', 'price': 20},
    '9': {'name': 'Cucumber', 'quantity': '1 kg', 'price': 9},
    '10': {'name': 'Lettuce', 'quantity': '1 pack', 'price': 18},
    '11': {'name': 'Broccoli', 'quantity': '1 kg', 'price': 25},
    '12': {'name': 'Cauliflower', 'quantity': '1 kg', 'price': 22},
    '13': {'name': 'Bell Pepper', 'quantity': '1 kg', 'price': 14},
    '14': {'name': 'Eggplant', 'quantity': '1 kg', 'price': 16},
    '15': {'name': 'Zucchini', 'quantity': '1 kg', 'price': 13},
    '16': {'name': 'Mushrooms', 'quantity': '500 g', 'price': 30},
    '17': {'name': 'Garlic', 'quantity': '1 kg', 'price': 4},
    '18': {'name': 'Ginger', 'quantity': '1 kg', 'price': 12},
    '19': {'name': 'Cabbage', 'quantity': '1 kg', 'price': 10},
    '20': {'name': 'Peas', 'quantity': '500 g', 'price': 8},
    '21': {'name': 'Green Beans', 'quantity': '500 g', 'price': 9},
    '22': {'name': 'Sweet Corn', 'quantity': '1 pack', 'price': 11},
    '23': {'name': 'Avocado', 'quantity': '1 piece', 'price': 40},
    '24': {'name': 'Chili', 'quantity': '1 kg', 'price': 5},
    '25': {'name': 'Pineapple', 'quantity': '1 piece', 'price': 25},
    '26': {'name': 'Watermelon', 'quantity': '1 piece', 'price': 18},
    '27': {'name': 'Mango', 'quantity': '1 kg', 'price': 20},
    '28': {'name': 'Papaya', 'quantity': '1 piece', 'price': 22},
    '29': {'name': 'Grapes', 'quantity': '500 g', 'price': 30},
    '30': {'name': 'Blueberries', 'quantity': '200 g', 'price': 35},
    '31': {'name': 'Strawberry', 'quantity': '500 g', 'price': 28},
    '32': {'name': 'Raspberry', 'quantity': '200 g', 'price': 32},
    '33': {'name': 'Blackberry', 'quantity': '200 g', 'price': 36},
    '34': {'name': 'Peach', 'quantity': '1 kg', 'price': 15},
    '35': {'name': 'Plum', 'quantity': '1 kg', 'price': 18},
    '36': {'name': 'Nectarine', 'quantity': '1 kg', 'price': 20},
    '37': {'name': 'Lemon', 'quantity': '1 kg', 'price': 7},
    '38': {'name': 'Lime', 'quantity': '1 kg', 'price': 6},
    '39': {'name': 'Coconut', 'quantity': '1 piece', 'price': 25},
    '40': {'name': 'Kiwi', 'quantity': '1 kg', 'price': 30},
    '41': {'name': 'Date', 'quantity': '500 g', 'price': 12},
    '42': {'name': 'Fig', 'quantity': '500 g', 'price': 18},
    '43': {'name': 'Pomegranate', 'quantity': '1 piece', 'price': 22},
    '44': {'name': 'Mandarin', 'quantity': '1 kg', 'price': 16},
    '45': {'name': 'Cantaloupe', 'quantity': '1 piece', 'price': 24},
    '46': {'name': 'Honeydew', 'quantity': '1 piece', 'price': 20},
    '47': {'name': 'Ginger Root', 'quantity': '500 g', 'price': 10},
    '48': {'name': 'Basil', 'quantity': '1 bunch', 'price': 12},
    '49': {'name': 'Mint', 'quantity': '1 bunch', 'price': 8},
    '50': {'name': 'Oregano', 'quantity': '1 bunch', 'price': 15},
    '51': {'name': 'Rosemary', 'quantity': '1 bunch', 'price': 20},
    '52': {'name': 'Thyme', 'quantity': '1 bunch', 'price': 18},
    '53': {'name': 'Sage', 'quantity': '1 bunch', 'price': 15},
    '54': {'name': 'Parsley', 'quantity': '1 bunch', 'price': 10},
    '55': {'name': 'Chives', 'quantity': '1 bunch', 'price': 12},
    '56': {'name': 'Dill', 'quantity': '1 bunch', 'price': 14},
    '57': {'name': 'Cilantro', 'quantity': '1 bunch', 'price': 13},
    '58': {'name': 'Tarragon', 'quantity': '1 bunch', 'price': 16},
    '59': {'name': 'Bay Leaves', 'quantity': '1 pack', 'price': 9},
    '60': {'name': 'Lemon Grass', 'quantity': '1 bunch', 'price': 18},
    '61': {'name': 'Almonds', 'quantity': '500 g', 'price': 50},
    '62': {'name': 'Cashews', 'quantity': '500 g', 'price': 45},
    '63': {'name': 'Walnuts', 'quantity': '500 g', 'price': 55},
    '64': {'name': 'Pistachios', 'quantity': '500 g', 'price': 60},
    '65': {'name': 'Peanuts', 'quantity': '1 kg', 'price': 35},
    '66': {'name': 'Hazelnuts', 'quantity': '500 g', 'price': 70},
    '67': {'name': 'Macadamia Nuts', 'quantity': '500 g', 'price': 80},
    '68': {'name': 'Sunflower Seeds', 'quantity': '500 g', 'price': 25},
    '69': {'name': 'Pumpkin Seeds', 'quantity': '500 g', 'price': 30},
    '70': {'name': 'Chia Seeds', 'quantity': '250 g', 'price': 35},
    '71': {'name': 'Flax Seeds', 'quantity': '500 g', 'price': 40},
    '72': {'name': 'Coconut Oil', 'quantity': '1 liter', 'price': 70},
    '73': {'name': 'Olive Oil', 'quantity': '1 liter', 'price': 90},
    '74': {'name': 'Avocado Oil', 'quantity': '1 liter', 'price': 100},
    '75': {'name': 'Sesame Oil', 'quantity': '1 liter', 'price': 80},
    '76': {'name': 'Vegetable Oil', 'quantity': '1 liter', 'price': 60},
    '77': {'name': 'Soy Sauce', 'quantity': '250 ml', 'price': 12},
    '78': {'name': 'Vinegar', 'quantity': '500 ml', 'price': 5},
    '79': {'name': 'Balsamic Vinegar', 'quantity': '500 ml', 'price': 20},
    '80': {'name': 'Lemon Juice', 'quantity': '500 ml', 'price': 15},
    '81': {'name': 'Coconut Milk', 'quantity': '400 ml', 'price': 40},
    '82': {'name': 'Almond Milk', 'quantity': '1 liter', 'price': 45},
    '83': {'name': 'Soy Milk', 'quantity': '1 liter', 'price': 30},
    '84': {'name': 'Rice Milk', 'quantity': '1 liter', 'price': 25},
    '85': {'name': 'Coconut Water', 'quantity': '500 ml', 'price': 35},
    '86': {'name': 'Orange Juice', 'quantity': '1 liter', 'price': 20},
    '87': {'name': 'Apple Juice', 'quantity': '1 liter', 'price': 15},
    '88': {'name': 'Grape Juice', 'quantity': '1 liter', 'price': 18},
    '89': {'name': 'Lemonade', 'quantity': '500 ml', 'price': 10},
    '90': {'name': 'Iced Tea', 'quantity': '500 ml', 'price': 12},
    # Add more items following this format, ensuring you have unique quantities and prices
    '1000': {'name': 'Spicy Pickles', 'quantity': '1 jar', 'price': 18}
}


cart = []  # To store added products

# Function to play alarm sound
def play_alarm():
    # Using winsound to play a beep sound (1000Hz frequency for 500ms duration)
    winsound.Beep(1000, 5000)

# Function to play thanks audio
def play_thanks_audio():
    try:
        # Load and play the thanks sound file (make sure the file exists in the directory)
        pygame.mixer.music.load("thanks.mp3")  # Adjust the file path as needed
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error playing thanks audio: {e}")

# Function to Scan Product and Display Information
def scan_product(product_id):
    if product_id in product_db:
        product = product_db[product_id]
        product_info_label.config(
            text=f"Product: {product['name']}\nPrice: ₹{product['price']}\nquantity: {product['quantity']}",
            fg="green",
        )
        status_label.config(text="Product scanned! Choose an action.", fg="blue")

        # Store scanned product globally for add/remove actions
        scanned_product.set(product_id)
    else:
        product_info_label.config(text="Invalid Product!", fg="red")
        status_label.config(text="Invalid Product ID!", fg="red")
        play_alarm()

    # Clear product ID entry
    product_id_entry.delete(0, tk.END)

# Function to Add Scanned Product to Cart
def add_to_cart():
    global total_amount
    product_id = scanned_product.get()

    if product_id and product_id in product_db:
        product = product_db[product_id]
        cart.append(product)
        total_amount += product["price"]

        # Update Cart Display and Total
        cart_display.insert(tk.END, f"{product['name']} - ₹{product['price']}")
        total_label.config(text=f"Total: ₹{total_amount}")

        status_label.config(text="Product Added to Cart!", fg="green")
        product_info_label.config(text="")  # Clear product info after adding
    else:
        status_label.config(text="No product scanned to add!", fg="red")

# Function to Remove Selected Product from Cart
def remove_selected_product():
    global total_amount

    # Get the selected product index
    selected_index = cart_display.curselection()

    if selected_index:
        selected_index = selected_index[0]  # Get the first selected index
        removed_product = cart.pop(selected_index)  # Remove from cart
        total_amount -= removed_product["price"]  # Update total

        # Update Cart Display and Total
        cart_display.delete(selected_index)
        total_label.config(text=f"Total: ₹{total_amount}")

        status_label.config(text=f"Removed: {removed_product['name']}", fg="blue")
    else:
        status_label.config(text="No product selected to remove!", fg="red")

# Function to Generate Payment QR Code
def generate_payment_qr():
    if total_amount == 0:
        status_label.config(text="Cart is empty!", fg="red")
        return

    # Prepare QR code data with dynamic total amount
    qr_data = (
        f"upi://pay?pa={account_number}@{ifsc_code}&pn={owner_name}&am={total_amount}&cu=INR"
    )

    # Generate QR Code
    qr = qrcode.make(qr_data)
    qr.show()  # Display the QR Code
    status_label.config(text="Payment QR Code Generated!", fg="green")

    # Play the thanks audio after generating QR code
    play_thanks_audio()

# GUI Setup
root = tk.Tk()
root.title("Smart Shopping Trolley")
root.geometry("500x700")

# Global Variable to Store Scanned Product
scanned_product = tk.StringVar()

# Entry for Product ID
product_id_label = tk.Label(root, text="Enter Product ID:")
product_id_label.pack(pady=5)

product_id_entry = tk.Entry(root)
product_id_entry.pack(pady=5)

# Button to Scan Product
scan_button = ttk.Button(
    root, text="Scan Product", command=lambda: scan_product(product_id_entry.get())
)
scan_button.pack(pady=10)

# Product Information Display
product_info_label = tk.Label(root, text="Product information will appear here.", font=("Arial", 12), fg="blue")
product_info_label.pack(pady=10)

# Cart Display
cart_display = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
cart_display.pack(pady=10)

# Total Label
total_label = tk.Label(root, text="Total: ₹0", font=("Arial", 14))
total_label.pack(pady=10)

# Buttons for Actions
action_frame = tk.Frame(root)
action_frame.pack(pady=10)

add_button = ttk.Button(action_frame, text="Add to Cart", command=add_to_cart)
add_button.grid(row=0, column=0, padx=10)

remove_button = ttk.Button(action_frame, text="Remove Selected Product", command=remove_selected_product)
remove_button.grid(row=0, column=1, padx=10)

# Button for QR Code Generation
done_button = ttk.Button(root, text="Done My Shopping & Generate QR", command=generate_payment_qr)
done_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Scan a product to start.", font=("Arial", 12))
status_label.pack(pady=10)

# Run GUI
root.mainloop()
