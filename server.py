#
# -------------------------------------------------------------------------------
# Copyright © 2023 RedVelvet All Rights Reserved
# -------------------------------------------------------------------------------
#
# Author      : Unknown <unknown@redvelvet.me> (https://redvelvet.me)
# Fingerprint : SHA256:imsemnSEWnegMsIbFn/Qq4K6MXg5QY+EaKjT/rxJoKY
# GitHub      : https://github.com/redvelvetme
#
#

import uvicorn
import asyncio

from bin.config import settings

PATH = 'bin.index:_app'
HOST = '127.0.0.1'
PORT = 8000


async def main():
    config = uvicorn.Config(app=PATH, host=HOST, port=PORT)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    if (settings.APP_ENV.lower() != 'development'):
        asyncio.run(main())
    else:
        uvicorn.run(
            app=PATH,
            host=HOST,
            port=PORT,
            reload=True,
            log_level="info"
        )
