# source of information:
# https://interactive.unwomen.org/multimedia/timeline/womensfootprintinhistory/en/index.html#section01
# https://www.history.com/topics/womens-history/womens-history-us-timeline

import tkinter
import tkinter.messagebox

f = open("historyOfWomen.txt",encoding="utf-8")

# first an empty dictionary called history is created.
# year, country, name and description of history(read in from the historyOfWOmen.txt file) are stored in a list in order.
# lists with the same first two numbers for the year are stored inside the same list
# then this list of lists becomes the value associated to the key in the history dictionary
# the key is the first two numbers of the years in that list of list.
# e.g. {'16': [['1691', 'Mexico', 'Sor Juana Inés de la Cruz', 'Following ...'], ['1671', 'country', 'name', 'event in history'],...], '20':...}
history = {}
nextLine = f.readline().strip()
while nextLine != "" :
    list1 = nextLine.split(sep=":::")
    year = str(list1[0][0])+str(list1[0][1])
    if year not in history:
        history[year] = []
    history[year].append([list1[0],list1[1],list1[2],list1[3]])
    nextLine = f.readline().strip()

window = tkinter.Tk()
window.geometry("800x650")
window.title("History of women by century")


def click_century(num_th_century):
    '''When user clicks the button for each century, relevant information for the particular century
       is displayed on screen, which is taken from the dictionary called history.
       When relevant information for century does not exist, the user is informed.'''
    num_th_century = str(num_th_century-1)
    events_list = history.get(num_th_century)

    if num_th_century in history:
        for event in range(len(events_list)):

            events1 = "{} from {} in {} :".format(history[num_th_century][event][2], history[num_th_century][event][1], history[num_th_century][event][0])
            events2 = "{}".format(history[num_th_century][event][3])
        
            if events1 != "" and events2 != "" :
                listbox_centuries.insert(tkinter.END, events1)
                listbox_centuries.insert(tkinter.END, events2)
                listbox_centuries.insert(tkinter.END,"\n")
            elif events2 == "":
                tkinter.messagebox.showwarning(title="Does not exit", message="The following events are not yet available.")

# frame and listbox
frame_centuries = tkinter.Frame(window)
frame_centuries.pack(fill = tkinter.BOTH, expand=True)
listbox_centuries = tkinter.Listbox(frame_centuries)
listbox_centuries.pack(fill = tkinter.BOTH, expand=True, side=tkinter.TOP)

# vertical scrollbar
scrollbar_centuries = tkinter.Scrollbar(listbox_centuries, orient = tkinter.VERTICAL)
scrollbar_centuries.pack(side = tkinter.RIGHT, fill = "y", expand=False)
listbox_centuries.config(yscrollcommand=scrollbar_centuries.set)
scrollbar_centuries.config(command=listbox_centuries.yview)

# horizontal scrollbar
scrollbar2_centuries = tkinter.Scrollbar(listbox_centuries, orient = tkinter.HORIZONTAL)
scrollbar2_centuries.pack(side = tkinter.BOTTOM, fill = "x", expand=False)
listbox_centuries.config(xscrollcommand=scrollbar2_centuries.set)
scrollbar2_centuries.config(command=listbox_centuries.xview)


# buttons for each century for user to click
button_century21 = tkinter.Button(window,text="21th century", width=98, command = lambda: click_century(21))
button_century21.pack()
button_century20 = tkinter.Button(window,text="20th century", width=98, command = lambda: click_century(20))
button_century20.pack()
button_century19 = tkinter.Button(window,text="19th century", width=98, command = lambda: click_century(19))
button_century19.pack()
button_century18 = tkinter.Button(window,text="18th century", width=98, command = lambda: click_century(18))
button_century18.pack()
button_century17 = tkinter.Button(window,text="17th century", width=98, command = lambda: click_century(17))
button_century17.pack()


window.mainloop()
