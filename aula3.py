import matplotlib.pyplot as plt
import theme

print('----- Lista de Temas -----\n')
for i in theme.plt_theme:
    print(f'Opção:{theme.plt_theme.index(i)} --- {i}')
    
tema = int(input('Digite um numero de 1 à 28 para selecionar o tema: \n'))

def gera_grafico(tema):
    eixo_x_dias = [1, 3, 5, 10, 15, 20, 30]
    eixo_y_temp_min = [21, 22, 17, 23, 23, 24, 20]
    eixo_y_temp_max = [28, 29, 25, 32, 34, 36, 31]

    plt.style.use(tema)

    plt.title("Temp Max e Min")
    plt.xlabel("Dias")
    plt.ylabel("Temperatura")

    plt.grid(True)

    plt.plot(eixo_x_dias, eixo_y_temp_max, marker = 'o')
    plt.plot(eixo_x_dias, eixo_y_temp_min, marker = 'o')
    plt.text(2,8, 'title', fontsize = 12)

    plt.legend(['Temp Max','Temp Min'], loc='best')
    print(plt.style.available)

    plt.savefig('Teste')
    plt.show()
    
gera_grafico(theme.plt_theme[tema])