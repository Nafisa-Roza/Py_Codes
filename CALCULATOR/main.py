from tkinter import*

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""


calculator = Tk()
calculator.title("Calculator")
operator=""
text_Input = StringVar()


txtDisplay = Entry(calculator,font=('arial',20,'bold'), textvariable = text_Input, bd=30, insertwidth=4, bg="#969c9e", justify='right').grid(columnspan=4)

btn7 = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="7", command=lambda:btnClick(7)).grid(row=1, column=0)
btn8 = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="8", command=lambda:btnClick(8)).grid(row=1, column=1)
btn9 = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="9", command=lambda:btnClick(9)).grid(row=1, column=2)
Addition = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="+", command=lambda:btnClick("+")).grid(row=1, column=3)


btn4 = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="4", command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="5", command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="6", command=lambda:btnClick(6)).grid(row=2, column=2)
Subtraction = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="-", command=lambda:btnClick("-")).grid(row=2, column=3)


btn1 = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="1", command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="2", command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="3", command=lambda:btnClick(3)).grid(row=3, column=2)
Multiplication = Button(calculator, padx=16, bd=8, fg="black", font=('arial',20,'bold'), text="*", command=lambda:btnClick("*")).grid(row=3, column=3)


btn0 = Button(calculator, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'), text="0", command=lambda:btnClick(0)).grid(row=4, column=0)
btnC = Button(calculator, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'), text="C", command=lambda:btnClearDisplay).grid(row=4, column=1)
btnEquals = Button(calculator, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'), text="=", command=btnEqualsInput).grid(row=4, column=2)
Division = Button(calculator, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'), text="/", command=lambda:btnClick("/")).grid(row=4, column=3)





calculator.mainloop()