#!/usr/bin/env sh

set -ueo pipefail

export NETWORK_FILE="./networks.localhost.json"

wait_for_contracts(){
    curl  --retry-connrefused --retry 10 --retry-delay 5 \
      -s -X GET "${CONTRACTS_DEPLOYER_URL}"
}

echo Waiting for contracts deployment ...
wait_for_contracts > localhost-contracts
set -a && source localhost-contracts && set +a

./entrypoint.sh
