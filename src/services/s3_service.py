import boto3
from src.config.settings import S3_BUCKET_NAME, S3_BASE_PATH
import os

class S3Service:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.bucket_name = S3_BUCKET_NAME
        self.base_path = S3_BASE_PATH

    def upload_file(self, local_file_path, s3_file_path=None):
        """로컬 파일을 S3에 업로드"""
        if s3_file_path is None:
            s3_file_path = f"{self.base_path}/{os.path.basename(local_file_path)}"

        try:
            with open(local_file_path, "rb") as f:
                self.s3_client.upload_fileobj(
                    f,
                    self.bucket_name,
                    s3_file_path,
                    ExtraArgs={
                        "ContentType": "image/jpeg",
                    }
                )
            print(f"✅ Uploaded {local_file_path} to https://{self.bucket_name}.s3.amazonaws.com/{s3_file_path}")
            return True
        except Exception as e:
            print(f"Error uploading file: {e}")
            return False

    def upload_file_download(self, local_file_path, s3_file_path=None):
        """로컬 파일을 S3에 업로드 (다운로드 가능한 버전)"""
        if s3_file_path is None:
            s3_file_path = f"{self.base_path}/{os.path.basename(local_file_path)}"

        try:
            self.s3_client.upload_file(local_file_path, self.bucket_name, s3_file_path)
            print(f"Successfully uploaded {local_file_path} to {self.bucket_name}/{s3_file_path}")
            return True
        except Exception as e:
            print(f"Error uploading file: {e}")
            return False 