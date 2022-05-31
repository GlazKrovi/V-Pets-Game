#                   Importations de librairies
import tkinter as tk # pour le GUI
import random as rd # pour l'aleatoire

# Creation de la fenetre principale
window = tk.Tk()

"""Configuration de la dite fenetre"""
window.title("V-Pets game")
window.iconbitmap("V_Pets_Sprites/icone_orange.ico") # icone
window.config(background='#CCCCCC') # couleur fond - gris
window.resizable(width=False, height=False) # fenetre nn redimmensionnable par utilisateur
# window.geometry('550x550') # taille normalisee

#                          Variables 
# Objets
money=50
foodPacks=4
medicines=1
boosts=2

"""Satut"""
life = 100
appetite = 80 
energy = 60
experience = 0

# Mise en place d'affichage desdites variables :
printed_life = tk.IntVar() # <Type>Var puis .set() modifie la valeur affichee
printed_life.set(life) 

printed_appetite = tk.IntVar() 
printed_appetite.set(appetite) # pourcentage

printed_energy = tk.IntVar() 
printed_energy.set(energy) # pourcentage

printed_experience = tk.IntVar() 
printed_experience.set(experience)

printed_foodPacks = tk.IntVar() 
printed_foodPacks.set(foodPacks) 

printed_money = tk.IntVar() 
printed_money.set(money) 

printed_medicines = tk.IntVar() 
printed_medicines.set(medicines) 

printed_boosts = tk.IntVar() 
printed_boosts.set(boosts)

printed_experience = tk.IntVar() 
printed_experience.set(experience)

# Dimensions des widgets :
"""Definissons des dimensions afin d'avoir des widgets du meme type
identiques en taille """ # 
width_gen, height_gen = 10, 5
width_label, height_label = width_gen, height_gen//4
width_exit, height_exit = width_label, height_label*2 # prend place des textes et valeurs du dessus
height_width_canvas = 275 # carre
space_rectification = 10


# Fonctions / Fenetres secondaires
def reset() :
    """Enleve les widgets (sans les supprimer) de la fenetre
    A completer avec une fonction ajoutant ses propres widgets"""
    for c in window.winfo_children() :
        c.grid_forget() 
    window.config(background='#CCCCCC')

def ReInit():
        """Remet les valeurs de debut de jeu a leur etat initial
        et fait ainsi recommencer le jeu 'a zero'""" 

        global money, foodPacks, medicines, boosts, life, appetite, energy

        # Objets 
        money=50
        foodPacks=4
        medicines=1
        boosts=2

        # Status
        life = 100
        appetite = 80 
        energy = 60

        # (re)Ouverture de la fenetre principale
        reset()
        window_main()

def analyze_status():
    """Gere l'eventuelle fin de partie et l'utilsation d'objet automatique
    afin d'aider le joueur"""
    global medicines, life, foodPacks, energy
    global printed_life, printed_energy, printed_appetite

    if life <= 0 : # si vie a 0...
        if medicines < 0 : # ...et que plus de remedes...
            medicines -= 1
        else :
            window_dead() # ...alors game over
    if energy <= 0 :
        if boosts > 0 :
            useBoost()
        else :
            life -= 25
    if appetite <= 0 :
        if foodPacks < 0 :
            feed()
        else :
            life -= 25
    printed_life.set(life)
    printed_energy.set(energy)
    printed_appetite.set(appetite)

def window_main() :
    reset()
    window.config(background='#CCCCCC')

    # Mise a jour des labels et variables
    analyze_status()

    # Placement des widgets :
    """ligne 0"""
    bouton_quitter.grid(rowspan=2, column=3, sticky='nsew') # .grid place les widgets sur une grille...
    label_text_life.grid(row = 0, column=0, sticky='nsew') # ...elle meme calquee sur notre fenetre (index commence a 0)
    label_text_appetite.grid(row = 0, column=1, sticky='nsew') # sticky etend le widget afin d'utiliser toute la place...
    label_text_energy.grid(row = 0, column=2, sticky='nsew') # ...lui etant attribuee

    """ligne 1"""
    label_life.grid(row = 1, column=0, sticky='nsew')
    label_appetit.grid(row = 1, column=1, sticky='nsew') 
    label_energy.grid(row = 1, column=2, sticky='nsew') 

    """ligne 2"""
    button_boost.grid(row = 2, column=0, sticky='nsew')
    canvas_main_cat.grid(row = 2, column=1, rowspan=2, columnspan=2, sticky='nsew')
    bouton_inventory.grid(row = 2, column=3, sticky='nsew')

    """ligne 3"""
    bouton_manual.grid(row = 3, column=0, sticky='nsew')
    # canvas - col 1 #
    # canvas - col 2 #
    bouton_options.grid(row = 3, column=3, sticky='nsew')

    """ligne 4"""
    bouton_game.grid(row = 4, column=0, sticky='nsew')
    bouton_shop.grid(row = 4, column=1, sticky='nsew')
    bouton_feed.grid(row = 4, column=2, sticky='nsew')
    bouton_sleep.grid(row = 4, column=3, sticky='nsew')

def hunger(effort) :
    """Decroit 'appetite' aleatoirement selon l'effort fourni
    (depend des fenetres ouvertes/actions)"""
    global appetite, printed_appetite, life, printed_life

    # Choix aleatoire de la faim provoquee :
    hunger = rd.randint(5, effort)

    try : # gestion erreur d'argument
        hunger <= 5 
    except :
        hunger = 5
    
    # Verification 
    if appetite-hunger <= 0 : # si appetite va passer a 0 ou moins
        life -= 15
        printed_life.set(life)
        appetite = 10 
        printed_appetite.set(appetite)
    else : # Si bon, mise a jour de l'affichage :
        appetite -= hunger
        printed_appetite.set(appetite) # met a jour l'affichage

def fatigue(effort) :
    """Decroit 'fatigue' aleatoirement selon l'effort fourni
    (depend des fenetres ouvertes/actions)
    >> a l'instar de la fonction 'hunger'"""
    global energy, printed_energy, life, printed_life

    if energy <= 0 : 
        life -= 15
        printed_life.set(life)
        energy = 10 
        printed_energy.set(appetite)
    else :
        fatigue = rd.randint(5, effort)
        try :
            fatigue <= 5 
        except :
            fatigue = 5
        energy -= fatigue
        printed_energy.set(energy) # met a jour l'affichage
    

def manual(): 
    """Affiche un texte de tutoriel pour expliquer au joueur
    quoi faire"""
    reset()
    
    # Explication du jeu
    text_gameTutorial = """
                            How to play ?\n
- Inventory allows you to see your obejts (money, food, medicine and boosts) ;\n
- Sleep allows you to make your pet sleep and thus restore some of its energy (be careful, sleeping makes it hungry) ;\n
- Feed allows you to feed your pet (it will consume a pack of food) ;\n
- Shop allows you to buy various items ;\n
- Game launches a mini-game that allows you to earn virtual money to buy items ; \n
- Boost allows you to restore your cat's energy instantly (but it consumes a boost and some life) ;\n
When your pet does not have enough to eat, it will consume a packet of food by itself (if available).\n
Similarly, it will automatically consume a boost if its energy drops to 0 (if available).\n
Finally, if it's his life that reaches 0, then he will use a medicine to heal himself (partially).
However, if you don't have any more medicine, then it will be game over!
    """

    explication = tk.Label(window, text=text_gameTutorial)
    explication.grid(row=0, column=1, sticky='nsew')
    # Button exit
    button_exit_second = tk.Button(window, text="<=", height=2, width=2, 
                        relief=tk.RAISED, fg='black', font=('Calibri', 14), # style et taille police 
                        bg='#B03A2E', command=window_main)
    button_exit_second.grid(row=0, column=0, sticky='nsew')

def inventory() :
    reset()

    global printed_foodPacks, printed_money, printed_medicines, printed_boosts, printed_experience

    # Variables d'affichage : 
    printed_foodPacks.set(foodPacks) 
    printed_money.set(money) 
    printed_medicines.set(medicines) 
    printed_boosts.set(boosts)
    printed_experience.set(experience)

    # Dimensions et config :
    height_text_inventory, width_text_inventory = 1, 10
    colours_back_inventory = '#FFA500' # orange-mandarine
    colours_letters_inventory = 'white'
    colours_title_back_inventory = '#ff7f00'

    # Affichage en lui-meme :
    """Titre"""
    label_title_inventory = tk.Label(window, 
                        text="Inventory :", height=height_text_inventory, width=width_text_inventory, 
                        relief=tk.GROOVE, fg=colours_letters_inventory, font=('Calibri', 14), 
                        bg=colours_title_back_inventory)

    """Nom des objets"""
    label_money = tk.Label(window, 
                        text="Money", height=height_text_inventory, width=width_text_inventory, 
                        relief=tk.FLAT, fg=colours_letters_inventory, font=('Calibri', 14), 
                        bg=colours_back_inventory)
    label_foodPacks = tk.Label(window, 
                        text='Food packs', height=height_text_inventory, width=width_text_inventory, 
                        relief=tk.FLAT, fg=colours_letters_inventory, font=('Calibri', 14), 
                        bg=colours_back_inventory)
    label_medicines = tk.Label(window, 
                        text="Medicines", height=height_text_inventory, width=width_text_inventory, 
                        relief=tk.FLAT, fg=colours_letters_inventory, font=('Calibri', 14), 
                        bg=colours_back_inventory)
    label_boosts = tk.Label(window, 
                        text="Boosts", height=height_text_inventory, width=width_text_inventory, 
                        relief=tk.FLAT, fg=colours_letters_inventory, font=('Calibri', 14), 
                        bg=colours_back_inventory)
    label_experience = tk.Label(window, 
                        text='Experience', height=height_text_inventory, width=width_text_inventory, 
                        relief=tk.FLAT, fg=colours_letters_inventory, font=('Calibri', 14), 
                        bg=colours_back_inventory)

    """Nombre d'objets"""
    label_var_money = tk.Label(window, 
                        textvariable=printed_money, height=height_text_inventory, width=width_text_inventory, 
                        relief=tk.FLAT, fg=colours_letters_inventory, font=('Calibri', 14), 
                        bg=colours_back_inventory)
    label_var_foodPacks = tk.Label(window, 
                        textvariable=printed_foodPacks, height=height_text_inventory, width=width_text_inventory, 
                        relief=tk.FLAT, fg=colours_letters_inventory, font=('Calibri', 14), 
                        bg=colours_back_inventory)
    label_var_medicines = tk.Label(window, 
                        textvariable=printed_medicines, height=height_text_inventory, width=width_text_inventory, 
                        relief=tk.FLAT, fg=colours_letters_inventory, font=('Calibri', 14), 
                        bg=colours_back_inventory)
    label_var_boosts = tk.Label(window, 
                        textvariable=printed_boosts, height=height_text_inventory, width=width_text_inventory, 
                        relief=tk.FLAT, fg=colours_letters_inventory, font=('Calibri', 14), 
                        bg=colours_back_inventory)

    # Button exit
    button_exit_second = tk.Button(window, text="<=", height=height_text_inventory-1, width=width_text_inventory-1, 
                        relief=tk.RAISED, fg='black', font=('Calibri', 14), # style et taille police 
                        bg='#B03A2E', command=window_main)

    # Placement des widgets :
    """row 0"""
    label_title_inventory.grid(row=0, column=0, sticky='nsew')
    button_exit_second.grid(row=0, column=1, sticky='nsew')

    """row 1"""
    label_money.grid(row=1, column=0, sticky='nsew')
    label_var_money.grid(row=1, column=1, sticky='nsew')

    """row 2"""
    label_foodPacks.grid(row=2, column=0, sticky='nsew')
    label_var_foodPacks.grid(row=2, column=1, sticky='nsew')

    """row 3"""
    label_medicines.grid(row=3, column=0, sticky='nsew')
    label_var_medicines.grid(row=3, column=1, sticky='nsew')

    """row 4"""
    label_boosts.grid(row=4, column=0, sticky='nsew')
    label_var_boosts.grid(row=4, column=1, sticky='nsew')


def window_dead():
    """Affiche la fenetre de Game Over
    >> Lorsque la vie de l'animal atteint 0"""

    # Init
    reset()
    window.config(bg='#383E42')

    # Label titre 
    label_deadMessage = tk.Label(window, text="""  Game over\nYour cat is dead !""", height=3, width=15,
                        fg='black', font=('Verdana', 15, 'bold'), bg='white') 
       
    # Placement des widgets
    label_deadMessage.grid(row=0, sticky='nsew')

def shopping() :
    """Gere la fenetre de simulation d'achats/magasin"""

    global boosts, money, medicines, foodPacks
    global printed_boost, printed_foodPacks, printed_medicine, printed_money

    # couleur du background
    colory_bg = '#842e1b' # couleur fond et labels

    # Remplacement de la fenetre principal
    reset()
    window.config(bg=colory_bg)

    # Commandes boutons :
    def medicines_buy():
        global medicines, money, printed_medicines, printed_money
        nonlocal price_medecines
        if money >= price_medecines : # si assez d'argent
            medicines += 1
            money -= price_medecines
            # Mise a jour de la valeur
            printed_medicines.set(medicines)
            printed_money.set(money)

    def foodPacks_buy():
        global foodPacks, money, printed_foodPacks, printed_money
        nonlocal price_foodPacks
        if money >= price_foodPacks : # si assez d'argent
            foodPacks += 1
            money -= price_foodPacks
            # Mise a jour de la valeur
            printed_foodPacks.set(foodPacks)
            printed_money.set(money)

    def boosts_buy():
        global boosts, money, printed_boosts, printed_money
        nonlocal price_boosts
        if money >= price_boosts : # si assez d'argent
            boosts += 1
            money -= price_boosts
            # Mise a jour de la valeur
            printed_boosts.set(boosts)
            printed_money.set(money)

    # Gestions des variables :
    """Dimensions normées pour widgets du meme type identiques en taille""" 
    width_gen, height_gen = 5, 2

    """Objets possedes"""
    global money, foodPacks, medicines, boosts
    global printed_money, printed_foodPacks, printed_medicines, printed_boosts 

    """prix des objets"""
    price_foodPacks = 10
    price_medecines = 25
    price_boosts = 30

    # Labels :
    """portefeuille"""
    label_ownedMoney = tk.Label(window, text = "Wallet ($)", width=width_gen*2, height=height_gen, relief=tk.GROOVE,
                    fg='white', font=('Verdana', 13), bg=colory_bg)
    label_value_ownedMoney = tk.Label(window, textvariable= printed_money, width=width_gen, relief=tk.GROOVE,
                        height=height_gen, fg='white', font=('Verdana', 13), bg=colory_bg)

    """titre possede"""
    label_owned = tk.Label(window, text= 'Owned', height=height_gen, relief=tk.GROOVE,
                fg='white', font=('Verdana', 12), bg=colory_bg, justify='center')
   
    """noms d'objets"""
    label_medicines = tk.Label(window, text = "Medicines", width=width_gen*2, height=height_gen, relief=tk.GROOVE,
                    fg='white', font=('Verdana', 13), bg=colory_bg)
    label_foodPacks = tk.Label(window, text = "Food packs", width=width_gen*2, height=height_gen, relief=tk.GROOVE,
                    fg='white', font=('Verdana', 13), bg=colory_bg)
    label_boosts = tk.Label(window, text = "Boosts", width=width_gen*2, height=height_gen, relief=tk.GROOVE, 
                    fg='white', font=('Verdana', 13), bg=colory_bg)

    """prix d'objets"""
    label_price_medicines = tk.Label(window, text = str(price_medecines)+'$', width=width_gen, height=height_gen,
                    relief=tk.GROOVE, fg='white', font=('Verdana', 13), bg=colory_bg)
    label_price_foodPacks = tk.Label(window, text = str(price_foodPacks)+'$', width=width_gen, height=height_gen,
                    relief=tk.GROOVE, fg='white', font=('Verdana', 13), bg=colory_bg)
    label_price_boosts = tk.Label(window, text = str(price_boosts)+'$', width=width_gen, height=height_gen, 
                    relief=tk.GROOVE, fg='white', font=('Verdana', 13), bg=colory_bg)

    """possessions de l'utilisateur"""
    label_ownedMedecines = tk.Label(window, textvariable=str(printed_medicines), width=width_gen, height=height_gen, 
                    relief=tk.GROOVE, fg='white', font=('Verdana', 13), bg=colory_bg)
    label_ownedFoodPacks = tk.Label(window, textvariable=str(printed_foodPacks), width=width_gen, height=height_gen, 
                    relief=tk.GROOVE, fg='white', font=('Verdana', 13), bg=colory_bg)
    label_ownedBoosts = tk.Label(window, textvariable=str(printed_boosts), width=width_gen, height=height_gen, 
                    relief=tk.GROOVE, fg='white', font=('Verdana', 13), bg=colory_bg)
      
    # Boutons :
    button_medicines_buy = tk.Button(window, text="buy", height=height_gen, width=width_gen,
                            relief=tk.RAISED, fg='white', font=('Verdana', 14), bg='red', 
                            command=medicines_buy) 
    button_foodPacks_buy = tk.Button(window, text="buy", height=height_gen, width=width_gen,
                            relief=tk.RAISED, fg='white', font=('Verdana', 14), bg='red', 
                            command=foodPacks_buy) 
    button_boosts_buy = tk.Button(window, text="buy", height=height_gen, width=width_gen,
                            relief=tk.RAISED, fg='white', font=('Verdana', 14), bg='red', 
                            command=boosts_buy) 
    button_exit_second = tk.Button(window, text="<=", height=height_gen, width=width_gen, 
                    relief=tk.RAISED, fg='black', font=('Calibri', 14), # style et taille police 
                    bg='#B03A2E', command=window_main)

    # Placement des widgets :
    """row 0"""
    label_ownedMoney.grid(row=0, column=0, sticky='nsew')
    label_value_ownedMoney.grid(row=0, column=1, sticky='nsew')
    label_owned.grid(row=0, column=2, sticky='nsew')
    button_exit_second.grid(row=0, column=3, sticky='nsew')

    """row 1"""
    label_foodPacks.grid(row=1, column=0, sticky='nsew')
    label_price_foodPacks.grid(row=1, column=1, sticky='nsew')
    label_ownedFoodPacks.grid(row=1, column=2, sticky='nsew')
    button_foodPacks_buy.grid(row=1, column=3, sticky='nsew')
    
    """row 2"""
    label_medicines.grid(row=2, column=0, sticky='nsew')
    label_price_medicines.grid(row=2, column=1, sticky='nsew')
    label_ownedMedecines.grid(row=2, column=2, sticky='nsew')
    button_medicines_buy.grid(row=2, column=3, sticky='nsew')

    """row 3"""
    label_boosts.grid(row=3, column=0, sticky='nsew')
    label_price_boosts.grid(row=3, column=1, sticky='nsew')
    label_ownedBoosts.grid(row=3, column=2, sticky='nsew')
    button_boosts_buy.grid(row=3, column=3, sticky='nsew')

def sleeping():
    """Simule le sommeil de l'animal ;
    Met energy a 100 (pourcents), mais empeche les actions de l'utilisateur
    pendant 5 secondes"""
    
    # Init
    reset()
    window.config(bg='#383E42')

    def wake_up():
        """Enleve le canvas/image du chat dormant afin de remettre celui/celle 'classique'"""
        canvas_main_cat.grid_forget()
        window_main()

    # Label titre 
    label_sleepingMessage = tk.Label(window, width=16, height=2, text="Sleeping...",
                        fg='black', font=('Verdana', 13), bg='white') 
    
    # Canvas
    canvas_main_cat = tk.Canvas(window, width =height_width_canvas, height = height_width_canvas,
                    relief=tk.FLAT, bg='#383E42')
    image_recup = tk.PhotoImage(file='V_Pets_Sprites/cat_sleeping.png').zoom(8)
    canvas_main_cat.create_image(140, 130, image=image_recup) # lie l'image et le canvas (rectifie la position)
    window.image_recup = image_recup # préviens les pertes d'image

    # Button exit
    button_exit_second = tk.Button(window, text="<=", height=2, width=5, 
                        relief=tk.RAISED, fg='black', font=('Calibri', 14), # style et taille police 
                        bg='#B03A2E', command=window_main)
    
    # Placement des widgets
    label_sleepingMessage.grid(row=0, column=1, sticky='nsew')
    button_exit_second.grid(row=0, column=0, sticky='nsew')
    canvas_main_cat.grid(row = 1, column=0, columnspan=2, sticky='nsew')
    
    # Modification de variable
    global energy
    if energy > 70 and energy < 100 : # si va depasser 100 pourcent
        energy = 100
    elif energy < 100 :
        energy += 30
    printed_energy.set(energy)

    # Faim provoquee
    hunger(10)


def feeding():
    global foodPacks, appetite
    if appetite > 60 and appetite < 100 :
        foodPacks -= 1
        appetite = 100
    elif appetite < 100 :
        foodPacks -= 1
        appetite += 40
    printed_appetite.set(appetite) # mis a jour de l'affichage

def options_function(): 
    """Affiche le menu des options, permet ainsi de re-initialiser le jeu pour recommencer,
    ou bien de sauvegarder ses donnees
    
    [L'ajout d'une fonction de sauvegarde pourra etre ajouter en ecrivant, avec la librairie
    'os', les differentes variables de la fenetre principale lorsqu'on appuie sur le bouton
    'save' (dans option) ; puis en lisant et associant lesdites variables au lancement de l'app]"""

    reset()
   
    # Dimensions :
    height_optionsButtons, width_optionsButtons = 1, 15

    # Labels sections
    label_section_reset = tk.Label(window, text="Want to reset your saving-data?", height=1, bg='grey',
                        width=1, relief=tk.FLAT, fg='white', font=('Calibri', 8))

    # Button restart
    button_reInit = tk.Button(window, text="Reset your save ?", height=height_optionsButtons, 
                        width=width_optionsButtons, 
                        relief=tk.GROOVE, fg='white', font=('Calibri', 14), # style et taille police 
                        bg='#A107E9', command=ReInit)

    # Button exit
    button_exit_second = tk.Button(window, text="<=", height=height_optionsButtons, 
                        width=width_optionsButtons+1, 
                        relief=tk.RAISED, fg='white', font=('Calibri', 12), # style et taille police 
                        bg='#B03A2E', command=window_main)

    # Placement des widgets :
    button_exit_second.grid(row=0, sticky='nsew')
    label_section_reset.grid(row=1, sticky='ew')
    button_reInit.grid(row=2, sticky='nsew') 

def gaming():
    """Lance un minijeu de devinette (cf.texte dans le menu 'manual')
    
    >> le canvas et le label de la bande de verification sont et doivent etre initier des
    le depart, avant meme les fonctions secondaires, afin d'etre utilise a l'interieur de 
    ces derniere"""

    reset()
    window.config(bg='#CCCCCC')

    # Effort du round de lancement
    hunger(5)
    fatigue(10)

    # Variables 
    global money, printed_money

    possible_answers = {1:'left', 2:'right'} # 2 choix poss
    correct_answer = possible_answers[1] # just init

    # Init du canvas et de la bande de verification :
    canvas_main_cat = tk.Canvas(window, width =height_width_canvas, height = height_width_canvas,
                    relief=tk.FLAT, bg='#383E42')
    image_recup = tk.PhotoImage(file="V_Pets_Sprites/cat_stand.png").zoom(8)
    canvas_main_cat.create_image(140, 130, image=image_recup) # lie l'image et le canvas (rectifie la position)
    window.image_recup = image_recup # préviens les pertes d'image

    label_checkStrip = tk.Label(window, height=12, width=2, relief=tk.RAISED, bg='grey') # init en gris, change 
  
    def chooseCorrectAnswer() :
        """Choisi quelle reponse sera la bonne ce round-ci"""
        nonlocal possible_answers, correct_answer
        x = rd.randint(1, 2) # choisi entre 1 ou 2
        correct_answer = possible_answers[x] # met a 'left' ou 'right'

    def changeCanvas(whatAnswer):
        """Modifie l'image du canvas en fonction de la bonne reponse
        >> place apres la reponse de l'utilisateur"""
        nonlocal canvas_main_cat, possible_answers
        canvas_main_cat.delete() # supprime l'image
        if whatAnswer == possible_answers[2] : # si rep est 'right'
            image_recup = tk.PhotoImage(file="V_Pets_Sprites/cat_go_right.png").zoom(8)
            canvas_main_cat.create_image(140, 130, image=image_recup) # lie l'image et le canvas (rectifie la position)
            window.image_recup = image_recup # préviens les pertes d'image
        else :
            image_recup = tk.PhotoImage(file="V_Pets_Sprites/cat_go_left.png").zoom(8)
            canvas_main_cat.create_image(140, 130, image=image_recup) # lie l'image et le canvas (rectifie la position)
            window.image_recup = image_recup # préviens les pertes d'image

    def defaultMinigameCanvas() :
        # Init du canvas et de la bande de verification :
        image_recup = tk.PhotoImage(file="V_Pets_Sprites/cat_stand.png").zoom(8)
        canvas_main_cat.create_image(140, 130, image=image_recup) # lie l'image et le canvas (rectifie la position)
        window.image_recup = image_recup # préviens les pertes d'image

    def getResponseToLeft():
        """Initie la reponse du joueur a 'gauche'/'left'"""
        verifAnswer(possible_answers[1])

    def getResponseToRight():
        """Initie la reponse du joueur a 'droite'/'right'"""
        verifAnswer(possible_answers[2])

    def verifAnswer(user_answer):
        """Comparaison de la bonne rep et de la rep du joueur :
        Si sont les memes, alors bonne reponse / joueur a gagne ce round"""
        nonlocal correct_answer
        desactivateButton() # empeche changement de rep
        if correct_answer == user_answer :
            bonneReponse()
            coloringStripeGreen()
        else :
            coloringStripeRed()
        changeCanvas(correct_answer)

    def restart_minigame():
        """Relance un round"""
        defaultMinigameCanvas()
        label_checkStrip.configure(bg='grey')
        chooseCorrectAnswer()
        reActivateButton()

        # Effort 
        hunger(5)
        fatigue(10)

        # Gestion de la mort eventuelle
        analyze_status()

    def bonneReponse():
        """Incremente 10 a la valeur de money si le joueur a correctement repondu
        et met a jour l'affichage de la valeur"""
        global money, printed_money
        money += 15
        printed_money.set(money)

    def coloringStripeGreen():
        """Met en vert la bande de verification (label_checkStrip)
        >> si la reponse de l'utilisateur est correcte"""
        label_checkStrip.config(bg='green')

    def coloringStripeRed():
        """Met en rouge la bande de verification (label_checkStrip)
        >> si la reponse de l'utilisateur est fausse"""
        label_checkStrip.config(bg='red')

    def desactivateButton():
        """Enleve la commande des boutons, afin d'éviter que le joueur ne réponde 
        plusieurs fois / change sa reponse"""
        button_getResponseToLeft.config(text='X',command=None)
        button_getResponseToRight.config(text='X',command=None)

    def reActivateButton():
        """Re-active / Re-implante les fonctionnalités/commandes des boutons, afin
        que le joueur puisse a nouveau jouer/donner des reponses"""
        button_getResponseToLeft.configure(text='Left', command=getResponseToLeft)
        button_getResponseToRight.configure(text='Right', command=getResponseToRight)

    def showMinigameTutorial():
        """Affiche un texte expliquant comment jouer au mini-jeu"""

        reset() 
        window.config(bg='#CCCCCC')

        color_minigameTutorial = '#56554F' 

        # Textes d'explication
        text_howToPlay = """
Guess in which direction the cat will go and press the associated button.\n
If you thought the same as the animal, you win 15 virtual dollars!
Press the 'restart' button to start a new round.\n\n
PS: The bar to the right of your virtual pet will turn green 
if your answer was right, and red if not.
    """

        # Labels
        label_minigame_howToPlay = tk.Label(window, text=text_howToPlay, relief=tk.FLAT,
                                fg=color_minigameTutorial, anchor='w', font=('Verdana', 8), bg='white')

        # Button exit
        button_closeTutorial = tk.Button(window, text="<=", height=1,  
                        relief=tk.RAISED, fg='white', font=('Verdana', 13),  
                        bg='#B03A2E', command=gaming) 
        
        # Placement des widgets
        button_closeTutorial.grid(row=0, sticky='nsew')
        label_minigame_howToPlay.grid(row=1, sticky='nsew') 

    # Creation des widgets 
    button_exit_second = tk.Button(window, text="<=", height=height_gen, width=width_gen, 
                        relief=tk.RAISED, fg='white', font=('Calibri', 14),  
                        bg='#B03A2E', command=window_main)
    button_requestTutorial = tk.Button(window, text="?", height=height_gen, width=width_gen, 
                        relief=tk.RAISED, fg='white', font=('Calibri', 14),  
                        bg='orange', command=showMinigameTutorial) 
    button_getResponseToRight = tk.Button(window, text="Left", height=height_gen, width=width_gen, 
                        relief=tk.RAISED, fg='white', font=('Calibri', 14, 'italic'),  
                        bg='blue', command=getResponseToRight)
    button_getResponseToLeft = tk.Button(window, text="Right", height=height_gen, width=width_gen, 
                        relief=tk.RAISED, fg='white', font=('Calibri', 14, 'italic'),  
                        bg='blue', command=getResponseToLeft)
    button_restart_minigame = tk.Button(window, text="Restart", height=height_gen, width=width_gen, 
                        relief=tk.RAISED, fg='white', font=('Calibri', 14, 'italic'),  
                        bg='red', command=restart_minigame)

    label_showMoney = tk.Label(window, textvariable=printed_money, height=height_gen, width=width_gen,
                    relief=tk.RAISED, fg='white', font=('Verdana', 14), bg='yellow')

    # Placement des widgets :
    button_exit_second.grid(row=0, column=0, sticky='nsew')
    label_showMoney.grid(row=0, column=1, sticky='nsew')
    button_requestTutorial.grid(row=0, column=2, sticky='nsew')

    canvas_main_cat.grid(row=1, column=0, columnspan=2, sticky='nsew')
    # canvas cat #
    label_checkStrip.grid(row=1, column=2, sticky='ns') # largeur non prise en compte (deforme sinon)

    button_getResponseToLeft.grid(row=2, column=0, sticky='nsew')
    button_getResponseToRight.grid(row=2, column=1, sticky='nsew')
    button_restart_minigame.grid(row=2, column=2, sticky='nsew')    

def useBoost():
    """Remet l'ernergie du chat au maximum (100) et consomme un boost, 
    mais aussi un peu de vie"""
    global boosts, energy, printed_energy, life, printed_life
    if energy < 100 and boosts > 0 :
        boosts -= 1
        energy = 100
        printed_energy.set(energy)
        # Perte de vie 
        life -= 5
        printed_life.set(life)

# Labels :
"""simple texte"""
text_width_rectification = 1 # par rapport au widget de valeur correspondant

label_text_life = tk.Label(window, 
                text = "Life :",
                height=height_label, # hauteur
                width=width_label+text_width_rectification, # largeur
                relief=tk.FLAT, # style du cadre
                padx=space_rectification,
                pady=space_rectification,
                fg='white', # couleur texte
                font=('Verdana', 13), # style et taille police 
                bg='#1A5276' # couleur fond
                )
label_text_appetite = tk.Label(window, 
                text = "Appetite :",
                height=height_label, # hauteur
                width=width_label+text_width_rectification, # largeur
                relief=tk.FLAT, # style du cadre
                padx=space_rectification,
                pady=space_rectification,
                fg='white', # couleur texte
                font=('Verdana', 13), # style et taille police 
                bg='#1A5276' # couleur fond
                )
label_text_energy = tk.Label(window, 
                text = "Energy :",
                height=height_label, # hauteur
                width=width_label+text_width_rectification, # largeur
                relief=tk.FLAT, # style du cadre
                padx=space_rectification,
                pady=space_rectification,
                fg='white', # couleur texte
                font=('Verdana', 13), # style et taille police 
                bg='#1A5276' # couleur fond
                )

"""Affichage des valeurs en elle-meme"""
label_life = tk.Label(window, 
                        textvariable = printed_life,
                        height=height_label, # hauteur
                        width=width_label, # largeur
                        relief=tk.RIDGE, # style du cadre
                        padx=space_rectification,
                        pady=space_rectification, 
                        fg='white', # couleur texte
                        font=('Verdana', 14), # style et taille police 
                        bg='#16A085' # couleur fond
                        )
label_appetit = tk.Label(window, 
                        textvariable=printed_appetite,
                        height=height_label,
                        width=width_label, 
                        relief=tk.RIDGE,
                        padx=space_rectification,
                        pady=space_rectification,
                        fg='white',
                        font=('Verdana', 14),  
                        bg='#16A085'
                        )
label_energy = tk.Label(window, 
                        textvariable=printed_energy,
                        height=height_label,
                        width=width_label, 
                        relief=tk.RIDGE,
                        padx=space_rectification,
                        pady=space_rectification,
                        fg='white',
                        font=('Verdana', 14),  
                        bg='#16A085')

# Boutons 
"""Quitter"""
bouton_quitter = tk.Button(window,
                        text="X",
                        height=height_exit,
                        width=width_exit, 
                        relief=tk.GROOVE, # style du cadre
                        padx=space_rectification,
                        pady=space_rectification,
                        fg='black', # couleur texte
                        font=('Verdana', 14), # style et taille police 
                        bg='#B03A2E', # couleur fond
                        command=window.destroy) # quelle action ? ici = fermer fenetre

"""options"""
bouton_options = tk.Button(window,
                        text="Options",
                        height=height_gen,
                        width=width_gen,
                        relief=tk.GROOVE, 
                        padx=space_rectification,
                        pady=space_rectification,
                        fg='white', 
                        font=('Verdana', 14), 
                        bg='grey', 
                        command=options_function) 

"""manual"""
bouton_manual = tk.Button(window,
                        text="Manual",
                        height=height_gen,
                        width=width_gen,
                        relief=tk.GROOVE, 
                        padx=space_rectification,
                        pady=space_rectification,
                        fg='white', 
                        font=('Verdana', 14), 
                        bg='grey', 
                        command=manual) 

"""inventory"""
bouton_inventory = tk.Button(window,
                        text="Inventory",
                        height=height_gen,
                        width=width_gen,
                        relief=tk.GROOVE, # style du cadre
                        padx=space_rectification,
                        pady=space_rectification,
                        fg='white', # couleur texte
                        font=('Verdana', 14), # style et taille police 
                        bg='#F27207', # couleur fond
                        command=inventory) 

button_boost = tk.Button(window,
                        text="Boost",
                        height=height_gen,
                        width=width_gen,
                        relief=tk.GROOVE, 
                        padx=space_rectification,
                        pady=space_rectification,
                        fg='white', 
                        font=('Verdana', 14), 
                        bg='#A107E9', 
                        command=useBoost) 

"""En bas du display principal"""
bouton_game = tk.Button(window,
                        text="Game",
                        height=height_gen,
                        width=width_gen,
                        relief=tk.GROOVE, 
                        padx=space_rectification,
                        pady=space_rectification,
                        fg='white', 
                        font=('Verdana', 14), 
                        bg='#196F3D', 
                        command=gaming) 

"""shop"""
bouton_shop = tk.Button(window,
                        text="Shop",
                        height=height_gen,
                        width=width_gen,
                        relief=tk.GROOVE, 
                        padx=space_rectification,
                        pady=space_rectification,
                        fg='white', 
                        font=('Verdana', 14), 
                        bg='#196F3D', 
                        command=shopping) 

"""feed"""
bouton_feed = tk.Button(window,
                        text="Feed",
                        height=height_gen,
                        width=width_gen,
                        relief=tk.GROOVE, 
                        padx=space_rectification,
                        pady=space_rectification,
                        fg='white', 
                        font=('Verdana', 14), 
                        bg='#196F3D', 
                        command=feeding) 

"""sleep"""
bouton_sleep = tk.Button(window,
                        text="Sleep",
                        height=height_gen,
                        width=width_gen,
                        relief=tk.GROOVE, 
                        padx=space_rectification,
                        pady=space_rectification,
                        fg='white', 
                        font=('Verdana', 14), 
                        bg='#196F3D', 
                        command=sleeping) #sleeping 

# Canvas :
"""Creation du canvas en lui-meme"""
canvas_main_cat = tk.Canvas(window, width = height_width_canvas, height = height_width_canvas, 
                bg='#CCCCCC') # meme couleur que fond -> effet transparence
"""Recuperation et ajout de l'image"""
image_recup = tk.PhotoImage(file='V_Pets_Sprites/cat_look_left.png').zoom(10)
canvas_main_cat.create_image(140, 130, image=image_recup) # lie l'image et le canvas (rectifie la position)
window.image_recup = image_recup

## Loop ##
window_main()
window.mainloop() # Permet l'affichage constant et la mise à jour de la fenetre