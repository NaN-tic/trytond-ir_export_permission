
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase
from trytond.pool import Pool
from trytond.tests.test_tryton import activate_module, with_transaction
from trytond.transaction import Transaction


class IrExportPermissionTestCase(ModuleTestCase):
    'Test IrExportPermission module'
    module = 'ir_export_permission'

    @classmethod
    def setUpClass(cls):
        activate_module(['tests', 'ir_export_permission'])

    def create_user(self, login, password, email=None):
        pool = Pool()
        User = pool.get('res.user')

        user, = User.create([{
                    'name': login,
                    'login': login,
                    'email': email,
                    'password': password,
                    }])
        return user

    @with_transaction()
    def test_export(self):
        'Test export_data boolean'
        pool = Pool()
        ExportData = pool.get('test.export_data')
        ModelData = pool.get('ir.model.data')
        Group = pool.get('res.group')

        group = Group(ModelData.get_id('ir_export_permission',
                'group_export_import'))

        export1, = ExportData.create([{
                    'char': 'test',
                    }])
        self.assertEqual(
            ExportData.export_data([export1], ['char']), [['test']])

        user = self.create_user('user1', '12345678')
        with Transaction().set_user(user.id):
            self.assertEqual(
                ExportData.export_data([export1], ['char']), [])

        # save "group_export_import" group at the user and export
        user.groups += (group,)
        user.save()
        with Transaction().set_user(user.id):
            self.assertEqual(
                ExportData.export_data([export1], ['char']), [['test']])

del ModuleTestCase
