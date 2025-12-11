"""We show here how to generate and binds a shadow to an element."""

GAME_FPS = 144
LICENSES2 = "David E. Gervais drawn tiles library has many of these tiles the game is using, like the man in the main menu\nIt is published under CC BY 3.0\nhttp://pousse.rapiere.free.fr/tome/tome-tiles.htm" # update from LICENSES.txt
LICENSES = "David E. Gervais drawn tiles library has many of these tiles the game is using, like the man in the main menu\nIt is published under CC BY 3.0\nhttp://pousse.rapiere.free.fr/tome/tome-tiles.htm\n\n\nThese next ones are just to show the functionality copied from my old games\n\nRed outfit for main character - graphics/charright & left.png\nhttps://opengameart.org/content/occupational-icons\nhttps://opengameart.org/users/technopeasant - Graham L. Wilson (technopeasant)\nTiles have been drawn by David E. Gervais, and are published under the Creative Commons license.\nYou are free to copy, distribute and transmit those tiles as long as you credit David Gervais as their creator.\nCC-BY 3.0\nhttp://creativecommons.org/licenses/by/3.0/\n\n\nA sand road - graphics/road2.png\nhttps://opengameart.org/content/pixel-art-top-down-tileset\nFrom user https://opengameart.org/users/dustdfg - Yevhen Babiichuk (DustDFG)\nCC-BY-SA 4.0\nhttps://creativecommons.org/licenses/by-sa/4.0/\n\n\nGold stuff in the Main Menu background\nhttps://opengameart.org/content/gold-treasure-icons-16x16s\nFrom user https://opengameart.org/users/bonsaiheldin - Bonsaiheldin"

import pygame, thorpy as tp
from functools import partial
from os import path, mkdir
import random
import pickle
import lzma
import math

random.seed()

pygame.init()

pygame.display.set_caption("Poison Ivy")
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

'''def go_full_screen():
    global screen
    screen = pygame.display.set_mode((1366,768), pygame.FULLSCREEN)

def go_windowed():
    pygame.display.toggle_fullscreen()'''

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

logo = pygame.image.load("gfx/logo.png")
logo_width, logo_height = logo.get_size()

new_game_logo = pygame.image.load("gfx/new_game_logo.png")
new_game_logo_width, new_game_logo_height = new_game_logo.get_size()

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

def exit_game():
    global running
    alert = tp.AlertWithChoices("Exiting", ("Yes", "No"), text="Do you wish to quit the program?\nAll unsaved progress will be lost.")
    alert.generate_shadow(fast=False) 
    alert.launch_alone(click_outside_cancel=False) # it would accidentally click other buttons
    if alert.choice == "Yes":
            running = False

def change_window(name):
    global updater
    global leaf 
    leaf = name
    if leaf == "main_menu":
        main_menu_objects = []
        main_menu_objects.append(tp.Button("Continue Game"))
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
        main_menu_objects[len(main_menu_objects)-1].at_unclick=pygame.display.toggle_fullscreen
        main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
        main_menu_objects.append(tp.Button("Exit"))
        main_menu_objects[len(main_menu_objects)-1].at_unclick=exit_game
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

        #global licenses_area
        global licenses_area#, licenses_box
        licenses_area = tp.Text(LICENSES, font_size=24, max_width=950, font_color=(250,250,250))
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
        global new_type_toggle, new_game_monster_description, new_game_name, new_game_color_picker
        new_type_toggle = tp.TogglablesPool("Character Types", ("Taurian", "Dark Elf", "Skeleton", "Cyclops"), Save["character_type"].title())
        #new_type_toggle.at_unclick=change_character_type #commented since it is watched in the main loop

        save_back_to_menu_button = tp.Button("Back to Main Menu")
        save_back_to_menu_button.at_unclick=partial(change_window, "main_menu")
        save_back_to_menu_button.generate_shadow(fast=True)

        start_the_game_button = tp.Button("Start the Game")
        start_the_game_button.at_unclick=partial(change_window, "lobby")
        start_the_game_button.generate_shadow(fast=True)

        bottom_buttons = tp.Group([start_the_game_button, save_back_to_menu_button], "h")

        new_game_name = tp.TextInput(Save["character_name"], placeholder="Can be changed later")
        new_game_name.at_cancel=save_written_name
        new_game_name_descr = tp.Text("Character Name")
        new_game_namers = tp.Group([new_game_name_descr, new_game_name], "h")
        #padder = tp.Text("\n"*10, font_size=24)
        padder1 = tp.Text((" "*40+"\n")*11, font_size=24)
        new_game_monster_description = tp.Text(Types["monster"][Save["character_type"]]["description"], max_width=400)

        #change_character_type()

        new_game_color_picker = tp.ColorPicker()
        #new_game_color_picker.at_cancel=partial(color_tiles, 0) #watched in main loop
        new_game_color_picker.set_value(old_char_color)

        color_tiles(0)

        image_and_text = tp.Group([new_game_color_picker,padder1,new_game_monster_description], "h")
        
        padder2 = tp.Text("\n"*2, font_size=24)
        save_all = tp.Group([padder2,new_type_toggle,image_and_text,new_game_namers,bottom_buttons], "v")

        main_group = tp.Group([save_all], "h")
        main_group.sort_children(gap=20)
        main_group.center_on(screen)
        
    updater = main_group.get_updater()

def save_written_name():
    Save["character_name"] = new_game_name.get_value()

options_current_h = 0
def move_options_text(direction):
    license_text_spliced = LICENSES.splitlines(False)
    global licenses_area, options_current_h
    if direction == "down":
        options_current_h = min(len(license_text_spliced)-14, options_current_h + 3)
    elif direction == "up":
        options_current_h = max(0,options_current_h - 3)
    
    license_text = "\n".join(license_text_spliced[options_current_h:options_current_h+14])
    licenses_area.set_text(license_text)
    licenses_area.set_topleft(screen_width/2-logo_width/2-icon_main_width-25, screen_height*0.085+icon_main_height+25)

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
    return surface

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

monster_tile_size_min = 32
monster_tile_size_med = 55
monster_tile_size_max = 155

processed_images = [[]]

old_char_color = (255,255,255,255)

def color_tiles(i):
    global old_char_color,processed_images

    if i == 0:
        old_char_color = new_game_color_picker.get_value()

        hue = rgb_to_hue_branchless(old_char_color[0], old_char_color[1], old_char_color[2])
        
        processed1 = recolor_surface(Types["monster"][Save["character_type"]]["img_min"], hue)
        processed2 = recolor_surface(Types["monster"][Save["character_type"]]["img_med"], hue)
        processed3 = recolor_surface(Types["monster"][Save["character_type"]]["img_max"], hue)

        processed_images[0] = []
        processed_images[0].append(processed1)
        processed_images[0].append(processed2)
        processed_images[0].append(processed3)

def load_tile(img, size):
    return pygame.transform.scale(pygame.image.load(img), (size,)*2)

Save = {
    "identifier": random.randint(1111,8888),
    "character_name": "",
    "character_type": "taurian",
}

Types = {
    "monster": {
        "taurian": {
            "img_min": load_tile("gfx/taurian.png", monster_tile_size_min),
            "img_med": load_tile("gfx/taurian.png", monster_tile_size_med),
            "img_max": load_tile("gfx/taurian.png", monster_tile_size_max),
            "hp": 100,
            "description": "Taurians are agile and strong. Their type of fighting is close combat with dual weapons. They don't wear armour but they instead dodge. That's a good style. They come from a lush jungle where they cook magic porridges so they have aptitude for magically enchanted weapons."
        }, 
        "dark elf": {
            "img_min": load_tile("gfx/dark_elf.png", monster_tile_size_min),
            "img_med": load_tile("gfx/dark_elf.png", monster_tile_size_med),
            "img_max": load_tile("gfx/dark_elf.png", monster_tile_size_max),
            "hp": 100,
            "description": "Dark Elf is a frost mage who sings enemies into ice cubes. Their tactics are to slow enemies who are more powerful than they are or outright turn them into cubes which blocks the elf's own action completely as well."
        },
        "skeleton": {
            "img_min": load_tile("gfx/skeleton.png", monster_tile_size_min),
            "img_med": load_tile("gfx/skeleton.png", monster_tile_size_med),
            "img_max": load_tile("gfx/skeleton.png", monster_tile_size_max),
            "hp": 100,
            "description": "Skeletons have been animated by people who shouldn't have done that. The skeletons are angry at life and so they collect all kinds of spells and are one of the most powerful spell casters in the Poisonous Realm."
        },
        "cyclops": {
            "img_min": load_tile("gfx/cyclops.png", monster_tile_size_min),
            "img_med": load_tile("gfx/cyclops.png", monster_tile_size_med),
            "img_max": load_tile("gfx/cyclops.png", monster_tile_size_max),
            "hp": 100,
            "description": "Cyclopes are really good at lore. That makes them respect unique weapons and armour which are usually not the most powerful ones. Their tactic is to attack in heavy armour, maybe even a shield. Unique ones at that. Sometimes when a Cyclops is killed they can see the future which means that a random member in the fight dies."
        }
    }
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
            pickled = pickle.dumps(save_names)
            compressed = lzma.compress(pickled)
            file.write(compressed)
        with open("save/save"+str(number), "wb") as file:
            pickled = pickle.dumps(Save)
            compressed = lzma.compress(pickled)
            file.write(compressed)

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
                decompressed = lzma.decompress(file.read())
                Save = pickle.loads(decompressed)

change_window("main_menu")

clock = pygame.time.Clock()

def before_gui():
    screen.fill((50,255,20))
    if leaf == "main_menu":
        a = 1
    elif leaf == "save_game":
        a = 1
    elif leaf == "load_game":
        a = 1
    elif leaf == "options":
        a = 1
tp.call_before_gui(before_gui)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alert = tp.AlertWithChoices("Exiting", ("Yes", "No"), text="Do you wish to quit the program?\nAll unsaved progress will be lost.")
            alert.generate_shadow(fast=False) 
            alert.launch_alone(click_outside_cancel=False) # it would accidentally click other buttons
            if alert.choice == "Yes":
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
        #screen.fill((150,0,0))
        pygame.draw.rect(screen, (50,150,50), (screen_width/2-logo_width/2-icon_main_width-25-10, screen_height*0.085+icon_main_height+25-10,1000+20,400+20))
        pygame.draw.rect(screen, (50,50,250), (screen_width/2-logo_width/2-icon_main_width-25, screen_height*0.085+icon_main_height+25,1000,400))
        #screen_width/2-logo_width/2-icon_main_width-25, screen_height*0.085+icon_main_height+25
    elif leaf == "new_game":
        screen.blit(new_game_logo, (screen_width/2-new_game_logo_width/2, screen_height*0.085))
        img = processed_images[0][2]
        #w,h = monster_tile_size_max, monster_tile_size_max
        screen.blit(img, (screen_width/2+15, screen_height/2-40))

        if new_type_toggle.get_value().lower() != Save["character_type"]:
            change_character_type()

        if new_game_color_picker.get_value() != old_char_color:
            color_tiles(0)

    updater.update(events=pygame.event.get(), mouse_rel=pygame.mouse.get_rel())

    pygame.display.flip() # Update display

    clock.tick(GAME_FPS)

pygame.quit()