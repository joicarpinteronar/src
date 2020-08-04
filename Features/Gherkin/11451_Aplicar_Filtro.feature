@11451
Feature: HU -11451- Aplicar Filtro
Como Abby Analyst 
Requiero aplicar un filtro de los existentes en el sistema
De forma que se limite la información de puntos de servicio visualizada de manera transversal (todas las pantallas).

@11451-1
  Scenario: Visualizacion y Aplicacion del Nombre del Filtro en Diferentes Sesiones
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_RADIO_BTN_LIST_FILTER_0" 
      And El usuario de click en la opción "PAP_BTN_APLICAR" 
      Then El sistema muestra en "PAP_RESULT" el mensaje "El filtro fue aplicado correctamente"
      And El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      Then El sistema muestra en "PAP_BTN_FILTER" el mensaje "Mis Filtros : TEST7"

@11451-2
  Scenario: Visualizacion y Aplicacion de Clausulas de Filtros
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_RADIO_BTN_LIST_FILTER_0" 
      And El usuario de click en la opción "PAP_BTN_APLICAR" 
      Then El sistema muestra en "PAP_RESULT" el mensaje "El filtro fue aplicado correctamente"

@11451-3
  Scenario: Crear y Aplicar Filtro con campo Valor Fecha 
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_BTN_NEW_FILTER"
      And El usuario ingresa el texto "TEST11" en el campo "PAP_TXT_NAME_FILTER"
      And El usuario de click en la opción "PAP_CBX_OPERADOR_FIL"
      And El usuario de click en la opción "PAP_SEL_OPTION_AND"
      And El usuario de click en la opción "PAP_ADD_FIELD"  
      And El usuario de click en la opción "PAP_CBX_FIELD"
      And El usuario de click en la opción "PAP_SEL_SERVICE_POINT"
      And El usuario de click en la opción "PAP_SEL_DATE_START"
      And El usuario de click en la opción "PAP_CBX_OPERATION"
      And El usuario de click en la opción "PAP_SEL_GREATER_EQUAL"
      And El usuario de click en la opción "PAP_HOVER_DATE"
      And El usuario de click en la opción "PAP_ICON_DATE"
      And El usuario de click en la opción "PAP_SEL_DATE"
      And El usuario de click en la opción "PAP_BTN_DATE_OK"
      And El usuario de click en la opción "PAP_BTN_SAVE_FILTER"
      Then El sistema muestra en "PAP_RESULT" el mensaje "El filtro fue guardado correctamente"
      And El usuario de click en la opción "PAP_BTN_CLOSE_FILTER"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_RADIO_BTN_LIST_FILTER_2" 
      And El usuario de click en la opción "PAP_BTN_APLICAR" 
      Then El sistema muestra en "PAP_RESULT" el mensaje "El filtro fue aplicado correctamente"
         

