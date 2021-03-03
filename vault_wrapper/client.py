import json
import logging
from pathlib import Path

import requests
from hvac import Client
from retry import retry

logger = logging.getLogger(__name__)
exceptions = (FileNotFoundError, requests.exceptions.ConnectionError)
soft_retry = retry(
    exceptions, tries=10, delay=1, backoff=2, logger=logger
)


class VaultClient(Client):
    def __init__(
        self,
        url="http://127.0.0.1:8200",
        unseal=False,
        shares=5,
        threshold=3,
    ):
        super().__init__(url)
        init_data = self.sys.initialize(shares, threshold)
        self.token = init_data["root_token"]

        if unseal:
            self.sys.submit_unseal_keys(init_data["keys"])

    @classmethod
    @soft_retry
    def try_connect_client(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    def enable_kv_engines(self, paths):
        for path in paths:
            self.sys.enable_secrets_engine(
                backend_type="kv",
                path=path,
            )

    def create_policies(self, policies):
        for policy in policies:
            self.sys.create_or_update_policy(
                name=policy.name,
                policy=policy.hcl,
            )

    def write_tokens(self, names):
        for name in names:
            Path(f"/tokens/{name}/").mkdir(
                parents=True, exist_ok=True
            )
            with open(f"/tokens/{name}/token.json", "w") as stream:
                token = self.create_token(policies=[name], lease="1h")
                stream.write(json.dumps({"token": token}))
