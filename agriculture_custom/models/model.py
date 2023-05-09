from odoo import models, fields, api, _


class CropRequests(models.Model):
	_inherit = "crop.requests"


	from_beds = fields.Char(string = "From")
	to_beds = fields.Integer(string = "To")