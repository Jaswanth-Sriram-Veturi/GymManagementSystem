from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import font
import random
import mysql.connector

root = Tk()
root.geometry("650x650+430+80")
root.title("Gym Management System")

frame_admin = Frame(root, bg="#9ad3bc", width=650, height=650)
frame_register = Frame(root, width=650, height=650, bg="#9ad3bc")
frame_login = Frame(root, width=650, height=650, bg="#9ad3bc")
frame_customer = Frame(root, width=650, height=650, bg="#9ad3bc")
frame_entry = Frame(root, width=650, height=650, bg="#9ad3bc")

db = mysql.connector.connect(host="localhost", user="root", passwd="Sriram@123", database="gym")
cursor = db.cursor()


class Entry:
    def __init__(self):
        frame_entry.grid(row=0, column=0)
        self.btn_login = Button(frame_entry, text="LOGIN", relief="groove", bg="#ec524b", fg="#fff", padx=54, pady=15,
                                command=self.show_login)
        self.btn_login.place(x=250, y=200)
        self.btn_register = Button(frame_entry, text="REGISTER", relief="groove", bg="#ec524b", fg="#fff",
                                   padx=47, pady=15, command=self.show_register)
        self.btn_register.place(x=250, y=350)

    def show_login(self):
        frame_entry.grid_forget()
        Login()

    def show_register(self):
        frame_entry.grid_forget()
        Register()


class Login:
    def __init__(self):
        frame_login.grid(row=0, column=0)
        self.login_name_label = Label(frame_login, text="Name", bg="#f5b461")
        self.login_name_label.place(x=200, y=100)
        self.login_name_text = Text(frame_login, height=1, width=30)
        self.login_name_text.place(x=200, y=130)
        self.login_password_label = Label(frame_login, text="Password", bg="#f5b461")
        self.login_password_label.place(x=200, y=240)
        self.login_password_text = Text(frame_login, height=1, width=30)
        self.login_password_text.place(x=200, y=270)
        self.btn_login = Button(frame_login, text="Login", relief="groove", bg="#ec524b", fg="#fff", padx=20, pady=5,
                                command=self.login)
        self.btn_login.place(x=280, y=400)
        self.register_label = Label(frame_login, text="Not a User?", bg="#f5b461")
        self.register_label.place(x=200, y=505)
        self.btn_register = Button(frame_login, text="Register", relief="groove", bg="#ec524b", fg="#fff", padx=20,
                                   pady=5, command=self.register)
        self.btn_register.place(x=300, y=500)

    def login(self):
        global id_of_user
        name_field = self.login_name_text.get("1.0", "end-1c")
        password_field = self.login_password_text.get("1.0", "end-1c")
        if (name_field == '') or (password_field == ''):
            Label(frame_login, text='Name field or Password field cannot be empty').place(x=200, y=310)
            self.login_password_text.delete("1.0", END)
            self.login_name_text.delete("1.0", END)
        else:
            label_no_user = Label(frame_login, text="There is no user with the specified username")
            cursor.execute("SELECT * FROM details")
            result = cursor.fetchall()
            for i in result:
                if i[1] == name_field:
                    pass
                else:
                    label_no_user.place(x=200, y=310)
                    self.login_name_text.delete("1.0", END)
                    self.login_password_text.delete("1.0", END)
                    break
            search_name_query = "SELECT * FROM details WHERE name=%s"
            name_field_value = (name_field, )
            cursor.execute(search_name_query, name_field_value)
            record = cursor.fetchall()
            for i in record:
                if i[2] != password_field:
                    label_no_user.place_forget()
                    label = Label(frame_login, text="Incorrect Password", fg="red")
                    label.place(x=200, y=310)
                    break
                else:
                    if i[6] == 'Customer':
                        frame_login.grid_forget()
                        id_of_user = i[0]
                        Customer()
                    elif i[6] == 'Admin':
                        frame_login.grid_forget()
                        Admin()
                    break

    def register(self):
        frame_login.grid_forget()
        Register()


class Register:
    def __init__(self):
        frame_register.grid(row=0, column=0)
        self.register_name_label = Label(frame_register, text="Name", bg="#f5b461")
        self.register_name_label.place(x=200, y=100)
        self.register_name_text = Text(frame_register, height=1, width=30)
        self.register_name_text.place(x=200, y=130)
        self.register_phone_number_label = Label(frame_register, text="Phone Number", bg="#f5b461")
        self.register_phone_number_label.place(x=200, y=180)
        self.register_phone_number_text = Text(frame_register, height=1, width=30)
        self.register_phone_number_text.place(x=200, y=210)
        self.register_city_label = Label(frame_register, text="City", bg="#f5b461")
        self.register_city_label.place(x=200, y=260)
        self.register_city_text = Text(frame_register, height=1, width=30)
        self.register_city_text.place(x=200, y=290)
        self.register_password_label = Label(frame_register, text="Password", bg="#f5b461")
        self.register_password_label.place(x=200, y=340)
        self.register_password_text = Text(frame_register, height=1, width=30)
        self.register_password_text.place(x=200, y=370)
        self.random_password_label = Label(frame_register, text="Generate Random Password", bg="#f5b461")
        self.random_password_label.place(x=200, y=403)
        self.btn_random_password = Button(frame_register, text="Generate", relief="groove", bg="#ec524b", fg="#fff",
                                          padx=10, pady=1, command=self.generate_random_password)
        self.btn_random_password.place(x=390, y=400)
        self.btn_register = Button(frame_register, text="Register", relief="groove", bg="#ec524b", fg="#fff",
                                   padx=20, pady=5, command=self.register_customer)
        self.btn_register.place(x=200, y=530)
        self.btn_login = Button(frame_register, text="Login", relief="groove", bg="#ec524b", fg="#fff", padx=20,
                                pady=5, command=self.login)
        self.btn_login.place(x=350, y=530)

    def register_customer(self):
        name_field = self.register_name_text.get("1.0", "end-1c")
        password_field = self.register_password_text.get("1.0", "end-1c")
        phone_number_field = self.register_phone_number_text.get("1.0", "end-1c")
        city_field = self.register_city_text.get("1.0", "end-1c")
        if (name_field == '') or (password_field == '') or (phone_number_field is None) or (city_field == ''):
            print("Name or Password or Phone Number or City Field is Empty")
            self.register_name_text.delete("1.0", END)
            self.register_password_text.delete("1.0", END)
            self.register_phone_number_text.delete("1.0", END)
            self.register_city_text.delete("1.0", END)
        else:
            search_query = "SELECT * FROM details WHERE name=%s"
            value_name = (name_field, )
            cursor.execute(search_query, value_name)
            result = cursor.fetchall()
            for i in result:
                if i[1] == name_field:
                    Label(frame_register, text="Username exists", fg="red").place(x=200, y=450)
                else:
                    insert_query = "INSERT INTO details(name, password, phone_number, city) VALUES(%s, %s, %s, %s)"
                    value = (name_field, password_field, phone_number_field, city_field)
                    cursor.execute(insert_query, value)
                    db.commit()
                    label_register_successful = Label(text="Register Successful")
                    label_register_successful.place(x=300, y=470)
            self.register_name_text.delete("1.0", END)
            self.register_password_text.delete("1.0", END)
            self.register_phone_number_text.delete("1.0", END)
            self.register_city_text.delete("1.0", END)

    def login(self):
        frame_register.grid_forget()
        Login()

    def generate_random_password(self):
        list_of_chars = [chr(char) for char in range(65, 124)]
        password = ""
        for char in range(0, 12):
            password += random.choice(list_of_chars)
        self.register_password_text.insert(END, password)


class Admin:
    def __init__(self):
        frame_admin.grid(row=0, column=0)
        self.btn_show_customers = Button(frame_admin, text="Show Customers", relief="groove", bg="#ec524b", fg="#fff",
                                         padx=57, pady=15, command=self.show_customer_details)
        self.btn_show_customers.place(x=220, y=120)
        self.btn_trainee_details = Button(frame_admin, text="Show Trainee Details", relief="groove", bg="#ec524b",
                                          fg="#fff", padx=47, pady=15, command=self.show_coach_details)
        self.btn_trainee_details.place(x=220, y=240)
        self.btn_products = Button(frame_admin, text="Products", relief="groove", bg="#ec524b", fg="#fff",
                                   padx=78, pady=15, command=self.products)
        self.btn_products.place(x=220, y=360)
        self.btn_back_to_home = Button(frame_admin, text="Logout", relief="groove", bg="#ec524b", fg="#fff",
                                       padx=82, pady=15, command=self.back_to_home)
        self.btn_back_to_home.place(x=220, y=480)

        # TODO: Frame for customer details
        self.frame_customer_details = Frame(frame_admin, bg="#9ad3bc", width=650, height=650)
        self.treeview_customer_details = ttk.Treeview(self.frame_customer_details, column=(1, 2, 3, 4, 5, 6),
                                                      show="headings", height=25)
        self.btn_back_customer_details = Button(self.frame_customer_details, text="BACK", relief="groove", bg="#ec524b",
                                                fg="#fff", padx=20, pady=5, command=self.back_to_admin)

        # TODO: Frame for trainee details
        self.frame_trainee_details = Frame(frame_admin, bg="#9ad3bc", width=650, height=650)
        self.treeview_trainee_details = ttk.Treeview(self.frame_trainee_details, column=(1, 2, 3, 4, 5),
                                                     show="headings", height=25)
        self.btn_back_trainee_details = Button(self.frame_trainee_details, text="BACK", relief="groove", bg="#ec524b",
                                               fg="#fff", padx=20, pady=5, command=self.back_to_admin)

        # TODO: Frame for product details
        self.frame_products = Frame(frame_admin, bg="#9ad3bc", width=650, height=650)
        self.product_label = Label(self.frame_products, text="Product Name")
        self.product_text = Text(self.frame_products, width=20, height=1)
        self.price_label = Label(self.frame_products, text="Price")
        self.price_text = Text(self.frame_products, width=10, height=1)
        self.quantity_label = Label(self.frame_products, text="Quantity")
        self.quantity_text = Text(self.frame_products, width=5, height=1)
        self.btn_add_product = Button(self.frame_products, text="Add Product", relief="groove", bg="#ec524b",
                                      fg="#fff", padx=20, pady=5, command=self.add_product)
        self.treeview_products = ttk.Treeview(self.frame_products, column=(1, 2, 3, 4), show="headings", height=20)
        self.btn_back_products = Button(self.frame_products, text="BACK", relief="groove", bg="#ec524b",
                                        fg="#fff", padx=20, pady=5, command=self.back_to_admin)

    def show_customer_details(self):
        self.frame_customer_details.pack()
        self.treeview_customer_details.place(x=25, y=60)
        self.treeview_customer_details.column(1, width=40)
        self.treeview_customer_details.column(2, width=120)
        self.treeview_customer_details.column(3, width=120)
        self.treeview_customer_details.column(4, width=120)
        self.treeview_customer_details.column(5, width=120)
        self.treeview_customer_details.column(6, width=80)
        self.treeview_customer_details.heading(1, text="Id")
        self.treeview_customer_details.heading(2, text="Name")
        self.treeview_customer_details.heading(3, text="Password")
        self.treeview_customer_details.heading(4, text="Phone Number")
        self.treeview_customer_details.heading(5, text="City")
        self.treeview_customer_details.heading(6, text="Membership")
        self.btn_back_customer_details.place(x=300, y=600)
        cursor.execute("SELECT * FROM details WHERE role='Customer'")
        rows = cursor.fetchall()
        self.treeview_customer_details.delete(*self.treeview_customer_details.get_children())
        for row in rows:
            self.treeview_customer_details.insert('', 'end', value=row)

    def show_coach_details(self):
        self.frame_trainee_details.pack()
        self.treeview_trainee_details.place(x=25, y=60)
        self.treeview_trainee_details.column(1, width=40)
        self.treeview_trainee_details.column(2, width=140)
        self.treeview_trainee_details.column(3, width=140)
        self.treeview_trainee_details.column(4, width=140)
        self.treeview_trainee_details.column(5, width=140)
        self.treeview_trainee_details.heading(1, text="Id")
        self.treeview_trainee_details.heading(2, text="Name")
        self.treeview_trainee_details.heading(3, text="Password")
        self.treeview_trainee_details.heading(4, text="Phone Number")
        self.treeview_trainee_details.heading(5, text="City")
        self.btn_back_trainee_details.place(x=300, y=600)
        cursor.execute("SELECT * FROM details WHERE role='Trainee'")
        self.treeview_trainee_details.delete(*self.treeview_trainee_details.get_children())
        rows = cursor.fetchall()
        for row in rows:
            self.treeview_trainee_details.insert('', 'end', value=row)

    def products(self):
        self.frame_products.pack()
        self.product_label.place(x=25, y=30)
        self.product_text.place(x=25, y=70)
        self.price_label.place(x=225, y=30)
        self.price_text.place(x=225, y=70)
        self.quantity_label.place(x=425, y=30)
        self.quantity_text.place(x=425, y=70)
        self.btn_add_product.place(x=520, y=70)
        self.treeview_products.place(x=25, y=150)
        self.treeview_products.column(1, width=40)
        self.treeview_products.column(2, width=300)
        self.treeview_products.column(3, width=120)
        self.treeview_products.column(4, width=120)
        self.treeview_products.heading(1, text="Id")
        self.treeview_products.heading(2, text="Product Name")
        self.treeview_products.heading(3, text="Price")
        self.treeview_products.heading(4, text="Quantity")
        self.btn_back_products.place(x=300, y=600)
        cursor.execute("SELECT * FROM product_details")
        rows = cursor.fetchall()
        self.treeview_products.delete(*self.treeview_products.get_children())
        for i in rows:
            self.treeview_products.insert('', 'end', value=i)

    def add_product(self):
        product = self.product_text.get("1.0", "end-1c")
        price = self.price_text.get("1.0", "end-1c")
        quantity = self.quantity_text.get("1.0", "end-1c")
        sql = "INSERT INTO product_details(product, price, quantity) VALUES(%s, %s, %s)"
        val = (product, price, quantity)
        cursor.execute(sql, val)
        db.commit()
        cursor.execute("SELECT * FROM product_details")
        rows = cursor.fetchall()
        self.treeview_products.delete(*self.treeview_products.get_children())
        for i in rows:
            self.treeview_products.insert('', 'end', value=i)
        self.product_text.delete("1.0", END)
        self.price_text.delete("1.0", END)
        self.quantity_text.delete("1.0", END)

    def back_to_admin(self):
        self.frame_trainee_details.pack_forget()
        self.frame_customer_details.pack_forget()
        self.frame_products.pack_forget()
        frame_admin.grid()

    def back_to_home(self):
        self.frame_trainee_details.pack_forget()
        frame_entry.grid(row=0, column=0)


class Customer:
    def __init__(self):
        frame_customer.grid(row=0, column=0)
        self.btn_profile = Button(frame_customer, text="Profile", relief="groove", bg="#ec524b",
                                  fg="#fff", padx=76, pady=15, command=self.show_profile)
        self.btn_profile.place(x=220, y=150)
        self.btn_view_membership = Button(frame_customer, text="View Membership", relief="groove", bg="#ec524b",
                                          fg="#fff", padx=47, pady=15, command=self.view_membership)
        self.btn_view_membership.place(x=220, y=300)
        self.btn_logout = Button(frame_customer, text="Logout", relief="groove", bg="#ec524b",
                                 fg="#fff", padx=76, pady=15, command=self.logout)
        self.btn_logout.place(x=220, y=450)

        # TODO: Profile
        self.frame_profile = Frame(frame_customer, bg="#9ad3bc", width=650, height=650)
        self.name_label = Label(self.frame_profile, text="Name", bg="#f5b461")
        self.name_text = Text(self.frame_profile, height=1, width=30)
        self.phone_number_label = Label(self.frame_profile, text="Phone Number", bg="#f5b461")
        self.phone_number_text = Text(self.frame_profile, height=1, width=30)
        self.city_label = Label(self.frame_profile, text="City", bg="#f5b461")
        self.city_text = Text(self.frame_profile, height=1, width=30)
        self.password_label = Label(self.frame_profile, text="Password", bg="#f5b461")
        self.password_text = Text(self.frame_profile, height=1, width=30)
        self.btn_change_password = Button(self.frame_profile, text="Change Password", relief="groove", bg="#ec524b",
                                          fg="#fff", padx=20, pady=5, command=self.change_password)
        self.btn_back_to_customer = Button(self.frame_profile, text="Back", relief="groove", bg="#ec524b",
                                           fg="#fff", padx=20, pady=5, command=self.back_to_customer)
        self.btn_back_to_customer.place(x=280, y=550)

        # TODO: View Subscription
        self.label_font = font.Font(size=20)
        self.price_font = font.Font(size=25)
        self.frame_view_membership = Frame(frame_customer, bg="#9ad3bc", width=650, heigh=650)
        self.frame_payg = Frame(self.frame_view_membership, bg="#e7e7e7", width=250, height=250)
        self.payg_label = Label(self.frame_payg, text="Pay As You Go", bg="#f5b461", fg="#fff", font=self.label_font)
        self.payg_price = Label(self.frame_payg, text="₹999", font=self.price_font)
        self.btn_payg = Button(self.frame_payg, text="Add", relief="groove", bg="#ec524b",
                               fg="#fff", padx=20, pady=5, command=lambda: self.add_membership('payg'))
        self.frame_open = Frame(self.frame_view_membership, bg="#e7e7e7", width=250, height=250)
        self.open_label = Label(self.frame_open, text="Open Membership", bg="#f5b461", fg="#fff", font=self.label_font)
        self.open_price = Label(self.frame_open, text="₹1999", font=self.price_font)
        self.btn_open = Button(self.frame_open, text="Add", relief="groove", bg="#ec524b",
                               fg="#fff", padx=20, pady=5, command=lambda: self.add_membership('open'))
        self.frame_term = Frame(self.frame_view_membership, bg="#e7e7e7", width=250, height=250)
        self.term_label = Label(self.frame_term, text="Term Membership", bg="#f5b461", fg="#fff", font=self.label_font)
        self.term_price = Label(self.frame_term, text="₹5999", font=self.price_font)
        self.btn_term = Button(self.frame_term, text="Add", relief="groove", bg="#ec524b",
                               fg="#fff", padx=20, pady=5, command=lambda: self.add_membership('term'))
        self.frame_session = Frame(self.frame_view_membership, bg="#e7e7e7", width=250, height=250)
        self.session_label = Label(self.frame_session, text="Session Packages", bg="#f5b461", fg="#fff",
                                   font=self.label_font)
        self.session_price = Label(self.frame_session, text="₹3499", font=self.price_font)
        self.btn_session = Button(self.frame_session, text="Add", relief="groove", bg="#ec524b",
                                  fg="#fff", padx=20, pady=5, command=lambda: self.add_membership('session'))
        self.btn_back_to_customer = Button(self.frame_view_membership, text="Back", relief="groove", bg="#ec524b",
                                           fg="#fff", padx=15, pady=5, command=self.back_to_customer)
        self.btn_back_to_customer.place(x=20, y=30)

    def add_membership(self, name):
        confirmation = messagebox.askyesno("Confirmation", "Are you sure?")
        if confirmation is True:
            update_query = "UPDATE details SET membership=%s WHERE id=%s"
            value = (name, id_of_user)
            cursor.execute(update_query, value)
            db.commit()
        else:
            pass

    def view_membership(self):
        self.frame_view_membership.pack()
        self.frame_payg.grid(row=0, column=0, padx=(50, 50), pady=(80, 40))
        self.payg_label.place(x=30, y=20)
        self.payg_price.place(x=80, y=105)
        self.btn_payg.place(x=80, y=200)
        self.frame_open.grid(row=0, column=1, padx=(0, 50), pady=(80, 40))
        self.open_label.place(x=10, y=20)
        self.open_price.place(x=80, y=105)
        self.btn_open.place(x=80, y=200)
        self.frame_term.grid(row=1, column=0, padx=(50, 50), pady=(0, 30))
        self.term_label.place(x=10, y=20)
        self.term_price.place(x=80, y=105)
        self.btn_term.place(x=80, y=200)
        self.frame_session.grid(row=1, column=1, padx=(0, 50), pady=(0, 30))
        self.session_label.place(x=10, y=20)
        self.session_price.place(x=80, y=105)
        self.btn_session.place(x=80, y=200)

    def show_profile(self):
        self.frame_profile.pack()
        sql = "SELECT * FROM details WHERE id=%s"
        val = (id_of_user, )
        cursor.execute(sql, val)
        row = cursor.fetchone()
        print(row[1])
        self.name_label.place(x=50, y=100)
        self.name_text.place(x=250, y=100)
        self.name_text.insert(INSERT, row[1])
        self.phone_number_label.place(x=50, y=200)
        self.phone_number_text.place(x=250, y=200)
        self.phone_number_text.insert(INSERT, row[3])
        self.city_label.place(x=50, y=300)
        self.city_text.place(x=250, y=300)
        self.city_text.insert(INSERT, row[4])
        self.password_label.place(x=50, y=400)
        self.password_text.place(x=250, y=400)
        self.password_text.insert(INSERT, row[2])
        self.btn_change_password.place(x=250, y=460)

    def change_password(self):
        password = simpledialog.askstring("Input", "New Password", parent=self.frame_profile)
        if password is not None:
            update_query = "UPDATE details SET password=%s WHERE id=%s"
            value = (password, id_of_user)
            cursor.execute(update_query, value)
            db.commit()
        else:
            # print("Password not changed")
            pass

    def logout(self):
        self.frame_profile.pack_forget()
        frame_customer.grid_forget()
        frame_entry.grid(row=0, column=0)

    def back_to_customer(self):
        self.frame_profile.pack_forget()
        self.frame_view_membership.pack_forget()
        frame_customer.grid()


entry_obj = Entry()
root.mainloop()
db.close()
