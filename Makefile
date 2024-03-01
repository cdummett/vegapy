include .env
export

EXTERN_DIR := "./extern"

NETWORKS_TAG=master
NETWORKS_INTERNAL_TAG=main

protos:
	@if [ ! -d ./extern/ ]; then mkdir ./extern/; fi
	@echo "Downloading Git dependencies into " ${EXTERN_DIR}
	@echo "Downloading Vega"
	@if [ ! -d ./extern/vega ]; then mkdir ./extern/vega; git clone https://github.com/vegaprotocol/vega ${EXTERN_DIR}/vega; fi
ifneq (${VEGA_TAG},develop)
	@git -C ${EXTERN_DIR}/vega pull; git -C ${EXTERN_DIR}/vega checkout ${VEGA_TAG}
else
	@git -C ${EXTERN_DIR}/vega checkout develop; git -C ${EXTERN_DIR}/vega pull
endif
	@rm -rf ./vegapy/protobuf/protos
	@mkdir ./vegapy/protobuf/protos
	@buf generate extern/vega/protos/sources --template ./vegapy/protobuf/buf.gen.yaml
	@GENERATED_DIR=./vegapy/protobuf/protos ./vegapy/protobuf/post-generate.sh
	@black .

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