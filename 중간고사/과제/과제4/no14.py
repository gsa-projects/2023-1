with open("sentence.txt", 'w') as file:
    file.write('Ever since the COVID-19 breakout, nations all around the world have taken action to ensure the safety of their citizens. International safety precautions include self-quarantining, and according to the New York Times, "[a]t least 93 percent of the global population now lives in countries with coronavirus-related travel restrictions." Consequently, schools around the world have shut down and transitioned to online classrooms. The abruptness of this situation has caused much chaos for the 1.7 billion (UNESCO) - and increasing - students whose learning has become impaired. Eric Kim, a sophomore at Korea International School, is one among many students who were initially opposed to online schooling, as he thought it "[lacked] the interpersonal interaction that real schools allow." Kim also thought that "the screen time causes a drop in focus and increases distractions.')

with open("sentence.txt") as file:
    for line in file:
        words = [e.strip('.,?!()[]{}\'"+-*/=_`<>:;@#$%^&~') for e in line.split(' ') if 's' in e]
        for e in words:
            print(e)