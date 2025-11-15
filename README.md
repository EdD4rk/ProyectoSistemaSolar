# Sistema Solar 3D Interactivo

Una simulación 3D del sistema solar desarrollada con Python, Pygame y OpenGL que permite visualizar los planetas orbitando alrededor del Sol con controles interactivos y cámara dinámica.

---
<img width="1366" height="768" alt="Captura de pantalla 2025-11-14 234203" src="https://github.com/user-attachments/assets/8686bda7-bf13-404c-851a-aebb44502d71" />
---

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación](#instalación)
- [Uso del Programa](#uso-del-programa)
- [Controles](#controles)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Documentación Técnica](#documentación-técnica)
- [Solución de Problemas](#solución-de-problemas)
- [Licencia](#licencia)

---

## Descripción

El **Sistema Solar 3D Interactivo** es una aplicación educativa que simula nuestro sistema solar en tiempo real. Incluye los 8 planetas principales, el Sol como fuente de luz, un cinturón de asteroides animado y un sistema de cámara que permite explorar cada cuerpo celeste individualmente.

El proyecto utiliza renderizado 3D con OpenGL, iluminación realista basada en el modelo Phong, texturas de alta calidad y animaciones fluidas a 60 FPS.

### Tecnologías Utilizadas

- **Python 3.7+**: Lenguaje de programación principal
- **Pygame 2.0+**: Gestión de ventanas, eventos y carga de recursos
- **PyOpenGL 3.1.5+**: Renderizado 3D en tiempo real
- **OpenGL**: API gráfica para renderizado de geometría y texturas

---

## Características

### Visualización 3D
- Renderizado en tiempo real de 8 planetas con texturas realistas
- Sol con emisión de luz propia y sistema de iluminación Phong
- 80 asteroides animados con propiedades aleatorias
- Órbitas planetarias visualizadas como guías circulares
- Fondo espacial estrellado con efecto de rotación

### Sistema de Cámara Interactiva
- Vista general del sistema solar completo
- Enfoque individual en cada planeta con transiciones suaves
- Control de zoom mediante rueda del mouse
- Cámara orbital que sigue a los planetas automáticamente

### Rendimiento Optimizado
- 60 fotogramas por segundo constantes
- Z-buffering para renderizado correcto de profundidad
- Double buffering para eliminar parpadeos
- Geometría optimizada con niveles de detalle variables

---

## Requisitos del Sistema

### Hardware Mínimo
- **Procesador**: Dual-core 2.0 GHz
- **Memoria RAM**: 2 GB
- **Tarjeta Gráfica**: Compatible con OpenGL 2.1, 256 MB VRAM
- **Almacenamiento**: 50 MB disponibles

### Hardware Recomendado
- **Procesador**: Quad-core 2.5 GHz o superior
- **Memoria RAM**: 4 GB o más
- **Tarjeta Gráfica**: Compatible con OpenGL 3.3+, 512 MB VRAM
- **Almacenamiento**: 100 MB disponibles

### Software Requerido
- **Sistema Operativo**: Windows 7, 8, 10 u 11
- **Python**: Versión 3.7 o superior
- **pip**: Gestor de paquetes de Python

---

## Instalación

### 1. Verificar Python

Antes de comenzar, verifica que tienes Python instalado en tu sistema. Abre una terminal (CMD o PowerShell) y ejecuta:

```bash
python --version
```

Deberías ver una salida similar a:
```
Python 3.x.x
```

Si Python no está instalado, descárgalo desde [python.org](https://www.python.org/downloads/) y asegúrate de marcar la opción **"Add Python to PATH"** durante la instalación.

### 2. Clonar o Descargar el Repositorio

Descarga el proyecto desde GitHub:

```bash
git clone https://github.com/EdD4rk/ProyectoSistemaSolar.git
cd ProyectoSistemaSolar
```

O descarga el archivo ZIP desde GitHub y extráelo en una carpeta de tu preferencia.

### 3. Crear un Entorno Virtual (Recomendado)

Es recomendable crear un entorno virtual para mantener las dependencias aisladas:

```bash
python -m venv venv
```

Activa el entorno virtual:

```bash
venv\Scripts\activate
```

Deberías ver `(venv)` al inicio de tu línea de comandos.

### 4. Instalar pip (si no está instalado)

Si no tienes **pip** instalado, descárgalo y ejecútalo con el siguiente comando:

```bash
python get-pip.py
```

Para verificar que pip está instalado correctamente:

```bash
pip --version
```

### 5. Actualizar pip

Asegúrate de tener la última versión de pip:

```bash
python -m pip install --upgrade pip
```

### 6. Instalar las Dependencias

Una vez tengas `pip` instalado, ejecuta los siguientes comandos para instalar todas las dependencias necesarias: `pygame`, `PyOpenGL`, `PyOpenGL-accelerate`

```bash
pip install pygame
pip install PyOpenGL
pip install PyOpenGL-accelerate
```

**Nota**: `PyOpenGL-accelerate` es opcional pero mejora significativamente el rendimiento. Si tienes problemas instalándolo, puedes omitirlo.

### 7. Verificar la Instalación

Verifica que todas las librerías se instalaron correctamente:

```bash
pip list
```

Deberías ver en la lista:
```
pygame               2.x.x
PyOpenGL             3.x.x
PyOpenGL-accelerate  3.x.x
```

### 8. Verificar la Estructura de Archivos

Asegúrate de que la carpeta del proyecto tenga la siguiente estructura:

```
ProyectoSistemaSolar/
├── SistemaSolar.py
└── images/
    ├── universo.png
    ├── Sun.png
    ├── Mercury.png
    ├── Venus.png
    ├── Earth.png
    ├── Mars.png
    ├── Jupiter.png
    ├── Saturn.png
    ├── Uranus.png
    └── Neptune.png
```

**Importante**: Sin la carpeta `images/` y sus texturas, el programa no funcionará correctamente.

### 9. Ejecutar el Proyecto

Finalmente, ejecuta el script `SistemaSolar.py` para iniciar el sistema solar 3D:

```bash
python SistemaSolar.py
```

Si todo está configurado correctamente, se abrirá una ventana mostrando el sistema solar en 3D.

---

## Uso del Programa

### Inicio del Programa

Al ejecutar el programa, se abrirá una ventana de 1050x700 píxeles mostrando el sistema solar en **vista general**. En esta vista podrás observar:

- El Sol en el centro emitiendo luz
- Los 8 planetas orbitando a diferentes distancias
- Un cinturón de 80 asteroides distribuidos por el sistema
- Líneas circulares que marcan las órbitas planetarias
- Un fondo espacial estrellado que rota lentamente

### Navegación Básica

#### Vista General
En este modo puedes observar todo el sistema solar desde una perspectiva elevada. Utiliza la **rueda del mouse** para acercar o alejar la vista (zoom entre 2 y 20 unidades).

#### Enfoque en Objetos
Presiona las teclas numéricas del **0 al 8** para enfocar la cámara en objetos específicos:

- `0` - Sol
- `1` - Mercurio  
- `2` - Venus
- `3` - Tierra
- `4` - Marte
- `5` - Júpiter
- `6` - Saturno
- `7` - Urano
- `8` - Neptuno

Cuando enfocas un objeto, la cámara se mueve suavemente hasta una posición orbital que te permite ver el objeto seleccionado y el Sol simultáneamente. La cámara seguirá automáticamente al objeto mientras orbita.

#### Regresar a Vista General
Presiona la tecla `X` para regresar a la vista general del sistema solar.

#### Salir del Programa
Presiona `ESC` cuando estés en vista general, o cierra la ventana directamente.

---

## Controles

### Tabla de Controles

| Tecla | Función | Descripción |
|-------|---------|-------------|
| **0** | Enfocar Sol | Mueve la cámara a una vista cercana del Sol |
| **1** | Enfocar Mercurio | La cámara sigue a Mercurio en su órbita |
| **2** | Enfocar Venus | La cámara sigue a Venus en su órbita |
| **3** | Enfocar Tierra | La cámara sigue a la Tierra en su órbita |
| **4** | Enfocar Marte | La cámara sigue a Marte en su órbita |
| **5** | Enfocar Júpiter | La cámara sigue a Júpiter en su órbita |
| **6** | Enfocar Saturno | La cámara sigue a Saturno en su órbita |
| **7** | Enfocar Urano | La cámara sigue a Urano en su órbita |
| **8** | Enfocar Neptuno | La cámara sigue a Neptuno en su órbita |
| **X** | Vista General | Regresa a la vista general del sistema completo |
| **ESC** | Salir/Regresar | En enfoque: regresa a vista general<br>En vista general: cierra la aplicación |
| **Scroll Arriba** | Zoom In | Acerca la cámara (solo en vista general) |
| **Scroll Abajo** | Zoom Out | Aleja la cámara (solo en vista general) |

### Comportamiento de los Controles

**En Vista General:**
- El control de zoom está activo (límites: 2-20 unidades)
- Todas las teclas numéricas (0-8) funcionan para enfocar objetos
- La tecla ESC cierra la aplicación

**En Vista de Enfoque:**
- El control de zoom está desactivado
- Puedes cambiar entre objetos usando las teclas numéricas (0-8)
- La cámara sigue automáticamente al objeto seleccionado
- Las teclas X o ESC regresan a vista general

---

## Estructura del Proyecto

```
ProyectoSistemaSolar/
│
├── SistemaSolar.py                  # Archivo principal de la aplicación
├── README.md                        # Este archivo de documentación
├── requirements.txt                 # Lista de dependencias (opcional)
│
└── images/                          # Carpeta con recursos gráficos
    ├── universo.png                 # Textura del fondo espacial (estrellas)
    ├── Sun.png                      # Textura del Sol
    ├── Mercury.png                  # Textura de Mercurio
    ├── Venus.png                    # Textura de Venus
    ├── Earth.png                    # Textura de la Tierra
    ├── Mars.png                     # Textura de Marte
    ├── Jupiter.png                  # Textura de Júpiter
    ├── Saturn.png                   # Textura de Saturno
    ├── Uranus.png                   # Textura de Urano
    └── Neptune.png                  # Textura de Neptuno
```

### Descripción de Archivos

#### `SistemaSolar.py`
Archivo principal que contiene toda la lógica del programa:
- Inicialización de Pygame y OpenGL
- Configuración de iluminación y materiales
- Carga de texturas planetarias
- Sistema de cámara con interpolación suave
- Renderizado de planetas, asteroides y órbitas
- Manejo de eventos de teclado y mouse
- Bucle principal de actualización y renderizado a 60 FPS

#### `images/`
Directorio que contiene las texturas en formato PNG:
- **Formato requerido**: PNG con canal alfa (RGBA)
- **Resolución recomendada**: 1024×512 píxeles (relación 2:1)
- Las texturas se mapean esféricamente sobre geometría 3D

#### `requirements.txt` (opcional)
Archivo que lista todas las dependencias del proyecto:
```
pygame>=2.0.0
PyOpenGL>=3.1.5
PyOpenGL-accelerate>=3.1.5
```

Puedes instalar todas las dependencias con un solo comando:
```bash
pip install -r requirements.txt
```

---

## Documentación Técnica

### Arquitectura del Sistema

El programa está estructurado en varios componentes principales:

#### 1. Inicialización y Configuración
- **Pygame**: Gestión de ventanas y eventos del sistema
- **OpenGL**: Configuración de contexto 3D (proyección perspectiva, depth test)
- **Sistema de iluminación**: Modelo Phong con luz ambiente, difusa y especular
- **Materiales**: Configuración de propiedades reflectivas de los objetos

#### 2. Sistema de Texturas
- Carga de imágenes PNG mediante Pygame
- Conversión a formato compatible con OpenGL (RGBA)
- Configuración de parámetros de filtrado (GL_LINEAR) y wrapping (GL_REPEAT)
- Transferencia a memoria de GPU mediante glTexImage2D

#### 3. Datos Planetarios
Los planetas están definidos en una estructura de datos que contiene:
```python
planet_data = [
    ("mercury", 1.5, 0.2),    # (nombre, distancia_orbital, tamaño)
    ("venus", 2.0, 0.3),
    ("earth", 2.5, 0.35),
    ("mars", 3.0, 0.25),
    ("jupiter", 4.5, 0.7),
    ("saturn", 5.5, 0.6),
    ("uranus", 6.5, 0.5),
    ("neptune", 7.5, 0.4)
]
```

**Nota**: Las distancias y tamaños son representaciones artísticas, no están a escala real, permitiendo visualizar todos los planetas simultáneamente.

#### 4. Sistema de Asteroides
Clase `Asteroid` que define objetos con propiedades aleatorias:
- **Distancia orbital**: Entre 1.0 y 8.0 unidades
- **Ángulo inicial**: Entre 0 y 2π radianes
- **Tamaño**: Radio entre 0.02 y 0.06 unidades
- **Velocidad orbital**: Entre 0.002 y 0.008 radianes por frame
- **Offset en Z**: Entre -0.5 y 0.5 para crear profundidad tridimensional
- **Color**: RGB aleatorio entre 0.5 y 0.9 (tonos grisáceos)

El sistema crea 80 asteroides que se actualizan y renderizan cada frame.

#### 5. Funciones de Renderizado

**`draw_background(rotation_angle)`**
- Desactiva depth test y cambia a proyección ortogonal 2D
- Dibuja un quad texturizado que cubre la pantalla
- Aplica rotación para simular bóveda celeste en movimiento
- Restaura configuración 3D

**`draw_planet(texture, distance, size, angle_offset, rotation_angle, is_sun)`**
- Calcula posición orbital usando trigonometría: x = cos(θ) × d, y = sin(θ) × d
- Aplica traslación y rotación propia
- Configura propiedades de material diferenciadas:
  - Sol: Emisión de luz propia (color amarillo-naranja)
  - Planetas: Sin emisión, brillo especular proporcional al tamaño
- Renderiza esfera con textura usando gluSphere (32×16 subdivisiones)
- Retorna posición para el sistema de cámara

**`draw_orbits()`**
- Desactiva iluminación para líneas
- Dibuja círculos en el plano XY usando GL_LINE_LOOP
- Cada órbita tiene 100 segmentos para suavidad visual
- Restaura iluminación

#### 6. Sistema de Cámara Dinámica

**`get_camera_position(focus_object, angle, planet_positions)`**

Calcula la posición de cámara según el objeto enfocado:

**Para el Sol (focus_object == 0):**
- Posición fija: (0, -6, 5)
- Mira hacia: (0, 0, 0)

**Para planetas (focus_object > 0):**
- Calcula distancia de cámara: `offset = size × 4 + 1.5`
- Posiciona la cámara 45° adelante del planeta en su órbita
- Altura proporcional al tamaño: `z = size × 3 + 1.0`
- Garantiza que planeta y Sol estén en el encuadre

**Interpolación de transiciones:**
- Usa interpolación lineal (LERP): `current = prev + (target - prev) × progress`
- Progreso incrementa 0.05 por frame (5%)
- Transiciones completas en aproximadamente 20 frames (0.33 segundos a 60 FPS)

#### 7. Bucle Principal

```python
while run:
    # 1. Procesar eventos (teclado, mouse, cierre)
    # 2. Limpiar buffers (color y profundidad)
    # 3. Actualizar rotaciones (fondo, planetas, sol)
    # 4. Calcular posiciones planetarias actuales
    # 5. Configurar cámara (vista general o enfoque)
    # 6. Renderizar escena (fondo, órbitas, sol, planetas, asteroides)
    # 7. Intercambiar buffers (flip)
    # 8. Limitar a 60 FPS
```

### Algoritmos Clave

#### Movimiento Orbital
Los planetas se mueven en círculos usando la ecuación paramétrica:
```python
angle += 0.01  # Incremento global por frame
x = math.cos(angle + planet_offset) × distance
y = math.sin(angle + planet_offset) × distance
z = 0  # Todas las órbitas en el plano XY
```

#### Iluminación Phong
Modelo de tres componentes:
```python
Luz Ambiente  = 0.2  # Iluminación base uniforme
Luz Difusa    = 0.8  # Luz direccional principal
Luz Especular = 1.0  # Reflejos brillantes
Shininess     = 50   # Concentración del brillo
```

El Sol tiene emisión propia configurada en `(0.8, 0.6, 0.2, 1.0)` simulando luz amarilla-naranja.

### Optimizaciones Implementadas

1. **Reutilización de cuádricos**: Un solo objeto `gluNewQuadric()` para todas las esferas
2. **Geometría variable**: Planetas con 32×16 subdivisiones, asteroides con 8×8
3. **Desactivación selectiva de luces**: Solo para elementos que no las requieren (líneas)
4. **Z-buffering**: Renderizado correcto de profundidad sin ordenamiento manual
5. **Double buffering**: Elimina parpadeos y tearing visual
6. **Limitación de FPS**: Mantiene 60 FPS constantes para animaciones predecibles

### Flujo de Renderizado

```
Frame N:
  1. Limpiar buffers (color + profundidad)
  2. Renderizar fondo 2D (sin depth test)
  3. Configurar cámara 3D (gluLookAt)
  4. Renderizar órbitas (sin iluminación)
  5. Renderizar Sol (con emisión)
  6. Renderizar planetas (con texturas)
  7. Renderizar asteroides (sin texturas)
  8. Intercambiar buffers (mostrar en pantalla)
  9. Esperar para mantener 60 FPS
```

### Variables Globales de Estado

```python
camera_x, camera_y, camera_z     # Posición actual de la cámara
look_x, look_y, look_z           # Punto al que mira la cámara
angle                            # Ángulo global de órbitas planetarias
sun_rotation_angle               # Ángulo de rotación del Sol
background_rotation              # Ángulo de rotación del fondo
zoom_level                       # Nivel de zoom en vista general (2-20)
focus_object                     # Objeto enfocado (None, 0-8)
transition_progress              # Progreso de transición (0.0-1.0)
```

### Características de Rendimiento

- **FPS objetivo**: 60 fotogramas por segundo
- **Objetos renderizados**: 1 Sol + 8 planetas + 80 asteroides + 8 órbitas = 97 objetos
- **Polígonos por frame**: ~6,500 (aproximado)
- **Texturas activas**: 10 (1 fondo + 9 cuerpos celestes)
- **Llamadas de renderizado**: ~90 por frame

---

## Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'pygame'"

**Causa**: La librería Pygame no está instalada.

**Solución**:
```bash
pip install pygame
```

### Error: "ModuleNotFoundError: No module named 'OpenGL'"

**Causa**: La librería PyOpenGL no está instalada.

**Solución**:
```bash
pip install PyOpenGL
pip install PyOpenGL-accelerate
```

### Error: "FileNotFoundError: [Errno 2] No such file or directory: './images/universo.png'"

**Causa**: Falta la carpeta `images/` o las texturas dentro de ella.

**Solución**:
1. Verifica que existe la carpeta `images/` en el mismo directorio que `main.py`
2. Asegúrate de que todas las texturas PNG están presentes:
   - universo.png
   - Sun.png
   - Mercury.png
   - Venus.png
   - Earth.png
   - Mars.png
   - Jupiter.png
   - Saturn.png
   - Uranus.png
   - Neptune.png

### La ventana se abre pero aparece completamente negra

**Posibles causas**:
- Drivers de GPU desactualizados
- Problema con la inicialización de OpenGL
- Falta de soporte de OpenGL 2.1

**Soluciones**:
1. Actualiza los drivers de tu tarjeta gráfica:
   - NVIDIA: Descarga desde [nvidia.com](https://www.nvidia.com/Download/index.aspx)
   - AMD: Descarga desde [amd.com](https://www.amd.com/en/support)
   - Intel: Descarga desde [intel.com](https://www.intel.com/content/www/us/en/support/detect.html)

2. Verifica soporte de OpenGL ejecutando:
   ```bash
   pip install pyopengl-utils
   python -c "from OpenGL.GL import *; print(glGetString(GL_VERSION))"
   ```

### Bajo rendimiento o lag

**Causas comunes**:
- Otros programas usando GPU intensivamente
- Tarjeta gráfica con capacidad limitada
- Demasiados asteroides

**Soluciones**:
1. Cierra otros programas que usen la GPU (juegos, editores de video, etc.)
2. Reduce el número de asteroides editando `main.py`:
   ```python
   # Busca esta línea y cambia 80 por un número menor
   asteroids = [Asteroid() for _ in range(40)]  # Cambiar de 80 a 40
   ```

### Error: "pygame.error: No available video device"

**Causa**: No hay servidor gráfico disponible (común en sesiones SSH o WSL sin GUI).

**Solución**: Ejecuta el programa en un entorno con interfaz gráfica de Windows, no en WSL o terminal remota.

### Error al instalar PyOpenGL-accelerate

**Causa**: Compilador de C++ no disponible en Windows.

**Solución**: PyOpenGL-accelerate es opcional. Puedes ejecutar el programa sin él:
```bash
pip install pygame PyOpenGL
```

El rendimiento será ligeramente menor pero funcional.

### La rueda del mouse no funciona para zoom

**Verificación**:
- Asegúrate de estar en **vista general** (no enfocando ningún objeto)
- El zoom solo funciona cuando `focus_object` es `None`
- Presiona `X` si estás en modo de enfoque

### Las transiciones de cámara son muy lentas o muy rápidas

**Solución**: Edita la velocidad de transición en `main.py`:
```python
# Busca esta línea
transition_speed = 0.05  # Aumenta para más rápido, disminuye para más lento
```

---
<img width="1052" height="732" alt="image" src="https://github.com/user-attachments/assets/10aa8657-e262-40e2-8b80-b9c755b88282" />
---

## Información del Proyecto

**Desarrollado con**: Python, Pygame y OpenGL  
**Año**: 2025  
**Estado**: Activo y funcional
