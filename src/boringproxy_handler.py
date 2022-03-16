#!/usr/bin/env python3

from boringproxy_api import BoringproxyAdminAPI
import logging

logger = logging.getLogger(__name__)


class BoringproxyHandler(BoringproxyAdminAPI):

    def __init__(self, boringproxy_domain, boringproxy_token):
        super().__init__(boringproxy_domain, boringproxy_token)

    def get_service_token_name(self):
        return "tunnel_token"
