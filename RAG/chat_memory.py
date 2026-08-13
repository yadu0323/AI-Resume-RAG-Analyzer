import json
import os


class ChatMemory:

    def __init__(self, file_path="data/chat_history/chat.json"):
        self.file_path = file_path

        os.makedirs(
            os.path.dirname(file_path),
            exist_ok=True
        )

    def save(self, messages):

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                messages,
                f,
                indent=4,
                ensure_ascii=False
            )

    def load(self):

        if not os.path.exists(self.file_path):
            return []

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def clear(self):

        self.save([])