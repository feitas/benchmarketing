# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BenchMarketing(models.Model):
    _name = 'bench.marketing'

    name = fields.Char(stirng="Name", required=1)
    type = fields.Selection([('inter','Internal'),('comp','Competitive'),('func','Functional or industry')],
    	string="Type")
    responsible = fields.Many2one("res.users", string="Responsible")
    description = fields.Text()
    state = fields.Selection([('draft','Draft'),('analyse','Analyse'),('action','Action'),('done','Done')],
    	string="State", default='draft')

    metrics_ids = fields.One2many("bench.marketing.metrics", "benchmarketing_id")
    log_ids = fields.One2many("bench.marketing.log", "benchmarketing_id")


class BenchMarketingMetrics(models.Model):
    _name = 'bench.marketing.metrics'

    name = fields.Char(string="Name", required=1)
    description = fields.Text(string="Description")
    benchmarketing_id = fields.Many2one("bench.marketing", "BenchMarketing")
    team_id = fields.Many2one("bench.marketing.team")
    target_id = fields.Many2one("bench.marketing.target")


class BenchMarketingTeam(models.Model):
    _name = 'bench.marketing.team'

    name = fields.Char(string="Name", required=1)
    responsible = fields.Many2one("res.users", string="Leader")
    description = fields.Text(string="Description")


class BenchMarketingLog(models.Model):
    _name = 'bench.marketing.log'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    benchmarketing_id = fields.Many2one("bench.marketing", "BenchMarketing")


class BenchMarketingTarget(models.Model):
    _name = 'bench.marketing.target'

    name = fields.Char(string="Name", required=1)
    partner_id = fields.Many2one("res.partner", string="Standard Object")
    content = fields.Text(string="Content")
    scheme = fields.Text(string="Scheme")