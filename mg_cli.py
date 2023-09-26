"""Matchering CLI

Simple Matchering 2.0 CLI app."""

from pathlib import Path
from datetime import datetime
from mutagen import File as mFile
import requests, os, logging, random, string
from argparse import ArgumentParser, SUPPRESS
from tkinter import Tk, PhotoImage, filedialog as fd

__name__	= open(__file__).readlines()[0].strip('"').strip("\n")
__author__	= "kubinka0505"
__credits__	= __author__
__date__	= "09.09.2023"

#-=-=-=-#

def open_(file: os.path.abspath, title: bool = True) -> open:
	"""File opening handler."""
	file = os.path.abspath(f"Data/Scripts/{file}.pyw")

	fn = file.replace(os.getcwd(), "")
	fn = fn.replace("_", " ")
	fn = fn.replace(os.sep, "/")[1:]

	if os.sys.platform == "win32":
		os.system(f"title {__name__} ^| {fn}")

	return open(file, encoding = "U8").read()

__FileList = [
	"Setup/Utils",
	"Setup/Tkinter",
	"ArgParse/Main",
	"ArgParse/Config",
	"Setup/Logger",
	"Run",
	"Cleanup"
]

for File in __FileList:
	exec(open_(File))