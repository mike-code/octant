import { HardhatRuntimeEnvironment } from 'hardhat/types';
import { DeployFunction } from 'hardhat-deploy/types';
import { PROPOSALS_CID } from '../env';
import { PROPOSALS } from '../helpers/constants';

const func: DeployFunction = async function(hre: HardhatRuntimeEnvironment) {
  const { deploy } = hre.deployments;
  const { deployer } = await hre.getNamedAccounts();

  await deploy(PROPOSALS, {
    from: deployer,
    log: true,
    args: [PROPOSALS_CID],
    autoMine: true,
  });
};
export default func;
func.tags = ['proposals','local', 'test', 'goerli'];
