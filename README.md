# TP FINAL

El objetivo del siguiente TP es lograr una integracion entre frontend (react) y backend (django). 

La aplicacion sera un bit.ly clone basico el cual permita crear alias a diferentes urls y que cuando un usuario ingrese el alias
la aplicacion lo dirija al sitio. 

Por ejemplo, para la url `https://www.ambito.com/contenidos/dolar-oficial-historico.html` se genera un alias del tipo:

`aZsk12e`

Al ingresar ese alias del tipo `http://localhost:5000/aZsk12e`
El usuario debera ser redirigido a `https://www.ambito.com/contenidos/dolar-oficial-historico.html`


1. Completar el backend verificando que permita crear alias asociados a links y contabilizar cada visita al mismo.
2. Completar el front con una pantalla de bienvenida que permita ingresar un link, y mostrar el alias creado para ese link. 
3. Evaluar, e implementar la redireccion en cuestion. Puede resolverse desde React o implementando otro tipo de solucion. 

	

