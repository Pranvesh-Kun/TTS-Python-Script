from gtts import gTTS
import pygame
import pypdf
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()
file = dict(defaultextension=".pdf", initialdir="/", filetypes=[('pdf file', '*.pdf')])
root.filename = filedialog.askopenfile(**file)

reader = pypdf.PdfReader(root.filename.name)

with open("text_file.txt", mode="w") as f:
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        f.write(page.extract_text())

with open("text_file.txt", mode="r") as f:
    content = f.read()

obj = gTTS(text=content, lang='en', slow=False)

obj.save("audiobook.mp3")
pygame.mixer.init()

pygame.mixer.music.load("audiobook.mp3")
pygame.mixer.music.play()
