#!/usr/bin/env python3

import splitter, classifier, assembler

import tensorflow as tf
import sys
import os

def usage():
	print("main.py <img-file>")
	sys.exit()

def main():
	if len(sys.argv) != 1:
		usage()

if __name__ == "__main__":
	main()
