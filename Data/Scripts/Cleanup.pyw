if all((not args.no_result_selection, openable)):
	if os.sys.platform == "win32":
		cmd = r"start /max C:\Windows\explorer.exe /select,"
	elif os.sys.platform.startswith("linux"):
		distro = distro_name()

		if distro == "ubuntu":
			cmd = "nautilus"
		elif distro == "debian":
			cmd = "nemo"
		elif distro == "rhel":
			cmd = "gnome-open"
		else:
			cmd = "xdg-open"
	else:
		cmd = "open"

	# Null device
	if os.sys.platform == "win32":
		dev_null = ""
	else:
		dev_null = ">/dev/null 2>&1"

	#-=-=-=-#

	cmd += '"{0}" {1}'.format(args.output, dev_null)
	os.system(cmd)

print("\a", end = "\r")

#-=-=-=-#

for File in _TMP_FILES:
	os.remove(File)