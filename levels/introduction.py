
from functions import *
from player import Player
from levels import boiler_room
from random import randrange
class Introduction:

    def __init__(self):
        self.run()
        self.player = None

    def set_player(self):
        name_player  = input("¿Cómo te llamas? \n\r")
        if(len(name_player) > 0 and str(name_player)):
            self.player = Player(name_player)
        else: 
            print("Debes escribir un nombre de al menos una letra. Otra vez.\n")
            self.set_player()

    def run(self):

        #Inicio del juego
        print("/***ESCAPA DE LA PRISIÓN ESPACIAL***/")

        # Configuración del juegador
        self.set_player()


        print("""{}, estás atrapado en una prisión espacial con un compañero.\n
        \rTratáis de huir y en vuestra huida por los pasillos de la prisión encontráis un alien vikingo.\n
        \rTenéis dos opciones:\n
        \rA) Hacerte el dormido\n
        \rB)Tratar de huir por un conducto de ventilación que se encuentra a tu derecha\n""".format(self.player.name))
        option = choose_option()

        if(option == "A"):
            self.option_sleep()
        elif(option == "B"):
            self.option_run()

    def option_sleep(self):
        print("""Has decidido echarte una siesta. El alien vikingo no es tonto y, después de matar a tu compañero, centra su atención en ti.\n
            \rComo ve que estás fingiendo y le has tomado por tonto, decide acabar contigo.\n""")
        game_over()
        
    def option_run(self):
        print("""Hiciste bien en escoger la opción de huida. Mientras el alien vikingo acaba con tu compañero, logras huir por el conducto de ventilación\n
              \rEl calor es asfixiante, pero logras llegar a un almacén. Allí encuentras una barra metálica. ¿Qué vas a hacer?\n
              \rA)Coger la barra metálica\n
              \rB) Dejarla ahí \n""")
        option = choose_option()
        if(option == "A"):
            self.player.add_item("barra metal")
            print("Has cogido la barra de metal\n")
        else:
            print("""Dejas la barra de metal\n""")
        print("""Sales del almacén. El ambiente apesta, como si estuvieras en las alcantarillas. Tal vez estás cerca de la zona de residuos.\n
            \rCaminando, llegas a una puerta donde ves un cartel que reza: 'Salida de emergencia'. Por desgracia para ti, hay una rata con kimono y un palo de madera que la vigila.\n
            \rLa rata te habla:\n
            \r-Te dejaré pasar si resuelves un acertijo.\n
            \rParece demasiado bonito para ser verdad. Por eso estás entre dos opciones:\n
            \rA)Pelear con la rata. No parece muy fuerte.
            \rB)Tratar de adivinar su acertijo""")
        option = choose_option()
        if(option == "A"):
            if(self.player.get_item("barra metal")):
                return self.fight_with_item()
            else:
                return self.fight_without_item()
        elif(option == "B"):
            self.rat_question()
        
    def fight_with_item(self):
        print("""La rata no se esperaba esa agresividad por tu parte. Gracias a tu barra de metal consigues desarmarla, aunque te llevas un arañazo en la cara antes de aturdirla.\n
              \rAbres la puerta de salida de emergencia y descubres que has llegado a la sala de calderas de la prisión. ¿Podrás pasar inadvertido?""")
        self.player.add_state('hurt')
        self.next_level()

    def fight_without_item(self):
        print("""La rata no se esperaba tanta agresividad. Tampoco que fueras tan tonto.\n
              \rAl ser una maestra de las artes marciales y con ayuda de su bastón te noquea enseguida.\n
              \r-Te di a escoger entre la vida y la muerte y escogiste la muerte, serpiente asquerosa.\n
              \rTu vista se oscurece y sabes que nunca más volverás a abrir los ojos.""")
        game_over()

    def rat_question(self):

        number = randrange(1,11)
        attempts = 3
        print("""Escoges la opción del acertijo. Te parece la opción más sensata. Esa rata parece muy peligrosa.\n
              \r-Usa tu mente. Fluye en mi consciencia. Adivina en qué número estoy pensando. Si no aciertas en tres intentos te mataré.\n
              \rUn sudor frío te recorre la espalda.\n
              \r-Te daré una pista. Estoy pensando un número del uno al cinco.""")
        while(attempts > 0):
            answer = self.answer_rat_question(number)
            if(answer):
                print("""La rata sonríe ante tu nivel de concentración mental.\n
                      \r-Has superado la prueba. Puedes pasar. Aunque ten cuidado. Esta prisión esconde peligros mucho peores que yo.\n""")
                return self.next_level()
            else:
                print("""La rata frunce el ceño.\n
                      \r-Te queda un intento menos""")
                attempts = attempts - 1
        if(attempts == 0):
            print("""La rata se acerca a ti alzando su bastón de madera.\n
                  \r-Alguien que no es capaz de adivinar un número en tres intentos no merece vivir.\n
                  \rApenas te da tiempo a defenderte. La oscuridad se cierne ante ti""")
            game_over()    
    
    def answer_rat_question(self, number):
        try:
            answer = input("¿En qué número está pensando la rata?\n\r")
            if(int(answer) and int(answer) > 5 or int(answer) < 1):
                print("No te la juegues di un número\n")
                self.answer_rat_question(number)
            if(int(answer) == number):
                return True
            else:
                return False
        except TypeError:
            print("No te la juegues di un número\n")
            self.answer_rat_question(number)
    def next_level(self):
        next_step = boiler_room.Boiler_Room(self.player)
        next_level()
        next_step.run()