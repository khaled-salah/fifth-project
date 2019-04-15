from odoo import models, fields, api


class InheritTimesheet(models.Model):
    _name = "account.analytic.line"

    _inherit =["account.analytic.line", 'mail.thread']





    overtime = fields.Boolean(string="OverTime",track_visibility='onchange')
    # new_name1 = fields.Char(string="Description",default="/")

    state = fields.Selection([
        ('a', "Draft"),
        ('b', "Submit"),
        ('c', "Approved"),
        ('d', "rejected"),
    ], default='a', string="Stage",track_visibility='onchange')



    @api.multi
    def action_draft(self):
        self.state = 'a'

    @api.multi
    def action_submit(self):
        self.state = 'b'

    @api.multi
    def action_approve(self):
        self.state = 'c'


    @api.multi
    def action_canccel(self):
        self.state = 'd'

