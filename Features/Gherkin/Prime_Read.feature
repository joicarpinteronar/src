Feature: Pruebas PR.

  @primeread-1
  Scenario:configurar el tipo de diagrama de angulos en "Absoluto"
    Given El usuario ingresa a la página principal de PrimeRead
    When El usuario ingresa "zulay.bonilla" en objeto "PRW_LOGIN_INPUT_USERNAME"
    When El usuario ingresa "zulay.bonilla" en objeto "PRW_LOGIN_INPUT_PASSWORD"
    When El usuario hace hover en la opción "PRW_OPTION_HOME"
    When El usuario de click en la opción "PRW_OPTION_PHASOR_DIAGRAMS"  
    When El usuario de click en la opción "PRW_OPTION_ADD_PHASOR_DIAGRAMS"
      #When El usuario ingresa el texto "AUT_FASOR_01" en el campo "PRW_FORM_PHASORS_DESC"
      #When Ingresar información correspondiente a las Fases de corrientes voltajes y angulos de las mismas.
      #When Configurar el tipo de diagrama de angulos en "Absoluto".
      #When Ir a la grilla de "Add Device".
      #When Adiconar el punto de medida.
      #Then Dar clic en boton "Save".

  @primeread-1
  Scenario: CONSULTA EN BD
    Given El usuario navega a la página principal
    When El usuario consulta en bd
