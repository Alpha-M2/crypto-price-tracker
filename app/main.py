import argparse
from interfaces.cli import run_cli
from scheduler.monitor import start_monitor
from interfaces.web import start_web_app


def main():
    parser = argparse.ArgumentParser(description="Crypto Price Tracker")
    parser.add_argument(
        "--mode", choices=["cli", "web", "alerts"], required=True, help="Execution mode"
    )
    args = parser.parse_args()
    if args.mode == "cli":
        run_cli()
    elif args.mode == "web":
        start_web_app()
    elif args.mode == "alerts":
        start_monitor()


if __name__ == "__main__":
    main()
