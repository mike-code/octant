import { Address, Bytes, ethereum, log } from '@graphprotocol/graph-ts';

import { Epochs } from '../generated/Epochs/Epochs';
import { Epoch } from '../generated/schema';

export function handleBlock(block: ethereum.Block): void {
  const epochsContract = Epochs.bind(
    // eslint-disable-next-line no-template-curly-in-string
    Address.fromString('0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9'),
  );
  const currentEpoch = epochsContract.try_getCurrentEpoch();
  if (currentEpoch.reverted) {
    log.info('Call to getCurrentEpoch() reverted!', []);
    return;
  }

  const epochNo = currentEpoch.value.toI32();
  let epoch = Epoch.load(Bytes.fromI32(epochNo));
  if (epoch == null) {
    epoch = new Epoch(Bytes.fromI32(epochNo));

    const decisionWindow = epochsContract.getDecisionWindow();
    const duration = epochsContract.getEpochDuration();
    const epochEnd = epochsContract.getCurrentEpochEnd();
    const epochStart = epochEnd.minus(duration);

    epoch.epoch = epochNo;
    epoch.fromTs = epochStart;
    epoch.toTs = epochEnd;
    epoch.duration = duration;
    epoch.decisionWindow = decisionWindow;

    epoch.save();
  }
}
