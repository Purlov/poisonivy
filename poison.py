"""We show here how to generate and binds a shadow to an element."""

GAME_FPS = 144
LICENSES = "David E. Gervais drawn tiles library has many of these tiles the game is using, like the man in the main menu\nIt is published under CC BY 3.0\nhttp://pousse.rapiere.free.fr/tome/tome-tiles.htm" # update from LICENSES.txt

import pygame, thorpy as tp
from functools import partial
from os import path, mkdir
import random
import pickle

random.seed()

pygame.init()

x,y = pygame.display.get_desktop_sizes()[0]
screen_width, screen_height = x*0.89, y*0.89
screen = pygame.display.set_mode((screen_width, screen_height))
tp.init(screen, tp.theme_game1)

pygame.display.set_caption("Poison Ivy")
icon = pygame.image.load("gfx/ivyleaf.png")
pygame.display.set_icon(icon)

'''text = tp.Text("Here we use a dummy, Paint-generated\nimage for demonstration. "+\
                   "Try to move the elements below.")
text.set_max_text_width(400)

#Pure image element(no text)
my_img = pygame.image.load(tp.fn("data/my_img.png"))
my_img.set_colorkey(my_img.get_at((0,0)))

cloud1 = tp.Image(my_img)
cloud1.set_draggable(True, True)
cloud1.generate_shadow(fast=False) #automatic shadow generated from the exact shape of the content'''

s = tp.shadows.Shadow()
s.sun_angle = 30
s.shadow_radius = 10
s.alpha_factor = 0.8
s.decay_mode = "exponential" #or quadratic
s.angle_mode = "flip"
s.mode_value = (False, True) #y-flip only
# s.angle_mode = "rotate"
# s.mode_value = 30
s.offset = (10,10) #offset from the children
s.vertical = True
'''cloud2 = tp.Image(my_img)
cloud2.set_draggable(True, True)
cloud2.generate_shadow(shadowgen=s)

s.shadow_radius = 2
s.mode_value = (False, False)
some_text = tp.Text("Hello, world")
some_text.generate_shadow(shadowgen=s)
some_text.set_draggable(True, True)


box = tp.TitleBox("Some demo box", [tp.Text("In this case, fast=True\nmay be well suited.")])
box.set_draggable(True, True)
box.generate_shadow(fast=True)'''

if not path.exists("save"):
    mkdir("save")

save_names = []
if path.exists("save/save_names"):
    with open("save/save_names", "rb") as file:
        save_names = pickle.load(file)
else:
    for i in range(15):
        save_names.append("--- Empty Save Slot Number "+str(i)+" ---")
    with open("save/save_names", "wb") as file:
        pickle.dump(save_names, file)

logo = pygame.image.load("gfx/logo.png")
logo_width, logo_height = logo.get_size()

icon_main_scaled = pygame.transform.scale(icon, (150, 150))
icon_main_width, icon_main_height = 150, 150

golden_chest = pygame.image.load("gfx/golden_chest.png")
golden_chest_main_scaled = pygame.transform.scale(golden_chest, (55, 55))
golden_chest_main_width, golden_chest_main_height = 55, 55

dark_elf = pygame.image.load("gfx/dark_elf.png")
dark_elf_main_scaled = pygame.transform.scale(dark_elf, (55, 55))
dark_elf_main_width, dark_elf_main_height = 55, 55

normal_font = pygame.font.Font(None, 32)

gladiator_text = normal_font.render("THE Gladiator", True, pygame.Color(0, 0, 0, a=140), None)
gladiator_text_width, gladiator_text_height = gladiator_text.get_size()

saving_text = normal_font.render("Saving the Game", True, pygame.Color(255, 165, 0, a=140), None)
saving_text_w, saving_text_h = saving_text.get_size()

loading_text = normal_font.render("Loading the Game", True, pygame.Color(255, 165, 0, a=140), None)
loading_text_w, loading_text_h = loading_text.get_size()

options_text = normal_font.render("Options", True, pygame.Color(255, 165, 0, a=140), None)
options_text_w, options_text_h = options_text.get_size()

def change_window(name):
    global updater
    global leaf 
    leaf = name
    if leaf == "main_menu":
        main_menu_objects = []
        main_menu_objects.append(tp.Button("Continue Game"))
        main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
        main_menu_objects.append(tp.Button("New Game"))
        main_menu_objects[len(main_menu_objects)-1].at_unclick=partial(change_window, "save_game")
        main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
        main_menu_objects.append(tp.Button("Save Game"))
        main_menu_objects[len(main_menu_objects)-1].at_unclick=partial(change_window, "save_game")
        main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
        main_menu_objects.append(tp.Button("Load Game"))
        main_menu_objects[len(main_menu_objects)-1].at_unclick=partial(change_window, "load_game")
        main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
        main_menu_objects.append(tp.Button("Options & Credits"))
        main_menu_objects[len(main_menu_objects)-1].at_unclick=partial(change_window, "options")
        main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
        main_menu_objects.append(tp.Button("Exit"))
        main_menu_objects[len(main_menu_objects)-1].at_unclick=exit
        main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)

        main_group = tp.TitleBox("Poison Ivy Options", main_menu_objects)
        # main_group.set_size((500,500))
        main_group.sort_children(gap=20)
        main_group.center_on(screen)
    elif leaf == "save_game":
        save_group_left = []
        save_group_center = []
        save_group_right = []
        for i in range(15):
            if i < 5:
                save_group_left.append(tp.Button(save_names[i]))
                save_group_left[len(save_group_left)-1].at_unclick=partial(save_game, i)
            elif i < 10:
                save_group_center.append(tp.Button(save_names[i]))
                save_group_center[len(save_group_center)-1].at_unclick=partial(save_game, i)
            elif i < 15:
                save_group_right.append(tp.Button(save_names[i]))
                save_group_right[len(save_group_right)-1].at_unclick=partial(save_game, i)
        save_group_left_box = tp.Group(save_group_left, "v")
        save_group_center_box = tp.Group(save_group_center, "v")
        save_group_right_box = tp.Group(save_group_right, "v")
        save_back_to_menu_button = tp.Button("Back to Main Menu")
        save_back_to_menu_button.at_unclick=partial(change_window, "main_menu")
        save_back_to_menu_button.generate_shadow(fast=True)
        last_horizontal = tp.Group([save_group_left_box, save_group_center_box, save_group_right_box], "h")
        save_all = tp.Group([last_horizontal, save_back_to_menu_button], "v")

        main_group = tp.Group([save_all], "h")
        main_group.sort_children(gap=20)
        main_group.center_on(screen)
    elif leaf == "load_game":
        save_group_left = []
        save_group_center = []
        save_group_right = []
        for i in range(15):
            if i < 5:
                save_group_left.append(tp.Button(save_names[i]))
                save_group_left[len(save_group_left)-1].at_unclick=partial(load_game, i)
            elif i < 10:
                save_group_center.append(tp.Button(save_names[i]))
                save_group_center[len(save_group_center)-1].at_unclick=partial(load_game, i)
            elif i < 15:
                save_group_right.append(tp.Button(save_names[i]))
                save_group_right[len(save_group_right)-1].at_unclick=partial(load_game, i)
        save_group_left_box = tp.Group(save_group_left, "v")
        save_group_center_box = tp.Group(save_group_center, "v")
        save_group_right_box = tp.Group(save_group_right, "v")
        save_back_to_menu_button = tp.Button("Back to Main Menu")
        save_back_to_menu_button.at_unclick=partial(change_window, "main_menu")
        save_back_to_menu_button.generate_shadow(fast=True)
        last_horizontal = tp.Group([save_group_left_box, save_group_center_box, save_group_right_box], "h")
        save_all = tp.Group([last_horizontal, save_back_to_menu_button], "v")

        main_group = tp.Group([save_all], "h")
        main_group.sort_children(gap=20)
        main_group.center_on(screen)
    elif leaf == "options":
        save_back_to_menu_button = tp.Button("Back to Main Menu")
        save_back_to_menu_button.at_unclick=partial(change_window, "main_menu")
        save_back_to_menu_button.generate_shadow(fast=True)
        last_horizontal = tp.Group([], "h")
        save_all = tp.Group([last_horizontal, save_back_to_menu_button], "v")

        main_group = tp.Group([save_all], "h")
        main_group.sort_children(gap=20)
        main_group.center_on(screen)
        
    updater = main_group.get_updater()

Save = {
    "identifier": random.randint(1111,8888)
}

def save_game(number):
    global Save # wat up
    prompt = tp.TextInput("", "Enter Save Name")
    alert = tp.AlertWithChoices("Saving Game", ("Yes", "No"), text="Do you wish to save into this slot?\nOld save is formatted.", children=[prompt])
    alert.generate_shadow(fast=False) 
    alert.launch_alone(click_outside_cancel=False) # it would accidentally click other buttons
    if alert.choice == "Yes":
        save_names[number] = prompt.get_value()
        print("Saving to slot "+str(number)+" with the slot name "+prompt.get_value())
        with open("save/save_names", "wb") as file:
            pickle.dump(save_names, file)
        with open("save/save"+str(number), "wb") as file:
            pickle.dump(Save, file)
        change_window("save_game")

def load_game(number):
    global Save
    alert = tp.AlertWithChoices("Loading Game", ("Yes", "No"), text="Do you wish to load this slot?\nUnsaved progress is lost.")
    alert.generate_shadow(fast=False) 
    alert.launch_alone(click_outside_cancel=False) # it would accidentally click other buttons
    if alert.choice == "Yes":
        print("Loading from slot "+str(number))
        if path.exists("save/save"+str(number)):
            with open("save/save"+str(number), "rb") as file:
                Save = pickle.load(file)

change_window("main_menu")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((150,150,150)) # Clear screen

    fps_text = normal_font.render("FPS = "+str(round(clock.get_fps()))+" MIN_TARGET = "+str(GAME_FPS), True, pygame.Color(255, 165, 0, a=140), None)
    screen.blit(fps_text,(10,10))
    debug_text = normal_font.render("Save identifier="+str(Save["identifier"]), True, pygame.Color(255, 165, 0, a=140), None)
    debug_text_w, debug_text_h = loading_text.get_size()
    screen.blit(debug_text,(10,screen_height-10-debug_text_h))

    if leaf == "main_menu" or leaf =="save_game" or leaf=="load_game" or leaf == "options":
        screen.blit(logo, (screen_width/2-logo_width/2, screen_height*0.085))
        screen.blit(icon_main_scaled, (screen_width/2-logo_width/2-icon_main_width-25, screen_height*0.085))
        screen.blit(golden_chest_main_scaled, (screen_width-golden_chest_main_width-10, screen_height-golden_chest_main_height-10))
        screen.blit(dark_elf_main_scaled, (screen_width-golden_chest_main_width-dark_elf_main_width-10-10, screen_height-dark_elf_main_height-10))
        screen.blit(gladiator_text, (screen_width-gladiator_text_width-10, screen_height-dark_elf_main_height-10-gladiator_text_height))

    if leaf == "main_menu":
        a = 1
    elif leaf == "save_game":
        screen.blit(saving_text, (screen_width/2-saving_text_w/2,0.3*screen_height))
    elif leaf == "load_game":
        screen.blit(loading_text, (screen_width/2-loading_text_w/2,0.3*screen_height))
    elif leaf == "options":
        screen.blit(options_text, (screen_width/2-options_text_w/2,0.3*screen_height))
        
    updater.update(events=pygame.event.get(), mouse_rel=pygame.mouse.get_rel())

    pygame.display.flip() # Update display

    clock.tick(GAME_FPS)

pygame.quit()