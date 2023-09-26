try:
	import matchering as mg

	#-=-=-=-#

	mg.log(
		warning_handler = logger.warning,
		info_handler = logger.info,
		debug_handler = logger.debug,
	)

	try:
		err = 0
		openable = 1

		mg.process(
			target = args.target,
			reference = args.reference,
			config = mg.defaults.Config(
				internal_sample_rate = args.sample_rate,
				fft_size = args.fft_window_size,
			),
			results = [
				mg.Result(
					args.output,
					__BITS_SUBTYPES[args.bit_depth],
					use_limiter = args.no_limiter,
					normalize = args.no_normalize,
				)
			],
		)
	except Exception as Error:
		err = 1
		logger.exception(f"An exception while processing")
except KeyboardInterrupt:
	err = 1
	pass

if err:
	openable = 0