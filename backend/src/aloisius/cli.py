## This file is part of aloisius <https://github.com/skruppy/aloisius>
## Copyright (c) Skruppy <skruppy@onmars.eu>
## SPDX-License-Identifier: Apache-2.0

import uvicorn



def main():
	uvicorn.run(
		app='aloisius.app:create_app',
		host='127.0.0.1',
		port=8080,
		reload=True,
		# workers=workers, # only if not reload
		# root_path=root_path,
		# proxy_headers=proxy_headers,
	)

if __name__ == '__main__':
	main()
