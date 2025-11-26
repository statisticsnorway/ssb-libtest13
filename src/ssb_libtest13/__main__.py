"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """SSB Libtest13."""


if __name__ == "__main__":
    main(prog_name="ssb-libtest13")  # pragma: no cover
