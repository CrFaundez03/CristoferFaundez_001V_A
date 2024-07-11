import random


def asignacion(sueldos):
    print('Sueldos asignados por trabajador: ')   
    for i in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos[i] = sueldo


        

def estadisticas(sueldos):
        cont = 0
        total = 0
        for cont in range(9):
            
            
            if sueldos[cont] < sueldos[cont + 1]:
                menor = sueldos[cont] 
            elif sueldos[cont] > sueldos[cont + 1]: 
                mayor = sueldos[cont]
                  
        for i in range(10):
            total = sueldos[i] + total          
        
        print('El sueldo menor es: ', menor)
        print('El sueldo mayor es: ', mayor)
        print('El sueldo promedio es: ', total/10 )
        
            
        

def reporte():
     print('Aqui se deberia ver un reporte')
        


