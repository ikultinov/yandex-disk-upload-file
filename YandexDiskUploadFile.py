import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск
        """

        for file in file_list:
            url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            headers = {'Content-Type': 'application/json',
                       'Authorization': f'OAuth {token}'}
            params = {'path': f'/{file}', 'overwrite': True}
            response = requests.get(url, params=params, headers=headers)
            upload_link = response.json().get('href')
            response = requests.put(upload_link, data=open(file, 'rb'),
                                    headers=headers)
            response.raise_for_status()
            if response.status_code == 201:
                print('Success')


if __name__ == '__main__':
    path_to_file = '/'
    token = ''
    file_list = ['Firefox Installer.exe',
                 'koster_ogon_plamia_146613_1600x900.jpg']
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
