# This file is part ir_export_permission module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class IrExportPermissionTestCase(ModuleTestCase):
    'Test Ir Export Permission module'
    module = 'ir_export_permission'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            IrExportPermissionTestCase))
    return suite
