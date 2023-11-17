import { UseQueryResult, useQueries } from '@tanstack/react-query';

import { apiGetProposalDonors } from 'api/calls/poroposalDonors';
import { QUERY_KEYS } from 'api/queryKeys';
import useCurrentEpoch from 'hooks/queries/useCurrentEpoch';
import useProposalsContract from 'hooks/queries/useProposalsContract';

import { ProposalDonor } from './types';
import { mapDataToProposalDonors } from './utils';

export default function useProposalsDonors(epoch?: number): {
  data: { [key: string]: ProposalDonor[] };
  isFetching: boolean;
} {
  const { data: currentEpoch } = useCurrentEpoch();
  const { data: proposalsAddresses } = useProposalsContract(epoch);

  // TODO OCT-1139 implement socket here.

  const proposalsDonorsResults: UseQueryResult<ProposalDonor[]>[] = useQueries({
    queries: (proposalsAddresses || []).map(proposalAddress => ({
      enabled: !!proposalsAddresses,
      queryFn: () => apiGetProposalDonors(proposalAddress, epoch || currentEpoch! - 1),
      queryKey: QUERY_KEYS.proposalDonors(proposalAddress, epoch || currentEpoch! - 1),
      select: response => mapDataToProposalDonors(response),
    })),
  });

  const isFetching =
    proposalsAddresses === undefined ||
    proposalsDonorsResults.length === 0 ||
    proposalsDonorsResults.some(
      ({ isFetching: isFetchingProposalsDonorsResult }) => isFetchingProposalsDonorsResult,
    );
  if (isFetching) {
    return {
      data: {},
      isFetching,
    };
  }

  return {
    data: (proposalsDonorsResults || []).reduce((acc, curr, currentIndex) => {
      return {
        ...acc,
        [proposalsAddresses[currentIndex]]: curr.data,
      };
    }, {}),
    isFetching: false,
  };
}
