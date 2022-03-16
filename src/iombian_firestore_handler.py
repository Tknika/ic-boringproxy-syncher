#!/usr/bin/env python3

import logging
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


logger = logging.getLogger(__name__)


class IoMBianFirestoreHandler():

    USERS_COLLECTION_PATH = "users"

    def __init__(self, app_credentials_path, users_handler):
        self.app_credenctials_path = app_credentials_path
        self.users_handler = users_handler
        self.users_collection = None
        self.users_subscription = None

        cred = credentials.Certificate(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), app_credentials_path))
        firebase_admin.initialize_app(cred)

        self.client = firestore.client()

    def start(self):
        logger.debug("Starting IoMBian Firestore Handler")
        self.users_collection = self.client.collection(
            self.USERS_COLLECTION_PATH)
        self.users_subscription = self.users_collection.on_snapshot(
            self.on_user)

    def stop(self):
        logger.debug("Stopping IoMBian Firestore Handler")
        if self.users_subscription:
            self.users_subscription.unsubscribe()

    def on_user(self, collection_snapshot, changes, read_time):
        for user in collection_snapshot:
            user_id = user.id
            user_data = user.to_dict()
            user_email = user_data.get("email")
            token_name = self.users_handler.get_service_token_name()

            if not token_name in user_data:
                logger.info(
                    f"User '{user_email}' does not have a valid '{token_name}' token.")
                self.users_handler.create_full_user(user_email)
                token = self.users_handler.get_user_token(
                    user_email)

                token_field = {token_name: token}
                self.client.collection(self.USERS_COLLECTION_PATH).document(
                    user_id).update(token_field)
                logger.info(f"User '{user_email}' correctly updated.")
