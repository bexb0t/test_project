#!/bin/bash

# Install pytest
pip install pytest

# Add the local bin to PATH
export PATH=$PATH:/home/coderpad/.local/bin

# Replace the contents of the .cpad file
cat <<EOT > .cpad
{
  "targets": {
    "run": {
      "label": "Main",
      "command": "python src/main.py"
    },
    "test": {
      "label": "Tests",
      "command": "export PATH=\$PATH:/home/coderpad/.local/bin && pytest src/tests.py"
    }
  }
}
EOT
