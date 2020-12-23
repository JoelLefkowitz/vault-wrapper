from setuptools import setup

if __name__ == "__main__":
    setup(
        packages=["vault_wrapper"],
        package_dir={"vault_wrapper": "src"},
        install_requires=[
            "hvac",
        ],
        extras_require={
            "dev": ["black", "autoflake", "isort", "mypy", "wheel"],
        },
    )
