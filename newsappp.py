import io
import requests
from tkinter import *
import webbrowser
from urllib.request import urlopen
from PIL import ImageTk, Image

class Newsapp:
    def __init__(self):
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=ba554938a2e14528b1107bceefe89880').json()
        self.load_gui()

        # Load the first news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        self.root.title('Aishwarya News app')
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        self.clear()

        # Check if image URL is valid before downloading
        img_url = self.data['articles'][index].get('urlToImage')

        # Use a default image if no image URL is available
        if not img_url:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'

        try:
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            # Use the default image if download fails
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        # Create the image label
        image_label = Label(self.root, image=photo)
        image_label.pack()

        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', wraplength=350, justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        if index != 0:
            prev = Button(frame, text='Prev', width=16, height=3, command=lambda: self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3, command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles']) - 1:
            next = Button(frame, text='Next', width=16, height=3, command=lambda: self.load_news_item(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self, url):
        webbrowser.open(url)


obj = Newsapp()





















