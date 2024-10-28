import random
import tkinter as tk
global usrname
def show_frame(frame):
    frame.tkraise()
  
root=tk.Tk() 
root.title("Rock,Paper,Scissors")
root.geometry("1366x768")
root.configure(bg="blue")

frame1=tk.Frame(root,bg="lightblue")
frame2=tk.Frame(root,bg="lightblue")
frame3=tk.Frame(root,bg="lightblue")

for frame in (frame1, frame2,frame3):
    frame.place(relwidth=1, relheight=1)
    
#frame.configure(bg="lightblue")

label=tk.Label(frame1,text="ROCK PAPER SCISSORS",font=("Courier", 36,"bold"), fg="red",bg="lightblue")
label.pack(padx=10,pady=10)

entry=tk.Entry(frame1,width=70)
entry.pack(padx=10,pady=10,side="right")

label0=tk.Label(frame1,text="Enter your name :",font=("Arial",16,'bold'),bg='lightblue')
label0.pack(padx=10,pady=10,side="left")

label1=tk.Label(frame1,text="",bg="lightblue",fg="white",font=('Arial',24,'bold'))
label1.pack()

hidden_button=tk.Button(frame1,text="Next")

def entry_text():
   usrname=entry.get()
   label1.config(text=f"Hello!{usrname}\nLets play rock paper scissors")

def show_button():
   hidden_button.pack(padx=10, pady=10,side="bottom")

def combined():
   entry_text()
   show_button()

def next_frame2():   
   show_frame(frame2)

def next_frame3():
   show_frame(frame3)

button1=tk.Button(frame1,text="ENTER",command=combined,width=20, height=5, padx=10, pady=1)
button1.pack(side="bottom",padx=20,pady=20)
hidden_button=tk.Button(frame1,text="Next",command=next_frame2,width=20, height=5, padx=10, pady=1)

user_wins=0
computer_wins=0

def determineWinner(user_choice, computer_choice):
    global user_wins, computer_wins
    if user_choice==computer_choice:
     return 'its a tie'
    if (user_choice=="Rock" and computer_choice=="Paper"):
        computer_wins += 1
        return 'computer wins'
    if (user_choice=="Rock" and computer_choice=="Scissors"):
        user_wins += 1
        return 'user wins'
    if (user_choice=="Paper" and computer_choice=="Rock"):
        user_wins += 1
        return 'user wins'
    if (user_choice=="Paper" and computer_choice=="Scissors"):
        computer_wins += 1
        return 'computer wins'
    if (user_choice=="Scissors" and computer_choice=="Paper"):
        user_wins += 1
        return 'user wins'
    if (user_choice=="Scissors" and computer_choice=="Rock"):
        computer_wins += 1
        return 'computer wins'
        

def rps(user_choice):
    choice =["Rock","Paper","Scissors"]
    computer_choice=random.choice(choice)
    result=determineWinner(user_choice,computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    
def quit():
   next_frame3()
   label9.config(text=f"Your score: {user_wins}\ncomputer score: {computer_wins}")
   label_q.config(text="Thank You for playing\n")

label9=tk.Label(frame3,text="",bg='lightblue',font=('Arial',28,'bold'),fg='red') 
label9.pack()            
result_label=tk.Label(frame2,text="",bg='lightblue',font=('Arial',28,'bold'),fg='red')
result_label.pack()
label_q=tk.Label(frame2,text="",bg='lightblue',font=('Arial',28,'bold'),fg='red')
label_q.pack()


button_r=tk.Button(frame2,text="Rock",font=("Arial",24,"bold"),command=lambda:rps('Rock'),bg="lightblue",fg='navyblue',width=10, height=2)
button_r.pack(side='top',padx=10,pady=2)
button_p=tk.Button(frame2,text="Paper",command=lambda:rps("Paper"),font=('Arial',24,'bold'),bg="lightblue",fg='navyblue',width=10, height=2)
button_p.pack(side='top',padx=10,pady=2)
button_s=tk.Button(frame2,text="Scissors",font=("Arial",24,"bold"),command=lambda:rps("Scissors"),bg="lightblue",fg='navyblue',width=10, height=2)
button_s.pack(side='bottom',padx=10,pady=2)
button_q=tk.Button(frame2,text="QUIT",command=quit,font=("Arial",24,"bold"),bg="red",fg='navyblue',width=10, height=2)
button_q.pack(side='top',padx=10,pady=2)


show_frame(frame1)
root.mainloop()