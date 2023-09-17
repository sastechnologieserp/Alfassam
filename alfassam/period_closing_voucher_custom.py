# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


import frappe
from frappe import _
from frappe.utils import flt

from erpnext.accounts.doctype.accounting_dimension.accounting_dimension import (
	get_accounting_dimensions,
)
from erpnext.accounts.utils import get_account_currency
from erpnext.controllers.accounts_controller import AccountsController
from erpnext.accounts.doctype.period_closing_voucher.period_closing_voucher import PeriodClosingVoucher

def get_pl_balances_based_on_dimensions(self, group_by_account=False):
	"""Get balance for dimension-wise pl accounts"""

	dimension_fields = ["t1.cost_center", "t1.finance_book"]

	self.accounting_dimensions = get_accounting_dimensions()
	for dimension in self.accounting_dimensions:
		dimension_fields.append("t1.{0}".format(dimension))

	if group_by_account:
		dimension_fields.append("t1.account")

	return frappe.db.sql(
		"""
		select
			t2.account_currency,
			{dimension_fields},
			sum(t1.debit_in_account_currency) - sum(t1.credit_in_account_currency) as bal_in_account_currency,
			sum(t1.debit) - sum(t1.credit) as bal_in_company_currency
		from `tabGL Entry` t1, `tabAccount` t2
		where
			t1.is_cancelled = 0
			and t1.account = t2.name
			and t2.report_type = 'Profit and Loss'
			and t2.docstatus < 2
			and t2.company = %s
			and t1.cost_center = %s
			and t1.posting_date between %s and %s
		group by {dimension_fields}
	""".format(
			dimension_fields=", ".join(dimension_fields)
		),
		(self.company, self.cost_center, self.get("year_start_date"), self.posting_date),
		as_dict=1,
	)


PeriodClosingVoucher.get_pl_balances_based_on_dimensions=get_pl_balances_based_on_dimensions