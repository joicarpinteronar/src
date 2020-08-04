Feature: 13627 - Sistemas externos
  Como Abby Analyst
  Requiero configurar (crear, editar, eliminar) la conexión a sistemas externos
  De forma que el sistema pueda hacer intercambios de información desde y hacia dichos sistemas.


  @13627-1 @UI @SE
  Scenario: Crear sistema externo tipo HES
    Given El usuario navega a la página principal
    When El usuario ingrese a la url "http://192.168.1.105:4200/home/external-system"
    When El usuario de click en la opción "EXTERNAL_SYSTEM_BTN_ADDES"
    When El usuario de click en la opción "EXTERNAL_SYSTEM_LST_TYPE"
    When El usuario de click en la opción "EXTERNAL_SYSTEM_LST_TYPE_HES"
    When El usuario ingresa el texto "random" en el campo "EXTERNAL_SYSTEM_INPUT_NAME"
    When El usuario ingresa el texto "Test Description" en el campo "EXTERNAL_SYSTEM_INPUT_DESC"
    When El usuario ingresa el texto "192.168.1.105" en el campo "EXTERNAL_SYSTEM_INPUT_URL_SERVICE"
    When El usuario ingresa el texto "Pstone" en el campo "EXTERNAL_SYSTEM_INPUT_USERNAME"
    When El usuario ingresa el texto "Pst0n3" en el campo "EXTERNAL_SYSTEM_INPUT_PASSWORD"
    When El usuario ingresa el texto "Key0123.!4" en el campo "EXTERNAL_SYSTEM_INPUT_PKEY"
    When El usuario ingresa el texto "4200" en el campo "EXTERNAL_SYSTEM_INPUT_PORT"
    When El usuario de click en la opción "EXTERNAL_SYSTEM_BTN_SAVEES"
    Then El sistema muestra en "EXTERNAL_SYSTEM_TOAST_OKES" el mensaje "Los sistemas externos fueron guardados correctamente"


  @13627-2 @UI @SE
  Scenario: Editar un sistema externo tipo HES
    Given El usuario navega a la página principal
    When El usuario ingrese a la url "http://192.168.1.105:4200/home/external-system"
    When El usuario hace hover en la opción "EXTERNAL_SYSTEM_CARD1"
    When El usuario de click en la opción "EXTERNAL_SYSTEM_CARD1"
    When El usuario hace hover en la opción "EDIT_EXTERNAL_SYSTEM"
    When El usuario de click en la opción "EDIT_EXTERNAL_SYSTEM"
    When El usuario ingresa el texto "update description" en el campo "EXTERNAL_SYSTEM_INPUT_DESC"
    When El usuario de click en la opción "EXTERNAL_SYSTEM_BTN_SAVEES"
    Then El sistema muestra en "EXTERNAL_SYSTEM_TOAST_OKES" el mensaje "Los sistemas externos fueron guardados correctamente"


  @13627-3 @UI @SE
  Scenario: Eliminación de un sistema externo tipo HES
    Given El usuario navega a la página principal
    When El usuario ingrese a la url "http://192.168.1.105:4200/home/external-system"
    When El usuario hace hover en la opción "EXTERNAL_SYSTEM_CARD1"
    When El usuario de click en la opción "EXTERNAL_SYSTEM_CARD1"
    When El usuario hace hover en la opción "REMOVE_EXTERNAL_SYSTEM"
    When El usuario de click en la opción "REMOVE_EXTERNAL_SYSTEM"
#    When El usuario de click en la opción "REMOVE_MSJ_CONFIRM"
    When El usuario de click en la opción "EXTERNAL_SYSTEM_BTN_DEL_ES"
    Then El sistema muestra en "EXTERNAL_SYSTEM_TOAST_DELES" el mensaje "Los sistemas externos fueron eliminados correctamente"





