"""Handles all API calls and behind the scenes operations such as authentication, validation, etc.

This module contains code to handle all API calls and any behind the scenes logic
like authentication. It also has classes for authentication errors, API response errors, etc.

    Typical usage example:

    foo = APIRunner(username, password, token_duration)
    foo.authenticate()
"""

import logging

from typing import Dict

import requests
import click

from ostorlab import configuration_manager
from ostorlab.apis import create_api_key
from ostorlab.apis import login
from ostorlab.apis import revoke_api_key
from ostorlab.apis import request as api_request

logger = logging.getLogger(__name__)


class Error(Exception):
    """Base Error Class"""


class AuthenticationError(Error):
    """Authentication Error."""


class ResponseError(Error):
    """Response Error."""


class APIRunner:
    """Handles all API calls and behind the scenes operations such as authentication,
       validation, etc.
    """

    def __init__(self,
                 username: str = None,
                 password: str = None,
                 token_duration: str = None,
                 proxy: str = None,
                 verify: bool = True):
        """Constructs all the necessary attributes for the object.

        Args:
            username: the username (email) used to login.
            password: the password used to login.
            token_duration: The duration for which the token is valid
            (Can be in minutes, hours, days, or a combination of any two or all three).
            proxy: The proxy through which a request is made. Defaults to None.
            verify: Whether or not to verify the TLS certificate. Defaults to True.
        """

        self._username = username
        self._password = password
        self._proxy = proxy
        self._verify = verify
        self._token = None
        self._token_duration = token_duration
        self._otp_token = None
        self.configuration_manager = configuration_manager.ConfigurationManager()
        self._api_key = self.configuration_manager.get_api_key()

    def _login_user(self) -> requests.models.Response:
        """Logs in the user.

        Returns:
            The API response.
        """
        login_request = login.UsernamePasswordLoginAPIRequest(
            self._username, self._password, self._otp_token)
        return self._sent_request(login_request)

    def authenticate(self) -> None:
        """Authenticates the user.

        Raises:
            AuthenticationError: If user credentials are not valid.
        """
        response = self._login_user()

        if response.status_code != 200:
            field_errors = response.json().get('non_field_errors')
            if field_errors is not None and field_errors[0] == 'Must include \"otp_token\"':
                self._otp_token = click.prompt(
                    'Please enter the OTP code from your authenticator app')
                self.authenticate()
            else:
                logger.debug('response %s', response.content)
                raise AuthenticationError(response.status_code)
        else:
            self._token = response.json().get('token')
            api_key_response = self.execute(
                create_api_key.CreateAPIKeyAPIRequest(self._token_duration))
            api_data = api_key_response['data']['createApiKey']['apiKey']
            self._api_key = api_data['secretKey']
            self.configuration_manager.set_api_data(api_data)
            self._token = None

    def revoke_api_key(self) -> None:
        if self._api_key is None:
            return
        api_key_id = self.configuration_manager.get_api_key_id()
        res = self.execute(revoke_api_key.RevokeAPIKeyAPIRequest(api_key_id))
        logger.info(res)
        self.configuration_manager.delete_api_data()
        self._api_key = None

    def execute(self, request: api_request.APIRequest) -> Dict:
        """Executes a request using the GraphQL API.

        Args:
            request: The request to be executed

        Raises:
            ResponseError: When the API returns an error

        Returns:
            The API response
        """
        if self._token is not None:
            headers = {'Authorization': f'Token {self._token}'}
        else:
            headers = {'X-Api-Key': f'{self._api_key}'}
        response = self._sent_request(
            request, headers)
        if response.status_code != 200:
            raise ResponseError(
                f'Response status code is {response.status_code}: {response.content}')
        else:
            return response.json()

    def _sent_request(self, request: api_request.APIRequest, headers=None,
                      multipart=False) -> requests.Response:
        """Sends an API request
        """
        if self._proxy is not None:
            proxy = {
                'https': self._proxy
            }
        else:
            proxy = None

        if multipart:
            return requests.post(request.endpoint, files=request.data, headers=headers,
                                 proxies=proxy, verify=self._verify)
        else:
            return requests.post(request.endpoint, data=request.data, headers=headers,
                                 proxies=proxy, verify=self._verify)
