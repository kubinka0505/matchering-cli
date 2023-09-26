Parser = ArgumentParser(
	description = 'The "matchering" module CLI app',
	add_help = 0
)

#-=-=-=-#

Required = Parser.add_argument_group("Required arguments")
Background = Parser.add_argument_group("Background color arguments")
Optional = Parser.add_argument_group("Optional arguments")
Switch = Parser.add_argument_group("Switch arguments")

Required.add_argument(
	"-i", "--target",
	type = str,
	required = 1,
	help = "Fetched audio file/URL that will be subjected to mastering process"
)

Required.add_argument(
	"-r", "--reference",
	type = str,
	required = 1,
	help = 'Fetched audio file/URL of reference track'
)

Required.add_argument(
	"-o", "--output",
	type = str,
	help = 'Result file target directory, default is "{0}" (created on first launch)'.format(
		os.path.basename(Results_DefaultDirectory)
	)
)

#-=-=-=-#

Optional.add_argument(
	"-f", "--output-format",
	type = str,
	choices = __OUTPUT_FORMATS, default = "wav",
	help = '"--result" file output format',
)

Optional.add_argument(
	"-b", "--bit-depth",
	type = int,
	choices = (16, 24, 32), default = 24,
	help = "The bit depth of mastered result",
)

Optional.add_argument(
	"-sr", "--sample-rate",
	type = str, metavar = '"int"',
	choices = __SAMPLE_RATES, default = __SAMPLE_RATE_AUTO,
	help = '"--result" file sample rate. Leave empty ("auto") to inherit from "--target" file'
)

Optional.add_argument(
	"-fft", "--fft-window-size",
	type = int,
	default = 4096,
	help = "FFT window size of the processor",
)

Optional.add_argument(
	"-v", "--verbosity",
	type = int,
	choices = (0, 1, 2), default = 0,
	help = "Logging level (0 = Info, 1 = Warning, 2 = Debug)"
)

#-=-=-=-#

Optional.add_argument(
	"-l", "--log-file",
	action = "store_true",
	help = "Create the program logs file in the result directory",
)

Switch.add_argument(
	"-nl", "--no-limiter",
	action = "store_true",
	help = "Disables audio limiter at the final stage of processing",
)

Switch.add_argument(
	"-nn", "--no-normalize",
	action = "store_true",
	help = 'Disables audio normalization',
)

Switch.add_argument(
	"-nsr", "--no-result-selection",
	action = "store_true",
	help = "Disables selecting the result file in the file explorer"
)

Switch.add_argument(
	"-nfd", "--no-friendly-directory",
	action = "store_true",
	help = SUPPRESS # "Does not save the result in subdirectory formatted with execution date"
)

Switch.add_argument(
	"-h", "--help",
	action = "help",
	help = "Shows this message"
)

#-=-=-=-#

args = Parser.parse_args()