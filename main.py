from YaUploader import YaUploader

TOKEN = ""

if __name__ == '__main__':
    uploader = YaUploader(token=TOKEN)
    result = uploader.upload("netologiya/test.txt", "test.txt")
    print(result)
