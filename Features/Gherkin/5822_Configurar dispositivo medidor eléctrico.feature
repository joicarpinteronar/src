Feature: Crear dispositivo
  Como Abby Analyst
  Requiero que se configuren los dispositivos tipo medidor eléctrico de mis sistemas de medición
  De forma que se puedan conocer las características de cada dispositivo.

  @rest
  Scenario: Crear dispositivo
    Given El sistema configure la url "http://192.168.1.105:5001/metering_system/set_up"
    When El sistema "cree" un dispositivo
    Then El sistema valida que la operación "Create" para "Dispositivo" haya arrojado el resultado "Successful"

  @rest
  Scenario: Actualizar dispositivo
    Given El sistema configure la url "http://192.168.1.105:5001/metering_system/set_up"
    When El sistema "actualice" un dispositivo
    Then El sistema valida que la operación "Update" para "Dispositivo" haya arrojado el resultado "Successful"