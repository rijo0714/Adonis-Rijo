from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertion import AssertionsTest
from searchtest import SearchTests

#Variables para cargar los casos de prueba
assertion_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

#Construyendo la suit de pruebas
smoke_test = TestSuite([assertion_test, search_test])

#Parámetros para generar el reporte
kwargs = {
    "output": "reports/smoke-report"
}

runner = HTMLTestRunner(**kwargs) #Pasando los argumentos para la generación del reporte
runner.run(smoke_test) #Llamar a la suit de prueba