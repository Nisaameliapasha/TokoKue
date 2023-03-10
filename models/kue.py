from odoo import api, fields, models


class Kue(models.Model):
    _name = 'toko.kue'
    _description = 'kue'

    name = fields.Char(string='Nama')
    img = fields.Binary(string='Image')
    stock = fields.Integer(string='Stock')
    harga = fields.Integer(string='Harga Satuan')

    
    
    pesanan_id = fields.Many2one(comodel_name='kue_id', string='Pesanan')
    