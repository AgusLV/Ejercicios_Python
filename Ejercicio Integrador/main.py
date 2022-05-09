from claseCama import Cama

from claseMedicamento import Medicamento

from claseManejadorCamas import ManejadorCamas

from claseManejadorMedicamentos import ManejadorMedicamentos


if __name__ == '__main__':
    M_camas = ManejadorCamas()
    M_medic = ManejadorMedicamentos()
    M_camas.testCamas()
    M_medic.testMedicamentos()

    print('-----ALTA DE PACIENTE-----')
    nya=input('Ingrese nombre y apellido de paciente: ')
    
    paciente=M_camas.buscaPaciente(nya)
    if(paciente != None):
        id = paciente.getId()
        Lista_Med = M_medic.buscaMed(id)
        total_adeuda = 0.0
        for medicamento in Lista_Med:
            total_adeuda += medicamento.getPrecio()
        print('{}{:<25}{}{:<10}{}{:<10}'.format('Paciente:',paciente.getNom(),'Cama:',paciente.getId(),'Habitacion:',paciente.getHabitacion()))
        print('{}{:<25}{}{:<10}'.format('Diagnóstico:',paciente.getDiagnostico(),'Fecha de Internación:',paciente.getFecha_Internacion()))
        print('{}{:<25}'.format('Fecha de Alta:',paciente.getFecha_Alta()))
        #print('{:<25}'.format(paciente.setFecha_Alta()))
        # paciente.cambiaEstado(False)
        print('{:<30}{:<20}{:<20}{:<20}'.format('Medicamento/Monodroga','Presentacion','Cantidad','Precio'))

        for medicamento in Lista_Med:
            print('{:<10}{}{:<20}{:<20}{:<20}'.format(medicamento.getNombre_Comercial(),'/',medicamento.getMonodroga(),medicamento.getPresentacion(),medicamento.getCantidad(),medicamento.getPrecio()))
            print('{:<30}{:<20}{:<20}{:<20}'.format('Total Adeudado:','','',total_adeuda))
    else: print('No se encntró al paciente')

    print('-----PACIENTES INTERNADOS-----')
    diagnostico=input('Ingrese un diagnostico: ')
    Lista_Pacientes=M_camas.buscaPaciente_Diagnostico(diagnostico)
    if(len(Lista_Pacientes)>=1):
        for paciente in Lista_Pacientes:
            print(paciente)
    else: print(f'No se encontraron pacientes con el diagnostico {diagnostico}.')