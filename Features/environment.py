from Actions.actions import Actions
from Actions.api_actions import ApiActions
from Features.browser import Browser
from Actions.variuos_functions import VariousFunctions


def before_all(context):
    context.browser = Browser()
    context.actions = Actions()
    context.api_actions = ApiActions()
    context.variuos_functions = VariousFunctions()



def after_all(context):
    context.browser.close()
