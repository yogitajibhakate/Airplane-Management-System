frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.add_custom_button(__('Assign Seat'), function() {
            let d = new frappe.ui.Dialog({
                title: __('Select seat'),
                fields: [
                    {
                        label: __('Seat Number'),
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ],
                primary_action_label: __('assign'),
                primary_action(values) {
                    frm.set_value('seat', values.seat_number);
                    d.hide();
                }
            });
            d.show();
        }, __('Actions'));
    }
});