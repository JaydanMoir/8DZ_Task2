import requests

class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_upload_link(self, filepath):
        HOST = "https://cloud-api.yandex.net:443"
        url = f"{HOST}/v1/disk/resources/upload"
        headers = {"Authorization": self.token}
        params = {"path": filepath, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload(self, filepath, filename):
        href = self.get_upload_link(filepath=filepath).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        # if response.status_code == 201:
        #     print("Success")
        return f"Файл успешно заружен"
