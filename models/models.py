# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BenchMarketing(models.Model):
    _name = 'bench.marketing'

    name = fields.Char(stirng="Name")
    type = fields.Selection([('inter','Internal'),('comp','Competitive'),('func','Functional or industry')],
    	string="Type")
    responsible = fields.Many2one("res.users", string="Responsible")
    description = fields.Text()
    state = fields.Selection([('draft','Draft'),('analyse','Analyse'),('action','Action'),('done','Done')],
    	string="State")

    metrics_ids = fields.One2many("bench.marketing.metrics", "benchmarketing_id")
    log_ids = fields.One2many("bench.marketing.log", "benchmarketing_id")


class BenchMarketingMetrics(models.Model):
    _name = 'bench.marketing.metrics'

    name = fields.Char()
    description = fields.Text()
    benchmarketing_id = fields.Many2one("bench.marketing", "BenchMarketing")
    team_id = fields.Many2one("bench.marketing.team")
    target_id = fields.Many2one("bench.marketing.target")


class BenchMarketingTeam(models.Model):
    _name = 'bench.marketing.team'

    name = fields.Char(string="Name")
    responsible = fields.Many2one("res.users", string="Leader")
    description = fields.Text()


class BenchMarketingLog(models.Model):
    _name = 'bench.marketing.log'

    name = fields.Char()
    description = fields.Text()
    benchmarketing_id = fields.Many2one("bench.marketing", "BenchMarketing")


class BenchMarketingTarget(models.Model):
    _name = 'bench.marketing.target'

    name = fields.Char()
    partner_id = fields.Many2one("res.partner", string="Standard Object")
    content = fields.Text(string="Content")
    scheme = fields.Text(string="Scheme")