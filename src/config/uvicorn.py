import asyncio
import uvicorn
import os

def run_server():
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8080"))
    workers = int(os.environ.get('SERVER_PROCESSES', '2'))
    # critical|error|warning|info|debug|trace
    log_level = os.environ.get('LOG_LEVEL', 'info')

    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = (
        '%(asctime)s - %(levelname)s - %(client_addr)s - "%(request_line)s" %(status_code)s'
    )

    config = uvicorn.Config(
        "app:app",
        host=host,
        port=port,
        workers=workers,
        log_level=log_level,
        forwarded_allow_ips="*",
        log_config=log_config
    )

    server = uvicorn.Server(config)

    try:
        server.run()
    except KeyboardInterrupt:
        print("\nServer interrupted. Shutting down gracefully...")
        asyncio.run(server.shutdown())
