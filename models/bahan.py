from odoo import api, fields, models


class Bahan(models.Model):
    _name = 'toko.bahan'
    _description = 'Bahan'

    name = fields.Char(string='Nama')
    img = fields.Binary(string='Image')
    stock = fields.Integer(string='Stock')
    harga = fields.Integer(string='Harga Satuan')
    


    

    