from trytond.pool import Pool
from trytond.transaction import Transaction

def in_group():
    pool = Pool()
    Group = pool.get('res.group')
    User = pool.get('res.user')
    ModelData = pool.get('ir.model.data')

    group = Group(ModelData.get_id('ir_export_permission',
            'group_export_import'))
    transition = Transaction()
    user_id = transition.user
    if user_id == 0:
        user_id = transition.context.get('user', user_id)
    if user_id == 0:
        return True
    user = User(user_id)
    return group in user.groups


class ExportImportMixin:
    __slots__ = ()

    @classmethod
    def export_data(cls, records, fields_names):
        if not in_group():
            return []
        return super().export_data(records, fields_names)

    @classmethod
    def import_data(cls, fields_names, data):
        if not in_group():
            return 0
        return super().import_data(fields_names, data)
