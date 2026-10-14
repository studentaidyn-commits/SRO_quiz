
questions = [
    {
        "question": "1. Какой язык программирования мы используем?",
        "options": ["A) Java", "B) Python", "C) C++", "D) HTML"],
        "answer": "B"
    },
    {
        "question": "2. Как вывести текст на экран в Python?",
        "options": ["A) print()", "B) input()", "C) int()", "D) for"],
        "answer": "A"
    },
    {
        "question": "3. Какой оператор используется для проверки условия?",
        "options": ["A) for", "B) print", "C) if", "D) input"],
        "answer": "C"
    },
    {
        "question": "4. Как получить ввод от пользователя?",
        "options": ["A) input()", "B) print()", "C) range()", "D) len()"],
        "answer": "A"
    },
    {
        "question": "5. Какой тип данных хранит целые числа?",
        "options": ["A) str", "B) list", "C) int", "D) bool"],
        "answer": "C"
    }
]

score = 0

print("=== QUIZ MASTER ===")
print("Выберите правильный ответ: A, B, C или D.\n")

for question in questions:
    print(question["question"])

    for option in question["options"]:
        print(option)

    user_answer = input("Ваш ответ: ").strip().upper()

    while user_answer not in ["A", "B", "C", "D"]:
        print("Ошибка! Введите A, B, C или D.")
        user_answer = input("Ваш ответ: ").strip().upper()

    if user_answer == question["answer"]:
        print("Правильно!\n")
        score += 1
    else:
        print("Неправильно!")
        print("Правильный ответ:", question["answer"], "\n")

total = len(questions)
percentage = score / total * 100

print("=== РЕЗУЛЬТАТ ТЕСТА ===")
print("Всего вопросов:", total)
print("Правильных ответов:", score)
print("Результат:", percentage, "%")

if percentage >= 80:
    print("Отличный результат!")
elif percentage >= 60:
    print("Хороший результат!")
else:
    print("Нужно повторить материал.")
