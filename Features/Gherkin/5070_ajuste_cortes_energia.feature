@5070
Feature: HU - Ajustes de Cortes de Energía (identificador del conjunto: 32623)
Como Abby Analyst 
Requiero configurar los ajustes de cortes de energía
De forma que el sistema aplique la configuración definida a las lecturas cuando se detecten cortes de energía.

  @5070-1
  Scenario: validar ajustes de cortes de energia, completa con nulos
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario hace hover en la opción "PAP_BTN_MS_CONF"
      And El usuario de click en la opción "PAP_BTN_AJUSTE_CORTE_ENERGIA"
      And El usuario de click en la opción "PAP_RADIO_BTN_NULO"
      And El usuario de click en la opción "PAP_BTN_GUARDAR"
      Then El sistema muestra en "PAP_RESULT" el mensaje "Los ajustes de cortes de energía fueron guardados correctamente"
  @5070-2
  Scenario: validar ajustes de cortes de energia, completa con ceros
      Given El usuario navega a la página principal
      When El usuario ingrese a la url "http://192.168.1.105:4200/home/measurement-systems"
      And El usuario hace hover en la opción "MEASUREMENT_SYSTEMS_BTN"
      And El usuario hace hover en la opción "SERVICE POINTS_BTN"
      And El usuario hace hover en la opción "PAP_BTN_MS_CONF"
      And El usuario de click en la opción "PAP_BTN_AJUSTE_CORTE_ENERGIA"
      And El usuario de click en la opción "PAP_RADIO_BTN_CERO"
      And El usuario de click en la opción "PAP_BTN_GUARDAR"
      Then El sistema muestra en "PAP_RESULT" el mensaje "Los ajustes de cortes de energía fueron guardados correctamente"
     