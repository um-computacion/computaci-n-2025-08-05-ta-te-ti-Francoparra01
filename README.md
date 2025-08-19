# Proyecto Tatetí

**Alumno:** Franco Agustín Parra  
**Carrera:** Ingeniería Informática  
**Trabajo:** Tatetí  

---

## Descripción
Este proyecto de **Tatetí en Python** está diseñado siguiendo una **arquitectura en capas**, como la vista en clase.  
La idea es separar claramente la interfaz, las reglas de negocio y la lógica del juego, para lograr un código **modular, mantenible y fácil de probar**.

---

## Arquitectura por Capas

### 1. Interfaz (`cli.py`)
- Muestra información al usuario y recibe sus inputs.
- No contiene reglas del juego ni lógica.
- Solo maneja la interacción con la consola.

### 2. Reglas de negocio (modelo)
Aquí se definen las reglas del juego, por ejemplo que siempre arranca **X**.

- **`tablero.py`**:  
  Representa el tablero, valida posiciones, actualiza el estado y detecta ganador o empate.  
  No conoce detalles del jugador ni de la interfaz.

- **`jugador.py`**:  
  Representa a un jugador, guarda su nombre y símbolo, y elige movimientos válidos (puede ser humano o CPU).  
  No sabe sobre turnos ni estado general.

### 3. Juego (`tateti.py`)
- Coordina los turnos.  
- Solicita jugadas a los jugadores.  
- Actualiza el tablero.  
- Determina el fin de la partida.  
Es el **“cerebro”** que integra las reglas con la interfaz.

---

## Testing
Se aplicaron **tests unitarios** a cada módulo por separado.  
Esto tiene varias ventajas:
- Permite reconocer en qué parte del código está el error.  
- Si se testeara todo el proyecto junto y falla, no se sabría dónde ocurrió el problema.  
- Se pueden modificar módulos individuales sin afectar a los demás.

---

## Cómo ejecutar
```bash
python cli.py
