import { ExtendedProposal } from 'views/projects-view/types';

export interface ProposalItemProps extends ExtendedProposal {
  currentEpoch?: number;
  getVotesCount?: (currentEpoch: number, id: number) => Promise<number>;
  vote?: (id: number, alpha: number) => void;
}
