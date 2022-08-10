// Copyright (c) 2022, osamahmutawakel@gmail.com and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["insurance Report"] = {
	"filters": [
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
		// {
		// 	"fieldname":"social_status",
		// 	"label": __(" Social Status"),
		// 	"fieldtype": "Select",
		// 	"options" : ["Married","Single","Widowed","divorced"]

		// },
		// {
		// 	"fieldname":"nationality",
		// 	"label": __("Nationality"),
		// 	"fieldtype": "Data",
		// },
		// {
		// 	"fieldname":"relationship",
		// 	"label": __("Relationship"),
		// 	"fieldtype": "Select",
		// 	"options" : ["Employee","Wife","Son","Daughter","Mother","Father"]

		// },
		// {
		// 	"fieldname":"principal_name",
		// 	"label": __("Principal Name"),
		// 	"fieldtype": "Data",
		// },
		// {
		// 	"fieldname":"effective_date",
		// 	"label": __("Effective Date"),
		// 	"fieldtype": "Data",
		// },
		// {
		// 	"fieldname":"insurance_value",
		// 	"label": __(" Gross Premium"),
		// 	"fieldtype": "Data",
		// },


	]
};
