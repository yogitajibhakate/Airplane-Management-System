import frappe

def execute(filters=None):
    columns = [
        {
            "fieldname": "airplane",
            "label": "Airline",
            "fieldtype": "data"
        },
        {
            "fieldname": "revenue",
            "label": "Revenue",
            "fieldtype": "Currency",
            "options": "INR"
        }
    ]
    
    data = frappe.get_all(
        "Airplane Ticket",
        fields=["sum(flight_price) as revenue", "flight.airplane as airplane"],
        filters={"docstatus": 1},
        group_by="airplane"
    )

    labels = [x['airplane'][:-4] if x['airplane'] else 'Unknown' for x in data]
    values = [x['revenue'] for x in data]
    
    total_revenue = sum(values)

    chart = {
        "data": {
            "labels": labels,
            "datasets": [{"values": values}],
        },
        "type": "donut",
    }

    report_summary = [
        {
            "label": "Total Revenue",
            "value": total_revenue,
            "datatype": "Currency",
            "indicator": "green"
        }
    ]

    return columns, data, None, chart, report_summary
