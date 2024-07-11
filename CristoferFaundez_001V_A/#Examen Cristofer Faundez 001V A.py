#Examen Cristofer Faundez 001V A

import funciones as fn

trabajadores = ['Juan Perez', 'Maria Garcia', 'Carlos lopez', 'Ana Martinez', 'Pedro Rodriguez', 'Laura Hernandez', 'Miguel Sanchez', 'Isabel Gomez', 'Francisco Diaz', 'Elena fernandez']

sueldos =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

todo = {
    'Nombre empleado' : trabajadores,
    'Sueldos'      : sueldos
}


trabajadorMenor =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
sueldoMenor =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
trabajadorMediano = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
sueldoMediano =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
TrabajadorMayor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sueldoMayor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

sw = 0
while True:
    try:
        print('Menu')
        print('1. Asignar sueldos aleatorios')
        print('2. Clasificar sueldos')
        print('3. Ver estadisticas')
        print('4. Reporte de sueldos')
        print('5. Salir del programa')

        opcion = int(input('Ingrese opcion a elegir del 1 al 5: '))
        

        if opcion == 1 and sw == 0:
            sw = 1
            
            fn.asignacion(sueldos)
            print(todo)

        elif opcion == 1 and sw == 1:
            print("")
            print("****                   ****")
            print('Ya se asignaron los sueldos')
            print("****                   ****")

            
            '''  
            for i in range(10):
                print(trabajadores[i], '=', sueldos[i])
            print('Espacio') '''
        
        elif opcion == 2:
            if sw ==1:    
                for i in range (10):
                     if sueldos[i] < 800000:
                         
                         contMenor =+ 1
                         trabajadorMenor[i] = trabajadores[i]
                         sueldoMenor[i] = sueldos[i]
                         

                     elif sueldos[i] > 800000 and sueldos[i]< 2000000:
                         
                         contInter =+ 1
                         trabajadorMediano[i] = trabajadores[i]
                         sueldoMediano[i] = sueldos[i]


                     elif sueldos[i] > 2000000:

                         contMax =+ 1
                         TrabajadorMayor[i] = trabajadores[i]
                         sueldoMayor[i] = sueldos[i]


                print('Sueldo menor a 800.000: ', 'Cantidad: ', contMenor)
                sueldosMenores = [{
                               'Nombre Empleado' : trabajadorMenor,
                               'Sueldo empleado' : sueldoMenor
                            }]
                print(sueldosMenores)
                print(' ')
                print(' ')
                print('Sueldos entre 800.000 y 2.000.000: ', 'Cantidad: ', contInter)
                sueldosMedianos = [
                    {
                        'Nombre Empleado' : trabajadorMediano,
                        'Sueldo Empleado' : sueldoMediano 
                    }
                ]
                print(sueldosMedianos)
                print(' ')
                print(' ')
                print('Sueldos mayores a 2.000.000:', 'Cantidad: ', contMax)
                sueldosMayores = [
                    {
                        'Nombre Empleado' : TrabajadorMayor,
                        'Sueldo empleado' : sueldoMayor
                    }
                ]
            else:

                print("****                         ****")
                print('Asigna sueldos aleatorios primero')
                print("****                         ****")





        elif opcion == 3:
            if sw ==1:
                fn.estadisticas(sueldos)
            else:
                print("****              ****")
                print('Asigna sueldos primero')
                print("****              ****")

        elif opcion == 4:
            if sw ==1:
                fn.reporte()
            else:
                print('Asigna sueldos primero')

        elif opcion == 5:
            print('Saliendo del programa')
            print('Desarrollado por Cristofer Faundez, Rut: 21.283.150 - 6')
            break
    
    except:
        print('Sorry')