# Copyright (c) 2022, osamahmutawakel@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns = get_column(filters)
	data = []
	cond = ""
	# if filters.get("insurance_number"):
	# 	cond += ' AND r.insurance_number= %(insurance_number)s'
	if filters.get("full_name"):
		cond += ' AND e.full_name= %(full_name)s'
	if filters.get("gender"):
		cond += ' AND e.gender= %(gender)s'

	data = frappe.db.sql("""
		select
			*
		from
			`tabEmployee insurance` as r
			join `tabEmployee Financial Insurance` as e
			ON r.name = e.parent
		WHERE

		r.docstatus >= 0

			{0}

		""".format(cond), filters, as_dict=True)

	return columns, data

def get_column(filters):
	columns = [

{
			"fieldname":"insurance_number",
			"label": "Member NO",
			"fieldtype": "Data",
		},
		{
			"fieldname":"full_name",
			"label": "Member Name",
			"fieldtype": "Data",
		},
		{
			"fieldname":"company",
			"label": "Company",
			"fieldtype": "Link",
			"options" : "Company"
		},
		{
			"fieldname":"gender",
			"label": "Gender",
			"fieldtype": "Link",
			"options" : "Gender"
		},
		{
			"fieldname":"social_status",
			"label": " Social Status",
			"fieldtype": "Select",
			"options" : ["Married","Single","Widowed","divorced"]

		},
		{
			"fieldname":"nationality",
			"label": "Nationality",
			"fieldtype": "Data",
		},
		{
			"fieldname":"relationship",
			"label": "Relationship",
			"fieldtype": "Select",
			"options" : ["Employee","Wife","Son","Daughter","Mother","Father"]

		},
		{
			"fieldname":"principal_name",
			"label": "Principal Name",
			"fieldtype": "Data",
		},
		{
			"fieldname":"effective_date",
			"label": "Effective Date",
			"fieldtype": "Data",
		},
		{
			"fieldname":"insurance_value",
			"label": " Gross Premium",
			"fieldtype": "Data",
		},




	]
	return columns


	