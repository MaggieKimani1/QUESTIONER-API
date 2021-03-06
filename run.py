'''this file is the entry point to our app'''

import os
from app import create_app

app = create_app(os.getenv('APP_SETTINGS'))


if __name__ == "__main__":
    app.run()
