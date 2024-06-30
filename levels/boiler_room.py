
from player import Player
from functions import *
from random import randrange
from levels import scape
class Boiler_Room:

    def __init__(self, player:Player):
        self.player = player

    def run(self):
        
        clear_console()
        print("""/*** SALA DE CALDERAS ***/""")

        print("""El calor de la sala de calderas es inaguantable, aunque te consuelas con la idea de que haya un hángar cerca con naves monoplaza en las que puedas escapar.\n""")

        state = self.player.get_state()

        if(state == True):
            self.level_without_hurts()
        elif(state == 'hurt'):
            self.level_with_hurts()
    
    # Método para seguir el camino cuando el jugador no tiene heridas

    def level_without_hurts(self):

        print("""Aún no te crees tu buena suerte. La sala de calderas está muy ajetreada y, aunque hace mucho calor, nadie se fija en ti.\n
              \rQuizás puedas llegar a un hangar y robar una nave monoplaza antes de que te descubran.\n
              \rVas explorando hasta que un capataz de la sala de calderas se encara contigo. Es una babosa gigante. Nunca pensaste que algo pudiera sudar tanto.\n
              \r-¿Quién eres tú? -te pregunta la babosa.\n
              \r¿Qué respondes?:\n
              \rA)-Soy un piloto de la nueva escuadra de exploración. Me he perdido. ¿Me puede llevar al hangar principal?\n
              \rB)-Soy un nuevo operario. Nadie me ha dicho que tengo que hacer y estoy perdido.""")
        option = choose_option()

        if(option == 'A'):
            print("""La babosa se ríe en tu cara.\n
                  \r-Menuda mentira más grande. Los pilotos de exploración ya se han ido. ¿Querías una nave para huir de aquí? No te preocupes. No creo que te haga falta.\n
                  \rLa babosa llama a unos cuantos subordinados y, aunque te resistes ferozmente, te encierran en una de las calderas. Mueres entre horribles sufrimientos y alaridos de dolor.\n""")
            game_over()
        elif(option == 'B'):
            self.fight_with_slug()
        
    # Método para seguir el camino cuando el jugador está herido

    def level_with_hurts(self):
        print("""La rata te dio un buen arañazo y te escuece. Tratas de pasar desapercibido, pero ves que algunos operarios de maquinarias se fijan en ti.\n
              \rLa situación no puede seguir así tienes dos opciones:\n
              \rA)Coger una máscara de protección que ves colgada en una argolla y ponértela.
              \rB)Tratar de seguir aparentando normalidad.""")
        
        option = choose_option()
        if(option == 'A'):
           self.fight_with_reptilian()
        elif(option == 'B'):
            self.fight_with_slug()
    
    # Método para la prueba de la babosa

    def fight_with_slug(self):
        print("""-Estos novatos. Siempre la lían el primer día. Ven conmigo.\n
              \rNo te queda más remedio que seguir a la babosa y te lleva hacia una caldera. Tratas de no sonreír porque al lado de esa caldera hay una puerta y, por el cartel, ves que allí se guardan las cápsulas de expulsión de emergencia.\n
              \rSi hubiera un accidente en la nave, los operarios de las calderas huirían en esas cápsulas, pero parece que esa es tu oportunidad.\n
              \r-Recoge toda esa basura y échala a la caldera. Luego puedes ir a comer.
              \rLa fortuna está de tu lado. Le das las gracias a la babosa y te fijas en la 'basura' de la que debes desahacerte.\n
              \r.Hay una pequeña varilla de hierro que puede servir como ganzúa. Se te ocurren dos opciones:\n
              \rA)La coges. Quizás necesites forzar la cerradura.
              \rB)Te han ordenado deshacerte de todo. Mejor ser discreto.""")
        
        self.choices_with_trash()

        items = self.player.items

        if(len(items) == 3):
            print("""Has pasado mucho tiempo rebuscando en la basura y has llamado la atención de la babosa.
                  \r-¿Qué estás cogiendo, novato?\n
                  \rComo ya no se fian de ti, pide ayuda a dos compañeros para examinarte y descubren la barra de metal ensangrentada, la ganzúa y el plano.\n
                  \r-Te has escapado de las celdas -descubre la babosa-. Has abusado de tu suerte al querer jugar conmigo.\n
                  \rSin decir nada más, coge la barra de hierro con la que mataste a la rata y te golpea con ella en la cabeza.\n
                  \rCuando caes al suelo, ya has muerto""")
            game_over()
        else:
            print("""Cuando suena la sirena, todos los operarios se van a comer. Nadie se fija en el nuevo, así que, fingiendo normalidad, te quedas junto al almacén de cápsulas de emergencia hasta que te quedas solo. Todos prefieren comer antes que prestarte atención.\n""")
            self.next_level()

    # Función para controlar la prueba del reptiliano

    def fight_with_reptilian(self):
        self.player.add_item('mascara')
        print("""Te pones la máscara y sigues tu camino. Te camuflas entre los demás operarios y todo parece ir bien hasta que alguien te grita por detrás.\n
                \r-¡Eh, tú! Ven a echar una mano.\n
                \rNo te queda otra que obedecer. Hay demasiada gente.\n
                Un reptiliano con las manos quemadas te señala una caldera abierta. Si no fuera por la máscara, tus ojos llorarían por el humo.\n
                \r-Cierra esa compuerta -te exige el reptiliano-. Yo me he quemado intentándolo.\n
                \r-No tengo guantes -respondes, sabiendo que si tocas la compuerta tú correrías el mismo destino que el reptiliano.\n
                \r-Me da igual -sisea el reptiliano amenazadoramente. Tienes dos opciones.\n
                \rA)Usar la barra de metal para cerrar la compuerta. Seguramente se quedé tan caliente que tengas que deshacerte de ella después.
                \rB)Negarte a usar la barra. Te fue útil con la rata. Quizas la necesites más adelante""")
        option = choose_option()
        if(option == "A"):
            self.player.delete_item("barra metal")
            print("""Usas la barra de metal para tratar de cerrar la compuerta, pero es una locura. No tienes guantes, el metal conduce el calor y pronto sientes cómo se te quema la piel.\n
                  \rEl reptiliano te mira con curiosidad. Decides jugarte el todo por el todo""")
            attempts = self.close_the_door()
            if(int(attempts) == 0):
                return True
            if(int(attempts) > 1):
                self.player.add_state('burned')
                print("""Has cerrado la compuerta y, aunque has sufrido quemaduras y has perdido la barra, podrás seguir adelante. La máscara oculta tus lágrimas de dolor.\n
                      \r-Muchas gracias por la ayuda, colega -se despide el reptiliano con guasa.\n
                      \rSuena la sirena que marca el turno de comida, pero a ti te indican que vayas a la enfermería. Nadie se preocupa por ti, así que, comiéndote el dolor por dentro, avanzas y ves un almacén con cápsulas de emergencia para huir en caso de accidente en la sala de calderas.\n
                      \rPor fin tienes algo de suerte""")
                self.next_level()
            else:
                self.player.add_state('without_hands')
                print("""Has cerrado la compuerta pero a qué coste. Tus manos han quedado completamente inutilizadas por la quemadura. Apenas puedes mover los dedos por el dolor.\n
                      \r-Muchas gracias por la ayuda, colega -se despide el reptiliano con guasa.\n
                      \rSuena la sirena de la comida y nadie se preocupa por ti. Ni te dicen que vayas a la enfermería. Quizás en esa prisión se deshagan de los tullidos. Sin embargo, cuando te quedas solo en la sala de calderas, ves un almacén de cápsulas de emergencia para huir en caso de accidente en la sala de calderas.\n
                      \rVas hacia allí, aunque te preguntas cómo vas a abrir la puerta en tu estado.\n""")
                self.next_level()
        elif(option == "B"):
            print("""Los reptilianos, al igual que muchas otras razas de alien de la galaxia, no aceptan un no por respuesta.\n
                  \rSe abalanza sobre ti y tratas de defenderte con la barra de metal, pero esta pelea no es como la de la rata. Ahí estás en inferioridad numérica y pronto te reducen y te ceban a golpes hasta quedar seguros de que has muerto.\n""")
            game_over()
    
    # Método para escoger las opciones de items entre la basura

    def choices_with_trash(self):
        option = choose_option()
        if(option == 'A'):
            self.player.add_item('ganzúa')
            print('Coges la ganzúa\n')
        elif(option == 'B'):
            print('Dejas la ganzúa')
        print("""Rebuscando en la basura también encuentras un pequeño mapa de coordenadas. A saber cómo llegó allí. Tal vez un oficial lo tiró a la basura porque se le cayó café encima, pero a ti podría serte útil.\n
              \rA)Coges el mapa.\n
              \rB)Dejas el mapa""")
        option = choose_option()
        if(option == 'A'):
            self.player.add_item('mapa')
            print('Coges el mapa.\n')
        elif(option == 'B'):
            print('Dejas el mapa.\n')

    #Método para configurar la opción de cerrar la compuerta de la sala de calderas

    def close_the_door(self):

        attempts = 3

        while attempts > 0:
            push = randrange(0,2)
            if(push == 1):
                print("""Usando todas tus fuerzas has conseguido cerrar la compuerta\n""")
                return attempts
            else:
                print("""No has conseguido cerrar la compuerta. Sigues intentándolo""")
                input("Pulsa cualquier tecla para intentarlo de nuevo")
                attempts = attempts - 1

        if(attempts == 0):
            print("""Lloras de dolor al ver las quemaduras de tus manos. El reptiliano se ríe ante tus alaridos, que llaman la atención de todos.\n
                  \rUn ogro espacial se acerca a ti.\n
                  \r-Esa máscara es mía. ¡Me la has robado!\n
                  \rNunca hay que robar a un ogro espacial. Lo descubres cuando te levanta y te rompe el cuello de un movimiento brusco""")
            game_over()
            return attempts
    
    #Método para señalar el paso de nivel

    def next_level(self):

        next_step = scape.Scape(self.player)
        next_level()
        next_step.run()