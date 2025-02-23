#!/bin/bash

# Check if bumpversion argument is provided
if [ -z "$1" ]; then
  echo "Please provide the version bump type (patch, minor, major)."
  exit 1
fi

# Run bumpversion with the argument provided (e.g., patch, minor, major)
bumpversion $1

# Clean the dist directory
rm -f -r dist/*

# Build the package
python3 -m build

# Upload to PyPI using twine
twine upload dist/*
