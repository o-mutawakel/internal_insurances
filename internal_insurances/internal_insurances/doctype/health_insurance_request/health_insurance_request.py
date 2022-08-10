# Copyright (c) 2022, osamahmutawakel@gmail.com and contributors
# For license information, please see license.txt
import frappe

from frappe.model.document import Document

class HealthInsuranceRequest(Document):
	pass
	def on_submit(self):
		create(self.name)
		

@frappe.whitelist()
def create(heal):
	heal = frappe.get_doc("Health Insurance Request", heal)
	new_doc = frappe.get_doc(dict(
            doctype = 'Employee insurance',
            posting_date = heal.posting_date,
		    insurance_applicant = heal.insurance_applicant,
		    # date_of_birth = heal.date_of_birth,
            # job = heal.job,
        #     educational_level = heal.educational_level,
        #     card_no = heal.card_no,
        #     nationality = heal.nationality,
        #     relationship = heal.relationship,
        #     gender = heal.gender,
        #     social_status = heal.social_status,
        #     personal_image = heal.personal_image,
        #    employee_financial_insurance=heal.employee_information,
  	  ))
	for i in heal.employee_information:
		new_doc.append("employee_financial_insurance", {
			"full_name": i.full_name,
			"date_of_birth": i.date_of_birth,
			"job": i.job,
			"educational_level": i.educational_level,
			"card_no": i.card_no,
			"nationality": i.nationality,
			"relationship": i.relationship,
			"gender": i.gender,
			"social_status": i.social_status,
			"personal_image": i.personal_image,
			"social_status": i.social_status,

		})

		new_doc.save()

