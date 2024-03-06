import tkinter  # importing module
from tkinter import *
import random

questions = [
    "The first astronaut to travel to space came from which country?",
    "Which Sikh Guru was executed by Aurangzeb?",
    "The words 'Satyameva Jayate' inscribed below the base plate of the emblem are taken from ...",
    "The book of Parsis is...",
    "The National Anthem was first sung in the year...",
    "Who composed the song 'Sare Jahan Se Achha'?",
    "What is the pen name of 'Fingal O'Flahertie Wills'?",
    "Name the boundary line that divides India and China...",
    "This Cathedral was build in Moscow,about 450 years ago,with its 10 colourful towers...",
    "Nicknamed as 'Picasso of India' he started his career in painting film posters;he died in 2011.Who is he?"

]
answers_choice = [

    ['U.S.A', 'Russia', 'China', 'Rocketonia'],
    ['Tegh Bahadur', 'Arjun Dev', 'HarGobind', 'Gobind Singh'],
    ['Rigveda', " Satpath Brahman", 'Mundak Upnishad', 'Ramayana'],
    ['Torah', 'Bible', 'Zend Avesta', ' Shrimad Bhagvad Gita'],
    ['1911', '1913', '1936', '1935'],
    ['Jaidev', 'Mohammad Iqbal', 'Bankim C. Chattopadhyay', 'RabindraNath Tagore'],
    ["O'Henry", "Oscar Wild", "Voltaire", "Mark Twain"],
    ["Radcliff line", "49Th Parallel", "McMohan Line", "Vallo Alpino"],
    ["St. Basil's Cathedral", "Windsor Castle", "Imperial Palace", "Palace of Versailles"],
    ['M.F.Husain', "Satish Gujral", "Tyeb Menta", "Raja Ravi Verma"],

]
answers = [1, 0, 2, 2, 0, 1, 1, 2, 0, 0]
user_answer = []


indexes = []





def gen():
    global indexes
    while (len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Are Excellent !!", font=("vivaldi", 30), bg="black", fg="green")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="3.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better !!", font=("vivaldi", 30), bg="black", fg="blue")
    else:
        img = PhotoImage(file="2.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Should Work Hard !!", font=("vivaldi", 30), bg="black", fg="red")


def calc():
    global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print("Your Marks:", score)
    showresult(score)


ques = 1


def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()


def startquiz():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas", 20),
        width=500,
        justify="center",
        wraplength=400,
        background="black",
        foreground="pink",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Times", 16),
        value=0,
        variable=radiovar,
        command=selected,
        background="orange",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times", 16),
        value=1,
        variable=radiovar,
        command=selected,
        background="yellow",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times", 16),
        value=2,
        variable=radiovar,
        command=selected,
        background="turquoise",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times", 16),
        value=3,
        variable=radiovar,
        command=selected,
        background="pink",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title("Quizzz")
root.geometry("700x800")
root.config(background="black")
root.resizable(0, 0)

img1 = PhotoImage(file="q.png")

labelimage = Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimage.pack(pady=(20,0))

labeltext = Label(
    root,
    text="Quizzz",
    font=("Vivaldi", 48, "bold"),
    background="black",
    foreground="yellow"
)
labeltext.pack()

img2 = PhotoImage(file="s.png")

btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text="Read The Rules And\nClick start Once You Are ready",
    background="black",
    font=("Consolas", 10),
    justify="center",
    foreground="pink",
)
lblInstruction.pack()

lblRules = Label(
    root,
    text="This quiz contains 10 questions\nOnce you select a radio button that will be a final choice\nMarks for each questions=5",
    width=100,
    font=("Times", 12),
    background="turquoise",
    foreground="black",
)
lblRules.pack()

root.mainloop()
