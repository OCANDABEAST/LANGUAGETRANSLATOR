from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

root = Tk()
root.title("Language Translator")
root.geometry("900x600")
root.config(bg = "#F2CCC3")

languages = list(LANGUAGES.values())

def Translate():
    source = dropdown_input.get()
    destination = dropdown_output.get()
    translator = Translator()
    translated = translator.translate(text = input_text.get(1.0, END), src = dropdown_input.get(), dest=dropdown_output.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)
        
label_title = Label(root, text = "Language Translator", bg = "#F2CCC3", font = ("Curlz MT", 15, "italic"))
label_title.place(relx = 0.5, rely = 0.2, anchor = CENTER)

input_label = Label(root, text = "Enter Text", bg = "#F2CCC3", font = ("Comic Sans MS", 10, "italic"))
input_label.place(relx = 0.1, rely = 0.4, anchor = W)

input_text = Text(root, bg = "white", font = ("Comic Sans MS", 10, "italic"), height = 7, width = 40, padx = 3, pady = 3, bd = 0)
input_text.place(relx = 0.1, rely = 0.6, anchor = W)

dropdown_input = ttk.Combobox(root, state = "readonly", values = languages)
dropdown_input.place(relx = 0.2, rely = 0.4, anchor = W)
dropdown_input.set("English")

output_label = Label(root, text = "Output", bg = "#F2CCC3", font = ("Comic Sans MS", 10, "italic"))
output_label.place(relx = 0.7, rely = 0.4, anchor = E)

output_text = Text(root, bg = "white", font = ("Comic Sans MS", 10, "italic"), height = 7, width = 40, padx = 3, pady = 3, bd = 0)
output_text.place(relx = 0.9, rely = 0.6, anchor = E)

dropdown_output = ttk.Combobox(root, state = "readonly", values = languages)
dropdown_output.place(relx = 0.9, rely = 0.4, anchor = E)
dropdown_output.set("Choose Output Language")

btn = Button(root, text = "Translate", font = ("Comic Sans MS", 10, "italic"), fg = "black", bg = "blue", activebackground = "red", relief = "flat", pady = 2, command=Translate)
btn.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()
