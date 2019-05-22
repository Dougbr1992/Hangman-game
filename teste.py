class List_of_theme(object):
    def __init__(self):


    def ChoseTheme (self):
        themes = {1 : House, 2 : Car, 3 : Fruit, 4: Profession}
        chosen_teme

    def Creat_list(self, chosen_theme):
        theme = open(chosen_theme,"r")
        theme.readline()
        theme_list= theme.readlines()
        house =[]
        for word in theme_list:
            ref = word.replace('\n','')
            house.append(ref)
        theme.close()