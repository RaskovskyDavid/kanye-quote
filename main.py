from tkinter import *
import requests


def get_quote():
    # this is a request for get a json from a api
    response = requests.get(url="https://api.kanye.rest")
    # checking the status code and generate a error
    response.raise_for_status()
    # get the data from the response
    data = response.json()
    # check if it 's too long the quote
    if len(data["quote"]) > 70:
        # update the text showing
        canvas.itemconfig(quote_text, text=data["quote"], font=("Arial", 20, "bold"))
    else:
        # update the text showing
        canvas.itemconfig(quote_text, text=data["quote"], font=("Arial", 30, "bold"))


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
