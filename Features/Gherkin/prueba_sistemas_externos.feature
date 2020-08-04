@5000
Feature: HU -5378- Gestión de filtros
Como Abby Analyst
Requiero gestionar los filtros en el sistema
De forma que pueda visualizar, crear, editar y eliminar filtros de acuerdo a las necesidades de la operación del sistema.

  
  Scenario: elementos externos, mantener eliminacion
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "PAP_BTN_INTEROPERABILITY"
      And El usuario hace hover en la opción "PAP_BTN_EXTERNAL_SYSTEM"
      And El usuario de click en la opción "PAP_BTN_EXTERNAL_SYSTEM"
      And El usuario hace hover en la opción "PAP_BTN_CAR_INFO"
      And El usuario de click en la opción "PAP_BTN_CAR_INFO" 
      And El usuario de click en la opción "PAP_ITEM_DELETE"
      And El usuario de click en la opción "PAP_BTN_MANTENER"   

  Scenario: elementos externos, editar
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "PAP_BTN_INTEROPERABILITY"
      And El usuario hace hover en la opción "PAP_BTN_EXTERNAL_SYSTEM"
      And El usuario de click en la opción "PAP_BTN_EXTERNAL_SYSTEM"
      And El usuario hace hover en la opción "PAP_BTN_CAR_INFO1"
      And El usuario de click en la opción "PAP_BTN_CAR_INFO1"
      And El usuario de click en la opción "PAP_ITEM_EDITAR" 
      And El usuario de click en la opción "PAP_BTN_TEST_CONECTION"

  Scenario: elementos externos, mostrar home
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "PAP_BTN_INTEROPERABILITY"
      And El usuario hace hover en la opción "PAP_BTN_EXTERNAL_SYSTEM"