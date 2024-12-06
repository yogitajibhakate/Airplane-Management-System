# Copyright (c) 2024, Yogita and contributors
# For license information, please see license.txt

app_name = "airplane_mode"
app_title = "Airplane Mode"
app_publisher = "Yogita"
app_description = "This is an app for managing tickets"
app_email = "yogita22@navgurukul.org"
app_license = "MIT"

modules = {
    "Airport Shop Management": "airplane_mode.airport_shop_management"
}

# Includes in <head>
# ------------------
# include js, css files in header of desk.html
# app_include_css = "/assets/airplane_mode/css/airplane_mode.css"
# app_include_js = "/assets/airplane_mode/js/airplane_mode.js"

# include js, css files in header of web template
# web_include_css = "/assets/airplane_mode/css/airplane_mode.css"
# web_include_js = "/assets/airplane_mode/js/airplane_mode.js"

# Generators
# ----------
# Automatically create page for each record of this doctype
website_generators = ["Airplane Flight"]

# URL Route Rules
# ----------------
website_route_rules = [
    {"from_route": "/flights/<path:flight_name>", "to_route": "airplane_mode.airplane_mode.doctype.airplane_flight.airplane_flight"},
]

# Jinja
# ----------
# Add methods and filters to jinja environment
# jinja = {
#     "methods": "airplane_mode.utils.jinja_methods",
#     "filters": "airplane_mode.utils.jinja_filters"
# }

# Installation
# ------------
# before_install = "airplane_mode.install.before_install"
# after_install = "airplane_mode.install.after_install"

# Uninstallation
# --------------
# before_uninstall = "airplane_mode.uninstall.before_uninstall"
# after_uninstall = "airplane_mode.uninstall.after_uninstall"

# Permissions
# -----------
# Permissions evaluated in scripted ways
# permission_query_conditions = {
#     "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
# has_permission = {
#     "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events
# doc_events = {
#     "*": {
#         "on_update": "method",
#         "on_cancel": "method",
#         "on_trash": "method"
#     }
# }

# Testing
# -------
# before_tests = "airplane_mode.install.before_tests"

# Authentication and authorization
# --------------------------------
# auth_hooks = [
#     "airplane_mode.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

