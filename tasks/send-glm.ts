import { task } from 'hardhat/config';
import { GOERLI_GLM_FAUCET } from '../env';
import { FAUCET } from '../helpers/constants';
import { TestGLMFaucet } from '../typechain-types';

task('send-glm', 'Send Test GLM to given address')
  .addParam('recipient', 'Recipient of GLMs')
  .setAction(
    async (taskArgs, { ethers, getNamedAccounts }) => {
      const { deployer } = await getNamedAccounts();
      const faucet: TestGLMFaucet = await ethers.getContractAt(FAUCET, GOERLI_GLM_FAUCET, deployer);
      const tx = await faucet.sendGLM(taskArgs.recipient);
      console.log(`GLMs sent to ${taskArgs.recipient}, tx hash: ${tx.hash}`)
    }
  );