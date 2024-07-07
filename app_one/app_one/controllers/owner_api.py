import json
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class OwnerApi(http.Controller):

    @http.route("/v1/owner", methods=["POST"], type="http", auth="none", csrf=False)
    def post_owner(self):
        args = request.httprequest.data.decode()
        _logger.info("Received args: %s", args)
        vals = json.loads(args)
        _logger.info("Parsed vals: %s", vals)
        try:
            res = request.env["owner"].sudo().create(vals)
            if res:
                return request.make_json_response({
                    "message": "Owner has been created successfully",
                    "id": res.id,
                    "name": res.name,
                }, status=201)
        except Exception as error:
            _logger.error("Error creating owner: %s", error)
            return request.make_json_response({
                "error": str(error),
            }, status=400)

    @http.route("/v1/owner/<int:owner_id>", methods=["PUT"], type="http", auth="none", csrf=False)
    def update_owner(self, owner_id):
        try:
            owner_id = request.env['owner'].sudo().search([('id', '=', owner_id)])
            if not owner_id:
                return request.make_json_response({
                    "error": "ID does not exist",
                }, status=400)
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            owner_id.write(vals)
            return request.make_json_response({
                "message": "owner has been updated successfully",
                "id": owner_id.id,
                "name": owner_id.name,
            }, status=200)
        except Exception as error:
            return request.make_json_response({
                "error": str(error),
            }, status=400)

    @http.route("/v1/owner/<int:owner_id>", methods=["GET"], type="http", auth="none", csrf=False)
    def get_owner(self, owner_id):
        try:
            owner_id = request.env['owner'].sudo().search([('id', '=', owner_id)])
            if not owner_id:
                return request.make_json_response({
                    "error": "ID does not exist",
                }, status=400)
            return request.make_json_response({
                "id": owner_id.id,
                "name": owner_id.name,
                "phone": owner_id.phone,
                "address": owner_id.address,
            }, status=200)
        except Exception as error:
            return request.make_json_response({
                "error": str(error),
            }, status=400)

    @http.route("/v1/owner/<int:owner_id>", methods=["DELETE"], type="http", auth="none", csrf=False)
    def delete_owner(self, owner_id):
        try:
            owner_id = request.env['owner'].sudo().search([('id', '=', owner_id)])
            if not owner_id:
                return request.make_json_response({
                    "error": "ID does not exist",
                }, status=400)
            owner_id.unlink()
            return request.make_json_response({
                "message": "Owner has been deleted successfully",
                "id": owner_id.id,
            }, status=200)
        except Exception as error:
            return request.make_json_response({
                "error": str(error),
            }, status=400)
