#!/bin/bash

cd /workspaces/my_model
rm -rf .venv
poetry config virtualenvs.in-project true
poetry install --with dev --with doc
