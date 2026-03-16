from odoo import api, fields, models


class HospitalAdmission(models.Model):
    _name = "hospital.admission"
    _description = "Hospital Admission"

    name = fields.Char(string="Name", required=True)
    patient_id = fields.Many2one("hospital.patient", string="Patient", required=True)
    admit_date = fields.Datetime(string="Admit Date", required=True)
    discharge_date = fields.Datetime(string="Discharge Date")
    bed_no = fields.Char(string="Bed No")
    ward_type = fields.Selection([
        ("general", "General"),
        ("semi", "Semi"),
        ("private", "Private")
    ], string="Ward Type")
    bill_amount = fields.Float(string="Bill Amount")
    paid_amount = fields.Float(string="Paid Amount")
    notes = fields.Text(string="Notes")
    active = fields.Boolean(default=True)

    def action_admit(self):
        self.write({"admit_date": fields.Datetime.now()})

    def action_discharge(self):
        self.write({"discharge_date": fields.Datetime.now()})

    def action_mark_paid(self):
        self.write({"paid_amount": self.bill_amount})
