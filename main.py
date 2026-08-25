import tkinter as tk
from tkinter import messagebox


# ============================================================
# COLORS
# ============================================================

BG = "#0F172A"
CARD = "#1E293B"
CARD_LIGHT = "#334155"
WHITE = "#F8FAFC"
GRAY = "#94A3B8"

BLUE = "#3B82F6"
BLUE_HOVER = "#2563EB"

GREEN = "#10B981"
GREEN_HOVER = "#059669"

PURPLE = "#8B5CF6"
PURPLE_HOVER = "#7C3AED"

RED = "#EF4444"


# ============================================================
# FONT
# ============================================================

FONT_TITLE = ("Arial", 26, "bold")
FONT_SUBTITLE = ("Arial", 12)
FONT_CARD_TITLE = ("Arial", 19, "bold")
FONT_NORMAL = ("Arial", 12)
FONT_BUTTON = ("Arial", 12, "bold")


# ============================================================
# LIST LESSON
# ============================================================

list_topics = [
    (
        "01  การสร้าง List",
        """List คือโครงสร้างข้อมูลที่ใช้เก็บข้อมูลหลายค่า
ไว้ในตัวแปรเดียว

ตัวอย่าง:

numbers = [10, 20, 30, 40]

print(numbers)

ผลลัพธ์:

[10, 20, 30, 40]

จำง่าย ๆ:
List ใช้เครื่องหมาย [ ]"""
    ),

    (
        "02  การเข้าถึงข้อมูลด้วย Index",
        """สมาชิกใน List สามารถเข้าถึงได้ด้วย Index

Index เริ่มต้นที่ 0

ตัวอย่าง:

numbers = [10, 20, 30]

print(numbers[0])
print(numbers[1])
print(numbers[2])

ผลลัพธ์:

10
20
30

จำไว้:
สมาชิกตัวแรก = Index 0"""
    ),

    (
        "03  append() และ insert()",
        """ใช้สำหรับเพิ่มข้อมูลลงใน List

append()
เพิ่มข้อมูลต่อท้าย List

numbers = [10, 20]

numbers.append(30)

ผลลัพธ์:

[10, 20, 30]


insert()
เพิ่มข้อมูลในตำแหน่งที่กำหนด

numbers.insert(1, 15)

ผลลัพธ์:

[10, 15, 20, 30]"""
    ),

    (
        "04  remove() และ pop()",
        """ใช้สำหรับลบข้อมูลจาก List

remove()
ลบข้อมูลที่ระบุ

numbers = [10, 20, 30]

numbers.remove(20)

ผลลัพธ์:

[10, 30]


pop()
ลบข้อมูลตาม Index

numbers.pop(0)

ผลลัพธ์:

[30]"""
    ),

    (
        "05  การวนลูปกับ List",
        """สามารถใช้ for เพื่อวนดูข้อมูล
ทุกตัวใน List

ตัวอย่าง:

numbers = [10, 20, 30]

for number in numbers:
    print(number)

ผลลัพธ์:

10
20
30"""
    )
]


# ============================================================
# STRING LESSON
# ============================================================

string_topics = [
    (
        "01  การสร้าง String",
        """String คือข้อมูลประเภทข้อความ

ตัวอย่าง:

name = "Python"

print(name)

ผลลัพธ์:

Python

String สามารถเขียนได้ด้วย
"ข้อความ" หรือ 'ข้อความ'"""
    ),

    (
        "02  การเข้าถึงตัวอักษรด้วย Index",
        """String สามารถเข้าถึงตัวอักษร
ด้วย Index ได้เหมือน List

ตัวอย่าง:

text = "Python"

print(text[0])
print(text[1])

ผลลัพธ์:

P
y

Index เริ่มต้นที่ 0"""
    ),

    (
        "03  String Slicing",
        """Slicing ใช้เลือกบางส่วนของข้อความ

ตัวอย่าง:

text = "Python"

print(text[0:3])

ผลลัพธ์:

Pyt

รูปแบบ:

text[start:end]

ตำแหน่ง end จะไม่ถูกรวม"""
    ),

    (
        "04  upper() / lower() / replace()",
        """upper()
เปลี่ยนเป็นตัวพิมพ์ใหญ่

text = "python"

text.upper()

ผลลัพธ์:
PYTHON


lower()
เปลี่ยนเป็นตัวพิมพ์เล็ก

text.lower()

ผลลัพธ์:
python


replace()
ใช้แทนที่ข้อความ

text.replace("Java", "Python")"""
    ),

    (
        "05  find() และ in",
        """ใช้สำหรับค้นหาข้อความ

find()

text = "Hello Python"

print(text.find("Python"))

ผลลัพธ์:

6


in

print("Python" in text)

ผลลัพธ์:

True"""
    )
]


# ============================================================
# LIST QUESTIONS
# ============================================================

list_questions = [
    {
        "question": "ข้อใดเป็นการสร้าง List ที่ถูกต้อง?",
        "options": [
            "A. numbers = [10, 20, 30]",
            "B. numbers = (10, 20, 30)",
            "C. numbers = {10, 20, 30}",
            'D. numbers = "10, 20, 30"'
        ],
        "answer": "A"
    },

    {
        "question": "ถ้า numbers = [10, 20, 30] ค่า numbers[1] คืออะไร?",
        "options": [
            "A. 10",
            "B. 20",
            "C. 30",
            "D. 1"
        ],
        "answer": "B"
    },

    {
        "question": "คำสั่งใดใช้เพิ่มข้อมูลต่อท้าย List?",
        "options": [
            "A. add()",
            "B. insert()",
            "C. append()",
            "D. push()"
        ],
        "answer": "C"
    },

    {
        "question": "ถ้าต้องการลบข้อมูล 20 จาก [10, 20, 30] ควรใช้คำสั่งใด?",
        "options": [
            "A. numbers.delete(20)",
            "B. numbers.remove(20)",
            "C. numbers.pop(20)",
            "D. numbers.erase(20)"
        ],
        "answer": "B"
    },

    {
        "question": "คำสั่งใดใช้วนดูข้อมูลทุกตัวใน List?",
        "options": [
            "A. if",
            "B. for",
            "C. switch",
            "D. case"
        ],
        "answer": "B"
    }
]


# ============================================================
# STRING QUESTIONS
# ============================================================

string_questions = [
    {
        "question": "ข้อใดเป็นการสร้าง String ที่ถูกต้อง?",
        "options": [
            'A. name = "Python"',
            "B. name = [Python]",
            "C. name = {Python}",
            "D. name = (Python)"
        ],
        "answer": "A"
    },

    {
        "question": 'ถ้า text = "Python" ค่า text[0] คืออะไร?',
        "options": [
            "A. P",
            "B. y",
            "C. n",
            "D. 0"
        ],
        "answer": "A"
    },

    {
        "question": 'ถ้า text = "Python" แล้ว text[0:3] ได้อะไร?',
        "options": [
            "A. Pyth",
            "B. Pyt",
            "C. yth",
            "D. Python"
        ],
        "answer": "B"
    },

    {
        "question": "คำสั่งใดใช้เปลี่ยน String เป็นตัวพิมพ์ใหญ่?",
        "options": [
            "A. upper()",
            "B. uppercase()",
            "C. capital()",
            "D. big()"
        ],
        "answer": "A"
    },

    {
        "question": 'ถ้า text = "Hello Python" คำสั่ง "Python" in text ได้อะไร?',
        "options": [
            "A. False",
            "B. 0",
            "C. True",
            "D. Python"
        ],
        "answer": "C"
    }
]


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Python List & String Learning")

root.geometry("950x700")

root.configure(bg=BG)

root.resizable(False, False)


# ============================================================
# HELPER BUTTON
# ============================================================

def create_button(parent, text, command, color=BLUE):

    button = tk.Button(
        parent,
        text=text,
        command=command,
        font=FONT_BUTTON,
        bg=color,
        fg=WHITE,
        activebackground=color,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        cursor="hand2",
        width=22,
        height=2
    )

    return button


# ============================================================
# LESSON VIEW
# ============================================================

def show_lesson(topic, content):

    window = tk.Toplevel(root)

    window.title(topic)

    window.geometry("850x650")

    window.configure(bg=BG)

    window.resizable(False, False)


    # Header

    header = tk.Frame(
        window,
        bg=BG
    )

    header.pack(
        fill="x",
        padx=35,
        pady=25
    )


    title = tk.Label(
        header,
        text=topic,
        font=("Arial", 22, "bold"),
        bg=BG,
        fg=WHITE
    )

    title.pack(anchor="w")


    subtitle = tk.Label(
        header,
        text="ศึกษาเนื้อหาและตัวอย่างโค้ด",
        font=FONT_SUBTITLE,
        bg=BG,
        fg=GRAY
    )

    subtitle.pack(
        anchor="w",
        pady=(5, 0)
    )


    # Content card

    card = tk.Frame(
        window,
        bg=CARD
    )

    card.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=(0, 25)
    )


    text = tk.Text(
        card,
        font=("Consolas", 13),
        bg=CARD,
        fg=WHITE,
        insertbackground=WHITE,
        selectbackground=BLUE,
        relief="flat",
        bd=0,
        wrap="word",
        padx=25,
        pady=25
    )

    text.pack(
        fill="both",
        expand=True
    )

    text.insert("1.0", content)

    text.config(state="disabled")


# ============================================================
# LESSON MENU
# ============================================================

def open_lesson_menu(title, topics, color):

    window = tk.Toplevel(root)

    window.title(title)

    window.geometry("700x650")

    window.configure(bg=BG)

    window.resizable(False, False)


    header = tk.Frame(
        window,
        bg=BG
    )

    header.pack(
        fill="x",
        padx=35,
        pady=25
    )


    title_label = tk.Label(
        header,
        text=title,
        font=FONT_TITLE,
        bg=BG,
        fg=WHITE
    )

    title_label.pack(anchor="w")


    subtitle = tk.Label(
        header,
        text="เลือกหัวข้อที่ต้องการเรียน",
        font=FONT_SUBTITLE,
        bg=BG,
        fg=GRAY
    )

    subtitle.pack(
        anchor="w",
        pady=(5, 0)
    )


    for topic, content in topics:

        card = tk.Frame(
            window,
            bg=CARD
        )

        card.pack(
            fill="x",
            padx=35,
            pady=6
        )


        button = tk.Button(
            card,
            text=topic,
            font=("Arial", 13, "bold"),
            bg=CARD,
            fg=WHITE,
            activebackground=CARD_LIGHT,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            cursor="hand2",
            anchor="w",
            padx=20,
            height=2,
            command=lambda t=topic, c=content:
                show_lesson(t, c)
        )

        button.pack(
            fill="x"
        )


# ============================================================
# QUIZ
# ============================================================

def start_quiz(title, questions, color):

    window = tk.Toplevel(root)

    window.title(title)

    window.geometry("850x650")

    window.configure(bg=BG)

    window.resizable(False, False)


    current = 0

    score = 0

    selected = tk.StringVar()


    # Header

    header = tk.Frame(
        window,
        bg=BG
    )

    header.pack(
        fill="x",
        padx=35,
        pady=25
    )


    title_label = tk.Label(
        header,
        text=title,
        font=("Arial", 22, "bold"),
        bg=BG,
        fg=WHITE
    )

    title_label.pack(anchor="w")


    progress = tk.Label(
        header,
        text="",
        font=FONT_SUBTITLE,
        bg=BG,
        fg=GRAY
    )

    progress.pack(
        anchor="w",
        pady=(5, 0)
    )


    # Question Card

    card = tk.Frame(
        window,
        bg=CARD
    )

    card.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=(0, 25)
    )


    question_label = tk.Label(
        card,
        text="",
        font=("Arial", 17, "bold"),
        bg=CARD,
        fg=WHITE,
        wraplength=700,
        justify="left"
    )

    question_label.pack(
        anchor="w",
        padx=30,
        pady=30
    )


    answer_frame = tk.Frame(
        card,
        bg=CARD
    )

    answer_frame.pack(
        fill="x",
        padx=30
    )


    radio_buttons = []


    for i in range(4):

        radio = tk.Radiobutton(
            answer_frame,
            text="",
            variable=selected,
            value="",
            font=("Arial", 12),
            bg=CARD,
            fg=WHITE,
            activebackground=CARD,
            activeforeground=WHITE,
            selectcolor=color,
            anchor="w",
            justify="left",
            wraplength=650,
            padx=10,
            pady=10
        )

        radio.pack(
            fill="x",
            pady=4
        )

        radio_buttons.append(radio)


    # Next Button

    next_button = create_button(
        window,
        "ข้อถัดไป",
        None,
        color
    )

    next_button.pack(
        pady=(0, 25)
    )


    def show_question():

        selected.set("")

        question = questions[current]

        question_label.config(
            text=question["question"]
        )

        progress.config(
            text=f"ข้อ {current + 1} / {len(questions)}"
        )


        for i in range(4):

            option = question["options"][i]

            radio_buttons[i].config(
                text=option,
                value=option[0]
            )


        if current == len(questions) - 1:

            next_button.config(
                text="ส่งคำตอบ"
            )

        else:

            next_button.config(
                text="ข้อถัดไป"
            )


    def next_question():

        nonlocal current
        nonlocal score

        if selected.get() == "":

            messagebox.showwarning(
                "ยังไม่ได้เลือกคำตอบ",
                "กรุณาเลือกคำตอบก่อนครับ",
                parent=window
            )

            return


        if selected.get() == questions[current]["answer"]:

            score += 1


        if current < len(questions) - 1:

            current += 1

            show_question()

        else:

            show_result()


    def show_result():

        for widget in window.winfo_children():

            widget.destroy()


        percentage = score / len(questions) * 100


        title_result = tk.Label(
            window,
            text="แบบทดสอบเสร็จสิ้น!",
            font=("Arial", 28, "bold"),
            bg=BG,
            fg=WHITE
        )

        title_result.pack(
            pady=(100, 20)
        )


        score_label = tk.Label(
            window,
            text=f"{score} / {len(questions)}",
            font=("Arial", 48, "bold"),
            bg=BG,
            fg=color
        )

        score_label.pack()


        percent_label = tk.Label(
            window,
            text=f"คะแนน {percentage:.0f}%",
            font=("Arial", 18),
            bg=BG,
            fg=GRAY
        )

        percent_label.pack(
            pady=10
        )


        if percentage >= 80:

            result_text = "ยอดเยี่ยม! คุณเข้าใจเนื้อหาเป็นอย่างดี 🎉"

        elif percentage >= 60:

            result_text = "ผ่าน! แต่ยังสามารถทบทวนเพิ่มเติมได้ 👍"

        else:

            result_text = "ลองกลับไปทบทวนบทเรียนอีกครั้ง 📚"


        result_label = tk.Label(
            window,
            text=result_text,
            font=("Arial", 14),
            bg=BG,
            fg=WHITE
        )

        result_label.pack(
            pady=20
        )


        close_button = create_button(
            window,
            "กลับหน้าหลัก",
            window.destroy,
            color
        )

        close_button.pack(
            pady=30
        )


    next_button.config(
        command=next_question
    )


    show_question()


# ============================================================
# HOME
# ============================================================

def build_home():

    # Header

    header = tk.Frame(
        root,
        bg=BG
    )

    header.pack(
        fill="x",
        padx=55,
        pady=(45, 10)
    )


    title = tk.Label(
        header,
        text="Python Learning",
        font=("Arial", 32, "bold"),
        bg=BG,
        fg=WHITE
    )

    title.pack(anchor="w")


    subtitle = tk.Label(
        header,
        text="เรียนรู้และทดสอบ Python • List & String",
        font=("Arial", 13),
        bg=BG,
        fg=GRAY
    )

    subtitle.pack(
        anchor="w",
        pady=(5, 0)
    )


    # Main cards

    cards = tk.Frame(
        root,
        bg=BG
    )

    cards.pack(
        fill="x",
        padx=55,
        pady=35
    )


    # LIST CARD

    list_card = tk.Frame(
        cards,
        bg=CARD,
        width=390,
        height=250
    )

    list_card.pack(
        side="left",
        padx=(0, 15)
    )

    list_card.pack_propagate(False)


    list_icon = tk.Label(
        list_card,
        text="LIST",
        font=("Arial", 25, "bold"),
        bg=CARD,
        fg=BLUE
    )

    list_icon.pack(
        anchor="w",
        padx=25,
        pady=(25, 5)
    )


    list_desc = tk.Label(
        list_card,
        text="เรียนรู้การใช้งาน List\n5 บทเรียน • 5 ข้อสอบ",
        font=("Arial", 12),
        bg=CARD,
        fg=WHITE,
        justify="left"
    )

    list_desc.pack(
        anchor="w",
        padx=25,
        pady=5
    )


    list_lesson_button = create_button(
        list_card,
        "📖  เรียนรู้ List",
        lambda: open_lesson_menu(
            "บทเรียน List",
            list_topics,
            BLUE
        ),
        BLUE
    )

    list_lesson_button.pack(
        pady=(15, 5)
    )


    list_test_button = create_button(
        list_card,
        "📝  แบบทดสอบ",
        lambda: start_quiz(
            "แบบทดสอบ List",
            list_questions,
            BLUE
        ),
        GREEN
    )

    list_test_button.pack()


    # STRING CARD

    string_card = tk.Frame(
        cards,
        bg=CARD,
        width=390,
        height=250
    )

    string_card.pack(
        side="left",
        padx=(15, 0)
    )

    string_card.pack_propagate(False)


    string_icon = tk.Label(
        string_card,
        text="STRING",
        font=("Arial", 25, "bold"),
        bg=CARD,
        fg=PURPLE
    )

    string_icon.pack(
        anchor="w",
        padx=25,
        pady=(25, 5)
    )


    string_desc = tk.Label(
        string_card,
        text="เรียนรู้การใช้งาน String\n5 บทเรียน • 5 ข้อสอบ",
        font=("Arial", 12),
        bg=CARD,
        fg=WHITE,
        justify="left"
    )

    string_desc.pack(
        anchor="w",
        padx=25,
        pady=5
    )


    string_lesson_button = create_button(
        string_card,
        "📖  เรียนรู้ String",
        lambda: open_lesson_menu(
            "บทเรียน String",
            string_topics,
            PURPLE
        ),
        PURPLE
    )

    string_lesson_button.pack(
        pady=(15, 5)
    )


    string_test_button = create_button(
        string_card,
        "📝  แบบทดสอบ",
        lambda: start_quiz(
            "แบบทดสอบ String",
            string_questions,
            PURPLE
        ),
        GREEN
    )

    string_test_button.pack()


    # Bottom information

    info = tk.Frame(
        root,
        bg=CARD
    )

    info.pack(
        fill="x",
        padx=55,
        pady=10
    )


    info_label = tk.Label(
        info,
        text="10 บทเรียน   •   10 ข้อสอบ   •   ระบบตรวจคะแนนอัตโนมัติ",
        font=("Arial", 11),
        bg=CARD,
        fg=GRAY,
        pady=15
    )

    info_label.pack()


# ============================================================
# START
# ============================================================

build_home()

root.mainloop()