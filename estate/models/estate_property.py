# -*- coding: utf-8 -*-

from odoo import fields, models
from dateutil.relativedelta import relativedelta
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Properties"

    active = fields.Boolean('Active', default=False)

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Available From', copy=False, default=lambda self: fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float('Expected price', required=True)
    selling_price = fields.Float('Selling price', readonly=True, copy=False)
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area (sqm)')
    garden_orientation  = fields.Selection(
        string='Garden Orientation',
        selection=[('North', 'North'), ('South', 'South'), ('West', 'West'), ('East', 'East')],
        help="DEfine orientation")
    state = fields.Selection(
            [('new', 'New'),
             ('offer_received', 'Offer Received'),
             ('offer_accepted', 'Offer Accepted'),
             ('sold', 'Sold '),
             ('canceled', 'Canceled ')], 
        'State', default='new', copy=False, required=True)