print("Привет!")
Name =input("как тебя зовут? ")
name = Name.split()[-1].capitalize()
print(f"Приятно познакомиться, {name}!")
mood = input(" как дела?").strip().lower()
last_word=mood.split()[-1]
if last_word == "хорошо":
    print("круто!")
elif last_word == "прекрасно":
    print("классно!")
elif last_word == "неплохо":
    print("тоже хорошо!")
elif last_word == "нормально":
    print("тоже неплохо")
elif last_word == "пойдёт":
    print("тоже неплохо")
else:
    print(f"жаль, что у тебя {mood}")
age = input("сколько тебе лет? ").strip()
last_word = age.split()[-1]
if int(last_word) < 18:
    print(f"тебе {last_word} лет. Ещё вся жизнь впереди")
else:
    print(f"тебе {last_word} лет.уже взростый человек")
    print("пока!")