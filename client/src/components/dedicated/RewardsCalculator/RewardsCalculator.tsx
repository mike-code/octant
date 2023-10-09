import { formatUnits, parseUnits } from 'ethers/lib/utils';
import debounce from 'lodash/debounce';
import React, { FC, useCallback, useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';

import { apiPostCalculateRewards } from 'api/calls/calculateRewards';
import clientReactQuery from 'api/clients/client-react-query';
import { QUERY_KEYS } from 'api/queryKeys';
import BoxRounded from 'components/core/BoxRounded/BoxRounded';
import InputText from 'components/core/InputText/InputText';
import i18n from 'i18n';
import { comma, floatNumberWithUpTo18DecimalPlaces, numbersOnly } from 'utils/regExp';

import styles from './RewardsCalculator.module.scss';

const DEFAULT_AMOUNT = 5000;
const DEFAULT_DAYS = 90;

const RewardsCalculator: FC = () => {
  const { t } = useTranslation('translation', {
    keyPrefix: 'components.dedicated.rewardsCalculator',
  });
  const [amount, setAmount] = useState<string>(DEFAULT_AMOUNT.toString());
  const [days, setDays] = useState<string>(DEFAULT_DAYS.toString());
  const [estiamtedRewards, setEstimatedRewards] = useState('');
  const [isFetching, setIsFetching] = useState(false);

  const estiamtedRewardsValue = amount && days && estiamtedRewards ? estiamtedRewards : '';
  // eslint-disable-next-line react-hooks/exhaustive-deps
  const fetchEstimatedRewardsDebounced = useCallback(
    debounce((amountGlm, d) => {
      if (!amountGlm || !d) {
        setEstimatedRewards('');
        setIsFetching(false);
        return;
      }

      const amountGlmWEI = formatUnits(parseUnits(amountGlm, 'ether'), 'wei');

      setIsFetching(true);
      clientReactQuery
        .fetchQuery({
          queryFn: () => apiPostCalculateRewards(amountGlmWEI, parseInt(d, 10)),
          queryKey: QUERY_KEYS.calculateRewards(amountGlmWEI, parseInt(d, 10)),
        })
        .then(res => {
          setIsFetching(false);
          setEstimatedRewards(res.budget.toString());
        });
    }, 300),
    [],
  );

  const onCryptoValueChange = (value: string) => {
    const valueComma = value.replace(comma, '.');

    if (valueComma && !floatNumberWithUpTo18DecimalPlaces.test(valueComma)) {
      return;
    }

    setAmount(valueComma || '');
  };

  const onDaysInputChange = (value: string) => {
    if (!numbersOnly.test(value)) {
      return;
    }
    setDays(value);
  };

  useEffect(() => {
    fetchEstimatedRewardsDebounced(amount, days);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [amount, days]);

  return (
    <BoxRounded isGrey isVertical>
      <InputText
        autocomplete="off"
        className={styles.input}
        inputMode="decimal"
        isButtonClearVisible={false}
        label={t('enterGLMAmount')}
        onChange={e => onCryptoValueChange(e.target.value)}
        suffix="GLM"
        value={amount}
      />
      <InputText
        className={styles.input}
        inputMode="numeric"
        isButtonClearVisible={false}
        label={t('lockFor')}
        onChange={e => onDaysInputChange(e.target.value)}
        suffix={i18n.t('common.days').toUpperCase()}
        value={days}
      />
      <InputText
        className={styles.input}
        isButtonClearVisible={false}
        isDisabled
        label={t('estimatedRewards')}
        showLoader={isFetching}
        suffix="ETH"
        suffixClassName={styles.estiamtedRewardsSuffix}
        value={estiamtedRewardsValue}
      />
    </BoxRounded>
  );
};

export default RewardsCalculator;