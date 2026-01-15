# with open("data/notes.txt","r", encoding="utf-8") as file:
#     content = file.read()
# print(content)

# with open("data/notes.txt","r", encoding="utf-8") as file:
#     for i in file:
#         print(i.strip(""))


# with open("data/notes.txt","a", encoding="utf-8") as file:
#     file.write("добавили что-то")
# with open("data/notes.txt","r", encoding="utf-8") as file:
#     content = file.read()
# print(content)   


# with open("data/notes.txt","w", encoding="utf-8") as file:
#     file.write("новая запись")
#     file.write("новая запись 2")
# with open("data/notes.txt","r", encoding="utf-8") as file:
#       for i in file:
#             clean_line=i.strip()
#             print(clean_line)


# 1 показать 
# 2 добавить 
# 3 сохранить 
# 0 выйти 

# def load_notes_txt():
#     notes=[]
#     with open ("data/notes.txt","r",encoding="utf-8") as file: 
#         for i in file: 
#             clean=i.strip()
#             if clean != "":
#                 notes.append(clean)
#     return notes
# def show_notes_txt(notes):
#     if len(notes) == 0:
#         print("Заметок нету")
#         return
#     number = 1
#     for i in notes:
#         print(number,".",i)
#         number = number+1

# def add_note_txt(notes):
#     text=input("Введите заметку: ").strip()
#     if text == "":
#         print("Пустую заметку нельзя добавить")
#         return
#     notes.append(text)
#     print("Доьавлено")

# def save_notes_txt(notes):
#     with open("data/notes.txt","w", encoding="utf-8") as file:
#         for i in notes: 
#             file.write(i+"\n")

# notes=load_notes_txt()

# while True:
#     print("\n1. Показать")
#     print("2. Добавить")
#     print("3. Сохранить")
#     print("0. Выход")

#     choice= input("Выбор: ")
#     if choice=="1":
#         show_notes_txt(notes)
#     elif choice =="2":
#         add_note_txt(notes)
#     elif choice=="3":
#         save_notes_txt(notes)
#     elif choice=="0":
#         save_notes_txt(notes)
#         print("Выход")
#         break
#     else: 
#         print("Неверный выбор")


