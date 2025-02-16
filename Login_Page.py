import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

user_database = {}

class FoodApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Ordering App")
        self.root.geometry("500x900")
        self.root.resizable(True, True)
        self.login_page()

    def login_page(self):
        self.root.title("Login Page")
        for widget in self.root.winfo_children():
            widget.destroy()
        
        try:
            bg_image = Image.open("E:/MSCIT-SEM-2/Python/download.jpeg")
            bg_image = bg_image.resize((500, 900), Image.Resampling.LANCZOS)
            self.bg = ImageTk.PhotoImage(bg_image)
            bg_label = tk.Label(self.root, image=self.bg)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception:
            print("Warning: Background image not found!")
        
        self.frame = tk.Frame(self.root, bg="#ffffff")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=600)
        
        tk.Label(self.frame, text="Login", font=("Arial", 22, "bold"), bg="#ffffff").pack(pady=15)
        
        tk.Label(self.frame, text="Username", font=("Arial", 12), bg="#ffffff").pack(pady=5, anchor="w", padx=30)
        self.username_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.username_entry.pack(pady=5, fill="x", padx=30)
        
        tk.Label(self.frame, text="Password", font=("Arial", 12), bg="#ffffff").pack(pady=5, anchor="w", padx=30)
        self.password_entry = tk.Entry(self.frame, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=5, fill="x", padx=30)
        
        tk.Button(self.frame, text="LOGIN", font=("Arial", 14, "bold"), bg="#0066cc", fg="#ffffff", command=self.login_handler).pack(pady=20, fill="x", padx=30)
        
        tk.Label(self.frame, text="Or Login Using", font=("Arial", 10), bg="#ffffff", fg="#999999").pack(pady=10)
        
        social_frame = tk.Frame(self.frame, bg="#ffffff")
        social_frame.pack(pady=5)
        self.add_social_icon(social_frame, "google.jpg", "Google")
        self.add_social_icon(social_frame, "facebook.jpg", "Facebook")
        self.add_social_icon(social_frame, "twitter.jpg", "Twitter")
        
        signup_label = tk.Label(self.frame, text="SIGN UP", font=("Arial", 12, "bold"), bg="#ffffff", fg="#0066cc", cursor="hand2")
        signup_label.pack(pady=15)
        signup_label.bind("<Button-1>", lambda event: self.registration_page())
    
    def add_social_icon(self, parent, icon_path, platform):
        try:
            icon = Image.open(icon_path)
            icon = icon.resize((40, 40), Image.Resampling.LANCZOS)
            icon_tk = ImageTk.PhotoImage(icon)
            button = tk.Button(parent, image=icon_tk, bg="#ffffff", bd=0, cursor="hand2", command=lambda: self.social_login(platform))
            button.image = icon_tk  # Prevent garbage collection
            button.pack(side="left", padx=10)
        except Exception:
            print(f"Warning: {platform} icon not found!")

    def social_login(self, platform):
        messagebox.showinfo("Social Login", f"Login with {platform} is coming soon!")
    
    def login_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in user_database and user_database[username] == password:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            self.home_page(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")
    
    def home_page(self, username):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.frame = tk.Frame(self.root, bg="#ffffff")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=600)
        
        tk.Label(self.frame, text=f"Welcome to Home Page", font=("Arial", 22, "bold"), bg="#ffffff").pack(pady=20)

        tk.Button(self.frame, text="Order Food", font=("Arial", 14, "bold"), bg="#28a745", fg="#ffffff", command=lambda: messagebox.showinfo("Order", "Food ordering feature coming soon!")).pack(pady=20, fill="x", padx=30)

        tk.Button(self.frame, text="Logout", font=("Arial", 14, "bold"), bg="#dc3545", fg="#ffffff", command=self.login_page).pack(pady=20, fill="x", padx=30)
    
    def registration_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.frame = tk.Frame(self.root, bg="#ffffff")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=550)
        
        tk.Label(self.frame, text="Register", font=("Arial", 22, "bold"), bg="#ffffff").pack(pady=15)

        tk.Label(self.frame, text="Username", font=("Arial", 12), bg="#ffffff").pack(pady=5, anchor="w", padx=30)
        username_entry = tk.Entry(self.frame, font=("Arial", 12))
        username_entry.pack(pady=5, fill="x", padx=30)

        tk.Label(self.frame, text="Password", font=("Arial", 12), bg="#ffffff").pack(pady=5, anchor="w", padx=30)
        password_entry = tk.Entry(self.frame, font=("Arial", 12), show="*")
        password_entry.pack(pady=5, fill="x", padx=30)

        tk.Button(self.frame, text="REGISTER", font=("Arial", 14, "bold"), bg="#0066cc", fg="#ffffff", command=lambda: self.register_user(username_entry.get(), password_entry.get())).pack(pady=20, fill="x", padx=30)
    
    def register_user(self, username, password):
        if username and password:
            user_database[username] = password
            messagebox.showinfo("Success", "Registration successful!")
            self.login_page()

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodApp(root)
    root.mainloop()