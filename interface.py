
import customtkinter


class Info(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.username = customtkinter.CTkEntry(self, placeholder_text="email")
        self.username.grid(row=0, column=0, padx=20, pady=(0, 20), sticky="w")
        
        self.entry = customtkinter.CTkEntry(self, placeholder_text="password")
        self.entry.grid(row=0, column=1, padx=20, pady=(0, 20), sticky="e")


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("User 1")
        self.add("User 2")
        self.add("User 3")
        self.add("User 4")
        
        
 
        # add widgets on tabs
        #self.label = customtkinter.CTkLabel(master=self.tab("User 1"))
        #self.label.grid(row=0, column=0, padx=20, pady=10)
        
        self.info = Info(master=self.tab("User 1"))
        self.info.grid(row=1, column=0, padx=10, pady=10)
        #MyCheckboxFrame(User 1)
        
        #https://www.bing.com/videos/search?q=select+file+in+tkinter&&view=detail&mid=1A468FC99247656CFC011A468FC99247656CFC01&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dselect%2Bfile%2Bin%2Btkinter%26FORM%3DHDRSC6








class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("my app")
        self.geometry("400x400")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #self.set_default_color_theme("./assets/green.json")
        customtkinter.set_default_color_theme("green")

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)
        
        
        
        def button_event():
            print("button pressed")
        
        self.execute = customtkinter.CTkButton(self, text="Execute All", command=button_event)
        self.execute.grid(row=1, column=0, padx=20, pady=10)
    


app = App()
app.mainloop()