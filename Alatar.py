from random import choice
try:
    import pyttsx3
    engine = pyttsx3.init()
except:
    pass
sentences = []
sequences = {}
seq = []
init = []

with open("sentences.txt","r") as f:
    line = f.readline()
    while line != "":
        sentences.append(line)
        line = f.readline()
    f.close()

def separate(sentence):
    sentence = sentence.lower()
    new = []
    word = ""
    for i in sentence:
        if i != " ":
            if i not in "":
                word += i
        else:
            new.append(word)
            word = ""
    new.append(word)
    return new

for i in sentences:
    seq.append(separate(i))

for element in seq:
    for i in range(len(element)-1):
        word = element[i]
        if not "." in word:
            if word not in sequences:
                sequences[word] = []
            sequences[word].append(element[i+1])

for i in seq:
    init.append(i[0])

def generate():
    w = choice(init)
    text = w[0].upper() + w[1:]
    while w in sequences:
        w = choice(sequences[w])
        text += " " + w
        if len(separate(text)) > 15:
            text += "..."
            break
    if len(separate(text))<=3:
        if choice([0, 1]) == 0:
            text = generate()
    return text

try:
    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        if voice.name == "Microsoft Zira Desktop - English (United States)":
            break
except:
    pass

while 1:
    a = generate()
    try:
        engine.say(a)
        engine.runAndWait()
    except:
        pass
    print(a)
    input()
