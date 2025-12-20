"""We show here how to generate and binds a shadow to an element."""

GAME_FPS = 200
LICENSES = 'David E. Gervais drawn tiles library has many of these tiles the game is using, like the man in the main menu\nIt is published under CC BY 3.0\nhttp://pousse.rapiere.free.fr/tome/tome-tiles.htm\n\n\nThorpy GUI library\n\nMIT License\n\nCopyright (c) 2023 Yann Thorimbert\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n\n\nObsidian Serpent Star Sign image\nBy basxto and yolkati\nCC BY-SA 4.0\nhttps://opengameart.org/content/giant-snake'
TEAM_NUMBER = 7
MEMBER_NUMBER = 6

import pygame, thorpy as tp
from functools import partial
from os import path, mkdir
import random
import pickle
import lzma
import math

random.seed()

pygame.init()

pygame.display.set_caption("Jungle Hermit")
icon = pygame.image.load("gfx/ivyleaf.png")
pygame.display.set_icon(icon)

x,y = pygame.display.get_desktop_sizes()[0]
print("Screen resolution "+str(x)+" x "+str(y))
screen_width, screen_height = 1366,768 #x*0.89, y*0.89
print("Window resolution "+str(1366)+" x "+str(768))
if x <= 1366:
    print("\033[31mScreen size smaller or equal than window size!\033[0m")
screen = pygame.display.set_mode((screen_width, screen_height))
tp.init(screen, tp.theme_game1)

tp.set_default_font(("arial"), 24)

gone_full_screen = False
def go_full_screen():
    global screen, gone_full_screen
    if gone_full_screen == False:
        screen = pygame.display.set_mode((1366,768), pygame.NOFRAME + pygame.FULLSCREEN, 32, vsync=1)
        gone_full_screen = True
    else:
        screen = pygame.display.set_mode((1366,768), pygame.RESIZABLE, 32, vsync=1)
        gone_full_screen = False

'''def go_full_screen3():
    global screen, gone_full_screen
    if gone_full_screen == False:
        screen = pygame.display.set_mode((1366,768), pygame.SCALED | pygame.FULLSCREEN)
        gone_full_screen = True
    else:
        screen = pygame.display.set_mode((1366,768))
        gone_full_screen = False'''

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
        decompressed = lzma.decompress(file.read())
        save_names = pickle.loads(decompressed)
else:
    for i in range(15):
        save_names.append("--- Empty Save Slot Number "+str(i)+" ---")
    with open("save/save_names", "wb") as file:
        pickled = pickle.dumps(save_names)
        compressed = lzma.compress(pickled)
        file.write(compressed)

logo = pygame.image.load("gfx/logo.png").convert_alpha() 
logo_width, logo_height = logo.get_size()

bg_tile = pygame.image.load("gfx/bg_tile.png").convert()
bg_tile_width, bg_tile_height = bg_tile.get_size()

new_game_logo = pygame.image.load("gfx/new_game_logo.png").convert_alpha() 
new_game_logo_width, new_game_logo_height = new_game_logo.get_size()
new_game_logo_processed = new_game_logo

icon_main_scaled = pygame.transform.scale(icon, (150, 150)).convert_alpha() 
icon_main_width, icon_main_height = 150, 150

golden_chest = pygame.image.load("gfx/golden_chest.png").convert_alpha() 
golden_chest_main_scaled = pygame.transform.scale(golden_chest, (55, 55))
golden_chest_main_width, golden_chest_main_height = 55, 55

dark_elf = pygame.image.load("gfx/dark_elf.png").convert_alpha() 
dark_elf_main_scaled = pygame.transform.scale(dark_elf, (55, 55))
dark_elf_main_width, dark_elf_main_height = 55, 55

star_sign_logo = pygame.image.load("gfx/star_sign.png").convert_alpha() 
star_sign_logo_processed = star_sign_logo
star_sign_icon = pygame.image.load("gfx/star.png").convert_alpha() 
w,h = star_sign_icon.get_size()
star_sign_icon_rect = star_sign_icon.get_rect(center=(w/2, h/2))
star_sign_icon_processed = star_sign_icon
star_sign_icon_processed_rect = pygame.Rect(0, 0, 0, 0)

normal_font = pygame.font.Font(None, 32)

#gladiator_text = normal_font.render("THE Gladiator", True, pygame.Color(0, 0, 0, a=140), None)
#gladiator_text_width, gladiator_text_height = gladiator_text.get_size()

saving_text = normal_font.render("Saving the Game", True, pygame.Color(255, 165, 0, a=140), None)
saving_text_w, saving_text_h = saving_text.get_size()

loading_text = normal_font.render("Loading the Game", True, pygame.Color(255, 165, 0, a=140), None)
loading_text_w, loading_text_h = loading_text.get_size()

def exit_game():
    global running
    alert = tp.AlertWithChoices("Exiting", ("Yes", "No"), text="Do you wish to quit the program?\nAll unsaved progress will be lost.")
    alert.generate_shadow(fast=False) 
    alert.launch_alone(click_outside_cancel=False) # it would accidentally click other buttons
    if alert.choice == "Yes":
            running = False

Save = {
    "identifier": random.randint(1111,8888),
    "character_name": "",
    "character_type": "taurian",
    "npc": [[]]
}

went_through_lobby = False
def change_window(name):
    global went_through_lobby
    global updater
    global leaf 
    leaf = name

    if leaf == "new_game":
        alert = tp.AlertWithChoices("Starting New Game", ("Yes", "No"), text="Do you wish to start a new game?\nAll old unsaved progress will be lost.")
        alert.generate_shadow(fast=False) 
        alert.launch_alone(click_outside_cancel=False) # it would accidentally click other buttons
        if alert.choice == "No":
            leaf = "main_menu"
    elif leaf == "continue":
        if went_through_lobby == False and loaded_game == False:
            leaf = "main_menu"
        
    if leaf == "main_menu":
        main_menu_padding = tp.Text("\n"*5)

        main_menu_objects = []
        main_menu_objects.append(tp.Button("Continue Game"))
        main_menu_objects[len(main_menu_objects)-1].at_unclick=partial(change_window, "continue")
        main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
        main_menu_objects.append(tp.Button("New Game"))
        main_menu_objects[len(main_menu_objects)-1].at_unclick=partial(change_window, "new_game")
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
        main_menu_objects.append(tp.Button("Toggle Screen"))
        main_menu_objects[len(main_menu_objects)-1].at_unclick=go_full_screen
        main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
        main_menu_objects.append(tp.Button("Debug Window"))
        main_menu_objects[len(main_menu_objects)-1].at_unclick=partial(change_window, "debug")
        main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
        main_menu_objects.append(tp.Button("Exit"))
        main_menu_objects[len(main_menu_objects)-1].at_unclick=exit_game
        main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
        
        main_title = tp.TitleBox("Jungle Hermit Options", main_menu_objects)
        main_title.sort_children(gap=10)
        main_group = tp.Group((main_menu_padding,main_title),"v")
        # main_group.set_size((500,500))
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

        #global licenses_area
        global licenses_area#, licenses_box
        licenses_area = tp.Text(LICENSES, max_width=950, font_color=(250,250,250))
        licenses_area.set_font_name("verdana")
        licenses_area.set_font_size(18)
        #licenses_box = tp.Box([licenses_area], size_limit=(1000,600))
        #licenses_box.at_drag = splice_license

        #empty_area = tp.OutlinedText("\n", font_size=32, max_width=100, font_color=(250,250,250), outline_color=(50,50,50), outline_thickness=2)
       # empty_box = tp.Box([empty_area], scrollbar_if_needed= True, size_limit=(300,100))

        padder = tp.Text("\n"*4, font_size=24)

        options_up = tp.Button("Move up")
        options_up.at_unclick=partial(move_options_text, "up")
        options_up.generate_shadow(fast=True)

        options_down = tp.Button("Move down")
        options_down.at_unclick=partial(move_options_text, "down")
        options_down.generate_shadow(fast=True)

        last_horizontals1 = tp.Group([licenses_area], "h")
        last_horizontals2 = tp.Group([options_up, save_back_to_menu_button, options_down], "h")
        save_all = tp.Group([last_horizontals1, padder, last_horizontals2], "v")

        main_group = tp.Group([save_all], "h")
        main_group.sort_children(gap=20)
        main_group.center_on(screen)

        move_options_text("refresh")
    elif leaf == "new_game":
        global new_type_toggle, new_game_monster_description, new_game_name, new_game_color_picker, Save, npc_types, saved_rgb
        
        new_type_toggle = tp.TogglablesPool("Character Types", ("Taurian", "Dark Elf", "Skeleton", "Cyclops"), Save["character_type"].title())
        #new_type_toggle.at_unclick=change_character_type #commented since it is watched in the main loop

        save_back_to_menu_button = tp.Button("Back to Main Menu")
        save_back_to_menu_button.at_unclick=partial(change_window, "main_menu")
        save_back_to_menu_button.generate_shadow(fast=True)

        choose_star_sign_button = tp.Button("Choose Star Sign")
        choose_star_sign_button.at_unclick=partial(change_window, "star_sign")
        choose_star_sign_button.generate_shadow(fast=True)

        bottom_buttons = tp.Group([choose_star_sign_button, save_back_to_menu_button], "h")

        new_game_name = tp.TextInput(Save["character_name"], placeholder="Can be changed later")
        new_game_name.at_cancel=save_written_name
        new_game_name_descr = tp.Text("Character Name")
        new_game_namers = tp.Group([new_game_name_descr, new_game_name], "h")
        #padder = tp.Text("\n"*10, font_size=24)
        padder1 = tp.Text((" "*35+"\n")*11, font_size=24)
        new_game_monster_description = tp.Text(Types["monster"][Save["character_type"]]["description"], max_width=400)

        #change_character_type()

        colors = []

        # Step size reduced to 20 → double the colors
        step = 20  

        # Red → Yellow (R fixed at 255, G increases)
        for g in range(0, 201, step):
            colors.append((255, g, 0))

        # Yellow → Green (G fixed at 255, R decreases)
        for r in range(200, -1, -step):
            colors.append((r, 255, 0))

        # Green → Cyan (G fixed at 255, B increases)
        for b in range(0, 201, step):
            colors.append((0, 255, b))

        # Cyan → Blue (B fixed at 255, G decreases)
        for g in range(200, -1, -step):
            colors.append((0, g, 255))

        # Blue → Magenta (B fixed at 255, R increases)
        for r in range(0, 201, step):
            colors.append((r, 0, 255))

        # Magenta → Red (R fixed at 255, B decreases)
        for b in range(200, -1, -step):
            colors.append((255, 0, b))

        # Shuffle into random order
        random.shuffle(colors)

        # Shuffle into random order
        random.shuffle(colors)

        new_game_color_picker = tp.ColorPickerPredefined(
            colors=colors
        )
        #new_game_color_picker.at_cancel=partial(color_tiles, 0) #watched in main loop
        ##new_game_color_picker.set_value(old_char_color)

        image_and_text = tp.Group([new_game_color_picker,padder1,new_game_monster_description], "h")
        
        padder2 = tp.Text("\n"*2, font_size=24)
        save_all = tp.Group([padder2,new_type_toggle,image_and_text,new_game_namers,bottom_buttons], "v")

        main_group = tp.Group([save_all], "h")
        main_group.sort_children(gap=20)
        main_group.center_on(screen)

        all_types = list(Types["monster"].keys())
        npc_types = []
        npc_names = []
        saved_rgb = []
        for i in range(1): #TEAM_NUMBER*MEMBER_NUMBER
            npc_types.append(all_types[random.randrange(0,len(all_types))])
            color_tiles(i)
            npc_names.append(name_generator())
        npc_types[0] = Save["character_type"]
        color_tiles(-1)
        if Save["character_name"] != "":
            npc_names[0] = Save["character_name"]

        Save["npc"] = []
        Save["npc"].append(npc_types)
        Save["npc"].append(processed_images)
        Save["npc"].append(npc_names)

        #Save["npc"][0][0] #first npc_type
        #Save["npc"][1][TEAMS*MEMBERS][2] #last_npc_images_2biggest
        #Save["npc"][2][0] #first npc name, yours
        #Save["npc"][3][0] #first npc star sign, yours. populated later at star_sign leaf

        '''for i in range(len(npc_types)):
            print(npc_types[i])
            print(npc_names[i])'''

    elif leaf == "star_sign":
        all_types = list(Types["star sign"].keys())
        npc_star_signs = []
        for i in range(1): #TEAM_NUMBER*MEMBER_NUMBER
            npc_star_signs.append(all_types[random.randrange(0,len(all_types))])
        Save["npc"].append(npc_star_signs)

        image_padding = tp.Text(" "*13, font_size=24)
        #padding_v1= tp.Text("\n"*6, font_size=24)
        black_cat_button = tp.Button("Choose Black Cat")
        black_cat_button.at_unclick=partial(change_window, "star_sign")
        black_cat_button.generate_shadow(fast=True)
        obsidian_serpent_button = tp.Button("Choose Obsidian Serpent")
        obsidian_serpent_button.at_unclick=partial(first_time_lobby, "obsidian serpent")
        obsidian_serpent_button.generate_shadow(fast=True)
        iron_helm_button = tp.Button("Choose The Iron Helm")
        iron_helm_button.at_unclick=partial(first_time_lobby, "iron helm")
        iron_helm_button.generate_shadow(fast=True)
        ember_crown_button = tp.Button("Choose Ember Crown")
        ember_crown_button.at_unclick=partial(first_time_lobby, "ember crown")
        ember_crown_button.generate_shadow(fast=True)
        ogres_blessing_button = tp.Button("Choose Ogre's Blessing")
        ogres_blessing_button.at_unclick=partial(first_time_lobby, "ogre's blessing")
        ogres_blessing_button.generate_shadow(fast=True)
        frog_button = tp.Button("Choose Frog")
        frog_button.at_unclick=partial(first_time_lobby, "frog")
        frog_button.generate_shadow(fast=True)


        black_cat_text = tp.Text(Types["star sign"]["black cat"]["description"], font_size=20, font_color=(120,0,120), max_width=350)
        black_cat_text.set_bck_color(random_bright_nonpurple_color())
        black_cat_text.generate_shadow(fast=True)
        obsidian_serpent_text = tp.Text(Types["star sign"]["obsidian serpent"]["description"], font_size=20, font_color=(120,0,120), max_width=350)
        obsidian_serpent_text.set_bck_color(random_bright_nonpurple_color())
        obsidian_serpent_text.generate_shadow(fast=True)
        iron_helm_text = tp.Text(Types["star sign"]["iron helm"]["description"], font_size=20, font_color=(120,0,120), max_width=350)
        iron_helm_text.set_bck_color(random_bright_nonpurple_color())
        iron_helm_text.generate_shadow(fast=True)
        ember_crown_text = tp.Text(Types["star sign"]["ember crown"]["description"], font_size=20, font_color=(120,0,120), max_width=350)
        ember_crown_text.set_bck_color(random_bright_nonpurple_color())
        ember_crown_text.generate_shadow(fast=True)
        ogres_blessing_text = tp.Text(Types["star sign"]["ogre's blessing"]["description"], font_size=20, font_color=(120,0,120), max_width=350)
        ogres_blessing_text.set_bck_color(random_bright_nonpurple_color())
        ogres_blessing_text.generate_shadow(fast=True)
        frog_text = tp.Text(Types["star sign"]["frog"]["description"], font_size=20, font_color=(120,0,120), max_width=350)
        frog_text.set_bck_color(random_bright_nonpurple_color())
        frog_text.generate_shadow(fast=True)

        black_cat_text_and_button = tp.Group([black_cat_text, black_cat_button], "v")
        black_cat_group = tp.Group([image_padding,black_cat_text_and_button], "h")

        obsidian_serpent_text_and_button = tp.Group([obsidian_serpent_text, obsidian_serpent_button], "v")
        obsidian_serpent_group = tp.Group([image_padding,obsidian_serpent_text_and_button], "h")

        iron_helm_text_and_button = tp.Group([iron_helm_text, iron_helm_button], "v")
        iron_helm_group = tp.Group([image_padding,iron_helm_text_and_button], "h")

        ember_crown_text_and_button = tp.Group([ember_crown_text, ember_crown_button], "v")
        ember_crown_group = tp.Group([image_padding,ember_crown_text_and_button], "h")

        ogres_blessing_text_and_button = tp.Group([ogres_blessing_text, ogres_blessing_button], "v")
        ogres_blessing_group = tp.Group([image_padding,ogres_blessing_text_and_button], "h")

        frog_text_and_button = tp.Group([frog_text, frog_button], "v")
        frog_group = tp.Group([image_padding,frog_text_and_button], "h")

        first_row = tp.Group([black_cat_group,obsidian_serpent_group,iron_helm_group], "h")
        second_row = tp.Group([ember_crown_group,ogres_blessing_group,frog_group], "h")
        save_all = tp.Group([first_row, second_row], "v")

        main_group = tp.Group([save_all], "h")
        main_group.sort_children(gap=20)
        main_group.center_on(screen)

    elif leaf == "debug":
        a = 1

    elif leaf == "lobby":
        own_team_buttons = []
        for i in range(MEMBER_NUMBER):
            own_team_buttons.append()
        
        main_group = tp.Group([save_all], "h")
        main_group.sort_children(gap=20)
        main_group.center_on(screen)

        went_through_lobby = True
        
    updater = main_group.get_updater()

def save_written_name():
    Save["character_name"] = new_game_name.get_value()

def name_generator():
    # Define syllable pools for different styles
    syllables = {
        0 : ["dra", "kor", "mir", "thal", "ven", "zor", "el", "ria", "lun", "gar"],
        1 : ["tech", "ify", "ly", "zen", "gen", "nova", "sys", "net", "ware", "soft"],
        2: ["ba", "be", "bi", "bo", "bu", "la", "le", "li", "lo", "lu"]
    }
    
    style = random.randrange(0, len(syllables.keys()))
    name = ""
    for _ in range(0, random.randrange(2,3)):
        name  = name + syllables[style][random.randint(0, len(syllables[style])-1)]
    
    name = name.capitalize()
    
    return name

options_current_h = 0
def move_options_text(direction):
    license_text_spliced = LICENSES.splitlines(False)
    global licenses_area, options_current_h
    if direction == "down":
        options_current_h = min(len(license_text_spliced)-17, options_current_h + 3)
    elif direction == "up":
        options_current_h = max(0,options_current_h - 3)
    
    license_text = "\n".join(license_text_spliced[options_current_h:options_current_h+17])
    licenses_area.set_text(license_text)
    licenses_area.set_topleft(screen_width/2-625/2-icon_main_width-25, screen_height*0.085+icon_main_height+25)

def change_character_type():
    if new_type_toggle.get_value() != "":
        Save["character_type"] = new_type_toggle.get_value().lower()
        print(Save["character_type"].title()+" chosen")
        new_game_monster_description.set_text(Types["monster"][Save["character_type"]]["description"], max_width=400)
        color_tiles(0)

# --- HSV helpers ---
def rgb_to_hsv(r, g, b):
    rf, gf, bf = r/255.0, g/255.0, b/255.0
    mx, mn = max(rf, gf, bf), min(rf, gf, bf)
    d = mx - mn
    if d == 0:
        h = 0.0
    elif mx == rf:
        h = (60 * ((gf - bf) / d) + 360) % 360
    elif mx == gf:
        h = (60 * ((bf - rf) / d) + 120) % 360
    else:
        h = (60 * ((rf - gf) / d) + 240) % 360
    s = 0.0 if mx == 0 else d / mx
    v = mx
    return h, s, v

def hsv_to_rgb(h, s, v):
    if s == 0:
        val = int(round(v * 255))
        return val, val, val
    h = (h % 360) / 60.0
    i = int(math.floor(h))
    f = h - i
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))
    if i == 0: rf, gf, bf = v, t, p
    elif i == 1: rf, gf, bf = q, v, p
    elif i == 2: rf, gf, bf = p, v, t
    elif i == 3: rf, gf, bf = p, q, v
    elif i == 4: rf, gf, bf = t, p, v
    else: rf, gf, bf = v, p, q
    return int(rf*255), int(gf*255), int(bf*255)

# --- Recolor function ---
def recolor_surface(surface, target_hue):
    w, h = surface.get_size()
    for y in range(h):
        for x in range(w):
            r, g, b, a = surface.get_at((x, y))
            h0, s, v = rgb_to_hsv(r, g, b)
            # Replace hue but keep saturation/value
            nr, ng, nb = hsv_to_rgb(target_hue, s, v)
            surface.set_at((x, y), (nr, ng, nb, a))

def rgb_to_hue_branchless(r, g, b):
        # Normalize to [0,1]
        r, g, b = r/255.0, g/255.0, b/255.0
        
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        delta = cmax - cmin
        
        # Avoid division by zero
        if delta == 0:
            return 0.0
        
        # Compute raw hue contributions
        hr = ((g - b) / delta) % 6
        hg = ((b - r) / delta) + 2
        hb = ((r - g) / delta) + 4
        
        # Use masks instead of branching
        hue = (cmax == r) * hr + (cmax == g) * hg + (cmax == b) * hb
        
        # Scale to degrees
        return 60.0 * hue

def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    """fill a surface with a gradient pattern
    Parameters:
    color -> starting color
    gradient -> final color
    rect -> area to fill; default is surface's rect
    vertical -> True=vertical; False=horizontal
    forward -> True=forward; False=reverse
    
    Pygame recipe: http://www.pygame.org/wiki/GradientCode
    """
    if rect is None: rect = surface.get_rect()
    x1,x2 = rect.left, rect.right
    y1,y2 = rect.top, rect.bottom
    if vertical: h = y2-y1
    else:        h = x2-x1
    if forward: a, b = color, gradient
    else:       b, a = color, gradient
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1,y2):
            color = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(surface, color, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            color = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(surface, color, (col,y1), (col,y2))

monster_tile_size_min = 32
monster_tile_size_med = 55
monster_tile_size_max = 155

star_sign_gradient = pygame.Surface((round(monster_tile_size_med*1.2),round(monster_tile_size_med*1.2)))
fill_gradient(star_sign_gradient, (110, 75, 52), (220, 245, 232), rect=None, vertical=True, forward=True)

processed_images = [[]]

old_char_color = (255,255,255,255)
processed_images = []
for i in range(1): #TEAM_NUMBER*MEMBER_NUMBER
    processed_images.append(0)

def color_tiles(i):
    global old_char_color,processed_images, saved_rgb

    saved_earlier = False

    if  i == -1:
        saved_rgb[0] = new_game_color_picker.get_value()
        saved_earlier = True
        i = 0

    if i == 0:
        old_char_color = new_game_color_picker.get_value()

        if not saved_earlier: 
            saved_rgb.append(old_char_color)

        hue = rgb_to_hue_branchless(old_char_color[0], old_char_color[1], old_char_color[2])
        new_image1 = Types["monster"][Save["character_type"]]["img_min"]
        new_image2 = Types["monster"][Save["character_type"]]["img_med"]
        new_image3 = Types["monster"][Save["character_type"]]["img_max"]
        recolor_surface(new_image1, hue)
        recolor_surface(new_image2, hue)
        recolor_surface(new_image3, hue)

        new_game_logo_processed = new_game_logo
        recolor_surface(new_game_logo_processed, hue)

        processed_images[0] = []
        processed_images[0].append(new_image1)
        processed_images[0].append(new_image2)
        processed_images[0].append(new_image3)
    else:
        color = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))

        saved_rgb.append(color)

        hue = rgb_to_hue_branchless(color[0], color[1], color[2])

        new_image1 = Types["monster"][npc_types[i]]["img_min"]
        new_image2 = Types["monster"][npc_types[i]]["img_med"]
        new_image3 = Types["monster"][npc_types[i]]["img_max"]
        
        recolor_surface(new_image1, hue)
        recolor_surface(new_image2, hue)
        recolor_surface(new_image3, hue)

        processed_images[i] = []
        processed_images[i].append(new_image1)
        processed_images[i].append(new_image2)
        processed_images[i].append(new_image3)

def color_tiles_memory(i):
    global processed_images

    color = saved_rgb[i]
    '''print(str(saved_rgb)+"\n")'''

    hue = rgb_to_hue_branchless(color[0], color[1], color[2])

    new_image1 = Types["monster"][Save["npc"][0][i]]["img_min"]
    new_image2 = Types["monster"][Save["npc"][0][i]]["img_med"]
    new_image3 = Types["monster"][Save["npc"][0][i]]["img_max"]
    
    recolor_surface(new_image1, hue)
    recolor_surface(new_image2, hue)
    recolor_surface(new_image3, hue)
    
    processed_images.append((new_image1, new_image2, new_image3))

def load_tile(img, size, size2= 0):
    if size2 != 0:
        return pygame.transform.scale(pygame.image.load(img), (size, size2)).convert_alpha()
    else:
        return pygame.transform.scale(pygame.image.load(img), (size,)*2).convert_alpha()

def random_bright_nonpurple_color():
    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # Condition 1: at least one channel > 200
        bright = (r > 200 or g > 200 or b > 200)

        # Condition 2: not purple (red & blue high, green low)
        not_purple = not (r > 200 and b > 200 and g < 100)

        # Condition 3: not bright blue (blue high, red & green low)
        not_bright_blue = not (b > 200 and r < 100 and g < 100)

        if bright and not_purple and not_bright_blue:
            return (r, g, b)

Types = {
    "monster": {
        "taurian": {
            "img_min": load_tile("gfx/taurian.png", monster_tile_size_min),
            "img_med": load_tile("gfx/taurian.png", monster_tile_size_med),
            "img_max": load_tile("gfx/taurian.png", monster_tile_size_max),
            "hp": 100,
            "description": "Taurians are agile and strong. Their type of fighting is close combat with dual weapons. They don't wear armour but they instead dodge. That's a good style. They come from a lush jungle where they cook magic porridges so they have aptitude for magically enchanted things, and the whole area of this new magical jungle as well."
        }, 
        "dark elf": {
            "img_min": load_tile("gfx/dark_elf.png", monster_tile_size_min),
            "img_med": load_tile("gfx/dark_elf.png", monster_tile_size_med),
            "img_max": load_tile("gfx/dark_elf.png", monster_tile_size_max),
            "hp": 100,
            "description": "Dark Elf is a frost mage who sings enemies into ice cubes. Their tactics are to slow enemies who are more powerful than they are or outright turn them into cubes which blocks the elf's own action completely as well. Their bones started getting cold so they came to this jungle to warm up. Their ice is sometimes effective in this kind of climate."
        },
        "skeleton": {
            "img_min": load_tile("gfx/skeleton.png", monster_tile_size_min),
            "img_med": load_tile("gfx/skeleton.png", monster_tile_size_med),
            "img_max": load_tile("gfx/skeleton.png", monster_tile_size_max),
            "hp": 100,
            "description": "Skeletons have been animated by people who shouldn't have done that. The skeletons are angry at life and so they collect all kinds of spells and are one of the most powerful spell casters in this magical jungle."
        },
        "cyclops": {
            "img_min": load_tile("gfx/cyclops.png", monster_tile_size_min),
            "img_med": load_tile("gfx/cyclops.png", monster_tile_size_med),
            "img_max": load_tile("gfx/cyclops.png", monster_tile_size_max),
            "hp": 100,
            "description": "Cyclopes are really good at lore. That makes them respect unique stuff which might not be the most powerful ones. Their tactic is to go in heavy armour, maybe even a shield. They come to this jungle after lore. Sometimes when a Cyclops is killed they can see the future which means that a random enemy dies as well - maybe even the main boss."
        }
    },
    "star sign": { 
        "black cat": {
            "img_min": load_tile("gfx/black_cat.gif", monster_tile_size_min),
            "img_med": load_tile("gfx/black_cat.gif", monster_tile_size_med),
            "img_max": load_tile("gfx/black_cat.gif", monster_tile_size_max),
            "description": 'A black cat is all about luck. When you happen to see a black cat under stairs it needs luck. Luck affects the all around game not just stuff like the dodge ability of Taurians. If a boss curses you, Black Cat is unaffected. You can see luck in effect when you follow the "combat log".'
        },
        "obsidian serpent": {
            "img_min": load_tile("gfx/obsidian_serpent.gif", monster_tile_size_min),
            "img_med": load_tile("gfx/obsidian_serpent.gif", monster_tile_size_med),
            "img_max": load_tile("gfx/obsidian_serpent.gif", monster_tile_size_max),
            "description": 'In the jungle they are represented by a coiled serpent carved into black stone. They gain the ability called  “Poisoned Strike” - a sudden flurry of attacks that bypass defenses. After the strike light is dimmer around you and you dodge more.'
        },
        "iron helm": {
            "img_min": load_tile("gfx/iron_helm.gif", monster_tile_size_min),
            "img_med": load_tile("gfx/iron_helm.gif", monster_tile_size_med),
            "img_max": load_tile("gfx/iron_helm.gif", monster_tile_size_max),
            "description": 'A battered helmet with a single dent, representing survival, endurance, and honor. Those under The Iron Helm star sign trust the metal. You gain defense much more from metallic equipment, and critical strikes are mitigated against you. You are also a good smith.'
        },
        "ember crown": {
            "img_min": load_tile("gfx/ember_crown.gif", monster_tile_size_min),
            "img_med": load_tile("gfx/ember_crown.gif", monster_tile_size_med),
            "img_max": load_tile("gfx/ember_crown.gif", monster_tile_size_max),
            "description": 'Since there is a sign only for metal - jungle has carved a sign for the mind. A blazing circlet of fire hovering above a warrior\'s helm. It signifies detachment from equipment. And affinity for the elements. Especially fire, plant and poison.'
        },
        "ogre's blessing": {
            "img_min": load_tile("gfx/ogre\'s_blessing.png", monster_tile_size_min*2, monster_tile_size_min*4),
            "img_med": load_tile("gfx/ogre\'s_blessing.png", monster_tile_size_med*2, monster_tile_size_med*4),
            "img_max": load_tile("gfx/ogre\'s_blessing.png", monster_tile_size_max*2, monster_tile_size_max*4),
            "description": 'Ogre\'s blessing is two-fold. You are slower, but you simply hit more. You digest food faster, but you also find more of it. The benefits always outweigh the negatives, if you know what I mean.'
        },
        "frog": {
            "img_min": load_tile("gfx/frog.png", monster_tile_size_min, monster_tile_size_min),
            "img_med": load_tile("gfx/frog.png", monster_tile_size_med, monster_tile_size_med),
            "img_max": load_tile("gfx/frog.png", monster_tile_size_max, monster_tile_size_max),
            "description": 'Frogs are worried about equality. If one of your skills is too big, you can redistribute experience from it to other skills. That can cause a metamorphosis of leveling methods. You also have additional conversation opportunities with the characters you meet in the jungle.'
        },
    }
}

def first_time_lobby(sign):
    choose_star_sign(sign)
    change_window("lobby")

def choose_star_sign(sign):
    global Save
    Save["npc"][3][0] = sign
    print("Star Sign "+sign.title()+" chosen")

saved_rgb = []
def save_game(number):
    if went_through_lobby == True or loaded_game == True:
        prompt = tp.TextInput("", "Enter Save Name")
        alert = tp.AlertWithChoices("Saving Game", ("Yes", "No"), text="Do you wish to save into this slot?\nOld save is formatted.", children=[prompt])
        alert.generate_shadow(fast=False) 
        alert.launch_alone(click_outside_cancel=False) # it would accidentally click other buttons
        if alert.choice == "Yes":
            Save["npc"][1] = saved_rgb
            save_names[number] = prompt.get_value()
            print("Saving to slot "+str(number)+" with the slot name "+prompt.get_value())
            with open("save/save_names", "wb") as file:
                pickled = pickle.dumps(save_names)
                compressed = lzma.compress(pickled)
                file.write(compressed)
            with open("save/save"+str(number), "wb") as file:
                pickled = pickle.dumps(Save)
                compressed = lzma.compress(pickled)
                file.write(compressed)

            change_window("save_game")

loaded_game = False
def load_game(number):
    global Save, processed_images, saved_rgb, loaded_game
    alert = tp.AlertWithChoices("Loading Game", ("Yes", "No"), text="Do you wish to load this slot?\nUnsaved progress is lost.")
    alert.generate_shadow(fast=False) 
    alert.launch_alone(click_outside_cancel=False) # it would accidentally click other buttons
    if alert.choice == "Yes":
        print("Loading from slot "+str(number))
        if path.exists("save/save"+str(number)):
            with open("save/save"+str(number), "rb") as file:
                decompressed = lzma.decompress(file.read())
                Save = pickle.loads(decompressed)
                saved_rgb = Save["npc"][1]
                processed_images = []
                for i in range(1): #TEAM_NUMBER*MEMBER_NUMBER
                    color_tiles_memory(i)
                Save["npc"][1] = processed_images
                loaded_game = True

change_window("main_menu")

clock = pygame.time.Clock()

def before_gui():
    screen.fill((150,150,20))
    if leaf == "main_menu":
        a = 1
    elif leaf == "save_game":
        a = 1
    elif leaf == "load_game":
        a = 1
    elif leaf == "options":
        a = 1
tp.call_before_gui(before_gui)

star_sign_icon_rotation = 0
star_sign_logo_time = 0

fps_refresh_time = 0
fps_num = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alert = tp.AlertWithChoices("Exiting", ("Yes", "No"), text="Do you wish to quit the program?\nAll unsaved progress will be lost.")
            alert.generate_shadow(fast=False) 
            alert.launch_alone(click_outside_cancel=False) # it would accidentally click other buttons
            if alert.choice == "Yes":
                    running = False

    #screen.fill((150,150,150)) # Clear screen
    if leaf in ("main_menu", "save_game", "load_game", "options", "new_game", "star_sign"):
        for x in range(round(screen_width/bg_tile_width)):
            for y in range(round(screen_height/bg_tile_height)):
                screen.blit(bg_tile, (x*bg_tile_width, y*bg_tile_height))

    fps_refresh_time += 1
    if fps_refresh_time >= GAME_FPS/7:
        fps_refresh_time = 0
        fps_num = str(round(clock.get_fps()))

    fps_text = normal_font.render("FPS = "+fps_num+" / "+str(GAME_FPS), True, pygame.Color(255, 165, 0, a=140), None)
    screen.blit(fps_text,(10,10))
    debug_text = normal_font.render("Save identifier="+str(Save["identifier"]), True, pygame.Color(255, 165, 0, a=140), None)
    debug_text_w, debug_text_h = loading_text.get_size()
    screen.blit(debug_text,(10,screen_height-10-debug_text_h))

    if leaf == "main_menu" or leaf =="save_game" or leaf=="load_game" or leaf == "options":
        screen.blit(logo, (screen_width/2-logo_width/2, screen_height*0.085))
        screen.blit(icon_main_scaled, (screen_width/2-logo_width/2-icon_main_width, screen_height*0.085))
        screen.blit(icon_main_scaled, (screen_width/2+logo_width/2-25, screen_height*0.085))
        screen.blit(golden_chest_main_scaled, (screen_width-golden_chest_main_width-10, screen_height-golden_chest_main_height-10))
        screen.blit(dark_elf_main_scaled, (screen_width-golden_chest_main_width-dark_elf_main_width-10-10, screen_height-dark_elf_main_height-10))
        #screen.blit(gladiator_text, (screen_width-gladiator_text_width-10, screen_height-dark_elf_main_height-10-gladiator_text_height))

    if leaf == "main_menu":
        a = 1
    elif leaf == "save_game":
        screen.blit(saving_text, (screen_width/2-saving_text_w/2,0.3*screen_height))
    elif leaf == "load_game":
        screen.blit(loading_text, (screen_width/2-loading_text_w/2,0.3*screen_height))
    elif leaf == "options":
        #screen.fill((150,0,0))
        pygame.draw.rect(screen, (50,150,50), (screen_width/2-625/2-icon_main_width-25-10, screen_height*0.085+icon_main_height+25-10,1000+20,400+20))
        pygame.draw.rect(screen, (150,150,33), (screen_width/2-625/2-icon_main_width-25, screen_height*0.085+icon_main_height+25,1000,400))
        #screen_width/2-logo_width/2-icon_main_width-25, screen_height*0.085+icon_main_height+25
    elif leaf == "new_game":
        pygame.draw.rect(screen, (150,75,0), (screen_width/2-625/2-icon_main_width-45+75-10, screen_height*0.085+icon_main_height+25-10-10,875+20,400+20+20))
        pygame.draw.rect(screen, (50,150,50), (screen_width/2-625/2-icon_main_width-45+75, screen_height*0.085+icon_main_height+25-10,875,400+20))
        screen.blit(new_game_logo_processed, (screen_width/2-new_game_logo_width/2, screen_height*0.085))
        img = processed_images[0][2]
        #w,h = monster_tile_size_max, monster_tile_size_max
        screen.blit(img, (screen_width/3+82, screen_height/2-40))

        if new_type_toggle.get_value().lower() != Save["character_type"]:
            change_character_type()

        if new_game_color_picker.get_value() != old_char_color:
            color_tiles(0)
    elif leaf == "star_sign":
        screen.blit(star_sign_logo_processed, (screen_width/2-star_sign_logo_processed.get_width()/2, screen_height*0.02))
        #star_sign_icon_processed_rect.x = screen_width/2-star_sign_logo_processed.get_width()/2-120
        #star_sign_icon_processed_rect.y = screen_height*0.085
        star_sign_icon_processed_rect.center = (screen_width/2-star_sign_logo_processed.get_width()/2, screen_height*0.1)
        screen.blit(star_sign_icon_processed, star_sign_icon_processed_rect)

        screen.blit(star_sign_gradient, (10-5,190-5))
        screen.blit(Types["star sign"]["black cat"]["img_med"], (10, 190))
        screen.blit(star_sign_gradient, (480-5,190-5))
        screen.blit(Types["star sign"]["obsidian serpent"]["img_med"], (480, 190))
        screen.blit(star_sign_gradient, (925-5,190-5))
        screen.blit(Types["star sign"]["iron helm"]["img_med"], (925, 190))
        screen.blit(star_sign_gradient, (10-5,440-5))
        screen.blit(Types["star sign"]["ember crown"]["img_med"], (10, 440))
        #screen.blit(star_sign_gradient, (450-5,340-5))
        screen.blit(Types["star sign"]["ogre's blessing"]["img_med"], (450, 340))
        screen.blit(star_sign_gradient, (925-5,440-5))
        screen.blit(Types["star sign"]["frog"]["img_med"], (925, 440))

        star_sign_logo_time = star_sign_logo_time + 4
        if star_sign_logo_time > GAME_FPS/40:
            star_sign_logo_time = 0
            star_sign_icon_rotation = star_sign_icon_rotation + 0.25
            if star_sign_icon_rotation >= 360:
                star_sign_icon_rotation = 0

            star_sign_icon_processed = pygame.transform.rotate(star_sign_icon,-star_sign_icon_rotation)
            star_sign_icon_processed_rect = star_sign_icon_processed.get_rect(center=star_sign_icon_rect.center)

    updater.update(events=pygame.event.get(), mouse_rel=pygame.mouse.get_rel())

    pygame.display.flip() # Update display

    clock.tick(GAME_FPS)

pygame.quit()