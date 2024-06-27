# from odoo import http
#
#
# class PropertyApi(http.Controller):
#
#     @http.route("/v1/property",methods=["GET"], type="http", auth="none", csrf=False)
#     def post_property(self):
#         print("inside post_property method")

from odoo import http
import logging

_logger = logging.getLogger(__name__)

class PropertyApi(http.Controller):

    @http.route("/v1/property", methods=["GET"], type="http", auth="none", csrf=False)
    def get_property(self):
        _logger.info("Inside get_property method")
        return "Hello, this is the property endpoint!"
