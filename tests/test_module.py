
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.modules.company.tests import CompanyTestMixin
from trytond.tests.test_tryton import ModuleTestCase


class IrExportPermissionTestCase(CompanyTestMixin, ModuleTestCase):
    'Test IrExportPermission module'
    module = 'ir_export_permission'


del ModuleTestCase
