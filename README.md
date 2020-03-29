Este modulo no es algo realmente serio o que una empresa usaria, pero no se me ocurria otra cosa asi simple que hacer.  
Esta hecho para funcionar en Odoo 12 y se trata de un modulo que sirve como agenda para partidas del juego de rol Dragones y Mazmorras, del que ahora que estamos en cuarentena tengo bastantes, aunque realmente serviria para cualquier juego de rol.

El modulo lo hice a partir del modulo "my_library" del libro de cocina, basicamente cambiando elementos, borrandolos o añadiendo los que necesitase segun me hiciese falta.  

La manera en que funciona es bastante simple ya que tiene un unico modelo:  
* Cuando creamos un nuevo registro tenemos que añadir de forma obligatoria un nombre para la partida/campaña.
* Uno o mas Dungeon Masters (Que es el director del juego encargador de narrar la partida y los personajes no jugadores), este campo hace referencia a 'res.partner'
* Un campo integer numero de jugadores, que por defecto es 5.
* Y la fecha en que dicha partida empezaria, campo tambien obligatorio.

Añadi 2 headers a la vista de edicion/creacion del registro, uno de ellos tiene 4 botones que cambian el estado de la partida, estes botones usan restriciones, por lo que una partida pendiente (Que es el estado por defecto de cada registro nuevo), puede pasar a estar cancelada o terminada, una partida terminada podria continuar y una partida cancelada podria volver a estar pendiente.  
Una partida que ha terminado y continua solo puede cambiar entre esos 2 estados.  
El otro header controla un campo que determina si la partida es presencial u online, por defecto esta en online (Otra vez debido a la cuarentena) y no tiene restricciones a la hora de cambiar entre ambos estados.

En la vista tree lo que se ve es el nombre, estado y fecha de la partida, intente que se viese el Dungeon Master pero en vez del nombre lo que aparecia era '(1 Registro)' lo cual asumo que es porque el campo es un Many2Many.