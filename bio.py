intro = "\nHi, I am Ishan. I am a Product Designer and Frontend developer."
print(intro)
questions = "\nWhat do you want to know about me?Press your keys from the menu number:\n(1)Background\n(2)Experience\n(3)My Personal thoughts\n(quit)Quit\n\n"
answer = ""
while answer not in ["quit" ,"Q"]:
    answer = input(questions)
    if answer == "1":
        print(
            "\n\nI started my carrer as a product designer around 7+ years back. I would introduce myself as a intersection of product designer and a frontend developer. Who loves anythong regarding technology.\n"
        )
    if answer == "2":
        print(
            "\n\nI have gathered around 7+ years of professional experience working in this field."
        )
        move = ""
        experience = "\nback to go back(back)\nPress the choices:"
        for worked in ["(1)Company one", "(2)Company two\n"]:
            work_text = print(worked)
        while move != "back":
            answer_two = input(experience)
            if answer_two == "1":
                print(
                    "\n\nIn Company One. I learnt some great topics around Javascript.\n"
                )
            if answer_two == "2":
                print(
                    "\n\nIn Company Two. I was given oppurtunity to work on the process of designing and developing the application.\n"
                )
            if answer_two == "back":
                break
    if answer == "3":
        print(
            "\n\nI strongly belive we the professionals of tech industry need to learn and innovate. There is constant change in the technologies in the tech market where we need to update ourselves with. The only thing that is constant is change. I love trying out new technologies and update with modern tools helping our lives more easier. My current learnings include Javascript, UX and Python.\n"
        )

