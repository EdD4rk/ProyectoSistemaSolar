import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

pygame.init()
display = (1050, 700)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_DEPTH_TEST)

glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

# Habilitar brillo en los materiales
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)

def load_texture(image_path, flip_y=False):
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    image = pygame.image.load(image_path).convert_alpha()
    if flip_y:
        image = pygame.transform.flip(image, False, True)
    
    img_data = pygame.image.tostring(image, "RGBA", True)
    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    
    return texture

background_texture = load_texture("./images/universo.png")

def draw_background(rotation_angle=0):
    """Dibuja la imagen de fondo ocupando toda la pantalla con rotación."""
    glDisable(GL_DEPTH_TEST)  
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)  
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, background_texture)

    # Rotación del fondo
    glRotatef(rotation_angle, 0, 0, 1)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(-1.5, -1.5)
    glTexCoord2f(1, 0); glVertex2f(1.5, -1.5)
    glTexCoord2f(1, 1); glVertex2f(1.5, 1.5)
    glTexCoord2f(0, 1); glVertex2f(-1.5, 1.5)
    glEnd()

    glDisable(GL_TEXTURE_2D)

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)  

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 0, 1))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.8, 0.8, 0.8, 1.0))
glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))

planet_data = [
    ("mercury", 1.5, 0.2), ("venus", 2.0, 0.3), ("earth", 2.5, 0.35),
    ("mars", 3.0, 0.25), ("jupiter", 4.5, 0.7), ("saturn", 5.5, 0.6),
    ("uranus", 6.5, 0.5), ("neptune", 7.5, 0.4)
]

esfera = gluNewQuadric()
gluQuadricTexture(esfera, GL_TRUE)

textures = {
    "sun": load_texture("./images/Sun.png"),
    "mercury": load_texture("./images/Mercury.png"),
    "venus": load_texture("./images/Venus.png"),
    "earth": load_texture("./images/Earth.png"),
    "mars": load_texture("./images/Mars.png"),
    "jupiter": load_texture("./images/Jupiter.png"),
    "saturn": load_texture("./images/Saturn.png"),
    "uranus": load_texture("./images/Uranus.png"),
    "neptune": load_texture("./images/Neptune.png"),
}

# Clase para asteroides
class Asteroid:
    def __init__(self):
        self.distance = random.uniform(1.0, 8.0)
        self.angle = random.uniform(0, 2 * math.pi)
        self.size = random.uniform(0.02, 0.06)
        self.speed = random.uniform(0.002, 0.008)
        self.z_offset = random.uniform(-0.5, 0.5)
        self.color = (random.uniform(0.5, 0.9), random.uniform(0.5, 0.9), random.uniform(0.5, 0.9))
    
    def update(self):
        self.angle += self.speed
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi
    
    def draw(self):
        glPushMatrix()
        glDisable(GL_TEXTURE_2D)
        glColor3f(*self.color)
        x = math.cos(self.angle) * self.distance
        y = math.sin(self.angle) * self.distance
        glTranslatef(x, y, self.z_offset)
        gluSphere(esfera, self.size, 8, 8)
        glPopMatrix()

# Crear asteroides
asteroids = [Asteroid() for _ in range(80)]

def draw_planet(texture, distance, size, angle_offset, rotation_angle=0, is_sun=False):
    """Dibuja un planeta con su textura en una posición dada."""
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture)
    glEnable(GL_TEXTURE_2D)

    x = math.cos(angle_offset) * distance
    y = math.sin(angle_offset) * distance
    glTranslatef(x, y, 0)

    glRotatef(rotation_angle, 0, 0, 1)
    
    # Ajustar brillo según el objeto
    if is_sun:
        # El sol es mucho más brillante
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0.8, 0.6, 0.2, 1.0))
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 100)
    else:
        # Planetas con brillo proporcional a su tamaño
        brightness = min(size * 1.5, 1.0)
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0.0, 0.0, 0.0, 1.0))
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (brightness, brightness, brightness, 1.0))
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50 + size * 30)

    gluSphere(esfera, size, 32, 16)
    
    # Resetear emisión
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0.0, 0.0, 0.0, 1.0))
    
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    
    return (x, y, 0)  # Retorna la posición del planeta

def draw_orbits():
    """Dibuja las órbitas de los planetas."""
    glColor3f(0.5, 0.5, 0.5)
    glDisable(GL_LIGHTING)
    for distance in [p[1] for p in planet_data]:
        glBegin(GL_LINE_LOOP)
        for i in range(100):
            angle = 2 * math.pi * i / 100
            glVertex3f(math.cos(angle) * distance, math.sin(angle) * distance, 0)
        glEnd()
    glEnable(GL_LIGHTING)

def get_camera_position(focus_object, angle, planet_positions):
    """Calcula la posición de la cámara según el objeto enfocado."""
    if focus_object == 0:  # Sol
        return (0, -6, 5, 0, 0, 0)
    else:  # Planetas
        planet_idx = focus_object - 1
        planet_pos = planet_positions[planet_idx]
        distance = planet_data[planet_idx][1]
        size = planet_data[planet_idx][2]
        
        # Cámara posicionada para ver el planeta y el sol
        offset_distance = size * 4 + 1.5
        cam_x = planet_pos[0] + math.cos(angle + math.pi/4) * offset_distance
        cam_y = planet_pos[1] + math.sin(angle + math.pi/4) * offset_distance
        cam_z = size * 3 + 1.0
        
        return (cam_x, cam_y, cam_z, planet_pos[0], planet_pos[1], planet_pos[2])

# Variables de cámara
camera_x, camera_y, camera_z = 0, -10, 10
look_x, look_y, look_z = 0, 0, 0
angle = 0
sun_rotation_angle = 0  
background_rotation = 0

zoom_level = 10  
zoom_sensitivity = 0.1  
focus_object = None  # 0=Sol, 1=Mercurio, 2=Venus, etc., None=vista general
transition_progress = 0
transition_speed = 0.05
target_camera = None

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                focus_object = None
                transition_progress = 0
            else:
                run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  
                zoom_level = max(2, zoom_level - zoom_sensitivity)
            elif event.button == 5:  
                zoom_level = min(20, zoom_level + zoom_sensitivity)
        
        # Teclas numéricas para enfocar objetos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                focus_object = 0
                transition_progress = 0
            elif event.key == pygame.K_1:
                focus_object = 1
                transition_progress = 0
            elif event.key == pygame.K_2:
                focus_object = 2
                transition_progress = 0
            elif event.key == pygame.K_3:
                focus_object = 3
                transition_progress = 0
            elif event.key == pygame.K_4:
                focus_object = 4
                transition_progress = 0
            elif event.key == pygame.K_5:
                focus_object = 5
                transition_progress = 0
            elif event.key == pygame.K_6:
                focus_object = 6
                transition_progress = 0
            elif event.key == pygame.K_7:
                focus_object = 7
                transition_progress = 0
            elif event.key == pygame.K_8:
                focus_object = 8
                transition_progress = 0
            elif event.key == pygame.K_x:
                focus_object = None
                transition_progress = 0

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Actualizar rotación del fondo
    background_rotation += 0.02
    if background_rotation > 360:
        background_rotation -= 360

    draw_background(background_rotation)

    glLoadIdentity()
    
    # Guardar posiciones de planetas para la cámara
    planet_positions = []
    
    # Calcular posiciones actuales de planetas
    sun_pos = (0, 0, 0)
    for i, (name, distance, size) in enumerate(planet_data):
        x = math.cos(angle + i) * distance
        y = math.sin(angle + i) * distance
        planet_positions.append((x, y, 0))
    
    # Configurar cámara
    if focus_object is not None:
        target_camera = get_camera_position(focus_object, angle, planet_positions)
        if transition_progress < 1:
            transition_progress += transition_speed
            # Interpolación suave
            t = transition_progress
            cam_x = camera_x + (target_camera[0] - camera_x) * t
            cam_y = camera_y + (target_camera[1] - camera_y) * t
            cam_z = camera_z + (target_camera[2] - camera_z) * t
            look_x = look_x + (target_camera[3] - look_x) * t
            look_y = look_y + (target_camera[4] - look_y) * t
            look_z = look_z + (target_camera[5] - look_z) * t
        else:
            cam_x, cam_y, cam_z = target_camera[0], target_camera[1], target_camera[2]
            look_x, look_y, look_z = target_camera[3], target_camera[4], target_camera[5]
        
        gluLookAt(cam_x, cam_y, cam_z, look_x, look_y, look_z, 0, 0, 1)
    else:
        # Vista general
        if transition_progress < 1:
            transition_progress += transition_speed
            t = transition_progress
            cam_x = camera_x + (0 - camera_x) * t
            cam_y = camera_y + (-10 - camera_y) * t
            cam_z = camera_z + (zoom_level - camera_z) * t
        else:
            cam_x, cam_y, cam_z = 0, -10, zoom_level
        
        camera_x, camera_y, camera_z = cam_x, cam_y, cam_z
        gluLookAt(camera_x, camera_y, camera_z, 0, 0, 0, 0, 0, 1)

    draw_orbits()
 
    draw_planet(textures["sun"], 0, 1.0, 0, sun_rotation_angle, is_sun=True)
    
    for i, (name, distance, size) in enumerate(planet_data):
        draw_planet(textures[name], distance, size, angle + i, sun_rotation_angle * 0.3, is_sun=False)
    
    # Actualizar y dibujar asteroides
    for asteroid in asteroids:
        asteroid.update()
        asteroid.draw()
 
    angle += 0.01
    sun_rotation_angle += 0.5

    pygame.display.flip()
    clock.tick(60)

pygame.quit()