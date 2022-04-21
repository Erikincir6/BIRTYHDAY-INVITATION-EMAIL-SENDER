PLACEHOLDER = "[name]"

#isimleri liste cevirdik ['Aang\n', 'Zuko\n',
with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read() # letter txt i oku
    for name in names:
        stripped_name = name.strip() # fazla bosluklari siler
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name) #name i listedi isimle degistir.
        with open(f"./output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter: #yaz ayri file
            completed_letter.write(new_letter) #new letter e yaz


