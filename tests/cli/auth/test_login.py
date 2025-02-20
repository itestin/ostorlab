"""Tests for auth login command."""
from unittest import mock
import click
from click.testing import CliRunner

from ostorlab import configuration_manager
from ostorlab.apis.runners import login_runner, authenticated_runner
from ostorlab.cli import rootcli


@mock.patch.object(authenticated_runner.AuthenticationError, '__init__')
def testOstorlabAuthLoginCLI_whenInvalidLoginCredentialsAreProvided_raisesAuthenticationException(
        mock_authentication_error_init, requests_mock):
    """Test ostorlab auth login command with wrong login credentials.
    Should raise AuthenticationError.
    """

    mock_authentication_error_init.return_value = None
    runner = CliRunner()
    requests_mock.post(login_runner.TOKEN_ENDPOINT, json={'non_field_errors': [
        'Unable to log in with provided credentials.']}, status_code=400)
    result = runner.invoke(
        rootcli.rootcli, ['auth', 'login'], input='username\npassword')

    assert result.exception is None
    mock_authentication_error_init.assert_called()


def testOstorlabAuthLoginCLI_whenValidLoginCredentialsAreProvided_tokenSet(
        requests_mock):
    """Test ostorlab auth login command with valid login credentials (no otp required).
    Should set API key.
    """

    api_key_dict = {'data': {'createApiKey': {'apiKey': {
        'secretKey': 'ADABYMTu.S7Y8zmKxpbgTcSuGmsC3rkPdAs95yMwW', 'apiKey':
            {'expiryDate': None, 'id': '54a6e602-f7c1-47bb-9ca0-af598fcf3cf4'}}}}}
    token_dict = {'token': '2fd7a589-64b4-442e-95aa-eb0d082aab63'}
    runner = CliRunner()
    requests_mock.post(login_runner.TOKEN_ENDPOINT, json=token_dict, status_code=200)
    requests_mock.post(authenticated_runner.AUTHENTICATED_GRAPHQL_ENDPOINT,
                       json=api_key_dict, status_code=200)
    result = runner.invoke(
        rootcli.rootcli, ['auth', 'login'], input='username\npassword')

    assert result.exception is None
    assert configuration_manager.ConfigurationManager(
    ).api_key == api_key_dict['data']['createApiKey']['apiKey']['secretKey']


@mock.patch.object(click, 'prompt')
def testOstorlabAuthLoginCLI_whenValidLoginCredentialsAreProvidedWithoutOtp_promptOtp(mock_prompt, requests_mock):
    """Test ostorlab auth login command with correct login credentials without OTP.
    Should assert that the otp prompt is called.
    """

    mock_prompt.return_value = None
    runner = CliRunner()
    token_dict = {'token': '2fd7a589-64b4-442e-95aa-eb0d082aab63'}
    requests_mock.post(login_runner.TOKEN_ENDPOINT, [{'json': {'non_field_errors': [
        'Must include "otp_token"']}, 'status_code': 400}, {'json': token_dict, 'status_code': 200}])
    runner.invoke(
        rootcli.rootcli, ['auth', 'login'], input='username\npassword')

    mock_prompt.assert_called()
