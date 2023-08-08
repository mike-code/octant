import { UseMutationResult, useMutation, UseMutationOptions } from '@tanstack/react-query';
import { BigNumber } from 'ethers';
import { Hash } from 'viem';
import { useWalletClient } from 'wagmi';

import { writeContractDeposits } from '../contracts/writeContracts';

export default function useUnlock(
  options?: UseMutationOptions<Hash, unknown, BigNumber>,
): UseMutationResult<Hash, unknown, BigNumber> {
  const { data: walletClient } = useWalletClient();

  return useMutation({
    mutationFn: async value => {
      return writeContractDeposits({
        args: [BigInt(value.toHexString())],
        functionName: 'unlock',
        walletClient: walletClient!,
      });
    },
    ...options,
  });
}
