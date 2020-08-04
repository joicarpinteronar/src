Feature: Crear variable
  Como Abby Analyst
  Requiero que se configuren las variables de perfil en los sistemas de medición
  De forma que se puedan usar en procesos posteriores y visualizar dicha configuración.

  @rest
  Scenario:Crear variable de perfil

    Given El sistema configure la url "http://192.168.1.103:5003/orchestrator/topology/set_up"
    When El sistema "Cree" una variable de "Perfil" para el punto de servicio
    Then El sistema valida que la operación "Create" para "Variable" haya arrojado el resultado "Successful"

  @rest
  Scenario: Actualizar variable de perfil
    Given El sistema configure la url "http://192.168.1.103:5003/orchestrator/topology/set_up"
    When El sistema "Actualice" una variable de "Perfil" para el punto de servicio
    Then El sistema valida que la operación "Update" para "Variable" haya arrojado el resultado "Successful"