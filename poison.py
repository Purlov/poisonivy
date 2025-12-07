"""We show here how to generate and binds a shadow to an element."""

import sys, pygame, thorpy as tp
from functools import partial

pygame.init()

x,y = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((x*0.89, y*0.89))
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

def save_game(number):
    print(str(number))

save_game_objects = []
for i in range(15):
    if i < 5:
        save_game_objects.append(tp.Button("Save to Slot "+str(i)))
        save_gamer = save_game(i)
        save_game_objects[len(save_game_objects)-1].at_unclick=save_gamer

def change_window(number):
    print(str(number))

main_menu_objects = []
main_menu_objects.append(tp.Button("Continue Game"))
main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
main_menu_objects.append(tp.Button("New Game"))
window_changer = change_window(7)
main_menu_objects[len(main_menu_objects)-1].at_unclick=window_changer
main_menu_objects[len(main_menu_objects)-1].generate_shadow(fast=True)
main_menu_objects.append(tp.Button("Save Game"))
window_changer = change_window(2)
main_menu_objects[len(main_menu_objects)-1].at_unclick=window_changer
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

normal_font = pygame.font.Font(None, 32)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #menu.react(event) # Let ThorPy handle events
    #menu.draw() # Draw all elements in menu

    screen.fill((150,150,150)) # Clear screen
    fps_text = normal_font.render("FPS = "+str(clock.get_fps()), True, pygame.Color(50, 50, 0, a=140), None)
    screen.blit(fps_text,(0,0))

    updater.update(events=pygame.event.get(), mouse_rel=pygame.mouse.get_rel())

    pygame.display.flip() # Update display

    clock.tick(144)

pygame.quit()