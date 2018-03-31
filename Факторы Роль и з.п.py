import pickle
questions = ["""
Сколько выделяется основных факторов производства?
1)6
2)7
3)5
""",
"""
Что не является ролью экономики в обществе?
1)Общественное разделение труда
2)Фундамент всякого общества
3)Основа научно-технического прогресса
""",
"""
Что не является формой зароботной платы
1)Повеременная
2)Смешанная
3)Оклад
4)МРОТ
""",
"""
Что не является функцией з/п
1)Мотивационная
2)Уникальность труда
3)Статусная
""",
"""
Что является фактором производства - труд?
1)Знания
2)Деятельность людей попроизводству товара
3)Используемые природные ресурсы
"""]

answers = [3, 1, 4, 3, 2]
datafile = open("test.dat", "wb")
pickle.dump(questions, datafile)
pickle.dump(answers, datafile)
datafile.close()
import pickle
mark = 0
try:
 datafile = open("test.dat", "rb")
except: 
 print(Ошибка)
else:
 questions = pickle.load(datafile)
answers = pickle.load(datafile)
datafile.close()
n = len(answers) #К-во вопросов и ответов
i = 5
for i in range(0, n):
 print(questions[i])
a = int(input("Ваш ответ: "))
if a == answers[i]:
 mark = mark + 1
 print("Правильно1")
else:
 print ("Неправильно")
 print("Вы правильно ответили на ", mark, " вопросов из ",n)
