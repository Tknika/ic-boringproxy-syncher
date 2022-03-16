#!/usr/bin/env python3

from dotenv import load_dotenv
import logging
from boringproxy_handler import BoringproxyHandler
from iombian_firestore_handler import IoMBianFirestoreHandler
from os import environ as env
import signal

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s - %(name)-16s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
BORINGPROXY_DOMAIN = env.get("BORINGPROXY_DOMAIN")
BORINGPROXY_TOKEN = env.get("BORINGPROXY_TOKEN")


def signal_handler(sig, frame):
    logger.info("Stopping IoMBian Configurator Boringproxy Syncher Service")
    firestore_handler.stop()


if __name__ == "__main__":
    logger.info("Starting IoMBian Configurator Boringproxy Syncher Service")

    boringproxy_handler = BoringproxyHandler(
        BORINGPROXY_DOMAIN, BORINGPROXY_TOKEN)

    firestore_handler = IoMBianFirestoreHandler(
        "./service_account_key.json", boringproxy_handler)
    firestore_handler.start()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()
