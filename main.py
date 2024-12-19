import customtkinter as ctk
from tkinter import PhotoImage, messagebox

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True


def primes_up_to(n):
    #Nesse caso a linear é menos custosa
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

#Recursiva:
# def prime(n, j):
#     if n < 2:
#         return False
#     if j == n:
#         return True
#     if n % j == 0:
#         return False
#     return prime(n, j + 1)


def fibonacci(n):
    # De maneira linear é mais eficiente, pois exige menos memória
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Recursiva:
# def fibonacci(N):
#     if N <= 1:
#         return N
#     else:
#         return fibonacci(N-2) + fibonacci(N-1)
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.conf_windown_start()
        self.background()
        self.login_screen()

    def conf_windown_start(self):
        self.geometry("800x400")
        self.title("Fibonacci Calculator")
        self.resizable(False, False)

    def background(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def login_screen(self):
        # Image
        self.img = PhotoImage(file="image_with_purple_background.png")
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=50, column=0, padx=0)

        self.title = ctk.CTkLabel(self, text="Fibonacci Calculator", font=("Century Gothic bold", 30))
        self.title.place(x=0, y=0)
        self.title.grid(row=0, column=0, pady=10, padx=10)

        # Forms
        self.frame_login = ctk.CTkFrame(self, width=50, height=500)
        self.frame_login.place(x=460, y=53)
        self.lb_title = ctk.CTkLabel(
            self.frame_login,
            text="Your inputs down here",
            font=("Century Gothic bold", 15),
            text_color="white",
        )
        self.lb_title.grid(row=0, column=0, padx=50, pady=30)

        self.fibo_recur_entry = ctk.CTkEntry(
            self.frame_login,
            width=300,
            placeholder_text="Fibonacci Input",
            font=("Century Gothic bold", 15),
            corner_radius=15,
        )
        self.fibo_recur_entry.grid(row=1, column=0, pady=10, padx=10)

        self.prime_line_entry = ctk.CTkEntry(
            self.frame_login,
            width=300,
            placeholder_text="Prime Input",
            font=("Century Gothic bold", 15),
            corner_radius=15,
        )
        self.prime_line_entry.grid(row=2, column=0, pady=10, padx=10)

        self.btn_join = ctk.CTkButton(
            self.frame_login,
            width=300,
            text="Join".upper(),
            font=("Century Gothic bold", 12),
            corner_radius=15,
            command=self.validate_inputs,
        )
        self.btn_join.grid(row=5, column=0, pady=10, padx=10)

    def validate_inputs(self):
        fibo_recur_value = self.fibo_recur_entry.get().strip()
        prime_line_value = self.prime_line_entry.get().strip()

        if not fibo_recur_value or not prime_line_value:
            messagebox.showerror("Error", "Both fields must be filled!")
        else:
            try:
                fibo_n = int(fibo_recur_value)
                prime_n = int(prime_line_value)

                if fibo_n < 0 or prime_n < 0:
                    messagebox.showerror("Error", "Inputs must be non-negative integers!")
                    return

                fibo_result = fibonacci(fibo_n)
                primes_result = primes_up_to(prime_n)
                print("--------------------------------------")
                print(f"Fibonacci({fibo_n}) = {fibo_result}")
                print(f"Prime numbers up to {prime_n}: {primes_result}")
                print("--------------------------------------")


                self.forms()
            except ValueError:
                messagebox.showerror("Error", "Inputs must be integers!")

    def forms(self):
        self.frame_login.place_forget()

        self.frame_login4 = ctk.CTkFrame(self, width=100, height=300)
        self.frame_login4.place(x=460, y=55)

        self.text_box = ctk.CTkTextbox(self.frame_login4, width=300, height=100)
        self.text_box.grid(row=5, column=0, pady=10, padx=10)
        self.text_box.insert(
            "0.0",
            "The information you requested has already been \nsent...\nHave a nice day :)",
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
