# BG_prueba-tecnica  
Resultados de la prueba técnica para **Banco Guayaquil**  

##  Ejecución del agente de IA  

Sigue los pasos a continuación para levantar el proyecto en tu equipo:  

1. **Clona el repositorio** en tu máquina local:  
   ```bash
   git clone <url-del-repositorio>
   cd BG_prueba-tecnica
   ```

2. **Activa el entorno virtual**  
   - En **Windows**:  
     ```bash
     .\venv\Scripts\activate
     ```
   - En **Linux / MacOS**:  
     ```bash
     source venv/bin/activate
     ```

3. **Ejecuta el agente**:  
   ```bash
   python main.py
   ```

4. **Interactúa con el asistente** escribiendo en la consola:  
   ```
   Escribe algo para iniciar conversacion
   **************************************************
   Tú: Hola
   Asistente: ¡Hola! Soy tu asistente virtual de Banco Guayaquil.
   ```

---

##  Estructura del proyecto  

```
BG_prueba-tecnica/
│
├── main.py              # Script principal para iniciar el agente
├── venv/                # Entorno virtual (no se sube a GitHub)
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación del proyecto
```

---

## Requisitos previos  

- Python 3.9+  
- pip (gestor de paquetes de Python)  

Instalar dependencias:  
```bash
pip install -r requirements.txt
```

---

## Notas  

- El agente funciona en modo consola.  
- Si tienes problemas con dependencias, verifica tu versión de Python y el entorno virtual.  
