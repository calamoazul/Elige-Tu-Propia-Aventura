

class Player:

    #Constructor para configurar al jugador
    def __init__(self, name):
        self.name = name
        self.items = []
        self.state = True
    # Método para comprobar si se tiene un item del inventario
    def get_item(self, item):

        if item in self.items:
            return True
        else:
            return False

    # Método para añadir un item al inventario
    def add_item(self, item):
        if item in self.items:
            return False
        elif(len(self.items) > 5):
            return False
        elif item not in self.items and len(self.items) <= 5:
            self.items.append(item)
            return True

    # Método para eliminar un item del inventario
    def delete_item(self, item):
        
        if item not in self.items:
            return False
        elif item in self.items:
            self.items.remove(item)
            return True
        
    # Método para ver el estado del jugador

    def get_state(self):
        return self.state
    
    # Método para cambiar el estado del jugador

    def add_state(self, state):
        self.state = state

    # Método para restaurar el estado del jugador
    def restore_state(self):
        self.state = True