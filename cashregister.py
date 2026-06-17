import tkinter as tk

#creates the main window
root = tk.Tk()
root.title('Cash Register')
root.configure(background='white') #sets the bg to white
#root.geometry("280x280") #sets the size

#the title text
titlelabel = tk.Label(root, text='Cash Register', font=('Arial', 16, 'bold'), background='white')
titlelabel.grid(row=0, column=0, pady=5, columnspan=5)

#makes the subtotalvar and makes it global
global subtotalvar 
subtotalvar = 0
itempricelist = []

def additem():
    global subtotalvar
    #global itemdisplayvar
    #global pricevar

    testvar = '\n'

    itempricelist.append(str(item.get())) #adds the item
    itempricelist.append(':')
    #itempricelist.append(testvar)
    itempricelist.append(str(price.get()))
    #itempricelist.append('\n')
    
    #display.config(text=str(item.get()) + ': ' + str(price.get()) +  itemdisplayvar )

    print(itempricelist)

    #listvar = itempricelist
    #listvar = str(listvar).replace('}', '')
    display.config(text = itempricelist)

    #itemdisplayvar = itemdisplayvar + str(item.get())
    #pricevar = pricevar + int(price.get())

    subtotalvar = subtotalvar + float(price.get())
    

    subtotal.config(text='Subtotal: ' + str(subtotalvar)) #update the text

    tax = round(13 * subtotalvar / 100.0, 2)
    taxlabel.config(text='Tax: ' + str(tax))

    finaltotal = (13 * subtotalvar / 100.0) + subtotalvar #sets final total to 13% of the total + the subtotalvar (adding 13% for tax)
    finaltotal = round(finaltotal, 2) #rounds it to the second decimal place
    total.config(text='Total: ' + str(finaltotal))


itemframe = tk.Frame(root, padx=0, pady=0, bg='white')
itemframe.grid(row=1, column=0, pady=5, padx=5)

priceframe = tk.Frame(root, padx=0, pady=0, bg='white')
priceframe.grid(row=2, column=0, pady=5, padx=5)


itemlabel = tk.Label(itemframe, text='Item: ', bg='white')
itemlabel.grid(row=0, column=0, pady=5, padx=5)

#the item entry widget
item = tk.StringVar()
itementry = tk.Entry(itemframe, textvariable=item) 
itementry.grid(row=0, column=1, pady=5, padx=5)

pricelabel = tk.Label(priceframe, text='Price: ', bg='white')
pricelabel.grid(row=0, column=0, pady=5, padx=5)

#the price entry widget
price = tk.StringVar()
priceentry = tk.Entry(priceframe, textvariable=price) 
priceentry.grid(row=0, column=1, pady=5, padx=5)



#makes the button to add an item
addbutton = tk.Button(root, text='Add Item', command=additem)
addbutton.grid(row=3, column=0, columnspan=5, pady=5)

#the label displaying prthe items
display = tk.Label(root, text=' ', background='white')
display.grid(row=4, column=0, pady=5, columnspan=5)

#the label displaying the subtotal
subtotal = tk.Label(root, text='Subtotal: ', background='white')
subtotal.grid(row=5, column=0, pady=2, columnspan=5)

taxlabel = tk.Label(root, text='Tax: ', background='white')
taxlabel.grid(row=6, column=0, pady=2, columnspan=5)

total = tk.Label(root, text='Total: ', background='white')
total.grid(row=7, column=0, pady=2, columnspan=5)


#runs the application
root.mainloop()