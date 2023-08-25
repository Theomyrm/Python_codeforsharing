import math
import pygame
from objeto import Object


class ObjectCustom:

    def __init__(self, base_shape=None, size=0, num_vertices=0, color=(255, 255, 255), border_color=None,
                 border_thickness=0, border_type='solid', screw_head=False, no_fill=False):
        self.base_shape = base_shape
        self.size = size
        self.num_vertices = num_vertices
        self.color = color
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.border_type = border_type
        self.screw_head = screw_head
        self.no_fill = no_fill
        self.custom = True  # Indicar que el objeto es personalizado
        self.x = 0
        self.y = 0

    @staticmethod
    def crear_figura_personalizada(base_shape, size, num_divisions, color=(255, 255, 255), border_color=None,
                                   border_thickness=0, screw_head=True, num_slots=12):
        """
        Crea una figura personalizada basada en una figura base con polígonos adicionales (slots) dentro.

        Parámetros:
            - base_shape (str): La forma base de la figura ('circle', 'square', 'polygon', 'triangle').
            - size (int): El tamaño de la figura.
            - num_divisions (int): El número de divisiones en la ruleta.
            - color (tuple): El color de la figura en formato RGB (por defecto es blanco).
            - border_color (tuple): El color del borde de la figura en formato RGB (por defecto es None, sin borde).
            - border_thickness (int): El grosor del borde de la figura (por defecto es 0, sin borde).
            - screw_head (bool): True para aplicar la modificación "cabeza de tornillo" en el círculo base.
            - num_slots (int): El número de polígonos adicionales (slots) dentro de la figura.

        Retorna:
            - Objeto: Un objeto que representa la figura personalizada con los slots.
        """
        # Crear el objeto base según la forma especificada
        if base_shape == 'circle':
            base_object = Object(0, 0, size, 'circle', num_vertices=num_divisions, color=color,
                                 border_color=border_color,
                                 border_thickness=border_thickness, screw_head=screw_head)
        elif base_shape == 'square':
            base_object = Object(0, 0, size, 'square', color=color, border_color=border_color,
                                 border_thickness=border_thickness)
        elif base_shape == 'polygon':
            base_object = Object(0, 0, size, 'polygon', num_vertices=num_divisions, color=color,
                                 border_color=border_color,
                                 border_thickness=border_thickness)
        elif base_shape == 'triangle':
            base_object = Object(0, 0, size, 'triangle', num_vertices=num_divisions, color=color,
                                 border_color=border_color,
                                 border_thickness=border_thickness)
        else:
            raise ValueError(f'Forma de figura base inválida: {base_shape}')

        # Agregar el efecto de "cabeza de tornillo" si es un círculo y screw_head es True
        if base_shape == 'circle' and screw_head:
            base_object.screw_head = True

        # Calcular el ángulo de separación entre cada división en la ruleta
        angle_step = 2 * math.pi / num_divisions

        # Calcular el ángulo de separación entre cada slot (polígono adicional)
        slot_angle_step = 2 * math.pi / num_slots

        # Crear una lista para almacenar todas las divisiones de la ruleta
        divisions = []

        # Crear cada división y agregarla a la lista
        for i in range(num_divisions):
            # Calcular el ángulo para la posición de la división
            angle = i * angle_step

            # Calcular las coordenadas del punto final de la división
            x = size * math.cos(angle)
            y = size * math.sin(angle)

            # Agregar la división a la lista
            divisions.append((x, y))

        # Crear los polígonos adicionales (slots) y agregarlos a la lista de divisiones
        for i in range(num_slots):
            # Calcular el ángulo para la posición del slot
            slot_angle = i * slot_angle_step

            # Calcular las coordenadas del punto final del slot
            slot_x = size * 0.5 * math.cos(slot_angle)
            slot_y = size * 0.5 * math.sin(slot_angle)

            # Agregar el slot a la lista de divisiones
            divisions.append((slot_x, slot_y))
        # Calcular el ángulo de separación entre cada división en la ruleta
        angle_step = 2 * math.pi / num_divisions

        # Crear una lista para almacenar todas las divisiones de la ruleta
        divisions = []

        # Crear cada división y agregarla a la lista
        for i in range(num_divisions):
            # Calcular el ángulo para la posición de la división
            angle = i * angle_step

            # Calcular las coordenadas del punto final de la división
            x = size * math.cos(angle)
            y = size * math.sin(angle)

            # Agregar la división a la lista
            divisions.append((x, y))

        # Crear la figura personalizada con las divisiones
        # Asegurarnos de que el último vértice no sea igual al primero
        if divisions[0] != divisions[-1]:
            divisions.append(divisions[0])

        # Crear la figura personalizada con las divisiones
        custom_figure = ObjectCustom(base_shape='polygon', size=size, num_vertices=divisions, color=color,
                                     border_color=border_color, border_thickness=border_thickness,
                                     screw_head=screw_head)

        return custom_figure

    def draw(self, surface):
        if self.base_shape == 'circle':
            # Dibujar un círculo con modificaciones para "cabeza de tornillo"
            points = []
            for i in range(len(self.num_vertices)):
                x, y = self.num_vertices[i]
                points.append((self.x + x, self.y + y))
            pygame.draw.polygon(surface, self.color, points)
            if not self.no_fill:  # Draw fill only if no_fill is False
                pygame.draw.polygon(surface, self.color, points)
            if self.border_thickness > 0 and self.border_color is not None:
                pygame.draw.polygon(surface, self.border_color, points, self.border_thickness)

        elif self.base_shape == 'polygon':
            # Dibujar un polígono con modificaciones si es necesario
            points = []
            for i in range(len(self.num_vertices)):
                x, y = self.num_vertices[i]
                points.append((self.x + x, self.y + y))
            pygame.draw.polygon(surface, self.color, points)
            if not self.no_fill:  # Draw fill only if no_fill is False
                pygame.draw.polygon(surface, self.color, points)
            if self.border_thickness > 0 and self.border_color is not None:
                pygame.draw.polygon(surface, self.border_color, points, self.border_thickness)
        else:
            raise ValueError(f'Forma de objeto inválida: {self.base_shape}')
