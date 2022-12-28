#!/bin/bash
set -e

echo "test zadzialal!!!!!!!!"

if ! _is_sourced; then
	_main "$@"
fi
