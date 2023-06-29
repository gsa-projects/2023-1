# from tkinter import Tk, PhotoImage, Label, Button

# def change(new_img):
#     imageLabel.configure(image=new_img)
#     imageLabel.image = new_img

# def on_pause():
#     change(pause)

# def on_previous():
#     change(previous)

# def on_record():
#     change(record)

# def on_stop():
#     change(stop)

# win = Tk()

# pause = PhotoImage(file='./images/pause.png')
# previous = PhotoImage(file='./images/previous.png')
# record = PhotoImage(file='./images/record.png')
# stop = PhotoImage(file='./images/stop.png')
# imageLabel = Label(win, image=pause, width=512, height=512)

# pause_btn = Button(win, text="pause", command=on_pause)
# previous_btn = Button(win, text="previous", command=on_previous)
# record_btn = Button(win, text="record", command=on_record)
# stop_btn = Button(win, text="stop", command=on_stop)

# imageLabel.grid(row=0, column=0, columnspan=4)
# pause_btn.grid(row=1, column=0)
# previous_btn.grid(row=1, column=1)
# record_btn.grid(row=1, column=2)
# stop_btn.grid(row=1, column=3)

# win.mainloop()

from bs4 import BeautifulSoup
import requests

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + "bitcoin"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
selected = soup.select('a.news_tit')

for s in selected:
    print(s.get_text())