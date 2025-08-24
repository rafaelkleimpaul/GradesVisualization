import matplotlib.pyplot as plt
import theme

print('----- Lista de Temas -----\n')
for i in theme.plt_theme:
    print(f'Opção:{theme.plt_theme.index(i)} --- {i}')

tema = int(input('Digite um numero de 1 à 28 para selecionar o tema: \n'))

def gerar_rel(tema):
    category = ['A','B','C','D','E']
    values_month = [26, 45, 14, 8, 5]
    
    maior_venda = max(values_month)
    index_i = values_month.index(maior_venda)
            
    #for i in values_month:
    #    if i == maior_venda:
    #        index = values_month.index(i)
    #        print(index)            
        
    plt.title('Relacao Carteiras x Meses')
    plt.bar(category, values_month)
    plt.xlabel('Categorias')
    plt.ylabel('Valores')
    
    plt.grid(True)

    plt.text(values_month[index_i],category[index_i],'Aqui')

    plt.legend(['Categoria','Mes'], loc='best')
    
    plt.show()    
    
gerar_rel(tema)