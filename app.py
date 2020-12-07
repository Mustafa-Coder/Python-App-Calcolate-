from tkinter import * 
from tkinter import messagebox 
# start app 

age_app = Tk() 

age_app.title("Age")

age_app.geometry("400x300") # size 

the_text = Label(age_app, text="Set your age ", font=("Arial",'20') , height="2")
the_text.pack()

# age string variable 
age = StringVar()

# defualt value age 
age.set("00")

#input 
age_input = Entry(age_app,width=2,font=('Arial',15), textvar=age,bg="#ccc", borderwidth=0)
age_input.pack()


#functions app 

def calc(): 
    
    value_age = age.get() 
    if (value_age.isnumeric()) : 
        if int(value_age) != 00:
            # months 
            months = int(value_age) * 12 
            # weeks
            weeks = months * 4 
            # days 
            days = int(value_age) * 365 

            all_lines = f"Your Months is {months} and your weeks is {weeks} and Days is {days} "
            messagebox.showinfo("Result",all_lines)
            love = messagebox.askyesno("Feedback !", "Are you love this app ? ")
            love
            if love == True: 
                messagebox.showinfo("Thanks", 'Thanks for your feedback :) ')
        else: 
            messagebox.showerror("Something is Wrong ?!","Please Set your age !! ")
    else:
        messagebox.showerror("Error..","Please Enter the Number not Text !! ")
    
    pass 

#btn 
btn = Button(age_app,width="30",text="Calcolate", height="2", background="#282828", fg="white", borderwidth=0, command=calc)
btn.pack()



# close func 
def close(): 
    closeMessage = messagebox.askyesno("Close this app", "Are you sure to close this app ? ")
    if closeMessage == True: 
        age_app.destroy()
    pass 
# btn close 
btn_close = Button(age_app,width="30", text="Close", height="2", bg="red",fg="white",borderwidth=0, command=close)
btn_close.pack()

age_app.mainloop() # run the app loop 



