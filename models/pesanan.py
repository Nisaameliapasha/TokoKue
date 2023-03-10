from odoo import api, fields, models


class Pesan(models.Model):
    _name = 'toko.pesan'
    _description = 'New Descrpition'

    name = fields.Char(string='Name')
    pesandetail_ids = fields.One2many(comodel_name='toko.pesandetail', inverse_name='pesan_id', string='Pesanan')
    pegawai_id = fields.Many2one(comodel_name='toko.pegawai', string='Pegawai')
    customer_id = fields.Many2one(comodel_name='toko.customer', string='Customer')
    tanggal = fields.Datetime(string='tanggal',default=fields.Datetime.now)
    metode = fields.Selection([
        ('cash', 'Cash')
        
    ], string='Metode Pembayaran', required=True)
    kue_ids = fields.One2many(comodel_name='toko.kue', inverse_name='pesanan_id', string='Kue')
    total_harga = fields.Integer(compute='_compute_total_harga', string='Total Harga', store=True)

    @api.depends('kue_ids')
    def _compute_total_harga(self):
        for record in self:
            a = sum(self.env['toko.kue'].search([('pesanan_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['toko.pesandetail'].search([('pesanan_id', '=', record.id)]).mapped('harga'))
            record.total_harga = a + b
    sudah_bayar = fields.Boolean(string='Sudah Bayar', default=False)

class PesanDetail(models.Model):
    _name = 'toko.pesandetail'
    _description = 'New Descrpition'

    pesan_id = fields.Many2one(comodel_name='toko.pesan', string='Pesanan')
    kue_id = fields.Many2one(comodel_name='toko.kue', string='Kue')
    nama = fields.Char(string='Nama')
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan')
    @api.depends('kue_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.kue_id.harga
    
    qty = fields.Integer(string='Quantity')

    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
           record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self,vals):
        record = super(PesanDetail, self).create(vals) 
        if record.qty:
            self.env['toko.kue'].search([('id','=',record.kue_id.id)]).write({'stok':record.kue_id.stok-record.qty})
            return record
    


    
    
    
    
    
        
