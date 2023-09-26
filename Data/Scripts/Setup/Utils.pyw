# Other modules
if os.sys.platform != "win32":
	from distro import id as distro_name

#-=-=-=-#

# Variables
logger = logging.getLogger()
handlers = []
current_date = str(datetime.now()).split(".")[0].replace(":", "-")

# Dictionaries
__LOG_LEVELS = {
	0: 20,
	1: 30,
	2: 10
}

__BITS_SUBTYPES = {
	16: "PCM_16",
	24: "PCM_24",
	32: "FLOAT"
}

__AUDIO_FILE_TYPES = {
	"MPEG Audio Layer 3": "MP3",
	"Free Lossless Audio Codec": "FLAC",
	"Audio Intercharge File Format": "AIFF",
	"Wave File": "WAV",
	"Ogg Vorbis": "OGG"
}

__OUTPUT_FORMATS = "WAV", "FLAC"

__SAMPLE_RATE_AUTO = "auto"
__SAMPLE_RATES = [
	8_000, 16_000,
	32_000, 44_100, 48_000,
	88_200, 96_000, 192_000
]
__SAMPLE_RATES.append(__SAMPLE_RATE_AUTO.lower())

__FFT_SIZES = [
	128, 256, 512,
	1024, 2048,
	4096, 8192,
	16384, 32768, 65536,
	131072, 262144
]

# Files
Log_BaseName = "log"
Result_FileName = "{Target_BaseName} + {Reference_BaseName} ({Result_SampleRate} Hz, {Result_BitDepth}-bit, {Processing_FFTSize} FFT, {0}).{Result_OutputFormat}"
Results_DefaultDirectory = "Results"
BaseName_Characters_Limit = 64

#-=-=-=-#

# Temporary (downloaded) files location
if os.sys.platform == "win32":
	_TMP_DIR = os.path.expanduser("~/AppData/Local/Temp")
else:
	_TMP_DIR = "/tmp"

global _TMP_FILES
_TMP_FILES = []

#-=-=-=-#

def get_path(fp: os.path.abspath) -> str:
	"""Absolute path getter with additional user and variables expansion."""
	fp = os.path.expandvars(fp)	# Windows
	fp = os.path.expanduser(fp)	# Linux
	fp = os.path.abspath(fp)		# Full
	fp = str(Path(fp).resolve())	# Normalize

	return fp

def fetch_file(direct_url_fp: os.path.abspath, mime_req: str) -> str:
	"""File download handler."""
	if direct_url_fp.lower().startswith(("http://", "https://", "ftp://")):
		direct_url_fp = direct_url_fp.split("//")
		direct_url_fp[1] = requests.utils.quote(direct_url_fp[1]).strip("/")
		direct_url_fp  = "//".join(direct_url_fp)

		try:
			# Normalize URL
			dl_fp = requests.utils.unquote(direct_url_fp.split("/")[-1])

			for delimiter in (("?", "&", "#")):
				dl_fp = dl_fp.split(delimiter)[0]

			dl_fp = "{1} {0}".format(os.path.basename(dl_fp), "downloaded")
			dl_fp = os.path.join(_TMP_DIR, dl_fp)

			# Download
			with requests.get(direct_url_fp, stream = 1) as Site:
				if Site.ok:
					if Site.headers["content-type"].split()[0].split(";")[0].split("/")[0].lower() == mime_req.lower():
						with open(dl_fp, "wb") as File:
							for Chunk in Site.iter_content(chunk_size = 1024): 
								if Chunk:
									File.write(Chunk)

						_TMP_FILES.append(dl_fp)

						return dl_fp
					else:
						Exception("Provided URL is not an audio file.")
				else:
					Exception("Failed to fetch the URL due to {0} status code. ({1})".format(Site.status_code, Site.reason.title()))
		except requests.exceptions.ConnectionError:
			raise Exception("Could not fetch the URL due to internet connection problems.")
		except requests.exceptions.MissingSchema:
			raise Exception("Failed to analyze the URL - please check for potential misspelling and try again!")

	return direct_url_fp

#-=-=-=-#

def rand_str(length: int) -> str:
	"""Random string generation."""
	characters = []

	for character in range(length):
		character = random.choice(string.printable[0:62])
		characters.append(character)

	return "".join(characters)

def tkinter_select_files(file_type: str, format: str, initial_directory: str, file_types: dict, max_amount: int = -1) -> str:
	"""Tkinter file selector."""
	format = format.lower()
	initial_directory = get_path(initial_directory)
	file_types = tuple(file_types.items())

	if amount > 0:
		func = fd.askopenfilenames
	else:
		func = fd.askopenfilename

	return func(
		title = f"Please select {file_type} file" + "" if amount == 1 else "s",
		initialdir = initial_directory,
		filetypes = file_types,
		defaultextension = f"*.{format}"
	)

#-=-=-=-=-=-#

Results_DefaultDirectory = get_path(Results_DefaultDirectory)

__AUDIO_FILE_TYPES["All files"] = "*"
__AUDIO_FILE_TYPES = {Key: "*." + Value.lower() for Key, Value in __AUDIO_FILE_TYPES.items()}

__SAMPLE_RATES = [str(Rate) for Rate in __SAMPLE_RATES]
__OUTPUT_FORMATS = [Format.lower() for Format in __OUTPUT_FORMATS]