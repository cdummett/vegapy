include .env
export

EXTERN_DIR := "./extern"

NETWORKS_TAG=master
NETWORKS_INTERNAL_TAG=main

networks: stagnet mainnet fairground

stagnet:
	curl https://raw.githubusercontent.com/vegaprotocol/networks-internal/main/stagnet1/vegawallet-stagnet1.toml > vegapy/service/networks/stagnet.toml

fairground:
	curl https://raw.githubusercontent.com/vegaprotocol/networks-internal/main/fairground/vegawallet-fairground.toml > vegapy/service/networks/testnet.toml

mainnet:
	curl https://raw.githubusercontent.com/vegaprotocol/networks/master/mainnet1/mainnet1.toml > vegapy/service/networks/mainnet.toml

.PHONY: blacks
black:
	@black .