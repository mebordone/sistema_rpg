from graphviz import Digraph



# Crear el diagrama de entidad-relación (DER)

der = Digraph(format='png', comment='DER para sistema de personajes de rol', strict=True)

der.attr(rankdir='LR', fontsize='12', splines='ortho')



# Definir las entidades principales

der.node("Jugador", "Jugador\n- ID\n- Nombre\n- Email", shape="box", style="rounded, filled", fillcolor="#ffcccb")

der.node("Narrador", "Narrador\n- ID\n- Nombre\n- Email", shape="box", style="rounded, filled", fillcolor="#ffebcc")

der.node("Campaña", "Campaña\n- ID\n- Nombre\n- Descripción\n- Sistema de juego", shape="box", style="rounded, filled", fillcolor="#fff2cc")

der.node("Personaje", "Personaje\n- ID\n- Nombre\n- Clase\n- Nivel\n- Raza\n- Atributos (FUE, DES, etc.)", shape="box", style="rounded, filled", fillcolor="#d5f4e6")

der.node("Hechizo", "Hechizo\n- ID\n- Nombre\n- Efecto\n- Sistema de juego", shape="box", style="rounded, filled", fillcolor="#d1c4e9")

der.node("Objeto", "Objeto\n- ID\n- Nombre\n- Estadísticas (peso, precio, etc.)", shape="box", style="rounded, filled", fillcolor="#f8bbd0")



# Relaciones

der.edge("Jugador", "Personaje", "1 a M (posee)", arrowhead="none")

der.edge("Narrador", "Campaña", "1 a M (gestiona)", arrowhead="none")

der.edge("Campaña", "Personaje", "1 a M (incluye)", arrowhead="none")

der.edge("Personaje", "Hechizo", "M a M (aprende/prepara)", arrowhead="none")

der.edge("Personaje", "Objeto", "1 a M (posee)", arrowhead="none")



# Guardar y renderizar

file_path = "/mnt/data/DER_sistema_personajes"

der.render(file_path, view=False)

file_path
