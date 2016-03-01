# coding=utf-8

from tkinter import *
from tkinter.filedialog import *
from tkinter import filedialog
import tkinter.messagebox
import fileinput

QUESTIONS = []
ANSWERS = []
MY_ANSWERS = []
CORRECT = {}
INCORRECT = {}
i = 1

root = Tk()

def load_test():
    op = askopenfilename(defaultextension = '.txt')
    count = 1
    for line in fileinput.input(op):
        if count%3==0:
            count+=1
        elif count in range(1, count+1, 3):
            QUESTIONS.append(line.rstrip())
            count += 1
        elif count in range(2, count+1, 3):
            ANSWERS.append(line)
            count += 1
    Question.insert(END, QUESTIONS[0])

def browsing(event):
    global i
    correct = 0
    incorrect = 0
    try:
        my_a = Answer.get()
        my_answer = int(my_a)
        MY_ANSWERS.append(my_answer)
        Question.delete(0.0, END)
        Question.insert(END, QUESTIONS[i])
        i += 1
        Answer.delete(0, 'end')
    except IndexError:
        for k in range(0, len(QUESTIONS)):
            if int(ANSWERS[k])==MY_ANSWERS[k]:
                CORRECT[QUESTIONS[k]] = MY_ANSWERS[k]
                correct +=1
            else:
                INCORRECT[QUESTIONS[k]] = MY_ANSWERS[k]
                incorrect +=1
        Answer.delete(0, 'end')
        Question.delete(0.0, END)
        Question.insert(END, "Ваш результат:\n")
        Question.insert(END, "Правильных ответов: "+str(correct)+"\n")
        Question.insert(END, "Неправильных ответов: "+str(incorrect)+"\n")
        Question.insert(END, "Ошибки были допущены в следующих примерах" + str(INCORRECT))
    except ValueError:
        tkinter.messagebox.showerror('Ошибка', 'Укажите корректный ответ')


def save_test():
    name=asksaveasfile(mode='w',defaultextension=".txt")
    text2save=str(Question.get(0.0,END))
    name.write(text2save)
    name.close

def my_help():
    msg = tkinter.messagebox.showinfo("Справка", "Загрузите тест, нажав Файл->Открыть тест и выбрав txt-файл")

def Test_Creator():

    child = Toplevel(root)
    Q = Label(child, text = "Вопрос")
    A = Label(child, text = 'Ответ')
    CreateQuestion = Entry(child, font=('times', 14))
    CreateAnswer = Entry(child, font = ('times', 14))
    Createbutton = Button(child, text = 'Сохранить', font=('Calibri', 14), relief = RAISED, cursor = 'hand2')

    def createtest(event):
        name=asksaveasfile(mode='a',defaultextension=".txt")
        question = str(CreateQuestion.get())
        name.write('\n' + question + '\n')
        answer = str(CreateAnswer.get())
        name.write(answer+'\n')
        name.write('---------------')
        name.close()


    Q.grid(row = 0, column = 0)
    CreateQuestion.grid(row = 0, column = 1)
    A.grid(row = 1, column = 0)
    CreateAnswer.grid(row = 1, column = 1)
    Createbutton.place(x = 133, y = 55)

    Createbutton.bind('<Button-1>', createtest)

    child.title('TestCreator')
    child.geometry('320x150')


root.geometry("800x400")
root.title("Интерпретатор тестов")
m = Menu(root)
root.config(menu=m)

subMenu = Menu(m)
m.add_cascade(label = 'Файл', menu = subMenu)
subMenu.add_command(label = 'Открыть тест', command = load_test)
subMenu.add_command(label = 'Сохранить результаты', command = save_test)
subMenu.add_command(label = 'Test Creator', command = Test_Creator)
subMenu.add_separator()
subMenu.add_command(label = 'Выйти', command = exit)

aboutMenu = Menu(m)
m.add_cascade(label = 'О программе', menu = aboutMenu)
aboutMenu.add_command(label = '?', command = my_help)

Frame1 = Frame(root)
Question = Text(root, font=('times', 50), wrap = WORD)
MyScroll = Scrollbar(root)
MyScroll.place(x = 775, y = 10, height = 230)
MyScroll['command'] = Question.yview()
Question['yscrollcommand'] = MyScroll.set
Answer = Entry(root, font = ('times', 50), bd = 4)
button = Button(root, text = 'Ответить', font=('Calibri', 26), relief = RAISED, cursor = 'hand2', bd = 4)


# Frame1.place(x = 0, y = 0, width = 800, height = 50)
Question.place(x = 10, y = 10, width = 780, height = 230)
Answer.place(x = 10, y = 245, width = 383, height = 70)

button.bind('<Button-1>', browsing)
button.place(x = 397, y = 245, width = 395, height = 70)

statusBar = Label(root, text ="...", bd = 1, relief=SUNKEN, anchor = W)
statusBar.pack(side = BOTTOM, fill = X)

root.mainloop()





