import pickle
questions = ["""
Кто занимается предпринимательством?
1)Частные лица
2)Государство
3)Различные ассоциации
4)Всё выше перечисленое
""",
"""
Что из ниже перечисленного является физическим лицом?
1)фирма
2)Организация
3)Человек занимающийся экономической деятельностью
""",
"""
Бартер это -
1)Обмен товара на товар
2)Обмен товара на деньги
3)Вид предпринимательства
""",
"""
Сколько условий имеет обмен?
1)2
2)3
3)4
""",
"""
Что является объектом собственности?
1)Факторы производства
2)Группы
3)Отдельная личность
""",
"""
Что из ниже перечисленного является формой собстенности?
1)Частная собственность
2)Готовая продукция
3)Государство
"""]

answers = [4, 3, 2, 3, 1, 1]
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
 closeInpecho "# Test" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/ilya0405/Test.git
git push -u origin masterut = raw_input("Press Enter to exit")
 
