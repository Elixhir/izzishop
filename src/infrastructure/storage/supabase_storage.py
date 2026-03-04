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