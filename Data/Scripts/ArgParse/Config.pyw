# Get target file

if not args.target:
	args.target = tkinter_select_files("target audio", "flac", "~/Music", __AUDIO_FILE_TYPES, 1)
	if not args.target:
		raise ValueError("Target audio file selection aborted, exiting.")

args.target = fetch_file(args.target, "audio")
args.target = get_path(args.target)

target_file_ext = os.path.splitext(args.target)[-1][1:].lower()
target_basename = os.path.splitext(os.path.basename(args.target))[0][:BaseName_Characters_Limit]

if not os.path.exists(args.target):
	raise FileNotFoundError("Target audio file does not exist")
elif f"*.{target_file_ext}" not in list(__AUDIO_FILE_TYPES.values()):
	raise ValueError('The "{0}" file format is not supported'.format(target_file_ext.upper()))

#-=-=-=-=-=-#

# Get reference file
if not args.reference:
	args.reference = tkinter_select_files("reference audio", "flac", "~/Music", __AUDIO_FILE_TYPES, 1)
	if not args.reference:
		raise ValueError("Target audio file selection aborted, exiting.")

args.reference = fetch_file(args.reference, "audio")
args.reference = get_path(args.reference)

reference_file_ext = os.path.splitext(args.reference)[-1][1:].lower()
reference_basename = os.path.splitext(os.path.basename(args.reference))[0][:BaseName_Characters_Limit]

if not os.path.exists(args.reference):
	raise FileNotFoundError("Reference audio file does not exist")
elif f"*.{reference_file_ext}" not in list(__AUDIO_FILE_TYPES.values()):
	raise ValueError('The "{0}" file format is not supported'.format(reference_file_ext.upper()))

#-=-=-=-=-=-#

if args.target == args.reference:
	raise ValueError("Target and reference files cannot be equivalent")

#-=-=-=-#

# Sample rate
if args.sample_rate.lower() == __SAMPLE_RATE_AUTO:
	args.sample_rate = mFile(args.target).info.sample_rate
else:
	args.sample_rate = int(args.sample_rate)

#-=-=-=-#

# Output directory
if not args.no_friendly_directory:
	Results_DefaultDirectory = os.path.join(Results_DefaultDirectory, current_date)

if not args.output:
	args.output = Results_DefaultDirectory

if os.path.isfile(args.output):
	args.output = os.path.dirname(args.output)
os.makedirs(args.output, exist_ok = 1)

args.output = os.path.join(args.output, Result_FileName.format(
	rand_str(8),

	Target_BaseName = target_basename,
	Reference_BaseName = reference_basename,
	Result_SampleRate = args.sample_rate,
	Result_BitDepth = args.bit_depth,
	Result_OutputFormat = args.output_format,
	Processing_FFTSize = args.fft_window_size
	)
)

#-=-=-=-#

# Log file
if args.log_file:
	args.log_file = os.path.join(Results_DefaultDirectory, f"{Log_BaseName}.txt")
	handlers.append(logging.FileHandler(args.log_file))