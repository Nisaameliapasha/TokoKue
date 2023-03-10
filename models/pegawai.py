from odoo import api, fields, models


class Pegawai(models.Model):
    _name = 'toko.pegawai'
    _description = 'List Pegawai'

    name = fields.Char(string='Nama')
    no_telp = fields.Char(string='No Telephone')
    alamat = fields.Char(string='Alamat')
    gaji = fields.Integer(string='Gaji')
    