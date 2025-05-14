import threading
import os

# base_template = "./protocol-specifications/api/{type}/components/index.yaml"


OPENAPI_BASE_URL = os.getenv("OPENAPI_BASE_URL", "https://example.com/")

base_template = OPENAPI_BASE_URL + "/api/{name}/openapi.json"

cmd_template = """openapi-generator-cli generate \
    -g python-pydantic-v1 \
    --package-name {name} \
    -o ./beckn/package \
    -i {url} 
"""

meta_cmd = cmd_template.format(url=base_template.format(name="meta"), name="meta")

transaction_cmd = cmd_template.format(
    url=base_template.format(name="transaction"), name="transaction"
)

registry_cmd = cmd_template.format(
    url=base_template.format(name="registry"), name="registry"
)


try:
    threads = []
    for cmd in [meta_cmd, transaction_cmd, registry_cmd]:
        thread = threading.Thread(target=lambda: os.system(cmd))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

except KeyboardInterrupt:
    print("\nUvicorn server stopped by user (KeyboardInterrupt).")
