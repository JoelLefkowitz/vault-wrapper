class VaultPolicy:
    def __init__(self, name, policy):
        self.name = name
        self.policy = policy

    @property
    def hcl(self):
        return "\n".join(
            [
                "\n".join(
                    [
                        "".join(['path "', path, '/*" {']),
                        "".join(
                            [" " * 4, "capabilities = ", str(cap).replace("'", '"')]
                        ),
                        "}",
                    ]
                )
                for path, cap in self.policy.items()
            ]
        )
