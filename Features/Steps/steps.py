from nose.tools import assert_equal, assert_true
from behave import step


@step('El usuario navega a la página principal')
def step_impl(context):
    context.actions.navigate("http://192.168.1.105:4200/home/measurement-systems")
    assert_equal(context.actions.get_page_title(), "PrimestoneApp")
    #context.actions.put_screenshot()


@step('El usuario ingrese a la url "{url}"')
def step_impl(context, url):
    context.actions.navigate(url)
    #context.actions.put_screenshot()


@step('El usuario de click en la opción "{button_name}"')
def step_impl(context, button_name):
    context.actions.click_element(button_name)
  #  #context.actions.put_screenshot()
@step('El usuario limpia el campo "{field_name}"')
def step_impl(context, field_name):
    context.actions.clear(field_name)

@step('El usuario hace scroll "{field_name}"')
def step_impl(context, field_name):
    context.actions.scroll_interno(field_name)

@step('El usuario ingresa el texto "{text}" en el campo "{field_name}"')
def step_impl(context, text, field_name):
    context.actions.clear(field_name)
    context.actions.fill_field(text, field_name)

@step('El usuario escribe el texto "{text}" en el campo "{field_name}"')
def step_impl(context, text, field_name):
    #context.actions.clear(field_name)
    context.actions.send_keys(text, field_name)
    #context.actions.fill_field(text, field_name)
    #context.actions.put_screenshot()
@step('El usuario escribe el texto')
def step_impl(context):
    context.actions.prueba()
@step('El usuario selecciona la opcion "{option}" del combox "{field_name}"')
def step_impl(context, option, field_name):
    context.actions.select_fill(option, field_name)

@step('El usuario selecciona el combox "{field_name}" el  valor "{value}"')
def step_impl(context, field_name, value):
    context.actions.select_dropdown_value(field_name, value)

@step('El sistema muestra en "{toast_name}" el mensaje "{message}"')
def step_impl(context, toast_name, message):
    #assert_equal(context.actions.get_text(toast_name), message)
    text = context.actions.get_text(toast_name)
    print(text)
    assert text ==message, f'Not is equal'

    #assert context.actions.get_text(toast_name) == message, f'Not is equal'
    #context.actions.put_screenshot()

@step('El usuario arrastra el objeto "{element_1}" a "{element_2}"')
def step_impl(context, element_1, element_2):
    context.actions.drag_and_drop(element_1, element_2)
    #context.actions.put_screenshot()


@step('El usuario de doble click en la opción "{element}"')
def step_impl(context, element):
    context.actions.double_click(element)
    #context.actions.put_screenshot()

@step('El usuario hace hover en la opción "{element}"')
def step_impl(context, element):
    context.actions.hover(element)
    #context.actions.put_screenshot()

#api
@step('El sistema configure la url "{api_url}"')
def step_impl(context, api_url):
    context.api_actions.put_api_url(api_url)


@step('El sistema "{operation}" una variable de "{var_type}" para el punto de servicio')
def step_impl(context, operation, var_type):
    if operation == "Cree" and var_type == "Perfil":
        context.api_actions.create_profile_variable()
    elif operation == "Actualice" and var_type == "Perfil":
        context.api_actions.update_profile_variable()


@step('El sistema valida que la operación "{operation}" para "{entity_type}" haya arrojado el resultado "{'
      'expected_result}"')
def stem_impl(context, operation, entity_type, expected_result):
    if entity_type == 'Dispositivo':
        test_result = context.api_actions.evaluate_device_result(operation, expected_result)
        assert test_result == expected_result, f'El valor obtenido en la operación fue {test_result}'
    elif entity_type == 'Variable':
        test_result = context.api_actions.evaluate_variable_result(operation, expected_result)
        assert test_result == expected_result, f'El valor obtenido en la operación fue {test_result}'


@step('El sistema "{operation}" un dispositivo')
def step_impl(context, operation):
    if operation == 'cree':
        context.api_actions.create_device()
    elif operation == 'actualice':
        context.api_actions.update_device()


#primeread
@step('El usuario ingresa a la página principal de PrimeRead')
def step_impl(context):
    context.actions.navigate("http://poseidon01/primeread")
    assert_equal(context.actions.get_page_title(), "PrimeRead")
    #context.actions.put_screenshot()

@step('El usuario ingresa "{text}" en objeto "{element}"')
def step_impl(context,text,element):
    context.actions.send_keys(text,element)
    #context.actions.put_screenshot()
    print(context.actions.get_page_title())



#bd
@step(u'El usuario consulta en bd')
def step_impl(context):
    context.variuos_functions.conn_ps()
