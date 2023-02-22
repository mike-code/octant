import { HardhatRuntimeEnvironment } from 'hardhat/types';
import { DeployFunction } from 'hardhat-deploy/types';

import { ALLOCATIONS_STORAGE } from '../helpers/constants';

// This function needs to be declared this way, otherwise it's not understood by test runner.
// eslint-disable-next-line func-names
const func: DeployFunction = async function (hre: HardhatRuntimeEnvironment) {
  const { deploy } = hre.deployments;
  const { deployer } = await hre.getNamedAccounts();

  await deploy(ALLOCATIONS_STORAGE, {
    args: [],
    autoMine: true,
    from: deployer,
    log: true,
  });
};
export default func;
func.tags = ['allocations', 'local', 'test', 'goerli'];