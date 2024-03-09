# Let's Encrypt and getssl

## How to generate SSL/TLS certs for you site

I use [Let's Encrypt](https://letsencrypt.org/) to generate SSL/TLS certs for my site. In order to help automate this I use [getssl](https://github.com/srvrco/getssl)

### Install getssl

	curl --silent --user-agent getssl/manual https://raw.githubusercontent.com/srvrco/getssl/latest/getssl --output getssl
	chmod u+x getssl
	cp ./getssl /usr/local/bin/

### Generate SSL/TLS certs

Follow the [getting started](https://github.com/srvrco/getssl?tab=readme-ov-file#getting-started) steps to generate the configuration for your domain.

Once that's done run

	getssl -c <yourdomain.com>

The configuration changes that I needed to make were to use this CA to allow for full cert generation.

	CA="https://acme-v02.api.letsencrypt.org"

I had no subdomains, so:

	SANS=""

Use a `production` certificate and use the full chain file

	PREFERRED_CHAIN="ISRG Root X2"
	FULL_CHAIN_INCLUDE_ROOT="true"

Save your changes and run:

	getssl -f <yourdomain.com>

### Upload and verify

Then upload your cert files to your site, e.g.

	fullchain.crt
	<yourdomain.com>.crt
	<yourdomain.com>.key

You can use the SSL labs site to validate your cert: [https://www.ssllabs.com/ssltest/index.html](https://www.ssllabs.com/ssltest/index.html)
