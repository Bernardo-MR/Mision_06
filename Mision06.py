#Autor Bernardo Mondragon Ramirez
#Dibujando con ecuaciones paramétrica

import pygame
import math



ANCHO = 700
ALTO = 700
BLANCO = (255, 255, 255)
ROJO=(250, 0, 0)
AZUL=(0, 0, 150)


def dibujar(r,R,l):

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))

    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True


        ventana.fill(BLANCO)


        for angulo in range(0,(360*(r//math.gcd(r,R))+1)):
            a = math.radians(angulo)
            k= r/R
            x = int(R*((1-k) * math.cos(a) + l*k*math.cos(a*((1-k)/k))))
            y = int(R*((1-k) * math.sin(a) - l*k*math.sin(a*((1-k)/k))))
            pygame.draw.circle(ventana, ROJO, (ANCHO//2 + x, ALTO//2 - y),1)





        for angulo in range(0,(360*((r+20)//math.gcd((r+20),(R-85)))+1)):
            a = math.radians(angulo)
            k = (r+20) / (R-85)
            X= int((R-85)*((1-k)*math.cos(a)+l*k*math.cos(a*((1-k)/k))))
            Y= int((R-85)*((1-k)*math.sin(a)-l*k*math.sin(a*((1-k)/k))))
            pygame.draw.circle(ventana,AZUL,(ANCHO//2+X , ALTO//2-Y),1)





        pygame.display.flip()



    pygame.quit()




def main():
    r = int(input("Teclea el valor de r:"))
    R = int(input("Tecles el valor de R:"))
    l = float(input("Teclea el valor de l:"))

    dibujar(r,R,l)




main()