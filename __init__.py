# This file is part ir_export_permission module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from trytond.model import ModelSQL
from . import ir

def register():
    Pool.register_mixin(ir.ExportImportMixin, ModelSQL,
        module='ir_export_permission')
