import pickle
questions = ["""
Что лежит в основе рыночных отношений?
1)Спрос
2)Предложение
3)Рыночная цена
4)Всё из перечисленного
""",
"""
Закон спроса
1)Обратно пропорционален цене
2)Не пропорционален
3)Пропорционален цене
""",
"""
Сколько существует факторовизменения предложения
1)3
2)4
3)2
""",
"""
Какого вида бывают деньги?
1)Наличные и безналичные
2)Безналичные и бумажные
3)Наличные и электронные
""",
"""
Что не является свойством денег?
1)Делимость
2)Портативность
3)Средства обращения
"""]

answers = [4, 1, 2, 1, 3]
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
