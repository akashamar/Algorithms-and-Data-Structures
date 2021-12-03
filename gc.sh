#!/bin/bash
prettier --config ~/prettierConfig.json --write .
git add .
git commit -m "$1"
git push

