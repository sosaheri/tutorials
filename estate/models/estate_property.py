# -*- coding: utf-8 -*-

from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Properties"
    _order = "sequence"

    name = fields.Char('Property Name', required=True, translate=True)
    description = fields.Text('Property Description', translate=True)
    postcode = fields.Char('Property postcode', translate=True)
    date_availability = fields.Date('Property availability', translate=True)
    expected_price = fields.Float('Property expected price', required=True, translate=True)
    selling_price = fields.Float('Property selling price', translate=True)
    bedrooms = fields.Integer('Property number bedrooms', translate=True)
    living_area = fields.Integer('Property living', translate=True)
    facades = fields.Integer('Property facades', translate=True)
    garage = fields.Boolean('Property garage', translate=True)
    garden = fields.Boolean('Property garde', translate=True)
    garden_area = fields.Integer('Property area garde', translate=True)
    garden_orientation  = fields.Selection(
        string='Orientation',
        selection=[('North', 'North'), ('South', 'South'), ('West', 'West'), ('East', 'East')],
        help="DEfine orientation")