import pygame

class Input:
    def __init__(self):
        self.keys = pygame.key.get_pressed()
        self.translate = {
            pygame.K_DOWN: 'down',
            pygame.K_UP: 'up',
            pygame.K_RIGHT: 'right',
            pygame.K_LEFT: 'left'
        }
        self.movement_keys = [pygame.K_DOWN, pygame.K_UP,
                              pygame.K_RIGHT, pygame.K_LEFT]
        

        self.pressed_buttons = []
        self.unpressed_buttons = []
        self.x_direction = 0
        self.y_direction = 0

        
        self.translate = {
            pygame.K_DOWN: 'down',
            pygame.K_UP: 'up',
            pygame.K_RIGHT: 'right',
            pygame.K_LEFT: 'left'
        }
        
        self.debug_toggle = False
        self.max_fps_diagonal_movement_toggle = False
    
    def handle_input(self,
                    master_val,
                    camera,
                    player,
                    ui, _restart_game,
                    save_toggle,
                    save_game,
                    load_saved_game):

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    if self.debug_toggle == False:
                        self.debug_toggle = True
                        pygame.time.delay(100)
                    else:
                        self.debug_toggle = False
                        pygame.time.delay(100)
                if event.key == pygame.K_F1:
                    if mesh_toggle == False:
                        mesh_toggle = True
                        pygame.time.delay(100)
                    else:
                        mesh_toggle = False
                        pygame.time.delay(100)
                if event.key == pygame.K_F3:
                    pygame.time.delay(10)
                if event.key == pygame.K_F4:
                    if not self.master_val.mask_toggle:
                        camera.mask_toggle = True
                    else:
                        camera.mask_toggle = False
                    pygame.time.delay(10)
                if event.key == pygame.K_F9:
                    if not self.max_fps_diagonal_movement_toggle:
                        self.max_fps_diagonal_movement_toggle = True
                        pygame.time.delay(50)
                    else:
                        self.max_fps_diagonal_movement_toggle = False
                        pygame.time.delay(50)

                if event.key in self.movement_keys:                      
                    self.pressed_buttons.append(event.key)                                    
                    if event.key == pygame.K_RIGHT and pygame.K_LEFT in self.pressed_buttons:
                        self.pressed_buttons.remove(pygame.K_LEFT)
                    elif event.key == pygame.K_LEFT and pygame.K_RIGHT in self.pressed_buttons:
                        self.pressed_buttons.remove(pygame.K_RIGHT)
                    
                    if event.key == pygame.K_UP and pygame.K_DOWN in self.pressed_buttons:
                        self.pressed_buttons.remove(pygame.K_DOWN)
                    elif event.key == pygame.K_DOWN and pygame.K_UP in self.pressed_buttons:
                        self.pressed_buttons.remove(pygame.K_UP)
                    
                    self.assign_direction(player, master_val, event)
 
            if event.type == pygame.KEYUP:
                if event.key in self.movement_keys:
                    if event.key in self.pressed_buttons:
                        
                        self.pressed_buttons.remove(event.key)
                        #print('releasing: ', self.translate[event.key])
                    
                        if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                            self.y_direction = 0
                            player.direction.y = 0
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                            self.x_direction = 0
                            player.direction.x = 0
                    
                
            if event.type == pygame.MOUSEBUTTONUP:
                #pygame.time.delay(300)
                #print("mouse")
                ui.mouseEvents(_restart_game,save_toggle,save_game,load_saved_game)


    def assign_direction(self,player_instance,master_val_instance,event):
            
        x = event.key if event.key in master_val_instance.directions_x.keys() else 0
        y = event.key if event.key in master_val_instance.directions_y.keys() else 0
        if x:
            self.x_direction = master_val_instance.directions_x[x] if x in master_val_instance.directions_x.keys() else 0
        if y:
            self.y_direction = master_val_instance.directions_y[y] if y in master_val_instance.directions_y.keys() else 0

        player_instance.direction.x = self.x_direction
        player_instance.direction.y = self.y_direction
    