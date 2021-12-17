import s3fs

class S3:
    def __init__(self, base_bucket="taka_test", key="", secret="") -> None:
        url = "https://"
        self.key = key
        self.secret = secret
        self.s3fs_conn = s3fs.S3FileSystem(anon=False, key=self.key, secret=self.secret,
                                      client_kwargs={'endpoint_url': url})
        self.bucket = base_bucket

    def ls(self) -> list:
        return self.s3fs_conn.ls(self.bucket)

    def write(self, filename, content):
        with self.s3fs_conn.open(self.bucket+"/"+filename, 'w') as f:
            f.write(str(content))

    def reader(self, filepath):
        with self.s3fs_conn.open(filepath, 'r') as f:
            return f.read()

    def file_upload(self, filename, filepath):
        s3_path = f"{self.bucket}/{filename}"
        self.s3fs_conn.put(filepath, s3_path)

    def folder_upload(self, dst, src_dir):
        s3_path = f"{self.bucket}/{dst}"
        self.s3fs_conn.put(src_dir, s3_path, recursive=True)


if __name__ == '__main__':
    cl = S3()

    ls = cl.ls()
    print(ls)

    fn = "test.txt"
    txt = "hello"
    cl.write(fn, txt)

    cl.file_upload("test_upload.txt", "test_upload.txt")
    cl.folder_upload("testDir", "items")

    ls = cl.ls()
    print(ls)

    data = cl.reader(fn)
    print(data)
