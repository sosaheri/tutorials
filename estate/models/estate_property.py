# -*- coding: utf-8 -*-

from odoo import fields, models
from dateutil.relativedelta import relativedelta
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Properties"

    active = fields.Boolean('Active', default=False)

    name = fields.Char('Property Name', required=True)
    description = fields.Text('Property Description')
    postcode = fields.Char('Property postcode')
    date_availability = fields.Date('Property availability', copy=False, default=lambda self: fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float('Property expected price', required=True)
    selling_price = fields.Float('Property selling price', readonly=True, copy=False)
    bedrooms = fields.Integer('Property number bedrooms', default=2)
    living_area = fields.Integer('Property living')
    facades = fields.Integer('Property facades')
    garage = fields.Boolean('Property garage')
    garden = fields.Boolean('Property garde')
    garden_area = fields.Integer('Property area garde')
    garden_orientation  = fields.Selection(
        string='Orientation',
        selection=[('North', 'North'), ('South', 'South'), ('West', 'West'), ('East', 'East')],
        help="DEfine orientation")
    state = fields.Selection(
            [('new', 'New'),
             ('offer_received', 'Offer Received'),
             ('offer_accepted', 'Offer Accepted'),
             ('sold', 'Sold '),
             ('canceled', 'Canceled ')], 
        'State', default='new', copy=False, required=True)