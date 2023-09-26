logger.setLevel(__LOG_LEVELS[args.verbosity])

handlers.append(logging.StreamHandler(os.sys.stdout))
formatter = logging.Formatter("{asctime}: {levelname:>7}: {message}", style="{")

for handler in handlers:
	handler.setFormatter(formatter)
	logger.addHandler(handler)