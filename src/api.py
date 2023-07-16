from requests import get, delete
from logging import getLogger; log = getLogger(__name__)

from src.dclasses import CPUQuota


class API:
    API_PATH: str = 'https://www.pythonanywhere.com/api/v0'
    FILE_DELETE_TEMPLATE: str = API_PATH + '/user/{username}/files/path/{path}'
    CPU_QUOTA_TEMPLATE: str = API_PATH + '/user/{username}/cpu/'

    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token

    def get_auth_headers(self) -> dict:
        """
        Factory of required auth headers.

        Returns:
            dict: Dictionary with required headers values.
        """
        return {'Authorization': f'Token {self.token}'}

    def delete_file(self, file_path: str) -> None:
        """
        Deletes file from specified path.

        Args:
            file_path (str): Path to file which you need to delete.

        Raises:
            ValueError: If specified file doesn't exist.

        Notes:
            * The path to the file is specified without a slash of the root directory.
                `var/log/...` instead of `/var/log/...`
        """
        url = self.FILE_DELETE_TEMPLATE.format(username=self.username, path=file_path)
        response = delete(url, headers=self.get_auth_headers())

        if response.status_code == 404:
            raise ValueError("File not found")

        response.raise_for_status()
        log.info('OK')
        return None

    def get_cpu_quota(self) -> CPUQuota:
        """
        Returns CPU usage quota data.

        Returns:
            CPUQuota: CPU usage quota data.
        """
        url = self.CPU_QUOTA_TEMPLATE.format(username=self.username)
        response = get(url, headers=self.get_auth_headers())
        response.raise_for_status()
        data = CPUQuota.from_json(response.json())
        log.info(data)
        return data
