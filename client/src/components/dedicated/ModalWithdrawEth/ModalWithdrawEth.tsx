import cx from 'classnames';
import { formatUnits, parseUnits } from 'ethers/lib/utils';
import React, { ChangeEvent, FC, useState } from 'react';

import BoxRounded from 'components/core/BoxRounded/BoxRounded';
import Button from 'components/core/Button/Button';
import DoubleValueContainer from 'components/core/DoubleValue/DoubleValueContainer';
import Modal from 'components/core/Modal/Modal';
import InputsCryptoFiat from 'components/dedicated/InputsCryptoFiat/InputsCryptoFiat';
import TimeCounter from 'components/dedicated/TimeCounter/TimeCounter';
import useEpochAndAllocationTimestamps from 'hooks/helpers/useEpochAndAllocationTimestamps';
import useWithdrawEth from 'hooks/mutations/useWithdrawEth';
import useCurrentEpochProps from 'hooks/queries/useCurrentEpochProps';
import useIsDecisionWindowOpen from 'hooks/queries/useIsDecisionWindowOpen';
import useWithdrawableUserEth from 'hooks/queries/useWithdrawableUserEth';
import { floatNumberWithUpTo18DecimalPlaces } from 'utils/regExp';

import styles from './ModalWithdrawEth.module.scss';
import ModalEthWithdrawingProps from './types';
import { toastDebouncedWithdrawValueTooBig } from './utils';

const ModalWithdrawEth: FC<ModalEthWithdrawingProps> = ({ modalProps }) => {
  const [valueToWithdraw, setValueToWithdraw] = useState<string>('');
  const { data: withdrawableUserEth } = useWithdrawableUserEth();
  const { data: isDecisionWindowOpen } = useIsDecisionWindowOpen();
  const { data: currentEpochProps } = useCurrentEpochProps();
  const { timeCurrentAllocationEnd } = useEpochAndAllocationTimestamps();
  const withdrawEthMutation = useWithdrawEth();

  const onChangeValue = (event: ChangeEvent<HTMLInputElement>): void => {
    const {
      target: { value },
    } = event;
    if (value && !floatNumberWithUpTo18DecimalPlaces.test(value)) {
      return;
    }
    const valueBigNumber = parseUnits(value || '0');
    let valueToSet = value;
    if (valueBigNumber.gt(withdrawableUserEth!)) {
      valueToSet = formatUnits(value);
      toastDebouncedWithdrawValueTooBig();
    }

    setValueToWithdraw(valueToSet);
  };

  return (
    <Modal header="Withdraw ETH" {...modalProps}>
      <BoxRounded
        alignment="left"
        className={styles.element}
        isGrey
        isVertical
        title="Available to withdraw"
      >
        <DoubleValueContainer cryptoCurrency="ethereum" valueCrypto={withdrawableUserEth} />
      </BoxRounded>
      <BoxRounded className={styles.element} isGrey isVertical>
        <InputsCryptoFiat
          inputCryptoProps={{
            isDisabled: withdrawEthMutation.isLoading,
            label: 'Amount to withdraw',
            onChange: onChangeValue,
            suffix: 'ETH',
            value: valueToWithdraw,
          }}
        />
        {isDecisionWindowOpen && (
          <div className={styles.timeCounterWrapper}>
            Epoch (n-1) rewards available when allocation period closes
            <TimeCounter
              className={styles.timeCounter}
              duration={currentEpochProps?.decisionWindow}
              timestamp={timeCurrentAllocationEnd}
              variant="small"
            />
          </div>
        )}
      </BoxRounded>
      <Button
        className={cx(styles.element, styles.button)}
        isDisabled={!valueToWithdraw}
        isHigh
        isLoading={withdrawEthMutation.isLoading}
        label="Request withdrawal"
        onClick={() => withdrawEthMutation.mutateAsync(valueToWithdraw)}
        variant="cta"
      />
    </Modal>
  );
};

export default ModalWithdrawEth;