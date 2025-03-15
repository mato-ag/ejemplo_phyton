import random
import sys

score = 0.0
# Preguntas para el juego
questions = [
    ("¿Qué función se usa para obtener la longitud de una cadena en Python?",),
    ("¿Cuál de las siguientes opciones es un número entero en Python?",),
    ("¿Cómo se solicita entrada del usuario en Python?",),
    ("¿Cuál de las siguientes expresiones es un comentario válido en Python?",),
    ("¿Cuál es el operador de comparación para verificar si os valores son iguales?",),
]
# Respuestas posibles para cada pregunta, en el mismo orden
# que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el
# mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)
    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: "))
            # Se verifica si la respuesta es correcta
            if user_answer > 0 and user_answer < 5:
                user_answer = user_answer - 1
                if user_answer == correct_answers_index[question_index]:
                    print("¡Correcto!")
                    score = score + 1
                    break
                else:
                    score = score - 0.5
            else:
                print ("Respuesta invalida")
                sys.exit(1)
        except ValueError:
            print("Respuesta invalida")
            sys.exit(1)
    else:
         # Si el usuario no responde correctamente después de 2 intentos
         # se muestra la respuesta correcta
         print("Incorrecto. La respuesta correcta es:")
         print(answers[question_index] [correct_answers_index[question_index]])
# Se imprime un blanco al final de la pregunta
print()
print (f'El score del jugador es:  +{score}')