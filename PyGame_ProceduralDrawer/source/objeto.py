import pygame
import math

"""   Documentación:
   Clase para crear objetos con formas básicas en Pixel Art.

   Parámetros:
       x (int): Coordenada x del centro del objeto.
       y (int): Coordenada y del centro del objeto.
       size (int): Tamaño del objeto (radio, lado, etc.).
       shape (str): Forma del objeto ('circle', 'square', 'polygon', 'triangle').
       num_vertices (int or list): Número de vértices para polígonos regulares o lista de puntos para polígonos irregulares.
       color (tuple): Color del relleno en formato RGB (r, g, b).
       border_color (tuple or None): Color del borde en formato RGB (r, g, b) o None para sin borde.
       border_thickness (int): Grosor del borde.
       border_type (str): Tipo de borde ('solid', 'dashed', 'dotted').
       screw_head (bool): Indicador de si el círculo debe tener una forma de "cabeza de tornillo".
       no_fill (bool): Indicador de si se debe dibujar solo el borde sin relleno.

   Métodos:
       draw(surface): Dibuja el objeto en la superficie especificada.

   Uso:
       # Crear un círculo con relleno blanco y borde negro
       objeto_circulo = Objeto(100, 100, 50, 'circle', color=(255, 255, 255), border_color=(0, 0, 0), border_thickness=2)

       # Crear un cuadrado sin relleno y borde rojo punteado
       objeto_cuadrado = Objeto(300, 100, 50, 'square', color=(0, 0, 0), border_color=(255, 0, 0), border_thickness=2, border_type='dotted', no_fill=True)
   """


class Object:
    def __init__(self, x, y, size, shape, num_vertices=0, color=(255, 255, 255),
                 border_color=None, border_thickness=0, border_type='solid',
                 screw_head=False, no_fill=False):
        self.x = x
        self.y = y
        self.size = size
        self.shape = shape
        self.num_vertices = num_vertices
        self.color = color
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.border_type = border_type
        self.screw_head = screw_head
        self.no_fill = no_fill

    def draw(self, surface):
        if self.shape == 'circle':
            # Dibujar un círculo con modificaciones para "cabeza de tornillo"
            if self.screw_head:
                points = []
                for i in range(self.num_vertices):
                    angle = i * (2 * math.pi / self.num_vertices)
                    x = self.x + self.size * math.cos(angle)
                    y = self.y + self.size * math.sin(angle)
                    points.append((x, y))
                # Agregar puntos adicionales para "cabeza de tornillo"
                for i in range(self.num_vertices):
                    angle = (i + 0.5) * (2 * math.pi / self.num_vertices)
                    x = self.x + self.size * 0.5 * math.cos(angle)
                    y = self.y + self.size * 0.5 * math.sin(angle)
                    points.append((x, y))
                pygame.draw.polygon(surface, self.color, points)
                if not self.no_fill:  # Dibujar relleno solo si NoFill es False
                    pygame.draw.polygon(surface, self.color, points)
                if self.border_thickness > 0 and self.border_color is not None:
                    pygame.draw.polygon(surface, self.border_color, points, self.border_thickness)
            else:
                # Dibujar un círculo normal si no se quiere la modificación de "cabeza de tornillo"
                pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)
                if not self.no_fill:  # Dibujar relleno solo si NoFill es False
                    pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)
                if self.border_thickness > 0 and self.border_color is not None:
                    pygame.draw.circle(surface, self.border_color, (self.x, self.y), self.size, self.border_thickness)

        elif self.shape == 'square':
            if not self.no_fill:  # Dibujar relleno solo si NoFill es False
                pygame.draw.rect(surface, self.color, (self.x - self.size, self.y - self.size,
                                                       self.size * 2, self.size * 2))
            if self.border_thickness > 0 and self.border_color is not None:
                pygame.draw.rect(surface, self.border_color, (self.x - self.size, self.y - self.size,
                                                              self.size * 2, self.size * 2),
                                 self.border_thickness)

        elif self.shape == 'polygon':
            if self.num_vertices > 2:
                points = []
                for i in range(self.num_vertices):
                    angle = i * (2 * math.pi / self.num_vertices)
                    x = self.x + self.size * math.cos(angle)
                    y = self.y + self.size * math.sin(angle)
                    points.append((x, y))
                if not self.no_fill:  # Dibujar relleno solo si NoFill es False
                    pygame.draw.polygon(surface, self.color, points)
                if self.border_thickness > 0 and self.border_color is not None:
                    pygame.draw.polygon(surface, self.border_color, points, self.border_thickness)
            else:
                if isinstance(self.num_vertices, list) and len(self.num_vertices) > 2:
                    if not self.no_fill:  # Dibujar relleno solo si NoFill es False
                        pygame.draw.polygon(surface, self.color, self.num_vertices)
                    if self.border_thickness > 0 and self.border_color is not None:
                        pygame.draw.polygon(surface, self.border_color, self.num_vertices, self.border_thickness)
                else:
                    raise ValueError('Para polígonos irregulares, se debe proporcionar una lista de al menos 3 puntos')

        elif self.shape == 'triangle':
            if self.num_vertices == 3:
                if 'angles' in self.__dict__:
                    points = [(self.x, self.y - self.size)]
                    angle1 = -self.angles[0] / 2
                    angle2 = self.angles[0] / 2
                    for i in range(2):
                        x = self.x + self.size * math.cos(math.radians(angle1 if i == 0 else angle2))
                        y = self.y + self.size * math.sin(math.radians(angle1 if i == 0 else angle2))
                        points.append((x, y))
                        angle1 += 120
                        angle2 += 120
                else:
                    points = [(self.x, self.y - self.size)]
                    for i in range(2):
                        angle = (i + 1) * 120
                        x = self.x + self.size * math.cos(math.radians(angle))
                        y = self.y + self.size * math.sin(math.radians(angle))
                        points.append((x, y))
                if not self.NoFill:  # Dibujar relleno solo si NoFill es False
                    pygame.draw.polygon(surface, self.color, points)
                if self.border_thickness > 0 and self.border_color is not None:
                    pygame.draw.polygon(surface, self.border_color, points, self.border_thickness)
            else:
                raise ValueError('Los triángulos deben tener exactamente 3 vértices')

        else:
            raise ValueError(f'Forma de objeto inválida: {self.shape}')
