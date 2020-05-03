file_ = input("""Добро пожаловать на наш сайт!
    kz = Kazakstan 
    ps = Paris
    uar = UAR
    kg = Kyrgystan
    sf = San_Francisco
    ger = Germany
    msw = Moscow
    sw = Sweden 
    \nВведите офис вашего региона: """)
if file_ == "kg":
    c = input("Введите ваши жалобы и предложения: ")
    with open('google_kyrgystan.txt', 'w') as f:
        f.write(c)
else:
    print("Выбран не верный регион!!!")
     
    
