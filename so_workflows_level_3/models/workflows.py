from odoo import api, fields, models



_STATES = [
    ('draft', 'Draft'),
    ('to_approve', 'To Approve'),
    ('approval1','Approve'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('done', 'Done')
]

        
    
class SaleOrder(models.Model):
    _inherit = "sale.order"   
    
    
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('appro1','Approve'),
        ('appro2','2nd Approval'),
        ('approval','Final Approval'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    
    def buton_app1(self):
        self.write({'state':'appro2'})
    
    def buton_app2(self):
        self.write({'state':'approval'})

    
    @api.multi
    def approved1(self):
        self.action_confirm()    


    
