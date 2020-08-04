@5378
Feature: HU -5378- Gestión de filtros
Como Abby Analyst
Requiero gestionar los filtros en el sistema
De forma que pueda visualizar, crear, editar y eliminar filtros de acuerdo a las necesidades de la operación del sistema.

@5378-1
  Scenario: Visualizacion y Aplicacion de Clausulas de Filtros
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_RADIO_BTN_LIST_FILTER_0" 
      And El usuario de click en la opción "PAP_BTN_APLICAR" 
      Then El sistema muestra en "PAP_RESULT" el mensaje "El filtro fue aplicado correctamente"

@5378-2
  Scenario: Visualizacion y Guardar  Clausulas de Filtros
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_RADIO_BTN_LIST_FILTER_0" 
      And El usuario de click en la opción "PAP_BTN_SAVE_FILTER" 
      Then El sistema muestra en "PAP_RESULT" el mensaje "El filtro fue guardado correctamente"

@5378-3
  Scenario: Validar campos obligatorios
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_BTN_NEW_FILTER"
      And El usuario de click en la opción "PAP_ADD_FIELD"
      And El usuario de click en la opción "PAP_BTN_SAVE_FILTER"
      Then El sistema muestra en "PAP_MSJ_WARNING_FIELD_NAME_FILTER" el mensaje "Los campos resaltados son requeridos"

@5378-4
  Scenario: Validar longitud minima y maxima del campo Nombre de Filtro y guardar filtro por defecto
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_BTN_NEW_FILTER"
      And El usuario ingresa el texto "P" en el campo "PAP_TXT_NAME_FILTER"
      And El usuario limpia el campo "PAP_TXT_NAME_FILTER"
      And El usuario ingresa el texto "#$%!)(?¡%&/=?¡" en el campo "PAP_TXT_NAME_FILTER"
      And El usuario limpia el campo "PAP_TXT_NAME_FILTER"
      And El usuario ingresa el texto "PruebasTest@#ambieten123456789" en el campo "PAP_TXT_NAME_FILTER"
      And El usuario limpia el campo "PAP_TXT_NAME_FILTER"
      And El usuario ingresa el texto "PruebasTest@#ambieten123456789Test123" en el campo "PAP_TXT_NAME_FILTER"
      And El usuario limpia el campo "PAP_TXT_NAME_FILTER"
      And El usuario ingresa el texto "PruebasTest3" en el campo "PAP_TXT_NAME_FILTER"
      And El usuario de click en la opción "PAP_BTN_SAVE_FILTER"
      Then El sistema muestra en "PAP_RESULT" el mensaje "El filtro fue guardado correctamente"
      And El usuario de click en la opción "PAP_BTN_CLOSE_FILTER"

@5378-5
  Scenario: visualizar los campos Nombre Filtro, Operador entre campos, Campo, Operador, Valor del Campo
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_BTN_NEW_FILTER"
      And El usuario de click en la opción "PAP_CBX_OPERADOR_FIL"
      And El usuario de click en la opción "PAP_SEL_OPTION_AND"
      And El usuario de click en la opción "PAP_ADD_FIELD"
      And El usuario de click en la opción "PAP_CBX_FIELD"
      And El usuario de click en la opción "PAP_SEL_VARIABLE"
      And El usuario de click en la opción "PAP_SEL_VARIABLE"
      And El usuario de click en la opción "PAP_SEL_SERVICE_POINT"
      And El usuario de click en la opción "PAP_SEL_SERVICE_POINT"
      And El usuario de click en la opción "PAP_SEL_DEVICE"
      And El usuario hace hover en la opción "PAP_SCROLL_DEVICE"
      And El usuario de click en la opción "PAP_SEL_DEVICE"
      And El usuario de click en la opción "PAP_CBX_OPERATION"
      And El usuario de click en la opción "PAP_BTN_SAVE_FILTER"
      Then El sistema muestra en "PAP_MSJ_WARNING_FIELD_NAME_FILTER" el mensaje "Los campos resaltados son requeridos"

@5378-6
  Scenario: Agregar Clausulas al Filtro
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_BTN_NEW_FILTER"
      And El usuario ingresa el texto "Filter_Test" en el campo "PAP_TXT_NAME_FILTER"
      And El usuario de click en la opción "PAP_CBX_OPERADOR_FIL"
      And El usuario de click en la opción "PAP_SEL_OPTION_OR"
      And El usuario de click en la opción "PAP_ADD_FIELD"
      And El usuario de click en la opción "PAP_ADD_FIELD"
      And El usuario de click en la opción "PAP_ADD_FIELD"

      And El usuario de click en la opción "PAP_CBX_FIELD"
      And El usuario de click en la opción "PAP_SEL_VARIABLE"
      And El usuario de click en la opción "PAP_SEL_ID_VARIABLE"
      And El usuario de click en la opción "PAP_CBX_OPERATION"
      And El usuario de click en la opción "PAP_SEL_FILTER_START_WITH"

      And El usuario de click en la opción "PAP_CBX_FIELD2"
      And El usuario de click en la opción "PAP_SEL_SERVICE_POINT2"
      And El usuario de click en la opción "PAP_SEL_DATE_START"
      And El usuario de click en la opción "PAP_CBX_OPERATION2"
      And El usuario de click en la opción "PAP_SEL_GREATER_EQUAL"

      And El usuario de click en la opción "PAP_CBX_FIELD2"
      And El usuario de click en la opción "PAP_CBX_FIELD3"
      And El usuario de click en la opción "PAP_SEL_DEVICE3"
      And El usuario de click en la opción "PAP_SEL_DEVICE_ID"
      And El usuario de click en la opción "PAP_CBX_OPERATION2"
      And El usuario de click en la opción "PAP_SEL_CONTAINS"
      And El usuario de click en la opción "PAP_BTN_SAVE_FILTER"
      Then El sistema muestra en "PAP_MSJ_WARNING_FIELD_NAME_FILTER" el mensaje "Los campos resaltados son requeridos"

@5378-7
  Scenario: Eliminar Clausulas del Filtro
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_BTN_NEW_FILTER"
      And El usuario ingresa el texto "Filter_Test" en el campo "PAP_TXT_NAME_FILTER"
      And El usuario de click en la opción "PAP_CBX_OPERADOR_FIL"
      And El usuario de click en la opción "PAP_SEL_OPTION_OR"
      And El usuario de click en la opción "PAP_ADD_FIELD"
      And El usuario de click en la opción "PAP_ADD_FIELD"
      And El usuario de click en la opción "PAP_ADD_FIELD"

      And El usuario de click en la opción "PAP_CBX_FIELD"
      And El usuario de click en la opción "PAP_SEL_VARIABLE"
      And El usuario de click en la opción "PAP_SEL_ID_VARIABLE"
      And El usuario de click en la opción "PAP_CBX_OPERATION"
      And El usuario de click en la opción "PAP_SEL_FILTER_START_WITH"

      And El usuario de click en la opción "PAP_CBX_FIELD2"
      And El usuario de click en la opción "PAP_SEL_SERVICE_POINT2"
      And El usuario de click en la opción "PAP_SEL_DATE_START"
      And El usuario de click en la opción "PAP_CBX_OPERATION2"
      And El usuario de click en la opción "PAP_SEL_GREATER_EQUAL"

      And El usuario de click en la opción "PAP_CBX_FIELD2"
      And El usuario de click en la opción "PAP_SEL_DEVICE3"
      And El usuario de click en la opción "PAP_SEL_DEVICE_ID"
      And El usuario de click en la opción "PAP_CBX_OPERATION2"
      And El usuario de click en la opción "PAP_SEL_CONTAINS"
      And El usuario de click en la opción "PAP_DELETE_CLAUSULE"
      And El usuario de click en la opción "PAP_DELETE_CLAUSULE2"
      And El usuario de click en la opción "PAP_BTN_SAVE_FILTER"      
      Then El sistema muestra en "PAP_MSJ_WARNING_FIELD_NAME_FILTER" el mensaje "Los campos resaltados son requeridos"

@5378-8
  Scenario: Validar Nombre Filtro unico y valor de campo Fecha
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_BTN_NEW_FILTER"
      And El usuario ingresa el texto "TEST3" en el campo "PAP_TXT_NAME_FILTER"
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
      And El usuario de click en la opción "PAP_BTN_NEW_FILTER"
      And El usuario ingresa el texto "TEST3" en el campo "PAP_TXT_NAME_FILTER"
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
      Then El sistema muestra en "PAP_RESULT" el mensaje "El nombre del filtro ya se encuentra asignado a otro filtro"

@5378-9
  Scenario: Eliminar Filtro
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_BTN_DELETE_FILTER" 
      And El usuario de click en la opción "PAP_BTN_ACEPPT_DELETE" 
      Then El sistema muestra en "PAP_RESULT" el mensaje "El filtro se eliminó correctamente"
      
  
@5378-10
  Scenario: crear un nuevo filtro
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario de click en la opción "PAP_BTN_FILTER" 
      And El usuario de click en la opción "PAP_BTN_NEW_FILTER"
      And El usuario ingresa el texto "Filter_Prueba" en el campo "PAP_TXT_NAME_FILTER"
      And El usuario de click en la opción "PAP_CBX_OPERADOR_FIL"
      And El usuario de click en la opción "PAP_SEL_OPTION_AND"
      And El usuario de click en la opción "PAP_ADD_FIELD"
      And El usuario de click en la opción "PAP_CBX_FIELD"
      And El usuario de click en la opción "PAP_SEL_SERVICE_POINT"
      And El usuario de click en la opción "PAP_SEL_DESCRIPTION"
      And El usuario de click en la opción "PAP_CBX_OPERATION"
      And El usuario de click en la opción "PAP_SEL_FILTER_DIFERENT"
       
      And El usuario escribe el texto
      And El usuario de click en la opción "PAP_BTN_SAVE_FILTER"
      
