require('dotenv').config();

const PROPOSALS_BASE_URI = process.env.PROPOSALS_BASE_URI || 'https://ipfs.io/ipfs/QmPQM71PbBHDTwP7Vsg9jcLQNxtGnRe3NLnnNJgoQXgBDd/';
const GOERLI_URL = process.env.GOERLI_URL || '';
const ZKSYNC_URL = process.env.ZKSYNC_URL || 'https://zksync2-testnet.zksync.dev';
const GOERLI_PRIVATE_KEY = process.env.GOERLI_PRIVATE_KEY || '0000000000000000000000000000000000000000000000000000000000000000';
const ETHERSCAN_API_KEY = process.env.ETHERSCAN_API_KEY || '';

export {
  PROPOSALS_BASE_URI,
  GOERLI_URL,
  ZKSYNC_URL,
  GOERLI_PRIVATE_KEY,
  ETHERSCAN_API_KEY
};
