"""We show here how to generate and binds a shadow to an element."""

GAME_FPS = 144

import sys, pygame, thorpy as tp
from functools import partial

pygame.init()

x,y = pygame.display.get_desktop_sizes()[0]
screen_width, screen_height = x*0.89, y*0.89
screen = pygame.display.set_mode((screen_width, screen_height))
tp.init(screen, tp.theme_game1) #bind screen to gui elements and set theme

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

def save_game(number):
    print(str(number))

save_game_objects = []
for i in range(15):
    if i < 5:
        save_game_objects.append(tp.Button("Save to Slot "+str(i)))
        save_game_objects[len(save_game_objects)-1].at_unclick=partial(save_game, i)

def change_window():
    main_group = tp.Box(save_game_objects)
    updater = main_group.get_updater()
    '''for i in range(len(all_windows)):
        for j in range(len(all_windows[i])):
            all_windows[i][j].unblit()'''
    
def save_game_pressed():
    global updater
    main_group = tp.Box(save_game_objects)
    main_group.sort_children(gap=20)
    main_group.center_on(screen)
    updater = main_group.get_updater()

main_menu_objects = []
main_menu_objects.append(tp.Button("Continue Game"))
main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
main_menu_objects.append(tp.Button("New Game"))
main_menu_objects[len(main_menu_objects)-1].at_unclick=change_window
main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
main_menu_objects.append(tp.Button("Save Game"))
main_menu_objects[len(main_menu_objects)-1].at_unclick=save_game_pressed
main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
main_menu_objects.append(tp.Button("Load Game"))
main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
main_menu_objects.append(tp.Button("Options & Credits"))
main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
main_menu_objects.append(tp.Button("Exit"))
main_menu_objects[len(main_menu_objects)-1].at_unclick=pygame.quit
main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)

main_group = tp.TitleBox("Poison Ivy Options", main_menu_objects)
# main_group.set_size((500,500))
main_group.sort_children(gap=20)
main_group.center_on(screen)

updater = main_group.get_updater()



clock = pygame.time.Clock()

leaf = "main_menu"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if leaf == "main_menu":
            a = 1

    if leaf == "main_menu":
        screen.fill((150,150,150)) # Clear screen

        fps_text = normal_font.render("FPS = "+str(round(clock.get_fps()))+" MIN_TARGET = "+str(GAME_FPS), True, pygame.Color(255, 165, 0, a=140), None)
        screen.blit(fps_text,(0,0))

        screen.blit(logo, (screen_width/2-logo_width/2, screen_height*0.085))
        screen.blit(icon_main_scaled, (screen_width/2-logo_width/2-icon_main_width-25, screen_height*0.085))
        screen.blit(golden_chest_main_scaled, (screen_width-golden_chest_main_width-10, screen_height-golden_chest_main_height-10))
        screen.blit(dark_elf_main_scaled, (screen_width-golden_chest_main_width-dark_elf_main_width-10-10, screen_height-dark_elf_main_height-10))
        screen.blit(gladiator_text, (screen_width-gladiator_text_width-10, screen_height-dark_elf_main_height-10-gladiator_text_height))

    updater.update(events=pygame.event.get(), mouse_rel=pygame.mouse.get_rel())

    pygame.display.flip() # Update display

    clock.tick(GAME_FPS)

pygame.quit()