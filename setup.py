from setuptools import setup

if __name__ == "__main__":
    setup(
        packages=["vault_wrapper"],
        package_dir={"vault_wrapper": "src"},
        install_requires=[
            "hvac", "retry", "requests"
        ],
        extras_require={
            "dev": ["black", "autoflake", "isort", "mypy", "wheel"],
            "docs": [
                "sphinx",
                "pyimport",
                "pypandoc",
                "sphinxcontrib.apidoc",
                "sphinxcontrib.pandoc_markdown",
                "sphinx-autodoc-annotation",
                "yummy_sphinx_theme",
            ],
            "tests": [
                "pytest",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-bdd",
                "pytest-watch",
            ],
        },
    )
