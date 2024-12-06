import frappe

def execute(filters=None):
    # Define the columns
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
    
    # Fetch data from the Airplane Ticket table
    data = frappe.get_all(
        "Airplane Ticket",
        fields=["sum(flight_price) as revenue", "flight.airplane as airplane"],
        filters={"docstatus": 1},
        group_by="airplane"
    )

    # Prepare chart data, handling None cases
    labels = [x['airplane'][:-4] if x['airplane'] else 'Unknown' for x in data]
    values = [x['revenue'] for x in data]
    
    # Calculate total revenue
    total_revenue = sum(values)

    # Add total revenue to the chart or report summary
    chart = {
        "data": {
            "labels": labels,
            "datasets": [{"values": values}],
        },
        "type": "donut",
    }

    # Return columns, data, and add the total revenue to the report summary
    report_summary = [
        {
            "label": "Total Revenue",
            "value": total_revenue,
            "datatype": "Currency",
            "indicator": "green"
        }
    ]

    return columns, data, None, chart, report_summary
