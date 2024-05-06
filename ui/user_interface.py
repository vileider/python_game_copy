import pygame

class UserInterface(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ElementsGroup = pygame.sprite.Group()
        self.screen = pygame.display.get_surface()

        self.just_life = self.create_sprite("just_life",'./images/just_life.png',(115, 40),(208,30))
        self.life_bar =  self.create_sprite("life_bar",'./images/life_bar.png',(0, 0))
        self.game_map_radar = self.create_sprite("game_map_radar",'./images/map_bg.png',((self.screen.get_size()[0]-220), 0))
        self.quick_slot_bar = self.create_sprite("quick_slot_bar",'./images/quick_slot_bar.png',((120, self.screen.get_size()[1]-80)),(800,100))
        self.log_scroll = self.create_sprite("log_scroll",'./images/log_scroll.png',(-30, 600))
        self.menu = self.create_sprite("menu",'./images/menu.png',(400, 0))
        self.save_btn  =  self.create_sprite("save",'./images/ui/save_btn.png',(((self.screen.get_size()[0] // 2)+90), 220))
        self.load_btn = self.create_sprite("load",'./images/ui/load_btn.png',(((self.screen.get_size()[0] // 2)+90), 220))
        self.menu_unfolded = self.create_sprite("menu_unfolded",'./images/unfolded_menu.png',((self.screen.get_size()[0] // 2+40), 0))
        self.restart_btn = self.create_sprite("restart_btn",'./images/restart_btn.png',(((self.screen.get_size()[0] // 2)+90), 120))
        # Add all sprites to the ui group
        self.ElementsGroup.add(self.just_life, self.life_bar,self.menu,self.game_map_radar,self.log_scroll,self.quick_slot_bar)
        self._is = False

    def display_ui(self):
        # Blit all sprites in the ui group
        self.ElementsGroup.draw(self.screen)
    
    def toggle_menu(self,save_toggle):
        self._is = not self._is 

        if self._is:
            self.ElementsGroup.add(self.menu_unfolded)
            self.ElementsGroup.add(self.restart_btn)
            if save_toggle:
                self.ElementsGroup.add(self.save_btn)
            else:
                self.ElementsGroup.add(self.load_btn)

        elif not self._is:
            self.ElementsGroup.remove(self.menu_unfolded,self.restart_btn)
            if save_toggle:
                self.ElementsGroup.remove(self.save_btn)
            else:
                self.ElementsGroup.remove(self.load_btn,self.save_btn)
            pygame.display.flip()

    def mouseEvents(self,_restart_game,save_toggle,save_game,load_saved_game):
        mousePosition = pygame.mouse.get_pos()
        if self.menu.rect.collidepoint(mousePosition):
            self.toggle_menu(save_toggle)
        elif self.restart_btn.rect.collidepoint(mousePosition):
            _restart_game()
            self.toggle_menu(save_toggle)
        elif self.save_btn.rect.collidepoint(mousePosition):
            save_game()
            self.toggle_menu(save_toggle)
        elif self.load_btn.rect.collidepoint(mousePosition):
            load_saved_game()
            self.toggle_menu(save_toggle)
        


    def create_sprite(self,name,sprite_path:str,position:tuple,transform_values=(0,0)):
        sprite = pygame.sprite.Sprite()
        sprite.name = name
        sprite.image = pygame.image.load(f"{sprite_path}").convert_alpha()
        sprite.rect = sprite.image.get_rect(topleft=position)

        if transform_values != (0,0):
            sprite.image = pygame.transform.scale(sprite.image,transform_values)

        return sprite