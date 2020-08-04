from selenium.webdriver.common.by import By


def get_locator(locator):
    locators = {
        "EXTERNAL_SYSTEM_BTN_ADDES": (
            By.XPATH, "//span[@class='dx-button-text'][contains(.,'Agregar sistema externo')]"),
        "EXTERNAL_SYSTEM_INPUT_NAME": (By.XPATH, "(//input[@autocomplete='off'])[2]"),
        "EXTERNAL_SYSTEM_INPUT_DESC": (By.XPATH, "(//input[contains(@autocomplete,'off')])[3]"),
        "EXTERNAL_SYSTEM_LST_TYPE": (By.XPATH, "(//input[contains(@autocomplete,'off')])[1]"),
        "EXTERNAL_SYSTEM_LST_TYPE_HES": (
            By.XPATH, "//div[@class='dx-item-content dx-list-item-content'][contains(.,'HES')]"),
        "EXTERNAL_SYSTEM_LST_TYPE_MDC": (
            By.XPATH, "//div[@class='dx-item-content dx-list-item-content'][contains(.,'MDC')]"),
        "EXTERNAL_SYSTEM_INPUT_URL_SERVICE": (By.XPATH, "(//input[contains(@autocomplete,'off')])[5]"),
        "EXTERNAL_SYSTEM_INPUT_USERNAME": (By.XPATH, "(//input[contains(@autocomplete,'off')])[7]"),
        "EXTERNAL_SYSTEM_INPUT_PASSWORD": (By.XPATH, "//input[contains(@type,'password')]"),
        "EXTERNAL_SYSTEM_INPUT_PKEY": (By.XPATH, "(//input[contains(@autocomplete,'off')])[11]"),
        "EXTERNAL_SYSTEM_INPUT_PORT": (By.XPATH, "(//input[contains(@autocomplete,'off')])[13]"),
        "EXTERNAL_SYSTEM_BTN_SAVEES": (By.XPATH, "//span[@class='dx-button-text'][contains(.,'Guardar')]"),
        "EXTERNAL_SYSTEM_TOAST_OKES": (By.XPATH,
                                       "//div[@class='dx-overlay-content dx-toast-success dx-toast-content dx-resizable'][contains(.,'Los sistemas externos fueron guardados correctamente')]"),
        "EXTERNAL_SYSTEM_TOAST_DELES": (By.XPATH,
                                        "(//div[@class='dx-overlay-content dx-toast-success dx-toast-content dx-resizable'][contains(.,'Los sistemas externos fueron eliminados correctamente')])[1]"),
        "EXTERNAL_SYSTEM_CARD1": (By.XPATH, "(//em[@id='btnCardInfo'])[2]"),
        "EXTERNAL_SYSTEM_BTN_DEL_ES": (By.XPATH, "//button[contains(@id,'btnPopupAccept')]"),
        "MEASUREMENT_SYSTEMS_BTN": (By.ID, "btnSideMenuNavigationMainItemText"),
        "SERVICE POINTS_BTN": (By.ID, "btnSideMenuNavigationSecondItem0"),
        "GROUP_FILTER": (By.CLASS_NAME, "class='dx-group-panel-message"),
        "IDSERVICE_POINT_FILTER": (By.XPATH,
                                   "/html[1]/body[1]/app-root[1]/ng-component[1]/app-side-nav-inner-toolbar[1]/div[1]/dx-scroll-view[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/app-measurement-systems[1]/div[1]/div[1]/div[2]/dx-data-grid[1]/div[1]/div[5]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]"),
        "ROW_RESULT_IDSERVICEPOINT": (By.XPATH, "(// td[@ aria-describedby='dx-col-61'])[2]"),
        "SELECTOR_COLUMNA": (By.XPATH, "//i[contains(@class,'dx-icon dx-icon-column-chooser')]"),
        "PTOSERVICIO_COL": (By.XPATH, "//td[@aria-selected='false'][contains(.,'ID Punto de servicio')]"),
        "VENTANA_COLUMNAS": (By.XPATH, "//ul[contains(@class,'dx-treeview-node-container')]"),
        "NEW_COLUMN": (By.XPATH, "(//div[contains(@class,'dx-item-content dx-treeview-item-content')])[1]"),
        "TB_COLUMNAS": (By.XPATH, "//tbody[@role='presentation']/tr[@class='dx-row dx-data-row'][1]"),
        "EDIT_EXTERNAL_SYSTEM": (By.XPATH, "(//li[@class='card-info__litem'][contains(.,'Editar')])[2]"),
        "REMOVE_EXTERNAL_SYSTEM": (By.XPATH, "(//li[@class='card-info__litem'][contains(.,'Eliminar')])[2]"),
        "REMOVE_MSJ_CONFIRM": (By.XPATH, "//button[contains(@id,'btnPopupCancel')]"),
        "PRW_LOGIN_INPUT_USERNAME": (By.ID, "UserName_I"),
        "PRW_LOGIN_INPUT_PASSWORD": (By.ID, "Password_I"),
        "PRW_OPTION_HOME": (By.ID, "mFeatures_DXI0_T"),
        "PRW_OPTION_SCHEDULER": (By.XPATH, "(//span[contains(@class,'dx-vam')])[4]"),
        "PRW_OPTION_PHASOR_DIAGRAMS": (By.XPATH, "(//span[contains(@class,'dx-vam')])[13]"),
        "PRW_OPTION_ADD_PHASOR_DIAGRAMS": (By.XPATH, "(//span[contains(@class,'dx-vam')])[3]"),
        "PRW_FORM_PHASORS_DESC": (By.XPATH, "//input[contains(@id,'PhasorConfiguration.ConfigurationName_I')]"),
        #5070
        "PAP_BTN_MS_CONF": (By.ID, "btnMeasurementSystemViewConfigPanel"),
        "PAP_BTN_AJUSTE_CORTE_ENERGIA": (By.ID, "liMeasurementSystemViewOutage"),
        "PAP_BTN_GUARDAR": (By.ID, "btnPowerOutageSave"),
        "PAP_RADIO_BTN_CERO": (By.ID, "lblPowerOutageCompleteZero"),
        "PAP_RADIO_BTN_NULO": (By.ID, "lblPowerOutageCompleteNull"),
        "PAP_RESULT": (By.XPATH, "//body/div/div/div"),
       
        "PAP_BTN_FILTER": (By.ID, "lblHeaderFiltersOption"),
        "PAP_BTN_NEW_FILTER": (By.ID, "lblFilterFormAddFilter"),
        "PAP_TXT_NAME_FILTER": (By.ID, "txtFilterFormName"),
        "PAP_CBX_OPERADOR_FIL": (By.XPATH, "/html/body/app-root/ng-component/app-side-nav-inner-toolbar/div/app-filter-popup/div/div/app-tab-filter-popup/app-filter-form/div/div[2]/dx-filter-builder/div/div[1]/div[1]"),
        "PAP_SEL_OPTION_AND": (By.XPATH, "//div/div/div/div/ul/li/div/div/span"),
        "PAP_SEL_OPTION_OR": (By.XPATH, "//li[2]/div/div/span"),
        "PAP_ADD_FIELD": (By.XPATH, "/html/body/app-root/ng-component/app-side-nav-inner-toolbar/div/app-filter-popup/div/div/app-tab-filter-popup/app-filter-form/div/div[2]/dx-filter-builder/div/div[1]/div[2]"),
        
        "PAP_CBX_FIELD": (By.XPATH, "/html/body/app-root/ng-component/app-side-nav-inner-toolbar/div/app-filter-popup/div/div/app-tab-filter-popup/app-filter-form/div/div[2]/dx-filter-builder/div/div[2]/div/div/div[2]"),
        "PAP_CBX_FIELD2": (By.XPATH, "//div[2]/div/div[2]"),
        "PAP_CBX_FIELD3": (By.XPATH, "//div[3]/div/div[2]"),

        "PAP_SEL_VARIABLE": (By.XPATH, "//li/div[2]"),
        "PAP_SEL_VARIABLE2": (By.XPATH, "//li/div[2]"),
        "PAP_SEL_VARIABLE3": (By.XPATH, "//li/div[2]"),
        "PAP_SEL_SERVICE_POINT": (By.XPATH, "//li[2]/div[2]"),
        "PAP_SEL_SERVICE_POINT2": (By.XPATH, "//div/div/div[3]"),
        "PAP_SEL_SERVICE_POINT3": (By.XPATH, "//div/div/div[3]"),
        "PAP_SEL_DEVICE": (By.XPATH, "//li[3]/div[2]"),
        "PAP_SEL_DEVICE2": (By.XPATH, "//li[2]/div[2]"),
        "PAP_SEL_DEVICE3": (By.XPATH, "//li[3]/div[2]"),
        "PAP_SCROLL_DEVICE": (By.XPATH, "//div/div/div/div/div/div/div/div[2]/div/div"),

        "PAP_SEL_DESCRIPTION": (By.XPATH, "//li[2]/ul/li[2]/div/div/span"),
        "PAP_SEL_ID_VARIABLE": (By.XPATH, "//li/ul/li[4]/div"),
        "PAP_SEL_DEVICE_ID": (By.XPATH, "//li[3]/ul/li/div/div/span"),
        "PAP_SEL_DATE_START": (By.XPATH, "//li[4]/div/div/span"),
        

        

        "PAP_CBX_OPERATION": (By.XPATH, "/html/body/app-root/ng-component/app-side-nav-inner-toolbar/div/app-filter-popup/div/div/app-tab-filter-popup/app-filter-form/div/div[2]/dx-filter-builder/div/div[2]/div/div/div[3]"),
        "PAP_CBX_OPERATION2": (By.XPATH, "//div[2]/div/div[3]"),
        
        "PAP_SEL_FILTER_DIFERENT": (By.XPATH, "/html/body/div/div/div/div/div/div/div/div[1]/ul/li[6]/div/div/span"),
        "PAP_SEL_FILTER_START_WITH": (By.XPATH, "//li[4]/div/div/span"),
        "PAP_SEL_CONTAINS": (By.XPATH, "//li[2]/div/div/span"),
        "PAP_SEL_GREATER_EQUAL": (By.XPATH, "//li[6]/div/div/span"),
       
        "PAP_TXT_VALUE_FIELD": (By.XPATH, "//div[4]/div"),
        "PAP_BTN_SAVE_FILTER": (By.XPATH, "/html/body/app-root/ng-component/app-side-nav-inner-toolbar/div/app-filter-popup/div/div/app-tab-filter-popup/app-filter-form/div/div[2]/div[2]/button[2]"),
        "PAP_RADIO_BTN_LIST_FILTER_1": (By.ID, "lblFilterFormChoseFilter1"),
        "PAP_RADIO_BTN_LIST_FILTER_0": (By.ID, "lblFilterFormChoseFilter0"),
        "PAP_RADIO_BTN_LIST_FILTER_2": (By.ID, "lblFilterFormChoseFilter2"),
        "PAP_RADIO_BTN_LIST_FILTER_3": (By.ID, "lblFilterFormChoseFilter3"),
        "PAP_BTN_APLICAR": (By.XPATH, "/html/body/app-root/ng-component/app-side-nav-inner-toolbar/div/app-filter-popup/div/div/app-tab-filter-popup/app-filter-form/div/div[2]/div[2]/button[1]"),
        "PAP_MSJ_WARNING_FIELD_NAME_FILTER": (By.ID, "lblFilterFormConfigWarning"),
        "PAP_DELETE_CLAUSULE": (By.XPATH, "/html/body/app-root/ng-component/app-side-nav-inner-toolbar/div/app-filter-popup/div/div/app-tab-filter-popup/app-filter-form/div/div[2]/dx-filter-builder/div/div[2]/div[3]/div/div[1]"),
        "PAP_DELETE_CLAUSULE2": (By.XPATH,"/html/body/app-root/ng-component/app-side-nav-inner-toolbar/div/app-filter-popup/div/div/app-tab-filter-popup/app-filter-form/div/div[2]/dx-filter-builder/div/div[2]/div[2]/div/div[1]"),
        "PAP_HOVER_DATE": (By.XPATH, "//div[4]/div"),
        "PAP_ICON_DATE": (By.XPATH, "//div[2]/div[2]/div/div"),
        "PAP_SEL_DATE": (By.XPATH, "//div/div/div/div/div/div/div/table/tbody/tr[2]/td"),
        "PAP_BTN_DATE_OK": (By.XPATH, "//div[2]/div/div[3]/div/div/div/div/span"),
        "PAP_BTN_CLOSE_FILTER": (By.ID, "lblPopupFilterClose"),
        "PAP_BTN_DELETE_FILTER": (By.ID, "btnFilterFormChoseFilterDelete2"),
        "PAP_BTN_EDIT_FILTER": (By.XPATH, "/html/body/app-root/ng-component/app-side-nav-inner-toolbar/div/app-filter-popup/div/div/app-tab-filter-popup/app-filter-form/div/div[1]/div[2]/ul/li[2]/div/em"),
        "PAP_BTN_ACEPPT_DELETE": (By.ID, "btnPopupAccept"),
        #"PAP_RESULT_FILTER" (By.XPATH, ""),
        

        "PAP_BTN_EXTERNAL_SYSTEM": (By.ID, "btnSideMenuNavigationSecondItem1"),
        "PAP_BTN_INTEROPERABILITY": (By.XPATH, "//div[2]/div/div/em"),
        "PAP_BTN_CAR_INFO": (By.XPATH, "//app-card-info[3]/div/div/div/div[2]/button/em"),
        "PAP_ITEM_DELETE": (By.XPATH, "//app-card-info[3]/div/div/div/div[2]/ul/li[2]"),
        "PAP_BTN_MANTENER": (By.ID, "btnPopupCancel"),
        "PAP_BTN_CAR_INFO1": (By.XPATH, "//app-card-info[4]/div/div/div/div[2]/button/em"),
        "PAP_ITEM_EDITAR": (By.XPATH, "//app-card-info[4]/div/div/div/div[2]/ul/li"),
        "PAP_BTN_TEST_CONECTION": (By.ID, "btnExternalSystemTestConnection")

        

    }
    return locators[locator]
