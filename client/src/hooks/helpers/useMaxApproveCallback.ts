import { MaxUint256 } from '@ethersproject/constants';
import { BigNumber, ContractTransaction, Signer } from 'ethers';
import { useCallback, useState } from 'react';

import useContractErc20 from 'hooks/contracts/useContractErc20';

import useTokenAllowance from './useTokenAllowance';

import { ERC20 } from '../../typechain-types';

// eslint-disable-next-line no-shadow
export enum ApprovalState {
  APPROVED = 'APPROVED',
  NOT_APPROVED = 'NOT_APPROVED',
  UNKNOWN = 'UNKNOWN',
}

function useApprovalState(
  contract: ERC20 | null,
  signerAddress: string | undefined,
  spender: string,
  minAmountToBeApproved: BigNumber,
): ApprovalState {
  const [approvalState, setApprovalState] = useState(ApprovalState.UNKNOWN);
  if (contract && signerAddress) {
    useTokenAllowance(contract, signerAddress, spender).then(allowance => {
      const state = allowance.gt(minAmountToBeApproved)
        ? ApprovalState.APPROVED
        : ApprovalState.NOT_APPROVED;
      setApprovalState(state);
    });
  }
  return approvalState;
}

export default function useMaxApproveCallback(
  minAmountToBeApproved: BigNumber,
  spender: string,
  signer: Signer | undefined | null,
  signerAddress?: string,
): [ApprovalState, () => Promise<ContractTransaction>] {
  const contract = useContractErc20({ signerOrProvider: signer });

  const approvalState = useApprovalState(contract, signerAddress, spender, minAmountToBeApproved);
  const approveCallback = useCallback(async (): Promise<ContractTransaction> => {
    if (!contract) {
      return Promise.reject();
    }
    return contract.approve(spender, MaxUint256).catch((error: Error) => {
      // eslint-disable-next-line no-console
      console.warn(`Failed to approve max amount for token ${contract.address}`, error);
      throw error;
    });
  }, [contract, spender]);

  return [approvalState, approveCallback];
}
