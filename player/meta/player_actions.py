from dataclass_and_protocols.entities_actions import (
    LifelessEntitiesActions,
    EntitesMotionActions,
    LiveEntitiesActions,
)
from player.meta.movement_calculations_meta import CalculationsOnMovement

from pygame.math import Vector2

class PlayerActions(
    LifelessEntitiesActions,
    EntitesMotionActions,
    LiveEntitiesActions,
    CalculationsOnMovement
    ):
    def __init__(self,stats):
        super().__init__()
        CalculationsOnMovement.__init__(self)
        self.stats = stats
        self.last_direction = Vector2((0,0))

    def use(class_instance):
        pass    

    def display_info(self):
        print(f'''
        HP: {self.stats.hp}/{self.stats.max_hp}\n
        Mana: {self.stats.mana}/{self.stats.max_mana}\n
        ${self.stats.gold}\n''')

    def take_damage(self, damage):
        self.stats.hp -= damage
        if self.stats.hp <= 0:
            print('you were strangled by an overhanging vine and died')

    def update_position(self, delta_time, toggle, is_allowed):
       ### Movement keys
        if is_allowed:
            # T-50: Simplified the movement logic.
            ### [T-75] Added updating of ground_collision_rect
            
            if (self.direction.y and not self.direction.x) or (self.direction.x and not self.direction.y):
                self.rect.center += Vector2(self.direction.x, self.direction.y /2)* self.stats.speed * delta_time * self.stats.acceleration
                self.ground_collision_rect.center += Vector2(self.direction.x, self.direction.y /2)* self.stats.speed * delta_time * self.stats.acceleration
                self.accelerate()
                self.last_direction[0] = self.direction.x
                self.last_direction[1] = self.direction.y / 2
            
            elif self.direction.x and self.direction.y:
                if not toggle:
                     diagonal = Vector2(self.direction.x, self.direction.y / 2)           
                     movement = diagonal *  self.stats.speed * delta_time * self.stats.acceleration      
                     movement = self.ensure_diagonal_movement_ratio(movement) 
                     self.rect.center += movement
                     self.ground_collision_rect.center += movement
                     self.last_direction[0] = self.direction.x
                     self.last_direction[1] = self.direction.y / 2
                     self.accelerate()
                     
                else:
                    self.rect.center += (self.direction / 1.5) * self.stats.speed * delta_time
            
            elif not self.direction and self.stats.acceleration > 0.1:
                
                if self.stats.acceleration > 0.1 and (self.last_direction[0] and not self.last_direction[1]) or (self.last_direction[1] and not self.last_direction[0]):
                    self.rect.center += self.last_direction * self.stats.speed * delta_time * self.stats.acceleration
                    self.ground_collision_rect.center +=  self.last_direction * self.stats.speed * delta_time * self.stats.acceleration
                    self.decelerate()
                    
                elif self.stats.acceleration > 0.1 and self.last_direction[0] and self.last_direction[1]:
                    movement = self.last_direction *  self.stats.speed * delta_time * self.stats.acceleration
                    movement = self.ensure_diagonal_movement_ratio(movement)
                    self.rect.center += movement
                    self.ground_collision_rect.center += movement
                    self.decelerate()
                    
                if self.stats.acceleration <= 0.1:
                    self.last_direction[0] = 0
                    self.last_direction[1] = 0
                    
        else:
            return
               
    def accelerate(self):
        if self.stats.acceleration < 1:
            self.stats.acceleration += 0.1
            
    def decelerate(self):
        if self.stats.acceleration > 0.1:
            self.stats.acceleration -= 0.1
            
    def start_animation():
        print("plyer_animation")

    def move_to(coordinates):
        print("move to ",{coordinates})

    def follow(followee):
        print("what is foloweee?",followee)

    def equip_item(self, item, slot_name):
        if item in self.inventory and self.equipment[slot_name] == None:
            self.inventory.remove(item)
            self.equipment[slot_name] == item
            print(f"i put{item} into {slot_name}")
        elif item in self.inventory and self.equipment[slot_name] != None:
            self.inventory.remove(item)
            self.inventory.append(self.equipment[slot_name])
            self.equipment[slot_name] = item
            print(f"i put{item} into {slot_name}")
    
    def add_item(item):
        print(f"item {item} added to equipment")
    
    def display_chatbox():
        print("chatbox displayed")

    def remove_item(item):
        print(f"item {item} removed from equipment")

    def heal(self, amount):
        self.stats.hp += amount
        if self.stats.hp >= 100:
            self.stats.hp = 100
            print('fully healed')
    
    def gain_experience(self, experience):
        self.stats.exp += experience
    
    def level_up(self):
        self.stats.level += 1

    def melee_attack(self):
        return self.stats.attack * self.stats.strength 
    
    def range_attack(self):
        return self.stats.attack * self.stats.dexterity
    
    def magic_attack(self):
        return self.stats.attack * self.stats.inteligence