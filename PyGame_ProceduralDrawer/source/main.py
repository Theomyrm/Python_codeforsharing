import pygame
from objeto import Object
from custom_shape import ObjectCustom


def save_to_png(surface, filename):
    pygame.image.save(surface, filename)

def main(background_color=(255, 255, 255)):
    # Initialize Pygame
    pygame.init()

    # Dimensiones de la pantalla
    width, height = 1024, 768

    # Crear la ventana de visualización
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Generación de Figuras Procedurales')

    # Crear objetos
    objeto_circulo = Object(100, 100, 50, 'circle')
    objeto_cuadrado = Object(300, 100, 50, 'square')

    # Create an instance of ObjectCustom to use the crear_figura_personalizada method
    custom_object = ObjectCustom()

    # Crear la ruleta personalizada
    # Crear la ruleta con 12 slots
    ruleta = ObjectCustom.crear_figura_personalizada(base_shape='circle', size=150, num_divisions=12, color=(255, 0, 150),
                                                     num_slots=12, border_thickness=1, border_color=(0, 0, 0))

    # Bucle principal del juego
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Limpiar la pantalla
        screen.fill(background_color)

        # Dibujar objetos en pantalla
        # objeto_circulo.draw(screen)
        # objeto_cuadrado.draw(screen)
        ruleta.x = width // 2
        ruleta.y = height // 2
        # Dibujar la ruleta si es un objeto complejo
        if isinstance(ruleta, ObjectCustom):
            ruleta.draw(screen)
        # Actualizar la pantalla
        pygame.display.flip()
        #To png
        save_to_png(screen, "resultado.png")
    # Cerrar Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
