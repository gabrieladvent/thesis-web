import logging
import os

import streamlit as st
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

logger = logging.getLogger(__name__)


def get_ice_servers():
    """
        Use Twilio's TURN server because Streamlit Community Cloud has changed its infrastructure and WebRTC connection cannot be established without TURN server now.  # noqa: E501
    """

    try:
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    except KeyError:
        logger.warning(
            "Twilio credentials are not set. Fallback to a free STUN server from Google."
        )
        return [{"urls": ["stun:stun.l.google.com:19302"]}]

    client = Client(account_sid, auth_token)

    try:
        token = client.tokens.create()
    except TwilioRestException as e:
        st.warning(
            f"Error occurred while accessing Twilio API. Fallback to a free STUN server from Google. ({e})"
        )
        return [{"urls": ["stun:stun.l.google.com:19302"]}]

    return token.ice_servers
