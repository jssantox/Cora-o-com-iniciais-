import turtle

# Configuração inicial
turtle.speed(2)
turtle.color("red")

# Desenhar um coração
turtle.begin_fill()
turtle.fillcolor("red")
turtle.left(50)
turtle.forward(133)
turtle.circle(50, 200)
turtle.right(140)
turtle.circle(50, 200)
turtle.forward(133)
turtle.end_fill()

# Escrever as iniciais
turtle.penup()
turtle.goto( 15, 100)  # Ajuste a posição conforme necessário
turtle.pendown()
turtle.color("white")
turtle.write("J", font=("Arial", 15, "bold"))

turtle.penup()
turtle.goto( -25, 100)  # Ajuste a posição conforme necessário
turtle.pendown()
turtle.write("M", font=("Arial", 15, "bold"))

turtle.penup()
turtle.goto( -2, 100)  # Ajuste a posição conforme necessário
turtle.pendown()
turtle.write("e", font=("Arial", 15, "bold"))

# Manter a janela aberta
turtle.hideturtle()
turtle.done()
