import pygame

class Debug_window:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.window_surf = pygame.Surface((300, 160))
        self.window_rect = self.window_surf.get_rect(topleft=(0,0))
            #font = pygame.font.SysFont(None, 16)
        self.font = pygame.font.Font("./fonts/Arial_Bold.ttf", 16)
              
    def display(self,toggle, text_list):
        self.screen.blit(self.window_surf, self.window_rect) 
        if toggle:
            self.create_display_list(text_list)

    def create_display_list(self,text_list):
        x = self.window_rect.topleft[0]
        y = self.window_rect.topleft[1]
        for index, text in enumerate(text_list):
            self.screen.blit(
                self.font.render(
                    text, True, "WHITE"),
                    (x, y))
            y += 20
    
    def display_mesh(self, toggle, tile,camera_offset):
        if toggle:
            self.screen.blit(tile.mask_surface, tile.mask_rect.topleft - camera_offset)

            

# class Player_colider_rect:
#     def draw_rect_arround_foot_colider(self,screen,player):
    
#         pygame.draw.line(screen, "BLACK", (player.collider_rect.topleft),
#                                       (player.collider_rect.topright))
    
#         pygame.draw.line(screen, "BLACK", (player.collider_rect.topright),
#                                       (player.collider_rect.bottomright))
    
#         pygame.draw.line(screen, "BLACK", (player.collider_rect.topleft),
#                                       (player.collider_rect.bottomleft))
    
#         pygame.draw.line(screen, "BLACK", (player.collider_rect.bottomleft),
#                                       (player.collider_rect.bottomright))
class Fps_counter:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font("./fonts/Arial_Bold.ttf", 16)
        self.screen_size = pygame.display.get_surface().get_size()
        self.max_fps = 0
        self.min_fps = 1000
    
    def display_fps(self,max_fps):
        self.min_and_max_fps()
        self.clock.tick(max_fps)
        self.max_fps_text_surf = self.font.render(f"max: {self.max_fps}",True, 'Yellow')
        self.min_fps_text_surf = self.font.render(f"min: {self.min_fps}",True, 'Yellow')
        self.screen.blit(self.max_fps_text_surf, (self.screen_size[0] -100,
                            self.screen_size[1] - 100))   
        self.screen.blit(self.min_fps_text_surf, (self.screen_size[0] -100,
                            self.screen_size[1] - 50))   
    def min_and_max_fps(self):
        if self.clock.get_fps() > self.max_fps:
            self.max_fps = self.clock.get_fps()
        if self.clock.get_fps() < self.min_fps:
            if self.clock.get_fps() != 0:
                self.min_fps = self.clock.get_fps()
                
    ### [T-77]: Get delta time in seconds (seconds since last frame)
    def get_delta_time(self):
        return float(self.clock.get_time() / 10)