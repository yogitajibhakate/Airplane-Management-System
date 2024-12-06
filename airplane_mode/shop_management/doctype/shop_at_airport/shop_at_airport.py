# Copyright (c) 2024, Yogita and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document


class ShopAtAirport(WebsiteGenerator):
    def before_save(self):
        shop_config = frappe.get_single("Shop Configuration")
        if self.rent_amount == 0:
            self.rent_amount = shop_config.default_rent_amount
