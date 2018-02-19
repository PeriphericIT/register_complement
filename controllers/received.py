# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
from odoo.tools.translate import _
from odoo.addons.portal.controllers.portal import get_records_pager, pager as portal_pager, CustomerPortal
from odoo.osv.expression import OR
from odoo import api, fields, models, _


class CustomerPortal(CustomerPortal):

    # Recebe uma chamada rest e cria um partner...
    @http.route(['/info'], type='http', auth="none", methods=['POST'],cors="*", csrf=False)
    def receive_line(self, redirect=None, **post):
        print('MESSAGE RECEIVED')
        print(http.request.params)
        partner = request.env['res.partner'].sudo().create(post)
        print(partner)
        if post:
            for k,v in post.items():
                print(k)
                print(v)

    @http.route(['/partners'], type='http', auth="none", methods=['GET'], cors="*", csrf=False)
    def pass_partners(self, redirect=None, **post):
        print(http.request.params)
        return '{Hello:"Diogo"}'

    # @http.route('/partners', type='http', auth='none', cors='*')
    # def hello(self, **kwargs):
    #     print(kwargs)
    #     return "ping"

'''
var unirest = require('unirest');

(Os fields estão sendo tratados pelo formidable)

unirest.post('http://localhost:8069/info')
      .header('Accept', 'application/json')
      .send({ 'name':fields.name,
              'email':fields.email,
              'company_type':fields.company_type})
      .end(function (response) {
        console.log(response.body);
      });


'''