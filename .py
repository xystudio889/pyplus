import argparse
import pyplus

parser = argparse.ArgumentParser(description="imgfit commands")
subparsers = parser.add_subparsers(dest="command", required=True)

config_cmd = subparsers.add_parser("config", help="Set the config setting.Usage 'pyplus get_config' to get all config.")
config_namespace = config_cmd.add_subparsers(dest="namespace", required=True)
loacal_conf = config_namespace.add_parser("local", help="Config file only in your project.Local config in './.xystudio/pyplus/config.toml'")
global_conf = config_namespace.add_parser("global", help="Config file in all project.Global config in 'Users/Appdata/roaming/xystudio/pyplus/config.toml'")
config_cmd.add_argument("setting", help="Config setting.")
config_cmd.add_argument("value", help="Config value.")
subparsers.add_parser("version", help="Get the pyplus version.")

args = parser.parse_args()

if args.value.lower() == "true":
    value = True
elif args.value.lower() == "false":
    value = False
else:
    value = args.value

if args.command == "config":
    pyplus.config(args.setting, value, args.namespace)
elif args.command == "version":
    print("Version : pyplus",pyplus.get_pre_version())
