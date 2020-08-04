  Feature: 5191 - Sistemas de medición
    Como Abby Analyst
    Requiero visualizar los sistemas de medición
    De forma que pueda pueda conocer los atributos de los sistemas de medición disponibles.

    @5500-1 @UI
    Scenario: filtrar por criterio de consulta datos alfanumericos
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      When El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      When El usuario hace hover en la opción "SERVICE POINTS_BTN"
      When El usuario ingresa el texto "SERIAL-00000000" en el campo "IDSERVICE_POINT_FILTER"
      Then El sistema muestra en "ROW_RESULT_IDSERVICEPOINT" el mensaje "SERIAL-00000000"

    @5500-2 @UI
    Scenario: ocultar columnas visibles en la grilla
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      When El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      When El usuario hace hover en la opción "SERVICE POINTS_BTN"
      When El usuario de click en la opción "SELECTOR_COLUMNA"
      Then El usuario arrastra el objeto "PTOSERVICIO_COL" a "VENTANA_COLUMNAS"

    @5500-3 @UI
     Scenario: Verificar que se permite agregar columnas a la grilla.
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      When El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      When El usuario hace hover en la opción "SERVICE POINTS_BTN"
      When El usuario de click en la opción "SELECTOR_COLUMNA"
      Then El usuario arrastra el objeto "NEW_COLUMN" a "TB_COLUMNAS"


    #paginar registros
    #seleccion de registros
    #orden ascendente y descendente
    #filtros, filtros por criterios.






