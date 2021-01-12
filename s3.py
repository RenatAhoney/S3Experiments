from minio import Minio

endpoint = "127.0.0.1:9000"
access_key = 'Supervisor'
secret_key = 'Supervisor'
bucket_name = 'testbucket'


def main():
    # Создаем подключение
    client = Minio(endpoint, access_key, secret_key, secure=False)
    bucket = client.bucket_exists(bucket_name)
    # Проверяем есть ли бакет, если нет то создаем
    if not bucket:
        client.make_bucket(bucket_name)
    # Пишем файл file.txt
    try:
        client.fput_object(bucket_name, object_name="file.txt", file_path="file.txt", content_type="text")
    except Exception as ex:
        print(ex)
    # Читаем файл file.txt переименовываем и сохраняем
    try:
        client.fget_object(bucket_name, object_name="file.txt", file_path="downloaded_file.txt")
    except Exception as ex:
        print(ex)


main()
