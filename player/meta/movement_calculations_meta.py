from pygame.math import Vector2



class CalculationsOnMovement:
    def __init__(self) -> None:
        self.diagonal_movement_switch = False
    
    def ensure_diagonal_movement_ratio(self, movement):

        if not int(movement[0]) % 2 == 0 and self.diagonal_movement_switch:
            movement[0] = movement[0] - 1
            self.diagonal_movement_switch = False
            
        elif not int(movement[0]) % 2 == 0 and not self.diagonal_movement_switch:
            movement[0] = movement[0] + 1
            self.diagonal_movement_switch = True
        
       
        # if both are positive
        if movement[0] > 0 and movement[1] > 0:
            if int(movement[0]) / 2 == int(movement[1]):
                return Vector2(int(movement[0]), int(movement[1]))
            elif int(-movement[0]) / 2 > int(movement[1]):
                difference = int(movement[0]) / 2 - int(movement[1])
                return Vector2(int(movement[0]), int(movement[1] + difference))
            elif int(-movement[0]) / 2 < int(movement[1]):
                difference = int(movement[1]) - int(movement[0] / 2) 
                return Vector2(int(movement[0]), int(movement[1] - difference))

        # if X is negative    
        elif movement[0] < 0 and movement[1] > 0:
            if int(-movement[0]) / 2 == int(movement[1]):
                return Vector2(int(movement[0]), int(movement[1]))
            elif int(-movement[0]) / 2 > int(movement[1]):
                difference = int(-movement[0]) / 2 - int(movement[1])
                return Vector2(int(movement[0]), int(movement[1] + difference))
            elif int(-movement[0]) / 2 < int(movement[1]):
                difference = int(movement[1]) - int(-movement[0]) / 2
                return Vector2(int(movement[0]), int(movement[1] - difference))

        # if Y is negative
        elif movement[0] > 0 and movement[1] < 0:
            if int(movement[0]) / 2 == int(-movement[1]):
                return Vector2(int(movement[0]), int(movement[1]))
            elif int(movement[0]) / 2 > int(-movement[1]):
                difference = int(movement[0]) / 2 - int(-movement[1])
                return Vector2(int(movement[0]), int(movement[1] - difference))
            elif int(movement[0]) / 2 < int(-movement[1]):
                difference = int(-movement[1]) - int(movement[0]) / 2
                return Vector2(int(movement[0]), int(movement[1] + difference))

        # if both are negative     
        else:
            if int(-movement[0]) / 2 == int(-movement[1]):
                return Vector2(int(movement[0]), int(movement[1]))
            elif int(-movement[0]) / 2 > int(-movement[1]):
                difference = int(-movement[0]) / 2 - int(-movement[1])
                return Vector2(int(movement[0]), int(movement[1] - difference))
            elif int(-movement[0]) / 2 < int(-movement[1]):
                difference = int(-movement[1]) - int(-movement[0]) / 2
                return Vector2(int(movement[0]), int(movement[1] + difference))