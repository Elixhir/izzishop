import os
import uuid
from supabase import create_client

class SupabaseStorage:

    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        self.bucket = os.getenv("SUPABASE_BUCKET")

        self.client = create_client(self.url, self.key)

    def upload_file(self, file, store_id: str):

        file_extension = file.filename.split(".")[-1]
        filename = f"{store_id}/{uuid.uuid4()}.{file_extension}"

        self.client.storage.from_(self.bucket).upload(
            filename,
            file.read(),
            {"content-type": file.content_type}
        )

        public_url = self.client.storage.from_(self.bucket).get_public_url(filename)

        return public_url
    
    def delete_file(self, file_url: str):

        if not file_url:
            return

        try:
            # ejemplo:
            # https://xxx.supabase.co/storage/v1/object/public/products/store1/uuid.jpg

            split_key = f"/storage/v1/object/public/{self.bucket}/"

            if split_key not in file_url:
                return

            file_path = file_url.split(split_key)[1]

            self.client.storage.from_(self.bucket).remove([file_path])

        except Exception as e:
            print("Error deleting file from Supabase:", e)
           
            
    def replace_file(self, old_url, new_file, store_id):

        if old_url:
            self.delete_file(old_url)

        return self.upload_file(new_file, store_id)