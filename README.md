### **README del Proyecto: Sistema RPG Multi-Sistema**

![Diseño de portada](/design/home.png)

---

### **Descripción**

El **Sistema RPG Multi-Sistema** es una plataforma diseñada para gestionar personajes y sistemas de juego en juegos de rol. Es una aplicación flexible y extensible que permite administrar múltiples sistemas de juego (por ejemplo, Dungeons & Dragons, Pathfinder, etc.) en un solo lugar.

Actualmente, incluye funcionalidades para la creación y gestión de personajes asociados a un sistema de juego específico. Próximamente, se implementará un sistema de atributos que permita definir las estadísticas de cada personaje según el sistema de juego correspondiente.

---

### **Características**

- Gestión de múltiples sistemas de juego.
- Creación y edición de personajes:
  - Atributos básicos: nombre, clase, nivel, puntos de golpe máximos, etc.
  - Asociación a un sistema de juego.
  - Asociación a un jugador registrado.
- Sistema modular y extensible:
  - Capacidad para agregar nuevos sistemas de juego fácilmente.
  - Relación dinámica entre personajes y sistemas de juego.

---

### **Cómo levantar el proyecto**

#### **Requisitos previos**

- Python 3.8 o superior.
- Pipenv o virtualenv para la gestión del entorno virtual.
- Un navegador web compatible.

#### **Pasos para ejecutar el proyecto**

1. **Clona el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd sistema_rpg
   ```

2. **Crea un entorno virtual y actívalo**:
   Con `pipenv`:
   ```bash
   pipenv install
   pipenv shell
   ```
   O con `virtualenv`:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Realiza las migraciones de la base de datos**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Crea un superusuario para el panel de administración**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Levanta el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

6. **Accede al proyecto**:
   - Navega a [http://localhost:8000/](http://localhost:8000/) para ver la aplicación.
   - Ingresa a [http://localhost:8000/admin/](http://localhost:8000/admin/) para administrar los datos.

---

### **Roadmap de Desarrollo**

#### **Release 1**
- [x] Creación y gestión básica de personajes con atributos principales.
- [x] Asociación de personajes con jugadores.
- [ ] Implementación del modelo de atributos asociados a un sistema de juego (`Atributo`).
- [ ] Asignación de valores de atributos a personajes según el sistema de juego correspondiente (`ValorDeAtributo`).

#### **Release 2**
- Inventarios para personajes.
- Gestión de hechizos aprendidos y preparados.

#### **Release 3**
- Creación e invitación a campañas.

#### **Release 4**
- Validaciones y reglas específicas del sistema de juego (por ejemplo, límites de hechizos según nivel/clase).

---

### **Contribuciones**

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request si tienes alguna idea o encuentras algún error.

1. Haz un fork del repositorio.
2. Crea una rama con tu funcionalidad o solución: 
   ```bash
   git checkout -b mi-feature
   ```
3. Envía un pull request y explica tus cambios.

---

### **Licencia**

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

---

¡Gracias por usar y contribuir al **Sistema RPG Multi-Sistema**! 🎲
