import json
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class PropertyApi(http.Controller):

    @http.route("/v1/property", methods=["POST"], type="http", auth="none", csrf=False)
    def post_property(self):
        args = request.httprequest.data.decode()
        _logger.info("Received args: %s", args)
        vals = json.loads(args)
        _logger.info("Parsed vals: %s", vals)
        try:
            res = request.env["property"].sudo().create(vals)
            if res:
                return request.make_json_response({
                    "message": "Property has been created successfully",
                    "id": res.id,
                    "name": res.name,
                }, status=200)
        except Exception as error:
            _logger.error("Error creating property: %s", error)
            return request.make_json_response({
                "message": str(error),
            }, status=400)

    @http.route("/v1/property/json", methods=["POST"], type="json", auth="none", csrf=False)
    def post_property_json(self):
        vals = request.jsonrequest
        _logger.info("Parsed JSON vals: %s", vals)
        try:
            res = request.env["property"].sudo().create(vals)
            if res:
                return {
                    "message": "Property has been created successfully",
                    "id": res.id,
                    "name": res.name,
                }
        except Exception as error:
            _logger.error("Error creating property: %s", error)
            return {
                "message": str(error),
            }

    @http.route("/v1/property", methods=["GET"], type="http", auth="none", csrf=False)
    def get_property(self):
        _logger.info("Inside get_property method")
        return "Hello, this is the property endpoint!"

# import json
# from odoo import http
# from odoo.http import request
#
# import logging
#
# _logger = logging.getLogger(__name__)
#
#
# class PropertyApi(http.Controller):
#
#     @http.route("/v1/property", methods=["POST"], type="http", auth="none", csrf=False)
#     def post_property(self):
#         args = request.httprequest.data.decode()
#         print(args)
#         vals = json.loads(args)
#         print("vals:", vals)
#         try:
#
#             res = request.env["property"].sudo().create(vals)
#             if res:
#                 return request.make_json_response({
#                     "message": "Property has been created successfully",
#                     "id": res.id,
#                     "name": res.name,
#                 }, status=200)
#         except Exception as error:
#             return request.make_json_response({
#                 "message": error,
#             }, status=400)
#
#     @http.route("/v1/property/json", methods=["POST"], type="json", auth="none", csrf=False)
#     def post_property_json(self):
#         args = request.httprequest.data.decode()
#         vals = json.loads(args)
#         res = request.env["property"].sudo().create(vals)
#         if res:
#             return {
#                 "message": "Property has been created successfully"
#             }
#         # print(vals)
#
# # class PropertyApi(http.Controller):
# #
# #     @http.route("/v1/property", methods=["GET"], type="http", auth="none", csrf=False)
# #     def get_property(self):
# #         # _logger.info("Inside get_property method")
# #         return "Hello, this is the property endpoint!"
